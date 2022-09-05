<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="Burg Both Hands Extracted EOG" version="2.0">
	<nodes>
		<node id="0" name="IIR Filter" position="(400, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Lowpass IIR" uuid="cb04221c-f792-4ccd-bb39-36602eb12ee2" version="1.1.0" />
		<node id="1" name="IIR Filter" position="(600, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Notch IIR" uuid="8d5354e0-c8f4-4f51-b367-ee1bf6fd006a" version="1.1.0" />
		<node id="2" name="IIR Filter" position="(300, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Highpass IIR" uuid="477471f3-e077-472f-9033-f6d77cfe22ef" version="1.1.0" />
		<node id="3" name="IIR Filter" position="(500, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Notch IIR" uuid="61c37e71-9364-4fe2-b618-cc17dd067082" version="1.1.0" />
		<node id="4" name="Surface Laplace Filter" position="(700, 200)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owlaplacefilter.OWLaplaceFilter" title="Laplace" uuid="b52e204b-bb72-4b58-b121-6033bba81e17" version="1.0.0" />
		<node id="5" name="IIR Filter" position="(900, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Bandpass IIR" uuid="56f02ce7-724f-4169-88a1-155ee769a0f6" version="1.1.0" />
		<node id="6" name="IIR Filter" position="(900, 100)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Lowpass IIR" uuid="173f60f4-7a11-4386-82b4-b13094d3f3bc" version="1.1.0" />
		<node id="7" name="Single Pole Filter" position="(700, 400)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owsinglepolefilter.OWSinglePoleFilter" title="Single Pole Filter" uuid="a2e3691e-2b08-4e5c-ba6c-0df84560ed69" version="1.0.0" />
		<node id="8" name="Dejitter Timestamps" position="(200, 200)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="3d135c80-0880-4de1-a03b-c4219d625b87" version="1.0.0" />
		<node id="9" name="Estimate Update Rate" position="(700, 500)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owestimateupdaterate.OWEstimateUpdateRate" title="Estimate Update Rate" uuid="c350cae3-5926-4706-a819-aef2cdb03ffd" version="1.0.0" />
		<node id="10" name="Power Spectrum (Burg)" position="(600, 400)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owburgspectrum.OWBurgSpectrum" title="Power Spectrum (Burg)" uuid="c816ef84-71aa-4d1f-afc7-890217a3d0e9" version="1.0.0" />
		<node id="11" name="Strip Singleton Axis" position="(900, 400)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owstripsingletonaxis.OWStripSingletonAxis" title="Strip Frequency Axis" uuid="21372a12-cee8-44ad-801d-050eed285019" version="1.0.0" />
		<node id="12" name="Concatenate Tensors" position="(1200, 300)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owconcatinputs.OWConcatInputs" title="Concatenate EOG and EEG" uuid="1f044e0a-76ad-41b8-bce2-41ed0623da53" version="1.0.0" />
		<node id="13" name="Rename Channels" position="(800, 400)" project_name="NeuroPype" qualified_name="widgets.utilities.owrenamechannels.OWRenameChannels" title="Rename Channels" uuid="d0194686-e76c-4995-b4e8-bda0751010e9" version="1.0.0" />
		<node id="14" name="LSL Output" position="(1500, 300)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="0ca774ca-43c3-4dde-8f99-0d4ebb61a0b5" version="1.0.0" />
		<node id="15" name="Segmentation" position="(500, 400)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="137ed69e-a9b9-48c9-baa9-346e63fb8c91" version="1.0.1" />
		<node id="16" name="Pick Times" position="(1100, 200)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owpicktimes.OWPickTimes" title="Pick Times" uuid="1b881cd2-91ad-4347-b731-b2ab2cec101b" version="1.0.0" />
		<node id="17" name="LSL Input" position="(100, 200)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL from Streaming Data" uuid="b0b05fe4-875b-4897-a6a1-ba2e60ebfff9" version="1.0.0" />
		<node id="18" name="Select Range" position="(800, 100)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Extract EOG" uuid="413d40a5-a1ab-47b4-a162-bc6bc71238e1" version="1.0.0" />
		<node id="19" name="Select Range" position="(800, 200)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Extract EEG" uuid="4bdb26a7-46c5-447a-abe4-61281a2dd200" version="1.0.0" />
		<node id="20" name="Override Sampling Rate" position="(1400, 300)" project_name="NeuroPype" qualified_name="widgets.utilities.owoverridesamplingrate.OWOverrideSamplingRate" title="Override Sampling Rate" uuid="10d91a32-9cb8-45ad-a216-1415c60d5c35" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="4" sink_channel="Data2" sink_node_id="12" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="9" sink_channel="Data1" sink_node_id="16" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="10" sink_channel="Data1" sink_node_id="12" source_channel="Outdata" source_node_id="16" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="15" sink_channel="Data2" sink_node_id="16" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="18" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="18" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="19" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="20" source_channel="Outdata" source_node_id="12" />
		<link enabled="true" id="21" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="20" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGS0ZhWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAcAAABs
b3dwYXNzcQlYEAAAAG9mZmxpbmVfZmlsdGZpbHRxColYBQAAAG9yZGVycQtLAlgJAAAAcGFzc19s
b3NzcQxHQAgAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxDWNzaXAKX3VucGlja2xlX3R5
cGUKcQ5YDAAAAFB5UXQ0LlF0Q29yZXEPWAoAAABRQnl0ZUFycmF5cRBDLgHZ0MsAAQAAAAAC6gAA
AREAAASYAAAC0wAAAvUAAAE+AAAEjQAAAsgAAAAAAABxEYVxEodxE1JxFFgOAAAAc2V0X2JyZWFr
cG9pbnRxFYlYCgAAAHN0b3BfYXR0ZW5xFkdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGNoZWJ5MXEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEstSzdlWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAgA
AABiYW5kc3RvcHEJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUAAABvcmRlcnELSwNYCQAAAHBh
c3NfbG9zc3EMRz+5mZmZmZmaWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ1jc2lwCl91bnBpY2ts
ZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJheXEQQy4B2dDLAAEAAAAA
AuoAAAERAAAEmAAAAtMAAAL1AAABPgAABI0AAALIAAAAAAAAcRGFcRKHcRNScRRYDgAAAHNldF9i
cmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGRz+5mZmZmZmaYVgLAAAAaWdub3JlX25hbnNxB4lYBAAAAG1vZGVx
CFgIAAAAaGlnaHBhc3NxCVgQAAAAb2ZmbGluZV9maWx0ZmlsdHEKiVgFAAAAb3JkZXJxC0sBWAkA
AABwYXNzX2xvc3NxDEdACAAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXENY3NpcApfdW5w
aWNrbGVfdHlwZQpxDlgMAAAAUHlRdDQuUXRDb3JlcQ9YCgAAAFFCeXRlQXJyYXlxEEMuAdnQywAB
AAAAAALqAAABEQAABJgAAALTAAAC9QAAAT4AAASNAAACyAAAAAAAAHERhXESh3ETUnEUWA4AAABz
ZXRfYnJlYWtwb2ludHEViVgKAAAAc3RvcF9hdHRlbnEWR0BJAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGNoZWJ5MXEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEstSzdlWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAgA
AABiYW5kc3RvcHEJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUAAABvcmRlcnELSwNYCQAAAHBh
c3NfbG9zc3EMRz+5mZmZmZmaWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ1jc2lwCl91bnBpY2ts
ZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJheXEQQy4B2dDLAAEAAAAA
AuoAAAERAAAEmAAAAtMAAAL1AAABPgAABI0AAALIAAAAAAAAcRGFcRKHcRNScRRYDgAAAHNldF9i
cmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAoAAABDM193ZWlnaHRzcQF9cQIoWAIAAABDM3EDSwFYAgAAAEYzcQRHv9AAAAAAAABY
AgAAAEN6cQVHv9AAAAAAAABYAgAAAFAzcQZHv9AAAAAAAABYAgAAAFQ3cQdHv9AAAAAAAAB1WAoA
AABDNF93ZWlnaHRzcQh9cQkoWAIAAABDNHEKSwFYAgAAAEY0cQtHv9AAAAAAAABYAgAAAEN6cQxH
v9AAAAAAAABYAgAAAFA0cQ1Hv9AAAAAAAABYAgAAAFQ4cQ5Hv9AAAAAAAAB1WAsAAABFT0dfd2Vp
Z2h0c3EPfXEQKFgCAAAARjdxEUsBWAIAAABGOHESSv////91WBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NC5RdENvcmVxFVgKAAAAUUJ5dGVB
cnJheXEWQy4B2dDLAAEAAAAAA8AAAAH+AAAFPQAAAzAAAAPLAAACKwAABTIAAAMlAAAAAAAAcReF
cRiHcRlScRpYDgAAAHNldF9icmVha3BvaW50cRuJdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEsBSx5lWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAgA
AABiYW5kcGFzc3EJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUAAABvcmRlcnELSwNYCQAAAHBh
c3NfbG9zc3EMR0AIAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ1jc2lwCl91bnBpY2ts
ZV90eXBlCnEOWAwAAABQeVF0NC5RdENvcmVxD1gKAAAAUUJ5dGVBcnJheXEQQy4B2dDLAAEAAAAA
BQ0AAADzAAAGuwAAAtsAAAUYAAABIAAABrAAAALQAAAAAAAAcRGFcRKHcRNScRRYDgAAAHNldF9i
cmVha3BvaW50cRWJWAoAAABzdG9wX2F0dGVucRZHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGSwVhWAsAAABpZ25vcmVfbmFuc3EHiVgEAAAAbW9kZXEIWAcAAABs
b3dwYXNzcQlYEAAAAG9mZmxpbmVfZmlsdGZpbHRxColYBQAAAG9yZGVycQtLAlgJAAAAcGFzc19s
b3NzcQxHQAgAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxDWNzaXAKX3VucGlja2xlX3R5
cGUKcQ5YDAAAAFB5UXQ0LlF0Q29yZXEPWAoAAABRQnl0ZUFycmF5cRBDLgHZ0MsAAQAAAAAFQQAA
AOoAAAbvAAACrAAABUwAAAEXAAAG5AAAAqEAAAAAAABxEYVxEodxE1JxFFgOAAAAc2V0X2JyZWFr
cG9pbnRxFYlYCgAAAHN0b3BfYXR0ZW5xFkdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABzYW1wbGluZ19yYXRlcQFLGVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXECY3Np
cApfdW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRlQXJyYXlxBUMu
AdnQywABAAAAAAMCAAABewAABH8AAAKOAAADDQAAAagAAAR0AAACgwAAAAAAAHEGhXEHh3EIUnEJ
WA4AAABzZXRfYnJlYWtwb2ludHEKiVgKAAAAdGltZV9jb25zdHELRz/gAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlj
a2xlX3R5cGUKcQVYDAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAA
AAAC5gAAAV0AAASbAAAChgAAAvEAAAGKAAAEkAAAAnsAAAAAAABxCIVxCYdxClJxC1gOAAAAc2V0
X2JyZWFrcG9pbnRxDIlYDgAAAHdhcm11cF9zYW1wbGVzcQ1K/////3Uu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWAcAAABkaXNwbGF5cQGIWAkAAABlc3RpbWF0b3JxAlgEAAAAbWVhbnEDWBQAAABpZ25v
cmVfZW1wdHlfcGFja2V0c3EEiVgMAAAAbWVhc3VyZV90eXBlcQVYBAAAAHJhdGVxBlgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEHY3NpcApfdW5waWNrbGVfdHlwZQpxCFgMAAAAUHlRdDQuUXRDb3Jl
cQlYCgAAAFFCeXRlQXJyYXlxCkMuAdnQywABAAAAAA9uAAACRgAAEOsAAAOMAAAPeQAAAnMAABDg
AAADgQAAAAEAAHELhXEMh3ENUnEOWA4AAABzZXRfYnJlYWtwb2ludHEPiVgLAAAAdGltZV93aW5k
b3dxEEsFdS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAkAAABiaW5fd2lkdGhxAUsDWAsAAABjcmVhdGVfYmluc3ECiFgNAAAAZXZhbHNfcGVy
X2JpbnEDSw9YAwAAAGZvaXEESwtYBQAAAG5iaW5zcQVLAVgEAAAAbmZmdHEGWA0AAAAodXNlIGRl
ZmF1bHQpcQdYCwAAAG91dHB1dF90eXBlcQhYCQAAAGFtcGxpdHVkZXEJWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQpjc2lwCl91bnBpY2tsZV90eXBlCnELWAwAAABQeVF0NC5RdENvcmVxDFgKAAAA
UUJ5dGVBcnJheXENQy4B2dDLAAEAAAAAAsMAAAEfAAAEvwAAAsQAAALOAAABTAAABLQAAAK5AAAA
AAAAcQ6FcQ+HcRBScRFYDgAAAHNldF9icmVha3BvaW50cRKJdS4=
</properties>
		<properties format="literal" node_id="11">{'axis': 'frequency', 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA0AAABhbGxvd19tYXJrZXJzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNYDQAAAGNv
cnJlY3Rfb3JkZXJxBIhYCgAAAGNyZWF0ZV9uZXdxBYlYCgAAAHByb3BlcnRpZXNxBlgNAAAAKHVz
ZSBkZWZhdWx0KXEHWA8AAAByZXF1aXJlZF9pbnB1dHNxCEsAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVB
cnJheXEMQy4B2dDLAAEAAAAAAwIAAAFAAAAEfwAAAqMAAAMNAAABbQAABHQAAAKYAAAAAAAAcQ2F
cQ6HcQ9ScRBYDgAAAHNldF9icmVha3BvaW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAwAAAByZXBsYWNlX2V4cHJxAVgEAAAAwrVcMXECWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQNjc2lwCl91bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NC5RdENvcmVxBVgKAAAAUUJ5dGVB
cnJheXEGQy4B2dDLAAEAAAAAAvQAAAFdAAAEjgAAAoYAAAL/AAABigAABIMAAAJ7AAAAAAAAcQeF
cQiHcQlScQpYCwAAAHNlYXJjaF9leHBycQtYCAAAAChDXGQpezF9cQxYDgAAAHNldF9icmVha3Bv
aW50cQ2JWAcAAABzdHJlYW1zcQ5dcQ9YBwAAAHZlcmJvc2VxEIl1Lg==
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYAAAAAHEEWBAAAABtYXJrZXJfc291cmNlX2lkcQVoBFgMAAAAbWF4X2J1
ZmZlcmVkcQZLPFgXAAAAcmVzZXRfaWZfbGFiZWxzX2NoYW5nZWRxB4lYEwAAAHNhdmVkV2lkZ2V0
R2VvbWV0cnlxCGNzaXAKX3VucGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ0LlF0Q29yZXEKWAoAAABR
Qnl0ZUFycmF5cQtDLgHZ0MsAAQAAAAAC+gAAANYAAASIAAADDgAAAwUAAAEDAAAEfQAAAwMAAAAA
AABxDIVxDYdxDlJxD1gMAAAAc2VuZF9tYXJrZXJzcRCJWA4AAABzZXRfYnJlYWtwb2ludHERiVgJ
AAAAc291cmNlX2lkcRJYEAAAAFByZXByb2Nlc3NlZERhdGFxE1gFAAAAc3JhdGVxFFgNAAAAKHVz
ZSBkZWZhdWx0KXEVWAsAAABzdHJlYW1fbmFtZXEWWBAAAABQcmVwcm9jZXNzZWREYXRhcRdYCwAA
AHN0cmVhbV90eXBlcRhYAwAAAEVFR3EZWBMAAAB1c2VfZGF0YV90aW1lc3RhbXBzcRqJWBYAAAB1
c2VfbnVtcHlfb3B0aW1pemF0aW9ucRuIdS4=
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgPAAAAb25saW5lX2Vwb2NoaW5ncQNYBwAAAHNsaWRpbmdxBFgNAAAAc2FtcGxlX29mZnNl
dHEFSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUKcQdYDAAA
AFB5UXQ0LlF0Q29yZXEIWAoAAABRQnl0ZUFycmF5cQlDLgHZ0MsAAQAAAAAC9QAAATAAAASNAAAC
tAAAAwAAAAFdAAAEggAAAqkAAAAAAABxCoVxC4dxDFJxDVgOAAAAc2VsZWN0X21hcmtlcnNxDlgN
AAAAKHVzZSBkZWZhdWx0KXEPWA4AAABzZXRfYnJlYWtwb2ludHEQiVgLAAAAdGltZV9ib3VuZHNx
EV1xEihLAEc/2ZmZmZmZmmVYBwAAAHZlcmJvc2VxE4l1Lg==
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAYAAABjaHVua3NxAV1xAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEDY3NpcApfdW5w
aWNrbGVfdHlwZQpxBFgMAAAAUHlRdDQuUXRDb3JlcQVYCgAAAFFCeXRlQXJyYXlxBkMuAdnQywAB
AAAAAAMCAAABiwAABH8AAAJZAAADDQAAAbgAAAR0AAACTgAAAAAAAHEHhXEIh3EJUnEKWA4AAABz
ZXRfYnJlYWtwb2ludHELiXUu
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
ClgMAAAAbWF4X2NodW5rbGVucQhLAFgMAAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVs
dClxClgFAAAAcXVlcnlxC1gfAAAAdHlwZT0nRUVHJyBhbmQgbmFtZT0nU291cmNlRUVHJ3EMWAcA
AAByZWNvdmVycQ2IWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEORz/gAAAAAAAAWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVx
EVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEAAAAAAuQAAAEBAAAEnQAAAuIAAALvAAABLgAABJIA
AALXAAAAAAAAcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJdS4=
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAFsgAAAlQAAAd/AAADfQAABb0A
AAKBAAAHdAAAA3IAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ1YCwAAAGJpcG9s
YXIgRU9HcQ5hWA4AAABzZXRfYnJlYWtwb2ludHEPiVgEAAAAdW5pdHEQWAUAAABuYW1lc3ERdS4=
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAFsgAAAlQAAAd/AAADfQAABb0A
AAKBAAAHdAAAA3IAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ0oWAIAAABDM3EO
WAIAAABDNHEPZVgOAAAAc2V0X2JyZWFrcG9pbnRxEIlYBAAAAHVuaXRxEVgFAAAAbmFtZXNxEnUu
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWBsAAABjaGFuZ2VfdHJpZ2dlcnNfc3RhdGVfcmVzZXRxAYhYDQAAAHNhbXBsaW5nX3Jh
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
            "node3",
            "data",
            "node1",
            "data"
        ],
        [
            "node1",
            "data",
            "node4",
            "data"
        ],
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
            "data"
        ],
        [
            "node12",
            "data",
            "node13",
            "data2"
        ],
        [
            "node12",
            "data",
            "node17",
            "data1"
        ],
        [
            "node13",
            "outdata",
            "node21",
            "data"
        ],
        [
            "node8",
            "data",
            "node14",
            "data"
        ],
        [
            "node14",
            "data",
            "node12",
            "data"
        ],
        [
            "node6",
            "data",
            "node16",
            "data"
        ],
        [
            "node16",
            "data",
            "node11",
            "data"
        ],
        [
            "node17",
            "outdata",
            "node13",
            "data1"
        ],
        [
            "node18",
            "data",
            "node9",
            "data"
        ],
        [
            "node9",
            "data",
            "node3",
            "data"
        ],
        [
            "node11",
            "data",
            "node8",
            "data"
        ],
        [
            "node11",
            "data",
            "node10",
            "data"
        ],
        [
            "node7",
            "data",
            "node17",
            "data2"
        ],
        [
            "node19",
            "data",
            "node7",
            "data"
        ],
        [
            "node5",
            "data",
            "node19",
            "data"
        ],
        [
            "node5",
            "data",
            "node20",
            "data"
        ],
        [
            "node20",
            "data",
            "node6",
            "data"
        ],
        [
            "node21",
            "data",
            "node15",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
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
            "uuid": "cb04221c-f792-4ccd-bb39-36602eb12ee2"
        },
        "node10": {
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
            "uuid": "c350cae3-5926-4706-a819-aef2cdb03ffd"
        },
        "node11": {
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
            "uuid": "c816ef84-71aa-4d1f-afc7-890217a3d0e9"
        },
        "node12": {
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
            "uuid": "21372a12-cee8-44ad-801d-050eed285019"
        },
        "node13": {
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
            "uuid": "1f044e0a-76ad-41b8-bce2-41ed0623da53"
        },
        "node14": {
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
            "uuid": "d0194686-e76c-4995-b4e8-bda0751010e9"
        },
        "node15": {
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
            "uuid": "0ca774ca-43c3-4dde-8f99-0d4ebb61a0b5"
        },
        "node16": {
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
            "uuid": "137ed69e-a9b9-48c9-baa9-346e63fb8c91"
        },
        "node17": {
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
            "uuid": "1b881cd2-91ad-4347-b731-b2ab2cec101b"
        },
        "node18": {
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
            "uuid": "b0b05fe4-875b-4897-a6a1-ba2e60ebfff9"
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
            "uuid": "413d40a5-a1ab-47b4-a162-bc6bc71238e1"
        },
        "node2": {
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
            "uuid": "8d5354e0-c8f4-4f51-b367-ee1bf6fd006a"
        },
        "node20": {
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
            "uuid": "4bdb26a7-46c5-447a-abe4-61281a2dd200"
        },
        "node21": {
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
                    "value": 25
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "10d91a32-9cb8-45ad-a216-1415c60d5c35"
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
            "uuid": "477471f3-e077-472f-9033-f6d77cfe22ef"
        },
        "node4": {
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
            "uuid": "61c37e71-9364-4fe2-b618-cc17dd067082"
        },
        "node5": {
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
            "uuid": "b52e204b-bb72-4b58-b121-6033bba81e17"
        },
        "node6": {
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
            "uuid": "56f02ce7-724f-4169-88a1-155ee769a0f6"
        },
        "node7": {
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
            "uuid": "173f60f4-7a11-4386-82b4-b13094d3f3bc"
        },
        "node8": {
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
            "uuid": "a2e3691e-2b08-4e5c-ba6c-0df84560ed69"
        },
        "node9": {
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
            "uuid": "3d135c80-0880-4de1-a03b-c4219d625b87"
        }
    },
    "version": 1.1
}</patch>
</scheme>
