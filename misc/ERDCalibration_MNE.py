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
from xdf2mne_ANNALISA import stream2raw
from LSLStreamInfoInterface import find_channel_index, find_stream
from matplotlib import pyplot as plt

Laterality = 'Left' # Select the hemisphere to compute laplace on: 'Right for C4 or 'Left' for C3

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
    # plt.plot(close_fftfreq, close_mean_power,
    #         label="close " + side, color=color)
    plt.plot(close_fftfreq, close_mean_power,
             label="open " + side, color=color)
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
# find correct stream (randomly assigned during recording)
streams, fileheader = pyxdf.load_xdf(r"C:/Users/marti/Desktop/2021_2022/WINTER 2021/Lab Exoskeleton/Python_Programs/pythonbci_git/data/MyomoTest/Martin/EEG_Calibration_03.xdf", dejitter_timestamps=True)
for x in range(len(streams)):
    if streams[x]['info']['name'][0] == 'SourceEEG': #RAW DATA (all channels)
        stream = streams[x]
        stream['time_series'] /= 1000000
    if streams[x]['info']['name'][0] == 'TaskOutput': #MARKERS (CLOSE, RELAX)
        marker_stream = streams[x]
    if streams[x]['info']['name'][0] == 'PreprocessedData': #PREPROCESSED DATA (C3, C4 and EOG)
        preprocessed_stream = streams[x]

#Extract raw and preprocessed data, convert into MNE raw_data object and assign as annotations the markers
raw, events, event_id = stream2raw(stream, marker_stream=marker_stream, marker_out=3)
preprocessed_data,ev, ev_id= stream2raw(preprocessed_stream,marker_stream=marker_stream, marker_out=3)

#Montage definition - Target channels - Band pass filtering
#easycap_montage = mne.channels.make_standard_montage("easycap-M1")
#montage = mne.io.Raw.set_montage(raw, montage=easycap_montage)

sampling_freq = raw.info['sfreq']
bci_freq = preprocessed_stream['info']['effective_srate']
targets = {#'raw': ['C3', 'C4', 'F3', 'F4', 'P3', 'P4', 'T7', 'T8', 'Cz'],
           'prep':['µC3', 'µC4']}
prep_channel = find_channel_index(preprocessed_stream, targets['prep'])
data_prep= preprocessed_data.pick_channels([ch for ch in targets['prep']])

filt_data = raw.copy().filter(l_freq=6, h_freq=30)

if Laterality == 'Left':
    targetC3 = ['C3']
    targetLaplace = ['F3','Cz','P3','T7']
    laplace_data = filt_data.copy().pick_channels(targetC3)
    ref_data = filt_data.copy().pick_channels(targetLaplace)
    #Compute Laplace
    laplaceC3 = np.sum(ref_data._data[:], axis=0)* 0.25
    laplace_data._data = laplace_data._data - laplaceC3
elif Laterality == 'Right':
    targetC4 = ['C4']
    targetLaplace = ['F4','Cz','P4','T8']
    laplace_data = filt_data.copy().pick_channels(targetC4)
    ref_data = filt_data.copy().pick_channels(targetLaplace)
    laplaceC4 = np.sum(ref_data._data[:], axis=0) * 0.25 #ch_numbers valid for 32 EEG channels recording 1,3,6
    laplace_data._data =  laplace_data._data - laplaceC4

#Extract events from annotations
Close_events = mne.events_from_annotations(raw, regexp="CLOSE") #Motor imagery task
Relax_events = mne.events_from_annotations(raw, regexp="RELAX") #Relax task

#Extract epochs from events
close_epochs = mne.Epochs (laplace_data,Close_events[0], tmin=0,tmax=5, baseline=None, preload=True)
relax_epochs = mne.Epochs (laplace_data, Relax_events[0], tmin=0, tmax=5, baseline=None, preload=True)


#Calculate Power spectrum with FFT for PSD plot
#  - hann the signal before to avoid bleeding
close_trials = close_epochs._data * np.hanning(close_epochs._data.shape[2]) * 2
relax_trials = relax_epochs._data * np.hanning(relax_epochs._data.shape[2]) * 2

#  - Real FFT because we just have real signals
#  - build abs because we aren't interested in phase
rfft_close = abs(np.fft.rfft(close_trials))
rfft_relax = abs(np.fft.rfft(relax_trials))

#  - multiply by two because we discard the "negative" frequencies
#  - divide by signal length for normalization
rfft_close = rfft_close * 2 / close_trials.shape[2]
rfft_close_mean = np.square(rfft_close).mean(axis=(0,1), keepdims=False)

rfft_relax = rfft_relax * 2 /relax_trials.shape[2]
rfft_relax_mean = np.square(rfft_relax).mean(axis=(0,1), keepdims=False)
#rfft_relax_mean = np.mean (rfft_relax,0)

# - get frequencies corresponding to FFT signal (the same for close or relax trials)
fftfreq = np.fft.rfftfreq(close_trials.shape[2], d=1/sampling_freq)
start = int(round(4 / (fftfreq[1] - fftfreq[0])))
end = 4 * start
mask_alpha = np.logical_and(fftfreq>start,fftfreq<end)

rfft_close_alpha = rfft_close_mean[start:end]
rfft_relax_alpha = rfft_relax_mean[start:end]
fftfreq_alpha = fftfreq[start:end]

# Calculate reference value (RV) on preprocessed data from Start on and normalize the data based on the RV
start = int(round(15 * bci_freq)) # Skip the first 15 seconds

if Laterality == 'Left':
    data_prepC3 = data_prep.copy().pick(targets['prep'][0])
    rv = data_prepC3.get_data([0],start=start).mean()
    # Extract Close and Relax trials from the preprocessed data from Neuropype
    Close_processed_events = mne.events_from_annotations(data_prepC3, regexp="CLOSE")
    Relax_processed_events = mne.events_from_annotations(data_prepC3, regexp="RELAX")
    close_preprocessed_epochs = mne.Epochs(data_prepC3, Close_processed_events[0], tmin=0, tmax=5, baseline=None,
                                           preload=True)
    relax_preprocessed_epochs = mne.Epochs(data_prepC3, Relax_processed_events[0], tmin=0, tmax=5, baseline=None,
                                           preload=True)
    # Normalize close and relax trials
    norm_close = (close_preprocessed_epochs._data / rv) - 1
    norm_relax = (relax_preprocessed_epochs._data/rv)-1


elif Laterality == 'Right':
    data_prepC4 = data_prep.copy().pick(targets['prep'][1])
    rv = preprocessed_data.get_data([1],start=start).mean()
    #Extract Close and Relax trials from the preprocessed data from Neuropype
    Close_processed_events = mne.events_from_annotations(data_prepC4, regexp="CLOSE")
    Relax_processed_events = mne.events_from_annotations(data_prepC4, regexp="RELAX")
    close_preprocessed_epochs = mne.Epochs (data_prepC4,Close_processed_events[0], tmin=0,tmax=5, baseline=None, preload=True)
    relax_preprocessed_epochs = mne.Epochs (data_prepC4, Relax_processed_events[0], tmin=0, tmax=5, baseline=None, preload=True)

    # Normalize close and relax trials
    norm_close = (close_preprocessed_epochs._data/rv) - 1
    norm_relax = (relax_preprocessed_epochs._data/rv)-1

# Calculate threshold - extract mean value of the close runs
close_mn = norm_close.copy().mean(axis=(0,2))
counter = 0
valid_trial = []
for x in range(len(norm_close)):
    if norm_close[x].mean() <= 0:
        valid_trial.append(counter)
        valid_trial[counter] = norm_close[x]
        counter += 1

valid_trials = np.concatenate(valid_trial)
close_TH = valid_trials.mean()

#print RV
print('RV : ' + str(rv))
print('easy TH : ' + str(close_mn))
print('hard TH : ' + str(close_TH))

#Average close and relax trials
close_prep = norm_close.mean(axis=0)
relax_prep = norm_relax.mean(axis=0)

# ========================#
#       PLOTTING         #
# ========================#

if Laterality == 'Right':
    title = 'C4'
    colorClose = "tab:orange"
elif Laterality == 'Left':
    title = 'C3'
    colorClose = "tab:red"
colorRelax = "tab:blue"
fig = plt.figure("ERD Analysis")
gs = plt.GridSpec(10, 3)

#Plot power spectrum
plot_power_spec(fftfreq_alpha, rfft_relax_alpha,
                fftfreq_alpha, rfft_close_alpha,
                title, str(Laterality), colorClose)
plt.xticks([4,5,6,7,8,9,10,11,12,13,14,15,16,17])
plt.show()
# Plot Close and Relax trials
plt.figure()
# plt.plot(close_prep[0], linestyle='solid', label="Close", color=colorClose)
plt.plot(close_prep[0], linestyle='solid', label="Open", color=colorClose) # for the Opening Task Module
plt.plot(relax_prep[0],  linestyle='solid', label="Relax", color=colorRelax)
plt.hlines(close_mn,xmin=0, xmax=len((close_prep)[0]),colors='black', linestyles='dashed')
plt.legend()
# plt.title('Close / Relax trials : ' + title)
plt.title('Open / Relax trials : ' + title)
plt.show()

print('End')

