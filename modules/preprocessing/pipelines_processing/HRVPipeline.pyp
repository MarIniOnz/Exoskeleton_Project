<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="HRVPipeline" version="2.0">
	<nodes>
		<node id="0" name="Dejitter Timestamps" position="(100, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="1fb94d11-9cd1-40c9-a3c4-41b33d8c558b" version="1.0.0" />
		<node id="1" name="Rename Channels" position="(900, 300)" project_name="NeuroPype" qualified_name="widgets.utilities.owrenamechannels.OWRenameChannels" title="Rename to ECG" uuid="02cdaf75-6e51-4579-89a3-142ab154764f" version="1.0.0" />
		<node id="2" name="Select Range" position="(800, 200)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select ECG channel 1" uuid="40df2146-035a-48e0-8078-6d7b16ccc19a" version="1.0.0" />
		<node id="3" name="Select Range" position="(800, 300)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select ECG channel 2" uuid="54d23dae-6a89-4069-9e7f-cfd9f4fbedb8" version="1.0.0" />
		<node id="4" name="Subtract" position="(1100, 300)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owsubtract.OWSubtract" title="Subtract" uuid="50960f07-b86d-44c3-b377-6369102d4c34" version="1.0.0" />
		<node id="5" name="Extract Inter-Beat Intervals" position="(500, 500)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owinterbeatintervals.OWInterBeatIntervals" title="Extract IBIs" uuid="86109960-bc06-4dc1-bc88-9e414529c6d6" version="1.0.0" />
		<node id="6" name="Sliding Buffer" position="(100, 500)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owslidingbuffer.OWSlidingBuffer" title="Sliding Buffer" uuid="01dad1f3-d045-449a-8021-fa55a12e330a" version="1.0.0" />
		<node id="7" name="Correct Ectopic Beats" position="(700, 500)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owcorrectectopics.OWCorrectEctopics" title="Correct Ectopics" uuid="fa329b22-6a1f-411d-8fa7-b4135f1fe791" version="1.0.0" />
		<node id="8" name="Variance" position="(1200, 600)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="886496fc-e0d8-4ae2-86b7-b1f1b4559786" version="1.0.0" />
		<node id="9" name="Square Root" position="(1300, 600)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owsquareroot.OWSquareRoot" title="Square Root" uuid="abcad210-b891-442a-abe6-1950dc2ae721" version="1.0.0" />
		<node id="10" name="Resample interbeat intervals" position="(800, 500)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owresampleibi.OWResampleIBI" title="Resample IBIs" uuid="c642ee0b-fc90-4435-81f9-7b4cac0c8eb3" version="1.0.0" />
		<node id="11" name="Select Range" position="(900, 500)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Unselect Amplitudes" uuid="c5d39a0f-3273-4d1f-ab7a-6540e9e3c5e6" version="1.0.0" />
		<node id="12" name="FFT Band-Pass Filter" position="(1000, 500)" project_name="NeuroPype" qualified_name="widgets.spectral.owspectralselection.OWSpectralSelection" title="FFT Band-Pass Filter" uuid="e9ad2911-c0c8-4fc0-bc65-ecfb7dd11484" version="1.0.0" />
		<node id="13" name="IIR Filter" position="(0, 500)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Lowpass IIR" uuid="0f8240ba-8536-494e-8c14-34937f66ff10" version="1.1.0" />
		<node id="14" name="Line Shift Filter" position="(200, 500)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owlineshiftfilter.OWLineShiftFilter" title="Line Shift Filter" uuid="d74c5640-cfbf-44f0-bf94-6a27d6044575" version="1.0.0" />
		<node id="15" name="Time Series Plot" position="(400, 600)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Plot Detected R Peaks" uuid="4448677c-405a-4088-b372-4a9cee9aae6b" version="1.0.1" />
		<node id="16" name="R Peak Segmentation" position="(300, 500)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owrsegmenter.OWRSegmenter" title="R Peak Segmentation" uuid="f3c1b769-cf6e-4249-a899-137967b4fb88" version="1.0.0" />
		<node id="17" name="RSA Porges" position="(1200, 500)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owrsaporges.OWRSAPorges" title="RSA Porges" uuid="afae7576-6c7a-4c72-a6b9-37f03a681264" version="1.0.0" />
		<node id="18" name="Print To Console" position="(1100, 800)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print HRV to Console (porges, std)" uuid="69e56d47-eaea-4bff-a889-e15d83708879" version="1.0.0" />
		<node id="19" name="LSL Input" position="(0, 100)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="06a9a8c0-9f42-46fa-b6ce-8b0046312f44" version="1.0.0" />
		<node id="20" name="Select Range" position="(800, 100)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Bipolar ECG LiveAmp" uuid="0b0f240c-bc19-48a4-9e3f-f1b48ec0a311" version="1.0.0" />
		<node id="21" name="Override Sampling Rate" position="(900, 800)" project_name="NeuroPype" qualified_name="widgets.utilities.owoverridesamplingrate.OWOverrideSamplingRate" title="Override Sampling Rate" uuid="355832d9-11df-4bac-bc94-2fd84e43db47" version="1.0.0" />
		<node id="22" name="Extract Channel Names" position="(200, 300)" project_name="NeuroPype" qualified_name="widgets.utilities.owextractchannels.OWExtractChannels" title="Extract Channel Names" uuid="f0fb180d-6d5e-45f8-80a0-bb3e9b9965d1" version="1.0.0" />
		<node id="23" name="Select Active Input" position="(1300, 300)" project_name="NeuroPype" qualified_name="widgets.programming.owselectactiveinput.OWSelectActiveInput" title="Select Active Input" uuid="b2cab345-eec0-4bc1-868d-467aff9a6cbe" version="1.0.0" />
		<node id="24" name="Passthrough" position="(600, 100)" project_name="NeuroPype" qualified_name="widgets.programming.owpassthrough.OWPassthrough" title="Passthrough LiveAmp" uuid="670df84f-ee91-4827-9869-b8a1c1e0a1af" version="1.0.0" />
		<node id="25" name="Passthrough" position="(600, 200)" project_name="NeuroPype" qualified_name="widgets.programming.owpassthrough.OWPassthrough" title="Passthrough Smarting" uuid="93acffbf-605a-43c0-b2b2-e5c19dba16c5" version="1.0.0" />
		<node id="26" name="Passthrough" position="(600, 300)" project_name="NeuroPype" qualified_name="widgets.programming.owpassthrough.OWPassthrough" title="Passthrough Smarting" uuid="41698b8e-61bf-4e06-bdd5-bed16d7039da" version="1.0.0" />
		<node id="27" name="Rename Channels" position="(900, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owrenamechannels.OWRenameChannels" title="Rename to ECG" uuid="cd8b969b-000c-4d58-9147-813c3c491cc2" version="1.0.0" />
		<node id="28" name="Rename Channels" position="(900, 200)" project_name="NeuroPype" qualified_name="widgets.utilities.owrenamechannels.OWRenameChannels" title="Rename to ECG" uuid="46e168a0-bea6-47e8-9d14-d2fab5fc3ea7" version="1.0.0" />
		<node id="29" name="Time Series Plot" position="(1000, 800)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Plot HRV" uuid="01df43f9-1fa3-451d-8455-fad8d7cfabe5" version="1.0.1" />
		<node id="30" name="Override Axis" position="(600, 800)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="10404c44-7339-44d6-a51b-325b9aedc223" version="1.0.2" />
		<node id="31" name="Centering" position="(1100, 500)" project_name="NeuroPype" qualified_name="widgets.statistics.owcentering.OWCentering" title="Centering" uuid="0d19a08e-4597-4aea-aa72-465c8033833a" version="1.1.0" />
		<node id="32" name="Concatenate Tensors" position="(800, 800)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owconcatinputs.OWConcatInputs" title="Concatenate Tensors" uuid="105e3d25-5aec-472e-a45f-a3aa1456169d" version="1.0.0" />
		<node id="33" name="Extract Streams" position="(500, 700)" project_name="NeuroPype" qualified_name="widgets.formatting.owextractstreams.OWExtractStreams" title="Extract Streams" uuid="91366b80-c831-4fb9-930a-72368058e21e" version="1.0.0" />
		<node id="34" name="Rename Streams" position="(500, 800)" project_name="NeuroPype" qualified_name="widgets.formatting.owrenamestreams.OWRenameStreams" title="Rename Streams" uuid="c6d4e7f7-265b-4555-bd26-00b08dc8a97a" version="1.0.0" />
		<node id="35" name="LSL Output" position="(1100, 700)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="ed05d18c-1186-49ca-8635-75b5c17cbebb" version="1.0.0" />
		<node id="36" name="Condition Test" position="(400, 300)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owconditiontestfixed.OWConditionTestFixed" title="Condition Test (Fixed)" uuid="ba16eff2-bd28-4d82-85a0-6dfb66b1fb1b" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="1" sink_channel="Data2" sink_node_id="4" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="6" sink_channel="Detected Peaks" sink_node_id="5" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="7" source_channel="Intervals" source_node_id="5" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="19" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="22" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="13" source_channel="Output" source_node_id="23" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="20" source_channel="Outdata" source_node_id="24" />
		<link enabled="true" id="15" sink_channel="Indata" sink_node_id="24" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="16" sink_channel="Indata" sink_node_id="25" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="2" source_channel="Outdata" source_node_id="25" />
		<link enabled="true" id="18" sink_channel="Indata" sink_node_id="26" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="3" source_channel="Outdata" source_node_id="26" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="27" source_channel="Data" source_node_id="20" />
		<link enabled="true" id="21" sink_channel="Input1" sink_node_id="23" source_channel="Data" source_node_id="27" />
		<link enabled="true" id="22" sink_channel="Input2" sink_node_id="23" source_channel="Outdata" source_node_id="4" />
		<link enabled="true" id="23" sink_channel="Data" sink_node_id="28" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="24" sink_channel="Data1" sink_node_id="4" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="25" sink_channel="Data" sink_node_id="31" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="26" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="31" />
		<link enabled="true" id="27" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="31" />
		<link enabled="true" id="28" sink_channel="Data" sink_node_id="33" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="29" sink_channel="Data1" sink_node_id="32" source_channel="Data" source_node_id="33" />
		<link enabled="true" id="30" sink_channel="Data2" sink_node_id="32" source_channel="Data" source_node_id="30" />
		<link enabled="true" id="31" sink_channel="Data" sink_node_id="34" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="32" sink_channel="Data" sink_node_id="30" source_channel="Data" source_node_id="34" />
		<link enabled="true" id="33" sink_channel="Data" sink_node_id="21" source_channel="Outdata" source_node_id="32" />
		<link enabled="true" id="34" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="21" />
		<link enabled="true" id="35" sink_channel="Data" sink_node_id="35" source_channel="Data" source_node_id="21" />
		<link enabled="true" id="36" sink_channel="Input" sink_node_id="36" source_channel="Channel Names" source_node_id="22" />
		<link enabled="true" id="37" sink_channel="Update" sink_node_id="24" source_channel="True" source_node_id="36" />
		<link enabled="true" id="38" sink_channel="Update" sink_node_id="25" source_channel="False" source_node_id="36" />
		<link enabled="true" id="39" sink_channel="Update" sink_node_id="26" source_channel="False" source_node_id="36" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlj
a2xlX3R5cGUKcQVYDAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAA
AAAQKAAAAhoAABHdAAADQwAAEDMAAAJHAAAR0gAAAzgAAAABAABxCIVxCYdxClJxC1gOAAAAc2V0
X2JyZWFrcG9pbnRxDIlYDgAAAHdhcm11cF9zYW1wbGVzcQ1K/////3Uu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAwAAAByZXBsYWNlX2V4cHJxAVgDAAAARUNHcQJYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0
cnlxA2NzaXAKX3VucGlja2xlX3R5cGUKcQRYDAAAAFB5UXQ0LlF0Q29yZXEFWAoAAABRQnl0ZUFy
cmF5cQZDLgHZ0MsAAQAAAAAC9AAAAV0AAASOAAAChgAAAv8AAAGKAAAEgwAAAnsAAAAAAABxB4Vx
CIdxCVJxClgLAAAAc2VhcmNoX2V4cHJxC1gCAAAARjhxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlY
BwAAAHN0cmVhbXNxDl1xD1gNAAAAYW5hbG9nc2lnbmFsc3EQYVgHAAAAdmVyYm9zZXERiXUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAC2gAAAV0AAASnAAAChgAAAuUA
AAGKAAAEnAAAAnsAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ1YAgAAAEY3cQ5h
WA4AAABzZXRfYnJlYWtwb2ludHEPiVgEAAAAdW5pdHEQWAUAAABuYW1lc3ERdS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAC2gAAAV0AAASnAAAChgAAAuUA
AAGKAAAEnAAAAnsAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ1YAgAAAEY4cQ5h
WA4AAABzZXRfYnJlYWtwb2ludHEPiVgEAAAAdW5pdHEQWAUAAABuYW1lc3ERdS4=
</properties>
		<properties format="literal" node_id="4">{'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAAAwIAAAGaAAAEfwAA
AkkAAAMNAAABxwAABHQAAAI+AAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
dS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAAAwIAAAF7AAAEfwAA
AmgAAAMNAAABqAAABHQAAAJdAAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
WAwAAABzaGlmdF93aW5kb3dxCksBWA0AAAB3aW5kb3dfbGVuZ3RocQtLPHUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAoAAABwZXJjZW50YWdlcQFLHlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXECY3NpcApf
dW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRlQXJyYXlxBUMuAdnQ
ywABAAAAAAMCAAABewAABH8AAAJoAAADDQAAAagAAAR0AAACXQAAAAAAAHEGhXEHh3EIUnEJWA4A
AABzZXRfYnJlYWtwb2ludHEKiVgEAAAAc3BhbnELSxV1Lg==
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQVjc2lwCl91
bnBpY2tsZV90eXBlCnEGWAwAAABQeVF0NC5RdENvcmVxB1gKAAAAUUJ5dGVBcnJheXEIQy4B2dDL
AAEAAAAAAtoAAAFtAAAEqAAAAncAAALlAAABmgAABJ0AAAJsAAAAAAAAcQmFcQqHcQtScQxYDgAA
AHNldF9icmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAAAwIAAAGaAAAEfwAA
AkkAAAMNAAABxwAABHQAAAI+AAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
dS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAkAAABmc19yZXNhbXBxAUsEWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQJjc2lwCl91
bnBpY2tsZV90eXBlCnEDWAwAAABQeVF0NC5RdENvcmVxBFgKAAAAUUJ5dGVBcnJheXEFQy4B2dDL
AAEAAAAAAwIAAAGLAAAEfwAAAlkAAAMNAAABuAAABHQAAAJOAAAAAAAAcQaFcQeHcQhScQlYDgAA
AHNldF9icmVha3BvaW50cQqJdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVx
A1gTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlR
dDQuUXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAALaAAABXQAABKcAAAKGAAAC
5QAAAYoAAAScAAACewAAAAAAAHEIhXEJh3EKUnELWAkAAABzZWxlY3Rpb25xDF1xDVgIAAAAaW50
ZXJ2YWxxDmFYDgAAAHNldF9icmVha3BvaW50cQ+JWAQAAAB1bml0cRBYBQAAAG5hbWVzcRF1Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAkAAABibG9ja3NpemVxAUtkWAsAAABmcmVxdWVuY2llc3ECXXEDKEc/wzMzMzMzM0c/
2ZmZmZmZmmVYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVY
DAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAC3AAAAXsAAASm
AAACaAAAAucAAAGoAAAEmwAAAl0AAAAAAABxCIVxCYdxClJxC1gOAAAAc2V0X2JyZWFrcG9pbnRx
DIl1Lg==
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGS8hhWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAcAAABs
b3dwYXNzcQlYEAAAAG9mZmxpbmVfZmlsdGZpbHRxColYBQAAAG9yZGVycQtLA1gJAAAAcGFzc19s
b3NzcQxHQAgAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxDWNzaXAKX3VucGlja2xlX3R5
cGUKcQ5YDAAAAFB5UXQ0LlF0Q29yZXEPWAoAAABRQnl0ZUFycmF5cRBDLgHZ0MsAAQAAAAAC6gAA
AREAAASYAAAC0wAAAvUAAAE+AAAEjQAAAsgAAAAAAABxEYVxEodxE1JxFFgOAAAAc2V0X2JyZWFr
cG9pbnRxFYlYCgAAAHN0b3BfYXR0ZW5xFkdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAkAAABsaW5lX2ZyZXFxAUsyWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQJjc2lwCl91
bnBpY2tsZV90eXBlCnEDWAwAAABQeVF0NC5RdENvcmVxBFgKAAAAUUJ5dGVBcnJheXEFQy4B2dDL
AAEAAAAAAwIAAAGLAAAEfwAAAlkAAAMNAAABuAAABHQAAAJOAAAAAAAAcQaFcQeHcQhScQlYDgAA
AHNldF9icmVha3BvaW50cQqJdS4=
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiVgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLAEsA
TYAHTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiFgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAAAwwAAABaAAAEiQAAA9kAAAMXAAAAhwAABH4A
AAPOAAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP+AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIohYCwAAAHN0cmVhbV9uYW1lcSNoFVgKAAAAdGltZV9y
YW5nZXEkSzxYBQAAAHRpdGxlcSVYEAAAAERldGVjdGVkIFIgUGVha3NxJlgKAAAAemVyb19jb2xv
cnEnWAcAAAAjN0Y3RjdGcShYCAAAAHplcm9tZWFucSmIdS4=
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAUAAABhZnRlcnEBWA0AAAAodXNlIGRlZmF1bHQpcQJYBgAAAGJlZm9yZXEDaAJYBgAA
AG1ldGhvZHEEWAgAAABjaHJpc3RvdnEFWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQZjc2lwCl91
bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NC5RdENvcmVxCFgKAAAAUUJ5dGVBcnJheXEJQy4B2dDL
AAEAAAAAAwIAAAFNAAAEfwAAApcAAAMNAAABegAABHQAAAKMAAAAAAAAcQqFcQuHcQxScQ1YDgAA
AHNldF9icmVha3BvaW50cQ6JWAYAAAB0aHJlc2hxD1gNAAAAKHVzZSBkZWZhdWx0KXEQWAkAAAB0
b2xlcmFuY2VxEWgCdS4=
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWAkAAABlcG9jaF9kdXJxAUsUWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQJjc2lwCl91
bnBpY2tsZV90eXBlCnEDWAwAAABQeVF0NC5RdENvcmVxBFgKAAAAUUJ5dGVBcnJheXEFQy4B2dDL
AAEAAAAAAwIAAAF7AAAEfwAAAmgAAAMNAAABqAAABHQAAAJdAAAAAAAAcQaFcQeHcQhScQlYDgAA
AHNldF9icmVha3BvaW50cQqJWAQAAAB1bml0cQtYBwAAAHNlY29uZHNxDHUu
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWA0AAABvbmx5X25vbmVtcHR5cQGIWA0AAABwcmludF9jaGFubmVscQKJWA0AAABwcmlu
dF9jb21wYWN0cQOJWAoAAABwcmludF9kYXRhcQSIWA0AAABwcmludF9tYXJrZXJzcQWJWA0AAABw
cmludF9zdHJlYW1zcQZdcQdYAwAAAGhydnEIYVgKAAAAcHJpbnRfdGltZXEJiVgLAAAAcHJpbnRf
dHJpYWxxColYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxC2NzaXAKX3VucGlja2xlX3R5cGUKcQxY
DAAAAFB5UXQ0LlF0Q29yZXENWAoAAABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAAAAACvAAAAL4AAAQ5
AAACVwAAAscAAADrAAAELgAAAkwAAAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRx
E4l1Lg==
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
HlgMAAAAbWF4X2NodW5rbGVucQhN9AFYDAAAAG5vbWluYWxfcmF0ZXEJWA0AAAAodXNlIGRlZmF1
bHQpcQpYBQAAAHF1ZXJ5cQtYEAAAAG5hbWU9J1NvdXJjZUVFRydxDFgHAAAAcmVjb3ZlcnENiFgU
AAAAcmVzb2x2ZV9taW5pbXVtX3RpbWVxDkc/4AAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAAUHlRdDQuUXRDb3JlcRFYCgAAAFFCeXRlQXJy
YXlxEkMuAdnQywABAAAAAAF4AAABKQAAA18AAAMKAAABgwAAAVYAAANUAAAC/wAAAAAAAHEThXEU
h3EVUnEWWA4AAABzZXRfYnJlYWtwb2ludHEXiXUu
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAFNwAAAQgAAAcEAAACVwAABUIA
AAE1AAAG+QAAAkwAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ1YAwAAADI1KnEO
YVgOAAAAc2V0X2JyZWFrcG9pbnRxD4lYBAAAAHVuaXRxEFgFAAAAbmFtZXNxEXUu
</properties>
		<properties format="pickle" node_id="21">gAN9cQAoWBsAAABjaGFuZ2VfdHJpZ2dlcnNfc3RhdGVfcmVzZXRxAYhYDQAAAHNhbXBsaW5nX3Jh
dGVxAksBWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91bnBpY2tsZV90eXBlCnEEWAwA
AABQeVF0NC5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQy4B2dDLAAEAAAAAAwIAAAF8AAAEfwAA
AmcAAAMNAAABqQAABHQAAAJcAAAAAAAAcQeFcQiHcQlScQpYDgAAAHNldF9icmVha3BvaW50cQuJ
dS4=
</properties>
		<properties format="pickle" node_id="22">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAAAwIAAAF8AAAEfwAA
AmcAAAMNAAABqQAABHQAAAJcAAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
WAYAAABzdHJlYW1xClgAAAAAcQtYBwAAAHZlcmJvc2VxDIl1Lg==
</properties>
		<properties format="literal" node_id="23">{'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="24">{'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="25">{'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="26">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAAAwIAAAGaAAAEfwAA
AkkAAAMNAAABxwAABHQAAAI+AAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
dS4=
</properties>
		<properties format="pickle" node_id="27">gAN9cQAoWAwAAAByZXBsYWNlX2V4cHJxAVgDAAAARUNHcQJYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0
cnlxA2NzaXAKX3VucGlja2xlX3R5cGUKcQRYDAAAAFB5UXQ0LlF0Q29yZXEFWAoAAABRQnl0ZUFy
cmF5cQZDLgHZ0MsAAQAAAAAC9AAAAV0AAASOAAAChgAAAv8AAAGKAAAEgwAAAnsAAAAAAABxB4Vx
CIdxCVJxClgLAAAAc2VhcmNoX2V4cHJxC1gEAAAAMjVcKnEMWA4AAABzZXRfYnJlYWtwb2ludHEN
iVgHAAAAc3RyZWFtc3EOXXEPWAcAAAB2ZXJib3NlcRCJdS4=
</properties>
		<properties format="pickle" node_id="28">gAN9cQAoWAwAAAByZXBsYWNlX2V4cHJxAVgDAAAARUNHcQJYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0
cnlxA2NzaXAKX3VucGlja2xlX3R5cGUKcQRYDAAAAFB5UXQ0LlF0Q29yZXEFWAoAAABRQnl0ZUFy
cmF5cQZDLgHZ0MsAAQAAAAAC9AAAAV0AAASOAAAChgAAAv8AAAGKAAAEgwAAAnsAAAAAAABxB4Vx
CIdxCVJxClgLAAAAc2VhcmNoX2V4cHJxC1gCAAAARjdxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlY
BwAAAHN0cmVhbXNxDl1xD1gHAAAAdmVyYm9zZXEQiXUu
</properties>
		<properties format="pickle" node_id="29">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiVgQAAAAYXV0b19saW5lX2NvbG9yc3EEiFgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLAE30
AU2AB030AWVYCgAAAGxpbmVfY29sb3JxDVgHAAAAIzAwMDAwMHEOWAoAAABsaW5lX3dpZHRocQ9H
P+gAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnEQWAcAAAAjRkYwMDAwcRFYDAAAAG5hbnNfYXNfemVy
b3ESiFgOAAAAbm9fY29uY2F0ZW5hdGVxE4lYDgAAAG92ZXJyaWRlX3NyYXRlcRRLAVgMAAAAcGxv
dF9tYXJrZXJzcRWIWAsAAABwbG90X21pbm1heHEWiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEX
Y3NpcApfdW5waWNrbGVfdHlwZQpxGFgMAAAAUHlRdDQuUXRDb3JlcRlYCgAAAFFCeXRlQXJyYXlx
GkMuAdnQywABAAAAAAL/AAAAWgAABJYAAAPZAAADCgAAAIcAAASLAAADzgAAAAAAAHEbhXEch3Ed
UnEeWAUAAABzY2FsZXEfSwFYDgAAAHNldF9icmVha3BvaW50cSCJWAwAAABzaG93X3Rvb2xiYXJx
IYhYCwAAAHN0cmVhbV9uYW1lcSJYAwAAAGhydnEjWAoAAAB0aW1lX3JhbmdlcSRNWAJYBQAAAHRp
dGxlcSVYAwAAAEhSVnEmWAoAAAB6ZXJvX2NvbG9ycSdYBwAAACNGN0Y3RjdxKFgIAAAAemVyb21l
YW5xKYh1Lg==
</properties>
		<properties format="pickle" node_id="30">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4lYDAAAAGN1c3RvbV9sYWJlbHEEWAAAAABxBVgJAAAAaW5p
dF9kYXRhcQZdcQdYAwAAAHN0ZHEIYVgIAAAAbmV3X2F4aXNxCVgFAAAAc3BhY2VxClgIAAAAb2xk
X2F4aXNxC1gHAAAAZmVhdHVyZXEMWAwAAABvbmx5X3NpZ25hbHNxDYhYEwAAAHNhdmVkV2lkZ2V0
R2VvbWV0cnlxDmNzaXAKX3VucGlja2xlX3R5cGUKcQ9YDAAAAFB5UXQ0LlF0Q29yZXEQWAoAAABR
Qnl0ZUFycmF5cRFDLgHZ0MsAAQAAAAAC8AAAASEAAASRAAAC6AAAAvsAAAFOAAAEhgAAAt0AAAAA
AABxEoVxE4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFol1Lg==
</properties>
		<properties format="pickle" node_id="31">gAN9cQAoWBIAAABhZGFwdF9vbl9zdHJlYW1pbmdxAYhYBAAAAGF4aXNxAlgEAAAAdGltZXEDWA8A
AABpbml0aWFsaXplX29uY2VxBIlYBgAAAHJvYnVzdHEFiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDQuUXRDb3JlcQhYCgAAAFFCeXRlQXJy
YXlxCUMuAdnQywABAAAAAAMCAAABXwAABH8AAAKEAAADDQAAAYwAAAR0AAACeQAAAAAAAHEKhXEL
h3EMUnENWA4AAABzZXRfYnJlYWtwb2ludHEOiXUu
</properties>
		<properties format="pickle" node_id="32">gAN9cQAoWA0AAABhbGxvd19tYXJrZXJzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNYDQAAAGNv
cnJlY3Rfb3JkZXJxBIhYCgAAAGNyZWF0ZV9uZXdxBYlYCgAAAHByb3BlcnRpZXNxBlgNAAAAKHVz
ZSBkZWZhdWx0KXEHWA8AAAByZXF1aXJlZF9pbnB1dHNxCEsAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVB
cnJheXEMQy4B2dDLAAEAAAAAAwIAAAFAAAAEfwAAAqMAAAMNAAABbQAABHQAAAKYAAAAAAAAcQ2F
cQ6HcQ9ScRBYDgAAAHNldF9icmVha3BvaW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="33">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAAAwIAAAF8AAAEfwAA
AmcAAAMNAAABqQAABHQAAAJcAAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
WAwAAABzdHJlYW1fbmFtZXNxCl1xC1gDAAAAaHJ2cQxhWBEAAABzdXBwb3J0X3dpbGRjYXJkc3EN
iXUu
</properties>
		<properties format="pickle" node_id="34">gAN9cQAoWAwAAABuYW1lX2NoYW5nZXNxAX1xAlgSAAAAaW50ZXJiZWF0aW50ZXJ2YWxzcQNYAwAA
AGhydnEEc1gTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlwZQpxBlgM
AAAAUHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAAAAMCAAABiwAABH8A
AAJZAAADDQAAAbgAAAR0AAACTgAAAAAAAHEJhXEKh3ELUnEMWA4AAABzZXRfYnJlYWtwb2ludHEN
iXUu
</properties>
		<properties format="pickle" node_id="35">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAvoAAADWAAAEiAAA
Aw4AAAMFAAABAwAABH0AAAMDAAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETWAMAAABIUlZxFFgFAAAAc3JhdGVx
FVgNAAAAKHVzZSBkZWZhdWx0KXEWWAsAAABzdHJlYW1fbmFtZXEXWAMAAABocnZxGFgLAAAAc3Ry
ZWFtX3R5cGVxGVgDAAAARUNHcRpYEwAAAHVzZV9kYXRhX3RpbWVzdGFtcHNxG4hYFgAAAHVzZV9u
dW1weV9vcHRpbWl6YXRpb25xHIh1Lg==
</properties>
		<properties format="pickle" node_id="36">gAN9cQAoWAsAAABjb2xsYXBzZV9vcHEBWAMAAABhbGxxAlgIAAAAb3BlcmF0b3JxA1gFAAAAZXF1
YWxxBFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlwZQpxBlgMAAAA
UHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAAAAMCAAABbAAABH8AAAJ4
AAADDQAAAZkAAAR0AAACbQAAAAAAAHEJhXEKh3ELUnEMWA4AAABzZXRfYnJlYWtwb2ludHENiVgF
AAAAdmFsdWVxDlgDAAAAMjUqcQ91Lg==
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node4",
            "data",
            "node2",
            "data"
        ],
        [
            "node2",
            "data",
            "node5",
            "data2"
        ],
        [
            "node9",
            "data",
            "node10",
            "data"
        ],
        [
            "node8",
            "data",
            "node11",
            "data"
        ],
        [
            "node11",
            "data",
            "node12",
            "data"
        ],
        [
            "node12",
            "data",
            "node13",
            "data"
        ],
        [
            "node17",
            "data",
            "node6",
            "detected_peaks"
        ],
        [
            "node6",
            "intervals",
            "node8",
            "data"
        ],
        [
            "node14",
            "data",
            "node7",
            "data"
        ],
        [
            "node7",
            "data",
            "node15",
            "data"
        ],
        [
            "node15",
            "data",
            "node17",
            "data"
        ],
        [
            "node20",
            "data",
            "node1",
            "data"
        ],
        [
            "node1",
            "data",
            "node23",
            "data"
        ],
        [
            "node1",
            "data",
            "node25",
            "indata"
        ],
        [
            "node1",
            "data",
            "node26",
            "indata"
        ],
        [
            "node1",
            "data",
            "node27",
            "indata"
        ],
        [
            "node24",
            "output",
            "node14",
            "data"
        ],
        [
            "node25",
            "outdata",
            "node21",
            "data"
        ],
        [
            "node26",
            "outdata",
            "node3",
            "data"
        ],
        [
            "node27",
            "outdata",
            "node4",
            "data"
        ],
        [
            "node21",
            "data",
            "node28",
            "data"
        ],
        [
            "node28",
            "data",
            "node24",
            "input1"
        ],
        [
            "node5",
            "outdata",
            "node24",
            "input2"
        ],
        [
            "node3",
            "data",
            "node29",
            "data"
        ],
        [
            "node29",
            "data",
            "node5",
            "data1"
        ],
        [
            "node13",
            "data",
            "node32",
            "data"
        ],
        [
            "node32",
            "data",
            "node18",
            "data"
        ],
        [
            "node32",
            "data",
            "node9",
            "data"
        ],
        [
            "node18",
            "data",
            "node34",
            "data"
        ],
        [
            "node34",
            "data",
            "node33",
            "data1"
        ],
        [
            "node31",
            "data",
            "node33",
            "data2"
        ],
        [
            "node10",
            "data",
            "node35",
            "data"
        ],
        [
            "node35",
            "data",
            "node31",
            "data"
        ],
        [
            "node33",
            "outdata",
            "node22",
            "data"
        ],
        [
            "node22",
            "data",
            "node19",
            "data"
        ],
        [
            "node22",
            "data",
            "node36",
            "data"
        ],
        [
            "node23",
            "channel_names",
            "node37",
            "input"
        ],
        [
            "node37",
            "true",
            "node25",
            "update"
        ],
        [
            "node37",
            "false",
            "node26",
            "update"
        ],
        [
            "node37",
            "false",
            "node27",
            "update"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "1fb94d11-9cd1-40c9-a3c4-41b33d8c558b"
        },
        "node10": {
            "class": "SquareRoot",
            "module": "neuropype.nodes.elementwise_math.SquareRoot",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "abcad210-b891-442a-abe6-1950dc2ae721"
        },
        "node11": {
            "class": "ResampleIBI",
            "module": "neuropype.nodes.exo_nodes.ResampleIBI",
            "params": {
                "fs_resamp": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 4
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c642ee0b-fc90-4435-81f9-7b4cac0c8eb3"
        },
        "node12": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        "interval"
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "names"
                }
            },
            "uuid": "c5d39a0f-3273-4d1f-ab7a-6540e9e3c5e6"
        },
        "node13": {
            "class": "SpectralSelection",
            "module": "neuropype.nodes.spectral.SpectralSelection",
            "params": {
                "blocksize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.15,
                        0.4
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e9ad2911-c0c8-4fc0-bc65-ecfb7dd11484"
        },
        "node14": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "butter"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        200
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "mode": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "lowpass"
                },
                "offline_filtfilt": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 3
                },
                "pass_loss": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 3.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "0f8240ba-8536-494e-8c14-34937f66ff10"
        },
        "node15": {
            "class": "LineShiftFilter",
            "module": "neuropype.nodes.exo_nodes.LineShiftFilter",
            "params": {
                "line_freq": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d74c5640-cfbf-44f0-bf94-6a27d6044575"
        },
        "node16": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        0,
                        1920,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 60
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Detected R Peaks"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "4448677c-405a-4088-b372-4a9cee9aae6b"
        },
        "node17": {
            "class": "RSegmenter",
            "module": "neuropype.nodes.exo_nodes.RSegmenter",
            "params": {
                "after": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "before": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "christov"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "thresh": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                }
            },
            "uuid": "f3c1b769-cf6e-4249-a899-137967b4fb88"
        },
        "node18": {
            "class": "RSAPorges",
            "module": "neuropype.nodes.exo_nodes.RSAPorges",
            "params": {
                "epoch_dur": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 20
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "seconds"
                }
            },
            "uuid": "afae7576-6c7a-4c72-a6b9-37f03a681264"
        },
        "node19": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "only_nonempty": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "print_data": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_streams": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "hrv"
                    ]
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "69e56d47-eaea-4bff-a889-e15d83708879"
        },
        "node2": {
            "class": "RenameChannels",
            "module": "neuropype.nodes.utilities.RenameChannels",
            "params": {
                "replace_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "ECG"
                },
                "search_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "F8"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "streams": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "analogsignals"
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "02cdaf75-6e51-4579-89a3-142ab154764f"
        },
        "node20": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 500
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='SourceEEG'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "06a9a8c0-9f42-46fa-b6ce-8b0046312f44"
        },
        "node21": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        "25*"
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "names"
                }
            },
            "uuid": "0b0f240c-bc19-48a4-9e3f-f1b48ec0a311"
        },
        "node22": {
            "class": "OverrideSamplingRate",
            "module": "neuropype.nodes.utilities.OverrideSamplingRate",
            "params": {
                "change_triggers_state_reset": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "sampling_rate": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 1
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "355832d9-11df-4bac-bc94-2fd84e43db47"
        },
        "node23": {
            "class": "ExtractChannels",
            "module": "neuropype.nodes.utilities.ExtractChannels",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f0fb180d-6d5e-45f8-80a0-bb3e9b9965d1"
        },
        "node24": {
            "class": "SelectActiveInput",
            "module": "neuropype.nodes.programming.SelectActiveInput",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b2cab345-eec0-4bc1-868d-467aff9a6cbe"
        },
        "node25": {
            "class": "Passthrough",
            "module": "neuropype.nodes.programming.Passthrough",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "670df84f-ee91-4827-9869-b8a1c1e0a1af"
        },
        "node26": {
            "class": "Passthrough",
            "module": "neuropype.nodes.programming.Passthrough",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "93acffbf-605a-43c0-b2b2-e5c19dba16c5"
        },
        "node27": {
            "class": "Passthrough",
            "module": "neuropype.nodes.programming.Passthrough",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "41698b8e-61bf-4e06-bdd5-bed16d7039da"
        },
        "node28": {
            "class": "RenameChannels",
            "module": "neuropype.nodes.utilities.RenameChannels",
            "params": {
                "replace_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "ECG"
                },
                "search_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "25\\*"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "cd8b969b-000c-4d58-9147-813c3c491cc2"
        },
        "node29": {
            "class": "RenameChannels",
            "module": "neuropype.nodes.utilities.RenameChannels",
            "params": {
                "replace_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "ECG"
                },
                "search_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "F7"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "46e168a0-bea6-47e8-9d14-d2fab5fc3ea7"
        },
        "node3": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        "F7"
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "names"
                }
            },
            "uuid": "40df2146-035a-48e0-8078-6d7b16ccc19a"
        },
        "node30": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "auto_line_colors": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        500,
                        1920,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 1
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "hrv"
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 600
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "HRV"
                },
                "zero_color": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "#F7F7F7"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "01df43f9-1fa3-451d-8455-fad8d7cfabe5"
        },
        "node31": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": true,
                    "type": "StringPort",
                    "value": ""
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "std"
                    ]
                },
                "new_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "10404c44-7339-44d6-a51b-325b9aedc223"
        },
        "node32": {
            "class": "Centering",
            "module": "neuropype.nodes.statistics.Centering",
            "params": {
                "adapt_on_streaming": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "initialize_once": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "robust": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0d19a08e-4597-4aea-aa72-465c8033833a"
        },
        "node33": {
            "class": "ConcatInputs",
            "module": "neuropype.nodes.tensor_math.ConcatInputs",
            "params": {
                "allow_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "correct_order": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "create_new": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "properties": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "required_inputs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "105e3d25-5aec-472e-a45f-a3aa1456169d"
        },
        "node34": {
            "class": "ExtractStreams",
            "module": "neuropype.nodes.formatting.ExtractStreams",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "hrv"
                    ]
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "91366b80-c831-4fb9-930a-72368058e21e"
        },
        "node35": {
            "class": "RenameStreams",
            "module": "neuropype.nodes.formatting.RenameStreams",
            "params": {
                "name_changes": {
                    "customized": true,
                    "type": "DictPort",
                    "value": {
                        "interbeatintervals": "hrv"
                    }
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c6d4e7f7-265b-4555-bd26-00b08dc8a97a"
        },
        "node36": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "HRV"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "hrv"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "ECG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "ed05d18c-1186-49ca-8635-75b5c17cbebb"
        },
        "node37": {
            "class": "ConditionTestFixed",
            "module": "neuropype.nodes.exo_nodes.ConditionTestFixed",
            "params": {
                "collapse_op": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "all"
                },
                "operator": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "equal"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "value": {
                    "customized": true,
                    "type": "Port",
                    "value": "25*"
                }
            },
            "uuid": "ba16eff2-bd28-4d82-85a0-6dfb66b1fb1b"
        },
        "node4": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        "F8"
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "names"
                }
            },
            "uuid": "54d23dae-6a89-4069-9e7f-cfd9f4fbedb8"
        },
        "node5": {
            "class": "Subtract",
            "module": "neuropype.nodes.elementwise_math.Subtract",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "50960f07-b86d-44c3-b377-6369102d4c34"
        },
        "node6": {
            "class": "InterBeatIntervals",
            "module": "neuropype.nodes.exo_nodes.InterBeatIntervals",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "86109960-bc06-4dc1-bc88-9e414529c6d6"
        },
        "node7": {
            "class": "SlidingBuffer",
            "module": "neuropype.nodes.exo_nodes.SlidingBuffer",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shift_window": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 1
                },
                "window_length": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 60
                }
            },
            "uuid": "01dad1f3-d045-449a-8021-fa55a12e330a"
        },
        "node8": {
            "class": "CorrectEctopics",
            "module": "neuropype.nodes.exo_nodes.CorrectEctopics",
            "params": {
                "percentage": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 30
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "span": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 21
                }
            },
            "uuid": "fa329b22-6a1f-411d-8fa7-b4135f1fe791"
        },
        "node9": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "886496fc-e0d8-4ae2-86b7-b1f1b4559786"
        }
    },
    "version": 1.1
}</patch>
</scheme>
