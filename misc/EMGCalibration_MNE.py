"""
Script to process motor imagery data
- Compute spatial Laplacian filter - to extract C3 or C4
- Compute Fast Fourier Transform to compute the Power Spectrum and target alpha peak
- Normalize data with Reference value and compute threshold (using preprocessed data)
- Plot ERD/ERS analysis with data acquired with the pythonBCI during rest and motor imagery

"""

import numpy as np
import pyxdf
import mne
import matplotlib
from xdf2mne_ANNALISA import stream2raw
from LSLStreamInfoInterface import find_channel_index, find_stream
from matplotlib import pyplot as plt
matplotlib.use('Qt5Agg')

Laterality = 'Right' # Select the hemisphere to compute laplace on: 'Right for C4 or 'Left' for C3

def plot_power_spec(relax_fftfreq, relax_mean_power,
                    close_fftfreq, close_mean_power,
                    title, side, color):
    """Plot power spectrum: plot mean power spectra of close and
    relax trials."""

    plt.title("{} power spectrum".format(title))
    plt.xlabel("frequency [$Hz$]")
    plt.ylabel("power [$(µV)^2$]")
    plt.grid()

    plt.plot(relax_fftfreq, relax_mean_power,
            label="relax", color=colorRelax)
    plt.plot(close_fftfreq, close_mean_power,
            label="lift " + side, color=color)
    plt.legend(loc="upper right")

def plot_preprocessedData (norm, bci_freq, title, label, color, start_indcs):
    start_indcs = start_indcs/bci_freq
    plot_norm_output(norm, bci_freq, title, label, color)

    for n in range(len(start_indcs)):
        if n == 0:
            plt.axvline(start_indcs[n],color='black')
        elif n % 2 == 0:
            plt.axvline(start_indcs[n],color='blue')
        else:
            plt.axvline(start_indcs[n],color='orange')

def plot_norm_output(norm, bci_freq,
                     title, label, color):
    """Plot normalizer output:

    normalized mean sensorimotor rhythm (SMR) across trials,
    confidence interval and the calculated SMR threshold."""

    plt.title("{} normalized SMR".format(title))
    plt.xlabel("time [$s$]")
    plt.ylabel("relative amplitude [$\%$]")

    x_norm = np.arange(len(norm))/bci_freq
    plt.figure()
    plt.plot(x_norm, norm*100, color=color, label="Normalized data")
    # plt.fill_between(x_relax,
    #                 mean_relax_norm*100 - ci_relax*100,
    #                 mean_relax_norm*100 + ci_relax*100,
    #                 color=colorRelax, alpha=0.1, label='95% C.I.')
    plt.legend(loc="upper right")


# Load data from xdf file
# find correct stream (randomly assigned during recording)m
streams, fileheader = pyxdf.load_xdf(r"C:/Users/marti/Desktop/2021_2022/WINTER 2021/Lab Exoskeleton/Python_Programs/pythonbci_git/data/MyomoTest/Martin/EMG_Calibration_03.xdf", dejitter_timestamps=True)
for x in range(len(streams)):
    if streams[x]['info']['name'][0] == 'MyomoEMG': #RAW DATA (all channels)
        stream = streams[x]
        stream['time_series'] /= 1000000
    if streams[x]['info']['name'][0] == 'TaskOutput': #MARKERS (LIFT, STILL, RELAX)
        marker_stream = streams[x]

# Extract raw and preprocessed data, convert into MNE raw_data object and assign as annotations the markers
raw, events, event_id = stream2raw(stream, marker_stream=marker_stream, marker_out=3)

# Montage definition - Target channels - Band pass filtering
# easycap_montage = mne.channels.make_standard_montage("easycap-M1")
# montage = mne.io.Raw.set_montage(raw, montage=easycap_montage)

sampling_freq = raw.info['sfreq']
# bci_freq = raw['info']['effective_srate']
targets = {'channels': ['arm_extensor', 'arm_flexor', 'hand_extensor','hand_flexor']}
EMG_channel = find_channel_index(stream, targets['channels'])
data= raw.pick_channels(['arm_flexor'])

# filt_data = raw.copy().filter(l_freq=6, h_freq=30)
# Extract events from annotations
Close_events = mne.events_from_annotations(data, regexp="LIFT") #Lifting arm task
Relax_events = mne.events_from_annotations(data, regexp="RELAX") #Relax task
Still_events = mne.events_from_annotations(data, regexp='STILL') #Holding still

# Extract epochs from events
close_epochs = mne.Epochs(data, Close_events[0], tmin=0, tmax=5, baseline=None, preload=True)
relax_epochs = mne.Epochs(data, Relax_events[0], tmin=0, tmax=5, baseline=None, preload=True)
still_epochs = mne.Epochs(data, Still_events[0], tmin=0, tmax=5, baseline=None, preload=True)

# Average close and relax trials
close_av = close_epochs._data.mean(axis=0)
relax_av = relax_epochs._data.mean(axis=0)
still_av = still_epochs._data.mean(axis=0)

# Extract epochs from events
close_epochs = mne.Epochs(data, Close_events[0], tmin=0, tmax=5, baseline=None, preload=True)
relax_epochs = mne.Epochs(data, Relax_events[0], tmin=0, tmax=5, baseline=None, preload=True)
still_epochs = mne.Epochs(data, Still_events[0], tmin=0, tmax=5, baseline=None, preload=True)

# Extract epochs from events from only 1-5 sec
close_thresh_ep = mne.Epochs(data, Close_events[0], tmin=1.5, tmax=5, baseline=None, preload=True)
relax_thresh_ep = mne.Epochs(data, Relax_events[0], tmin=1.5, tmax=5, baseline=None, preload=True)
still_thresh_ep = mne.Epochs(data, Still_events[0], tmin=1.5, tmax=5, baseline=None, preload=True)

# Calculate threshold - extract mean value of the close runs
close_mn = close_thresh_ep._data.copy().mean(axis=(0, 2))
relax_mn = relax_thresh_ep._data.copy().mean(axis=(0, 2))
still_mn = still_thresh_ep._data.copy().mean(axis=(0, 2))

# Thresholds
high_thresh = np.round((close_mn + still_mn)/2, 8)
# low_thresh = np.round((still_mn + relax_mn)/2, 8)
low_thresh = np.round(relax_mn, 8)
print('Threshold LIFT: ' + str(high_thresh))
print('Threshold LOWER: ' + str(low_thresh))

# ========================#
#       PLOTTING         #
# ========================#

colorClose = 'tab:red'
colorRelax = "tab:blue"
colorStill = 'tab:green'
fig = plt.figure("EMG Analysis")
gs = plt.GridSpec(10, 3)
title = 'EMG Activity'

# Plot Close and Relax trials
plt.plot(close_av[0], linestyle='solid', label="Close", color=colorClose)
plt.plot(relax_av[0], linestyle='solid', label="Relax", color=colorRelax)
plt.plot(still_av[0], linestyle='solid', label='Still', color=colorStill)
plt.hlines(high_thresh, xmin=0, xmax=len(close_av[0]), colors='red', linestyles='dashed', label='High thresh= %.8f' %(high_thresh))
plt.hlines(low_thresh, xmin=0, xmax=len(relax_av[0]), colors='blue', linestyles='dashed', label='Low thresh= %.8f' %(low_thresh))


plt.legend()
plt.title('Lift / Relax / Still trials : ' + title)
plt.show()

print('End')

