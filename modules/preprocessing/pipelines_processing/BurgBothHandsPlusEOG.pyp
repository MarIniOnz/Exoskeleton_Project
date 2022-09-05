<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="Burg Both Hands With EOG Channels" version="2.0">
	<nodes>
		<node id="0" name="Strip Singleton Axis" position="(800, 600)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owstripsingletonaxis.OWStripSingletonAxis" title="Strip Frequency Axis" uuid="15c6b663-de3f-481d-b17e-d26831661a00" version="1.0.0" />
		<node id="1" name="Rename Channels" position="(700, 600)" project_name="NeuroPype" qualified_name="widgets.utilities.owrenamechannels.OWRenameChannels" title="Rename Channels" uuid="927bc2a3-dee4-4227-a5c9-8b3f27231501" version="1.0.0" />
		<node id="2" name="IIR Filter" position="(900, 300)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Lowpass IIR" uuid="caf48640-beb6-4274-936a-0cc11cd37d72" version="1.1.0" />
		<node id="3" name="Surface Laplace Filter" position="(700, 400)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owlaplacefilter.OWLaplaceFilter" title="Laplace" uuid="605b56de-9cda-4465-b288-f017766b57e4" version="1.0.0" />
		<node id="4" name="Pick Times" position="(1100, 400)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owpicktimes.OWPickTimes" title="Pick Times" uuid="50dfd23e-1f86-492f-9510-cdc03f1bfb75" version="1.0.0" />
		<node id="5" name="Dejitter Timestamps" position="(200, 400)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="5753cb7c-7a15-48d0-87d4-2bf987781b4c" version="1.0.0" />
		<node id="6" name="Estimate Update Rate" position="(600, 700)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owestimateupdaterate.OWEstimateUpdateRate" title="Estimate Update Rate" uuid="32a7fc72-112a-4456-97cc-72214819c458" version="1.0.0" />
		<node id="7" name="IIR Filter" position="(500, 400)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Notch IIR" uuid="b77f29fc-851e-46d8-8bfd-aa86abe108b3" version="1.1.0" />
		<node id="8" name="LSL Output" position="(1500, 500)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="be01411d-a1f4-4cc7-9724-5253de2bc360" version="1.0.0" />
		<node id="9" name="Single Pole Filter" position="(600, 600)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owsinglepolefilter.OWSinglePoleFilter" title="Single Pole Filter" uuid="b49e92c1-4fec-4295-9714-d585cf5ca024" version="1.0.0" />
		<node id="10" name="LSL Input" position="(100, 400)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL from Streaming Data" uuid="f63d8ae9-dee9-4496-892d-b3cf825ca7b1" version="1.0.0" />
		<node id="11" name="IIR Filter" position="(600, 400)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Notch IIR" uuid="44f69b9d-93e5-4890-afb7-07b9669c6385" version="1.1.0" />
		<node id="12" name="IIR Filter" position="(300, 400)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Highpass IIR" uuid="55dae379-0a5b-48a6-a533-a53b462f6667" version="1.1.0" />
		<node id="13" name="Segmentation" position="(400, 600)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="140d01d7-081b-43c8-a167-a173d68f5d32" version="1.0.1" />
		<node id="14" name="Concatenate Tensors" position="(1200, 500)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owconcatinputs.OWConcatInputs" title="Concatenate EOG and EEG" uuid="df078116-cb1d-4d43-af90-d6bec05855fd" version="1.0.0" />
		<node id="15" name="Power Spectrum (Burg)" position="(500, 600)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owburgspectrum.OWBurgSpectrum" title="Power Spectrum (Burg)" uuid="7b6c993c-58c6-41b2-bd55-478dbadeebf6" version="1.0.0" />
		<node id="16" name="IIR Filter" position="(900, 400)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Bandpass IIR" uuid="c74447a8-d314-4d48-8c1c-bdfb92ccc234" version="1.1.0" />
		<node id="17" name="Select Range" position="(800, 300)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Extract EOG" uuid="01aaa610-6f93-4b78-b668-0027ad6931a0" version="1.0.0" />
		<node id="18" name="Select Range" position="(800, 400)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Extract EEG" uuid="f32c0470-62c2-481d-95c9-b97d3ddfad40" version="1.0.0" />
		<node id="19" name="IIR Filter" position="(400.0, 400.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Lowpass IIR" uuid="44a3b725-d549-48f6-9973-bca7be93218c" version="1.1.0" />
		<node id="20" name="Override Sampling Rate" position="(1400, 500)" project_name="NeuroPype" qualified_name="widgets.utilities.owoverridesamplingrate.OWOverrideSamplingRate" title="Override Sampling Rate" uuid="b0ab32ff-2b4e-4b17-be47-aff6826f0780" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="1" sink_channel="Data2" sink_node_id="14" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data1" sink_node_id="4" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="4" sink_channel="Data2" sink_node_id="4" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="6" sink_channel="Data1" sink_node_id="14" source_channel="Outdata" source_node_id="4" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="18" />
		<link enabled="true" id="18" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="19" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="20" source_channel="Outdata" source_node_id="14" />
		<link enabled="true" id="21" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="20" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="literal" node_id="0">{'axis': 'frequency', 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAwAAAByZXBsYWNlX2V4cHJxAVgEAAAAwrVcMXECWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQNjc2lwCl91bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NC5RdENvcmVxBVgKAAAAUUJ5dGVB
cnJheXEGQy4B2dDLAAEAAAAAD2AAAAJUAAAQ+gAAA30AAA9rAAACgQAAEO8AAANyAAAAAQAAcQeF
cQiHcQlScQpYCwAAAHNlYXJjaF9leHBycQtYCAAAAChDXGQpezF9cQxYDgAAAHNldF9icmVha3Bv
aW50cQ2JWAcAAABzdHJlYW1zcQ5dcQ9YBwAAAHZlcmJvc2VxEIl1Lg==
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGSwVhWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAcAAABs
b3dwYXNzcQlYEAAAAG9mZmxpbmVfZmlsdGZpbHRxColYBQAAAG9yZGVycQtLAlgJAAAAcGFzc19s
b3NzcQxHQAgAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxDWNzaXAKX3VucGlja2xlX3R5
cGUKcQ5YDAAAAFB5UXQ0LlF0Q29yZXEPWAoAAABRQnl0ZUFycmF5cRBDLgHZ0MsAAQAAAAAPVgAA
AggAABEEAAADygAAD2EAAAI1AAAQ+QAAA78AAAABAABxEYVxEodxE1JxFFgOAAAAc2V0X2JyZWFr
cG9pbnRxFYlYCgAAAHN0b3BfYXR0ZW5xFkdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAoAAABDM193ZWlnaHRzcQF9cQIoWAIAAABDM3EDSwFYAgAAAEN6cQRHv9AAAAAAAABY
AgAAAEYzcQVHv9AAAAAAAABYAgAAAFAzcQZHv9AAAAAAAABYAgAAAFQ3cQdHv9AAAAAAAAB1WAoA
AABDNF93ZWlnaHRzcQh9cQkoWAIAAABDNHEKSwFoBEe/0AAAAAAAAFgCAAAARjRxC0e/0AAAAAAA
AFgCAAAAUDRxDEe/0AAAAAAAAFgCAAAAVDhxDUe/0AAAAAAAAHVYCwAAAEVPR193ZWlnaHRzcQ59
cQ8oWAIAAABGN3EQSwFYAgAAAEY4cRFK/////3VYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEmNz
aXAKX3VucGlja2xlX3R5cGUKcRNYDAAAAFB5UXQ0LlF0Q29yZXEUWAoAAABRQnl0ZUFycmF5cRVD
LgHZ0MsAAQAAAAAEYgAAAcIAAAXfAAACzgAABG0AAAHvAAAF1AAAAsMAAAAAAABxFoVxF4dxGFJx
GVgOAAAAc2V0X2JyZWFrcG9pbnRxGol1Lg==
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAYAAABjaHVua3NxAV1xAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEDY3NpcApfdW5w
aWNrbGVfdHlwZQpxBFgMAAAAUHlRdDQuUXRDb3JlcQVYCgAAAFFCeXRlQXJyYXlxBkMuAdnQywAB
AAAAABAiAAACmQAAEZ8AAANnAAAQLQAAAsYAABGUAAADXAAAAAEAAHEHhXEIh3EJUnEKWA4AAABz
ZXRfYnJlYWtwb2ludHELiXUu
</properties>
		<properties format="literal" node_id="5">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="literal" node_id="6">{'display': True, 'estimator': 'mean', 'ignore_empty_packets': False, 'measure_type': 'rate', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'time_window': 5}</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGNoZWJ5MXEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEstSzdlWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAgA
AABiYW5kc3RvcHEJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUAAABvcmRlcnELSwNYCQAAAHBh
c3NfbG9zc3EMRz+5mZmZmZmaWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ1jc2lwCl91bnBpY2ts
ZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJheXEQQy4B2dDLAAEAAAAA
D1YAAAIIAAARBAAAA8oAAA9hAAACNQAAEPkAAAO/AAAAAQAAcRGFcRKHcRNScRRYDgAAAHNldF9i
cmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYAAAAAHEEWBAAAABtYXJrZXJfc291cmNlX2lkcQVoBFgMAAAAbWF4X2J1
ZmZlcmVkcQZLPFgXAAAAcmVzZXRfaWZfbGFiZWxzX2NoYW5nZWRxB4lYEwAAAHNhdmVkV2lkZ2V0
R2VvbWV0cnlxCGNzaXAKX3VucGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ0LlF0Q29yZXEKWAoAAABR
Qnl0ZUFycmF5cQtDLgHZ0MsAAQAAAAAPZgAAAc0AABD0AAAEBQAAD3EAAAH6AAAQ6QAAA/oAAAAB
AABxDIVxDYdxDlJxD1gMAAAAc2VuZF9tYXJrZXJzcRCJWA4AAABzZXRfYnJlYWtwb2ludHERiVgJ
AAAAc291cmNlX2lkcRJYEAAAAFByZXByb2Nlc3NlZERhdGFxE1gFAAAAc3JhdGVxFFgNAAAAKHVz
ZSBkZWZhdWx0KXEVWAsAAABzdHJlYW1fbmFtZXEWWBAAAABQcmVwcm9jZXNzZWREYXRhcRdYCwAA
AHN0cmVhbV90eXBlcRhYAwAAAEVFR3EZWBMAAAB1c2VfZGF0YV90aW1lc3RhbXBzcRqJWBYAAAB1
c2VfbnVtcHlfb3B0aW1pemF0aW9ucRuIdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA0AAABzYW1wbGluZ19yYXRlcQFLGVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXECY3Np
cApfdW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRlQXJyYXlxBUMu
AdnQywABAAAAAA9uAAACcgAAEOsAAANfAAAPeQAAAp8AABDgAAADVAAAAAEAAHEGhXEHh3EIUnEJ
WA4AAABzZXRfYnJlYWtwb2ludHEKiVgKAAAAdGltZV9jb25zdHELRz/gAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
ClgMAAAAbWF4X2NodW5rbGVucQhLAFgMAAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVs
dClxClgFAAAAcXVlcnlxC1gfAAAAdHlwZT0nRUVHJyBhbmQgbmFtZT0nU291cmNlRUVHJ3EMWAcA
AAByZWNvdmVycQ2IWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEORz/gAAAAAAAAWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVx
EVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEAAAAAD1AAAAH4AAARCQAAA9kAAA9bAAACJQAAEP4A
AAPOAAAAAQAAcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGNoZWJ5MXEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEstSzdlWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAgA
AABiYW5kc3RvcHEJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUAAABvcmRlcnELSwNYCQAAAHBh
c3NfbG9zc3EMRz+5mZmZmZmaWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ1jc2lwCl91bnBpY2ts
ZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJheXEQQy4B2dDLAAEAAAAA
EAoAAAIfAAARuAAAA+EAABAVAAACTAAAEa0AAAPWAAAAAQAAcRGFcRKHcRNScRRYDgAAAHNldF9i
cmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGRz+5mZmZmZmaYVgLAAAAaWdub3JlX25hbnNxB4lYBAAAAG1vZGVx
CFgIAAAAaGlnaHBhc3NxCVgQAAAAb2ZmbGluZV9maWx0ZmlsdHEKiVgFAAAAb3JkZXJxC0sBWAkA
AABwYXNzX2xvc3NxDEdACAAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXENY3NpcApfdW5w
aWNrbGVfdHlwZQpxDlgMAAAAUHlRdDQuUXRDb3JlcQ9YCgAAAFFCeXRlQXJyYXlxEEMuAdnQywAB
AAAAAAXRAAACCAAAB38AAAPKAAAF3AAAAjUAAAd0AAADvwAAAAAAAHERhXESh3ETUnEUWA4AAABz
ZXRfYnJlYWtwb2ludHEViVgKAAAAc3RvcF9hdHRlbnEWR0BJAAAAAAAAdS4=
</properties>
		<properties format="literal" node_id="13">{'keep_marker_chunk': False, 'max_gap_length': 0.2, 'online_epoching': 'sliding', 'sample_offset': 0, 'savedWidgetGeometry': None, 'select_markers': '(use default)', 'set_breakpoint': False, 'time_bounds': [0, 0.4], 'verbose': False}</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWA0AAABhbGxvd19tYXJrZXJzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNYDQAAAGNv
cnJlY3Rfb3JkZXJxBIhYCgAAAGNyZWF0ZV9uZXdxBYlYCgAAAHByb3BlcnRpZXNxBlgNAAAAKHVz
ZSBkZWZhdWx0KXEHWA8AAAByZXF1aXJlZF9pbnB1dHNxCEsAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVB
cnJheXEMQy4B2dDLAAEAAAAAAwIAAAFAAAAEfwAAAqMAAAMNAAABbQAABHQAAAKYAAAAAAAAcQ2F
cQ6HcQ9ScRBYDgAAAHNldF9icmVha3BvaW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWAkAAABiaW5fd2lkdGhxAUsDWAsAAABjcmVhdGVfYmluc3ECiFgNAAAAZXZhbHNfcGVy
X2JpbnEDSw9YAwAAAGZvaXEESwtYBQAAAG5iaW5zcQVLAVgEAAAAbmZmdHEGWA0AAAAodXNlIGRl
ZmF1bHQpcQdYCwAAAG91dHB1dF90eXBlcQhYCQAAAGFtcGxpdHVkZXEJWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQpjc2lwCl91bnBpY2tsZV90eXBlCnELWAwAAABQeVF0NC5RdENvcmVxDFgKAAAA
UUJ5dGVBcnJheXENQy4B2dDLAAEAAAAADycAAAImAAARMwAAA6wAAA8yAAACUwAAESgAAAOhAAAA
AQAAcQ6FcQ+HcRBScRFYDgAAAHNldF9icmVha3BvaW50cRKJdS4=
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSx5lWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAgA
AABiYW5kcGFzc3EJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUAAABvcmRlcnELSwNYCQAAAHBh
c3NfbG9zc3EMR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ1jc2lwCl91bnBpY2ts
ZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJheXEQQy4B2dDLAAEAAAAA
EAoAAAIfAAARuAAAA+EAABAVAAACTAAAEa0AAAPWAAAAAQAAcRGFcRKHcRNScRRYDgAAAHNldF9i
cmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAFsgAAAlQAAAd/AAADfQAABb0A
AAKBAAAHdAAAA3IAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ1YCwAAAGJpcG9s
YXIgRU9HcQ5hWA4AAABzZXRfYnJlYWtwb2ludHEPiVgEAAAAdW5pdHEQWAUAAABuYW1lc3ERdS4=
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAFsgAAAmsAAAd/AAADlAAABb0A
AAKYAAAHdAAAA4kAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ0oWAIAAABDM3EO
WAIAAABDNHEPZVgOAAAAc2V0X2JyZWFrcG9pbnRxEIlYBAAAAHVuaXRxEVgFAAAAbmFtZXNxEnUu
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGS0ZhWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAcAAABs
b3dwYXNzcQlYEAAAAG9mZmxpbmVfZmlsdGZpbHRxColYBQAAAG9yZGVycQtLAlgJAAAAcGFzc19s
b3NzcQxHQAgAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxDWNzaXAKX3VucGlja2xlX3R5
cGUKcQ5YDAAAAFB5UXQ0LlF0Q29yZXEPWAoAAABRQnl0ZUFycmF5cRBDLgHZ0MsAAQAAAAAC6gAA
AREAAASYAAAC0wAAAvUAAAE+AAAEjQAAAsgAAAAAAABxEYVxEodxE1JxFFgOAAAAc2V0X2JyZWFr
cG9pbnRxFYlYCgAAAHN0b3BfYXR0ZW5xFkdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWBsAAABjaGFuZ2VfdHJpZ2dlcnNfc3RhdGVfcmVzZXRxAYlYDQAAAHNhbXBsaW5nX3Jh
dGVxAksZWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQNjc2lwCl91bnBpY2tsZV90eXBlCnEEWAwA
AABQeVF0NC5RdENvcmVxBVgKAAAAUUJ5dGVBcnJheXEGQy4B2dDLAAEAAAAAAwIAAAF8AAAEfwAA
AmcAAAMNAAABqQAABHQAAAJcAAAAAAAAcQeFcQiHcQlScQpYDgAAAHNldF9icmVha3BvaW50cQuJ
dS4=
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
            "node2",
            "data",
            "node1",
            "data"
        ],
        [
            "node1",
            "data",
            "node15",
            "data2"
        ],
        [
            "node1",
            "data",
            "node5",
            "data1"
        ],
        [
            "node10",
            "data",
            "node2",
            "data"
        ],
        [
            "node3",
            "data",
            "node5",
            "data2"
        ],
        [
            "node12",
            "data",
            "node4",
            "data"
        ],
        [
            "node5",
            "outdata",
            "node15",
            "data1"
        ],
        [
            "node11",
            "data",
            "node6",
            "data"
        ],
        [
            "node6",
            "data",
            "node13",
            "data"
        ],
        [
            "node16",
            "data",
            "node7",
            "data"
        ],
        [
            "node16",
            "data",
            "node10",
            "data"
        ],
        [
            "node8",
            "data",
            "node12",
            "data"
        ],
        [
            "node15",
            "outdata",
            "node21",
            "data"
        ],
        [
            "node17",
            "data",
            "node14",
            "data"
        ],
        [
            "node14",
            "data",
            "node16",
            "data"
        ],
        [
            "node4",
            "data",
            "node18",
            "data"
        ],
        [
            "node4",
            "data",
            "node19",
            "data"
        ],
        [
            "node18",
            "data",
            "node3",
            "data"
        ],
        [
            "node19",
            "data",
            "node17",
            "data"
        ],
        [
            "node13",
            "data",
            "node20",
            "data"
        ],
        [
            "node20",
            "data",
            "node8",
            "data"
        ],
        [
            "node21",
            "data",
            "node9",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "StripSingletonAxis",
            "module": "neuropype.nodes.tensor_math.StripSingletonAxis",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "frequency"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "15c6b663-de3f-481d-b17e-d26831661a00"
        },
        "node10": {
            "class": "SinglePoleFilter",
            "module": "neuropype.nodes.exo_nodes.SinglePoleFilter",
            "params": {
                "sampling_rate": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 25
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_const": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                }
            },
            "uuid": "b49e92c1-4fec-4295-9714-d585cf5ca024"
        },
        "node11": {
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
                    "customized": true,
                    "type": "IntPort",
                    "value": 10
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "type='EEG' and name='SourceEEG'"
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
            "uuid": "f63d8ae9-dee9-4496-892d-b3cf825ca7b1"
        },
        "node12": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "cheby1"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        45,
                        55
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
                    "value": "bandstop"
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
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.1
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
            "uuid": "44f69b9d-93e5-4890-afb7-07b9669c6385"
        },
        "node13": {
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
                        0.1
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
                    "value": "highpass"
                },
                "offline_filtfilt": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "order": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 1
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
            "uuid": "55dae379-0a5b-48a6-a533-a53b462f6667"
        },
        "node14": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "online_epoching": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "sliding"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        0.4
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "140d01d7-081b-43c8-a167-a173d68f5d32"
        },
        "node15": {
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
            "uuid": "df078116-cb1d-4d43-af90-d6bec05855fd"
        },
        "node16": {
            "class": "BurgSpectrum",
            "module": "neuropype.nodes.exo_nodes.BurgSpectrum",
            "params": {
                "bin_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 3
                },
                "create_bins": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "evals_per_bin": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 15
                },
                "foi": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 11
                },
                "nbins": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "nfft": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "output_type": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "amplitude"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "7b6c993c-58c6-41b2-bd55-478dbadeebf6"
        },
        "node17": {
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
                        1,
                        30
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
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
            "uuid": "c74447a8-d314-4d48-8c1c-bdfb92ccc234"
        },
        "node18": {
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
                        "bipolar EOG"
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
            "uuid": "01aaa610-6f93-4b78-b668-0027ad6931a0"
        },
        "node19": {
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
                        "C3",
                        "C4"
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
            "uuid": "f32c0470-62c2-481d-95c9-b97d3ddfad40"
        },
        "node2": {
            "class": "RenameChannels",
            "module": "neuropype.nodes.utilities.RenameChannels",
            "params": {
                "replace_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "\u00b5\\1"
                },
                "search_expr": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(C\\d){1}"
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
            "uuid": "927bc2a3-dee4-4227-a5c9-8b3f27231501"
        },
        "node20": {
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
                        70
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
                    "value": 2
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
            "uuid": "44a3b725-d549-48f6-9973-bca7be93218c"
        },
        "node21": {
            "class": "OverrideSamplingRate",
            "module": "neuropype.nodes.utilities.OverrideSamplingRate",
            "params": {
                "change_triggers_state_reset": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "sampling_rate": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 25
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b0ab32ff-2b4e-4b17-be47-aff6826f0780"
        },
        "node3": {
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
                        5
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
                    "value": 2
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
            "uuid": "caf48640-beb6-4274-936a-0cc11cd37d72"
        },
        "node4": {
            "class": "LaplaceFilter",
            "module": "neuropype.nodes.exo_nodes.LaplaceFilter",
            "params": {
                "C3_weights": {
                    "customized": true,
                    "type": "DictPort",
                    "value": {
                        "C3": 1,
                        "Cz": -0.25,
                        "F3": -0.25,
                        "P3": -0.25,
                        "T7": -0.25
                    }
                },
                "C4_weights": {
                    "customized": true,
                    "type": "DictPort",
                    "value": {
                        "C4": 1,
                        "Cz": -0.25,
                        "F4": -0.25,
                        "P4": -0.25,
                        "T8": -0.25
                    }
                },
                "EOG_weights": {
                    "customized": true,
                    "type": "DictPort",
                    "value": {
                        "F7": 1,
                        "F8": -1
                    }
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "605b56de-9cda-4465-b288-f017766b57e4"
        },
        "node5": {
            "class": "PickTimes",
            "module": "neuropype.nodes.exo_nodes.PickTimes",
            "params": {
                "chunks": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "50dfd23e-1f86-492f-9510-cdc03f1bfb75"
        },
        "node6": {
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
            "uuid": "5753cb7c-7a15-48d0-87d4-2bf987781b4c"
        },
        "node7": {
            "class": "EstimateUpdateRate",
            "module": "neuropype.nodes.diagnostics.EstimateUpdateRate",
            "params": {
                "display": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "estimator": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "mean"
                },
                "ignore_empty_packets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "measure_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "rate"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_window": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                }
            },
            "uuid": "32a7fc72-112a-4456-97cc-72214819c458"
        },
        "node8": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "cheby1"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        45,
                        55
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
                    "value": "bandstop"
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
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.1
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
            "uuid": "b77f29fc-851e-46d8-8bfd-aa86abe108b3"
        },
        "node9": {
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
                    "customized": true,
                    "type": "StringPort",
                    "value": ""
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
                    "value": "PreprocessedData"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "PreprocessedData"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numpy_optimization": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "be01411d-a1f4-4cc7-9724-5253de2bc360"
        }
    },
    "version": 1.1
}</patch>
</scheme>
