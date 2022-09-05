<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="Burg Both Hands - 3 electrodes laplace" version="2.0">
	<nodes>
		<node id="0" name="IIR Filter" position="(400, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Lowpass IIR" uuid="14086d9d-4ded-420e-8031-d9b860596891" version="1.1.0" />
		<node id="1" name="IIR Filter" position="(600, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Notch IIR" uuid="e460f646-a626-4cc8-ab06-f9512df99f59" version="1.1.0" />
		<node id="2" name="IIR Filter" position="(300, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Highpass IIR" uuid="864cd650-fa19-47b9-a492-f3f7e780937e" version="1.1.0" />
		<node id="3" name="IIR Filter" position="(500, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Notch IIR" uuid="8d408007-3267-4f6b-97b9-9c6050be2dad" version="1.1.0" />
		<node id="4" name="Surface Laplace Filter" position="(700, 200)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owlaplacefilter.OWLaplaceFilter" title="Laplace" uuid="293dfc9d-ef5f-45e7-86aa-d3b1b950561b" version="1.0.0" />
		<node id="5" name="IIR Filter" position="(900, 200)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Bandpass IIR" uuid="a5ef95f2-4269-4ec9-b09a-fab52a2d3285" version="1.1.0" />
		<node id="6" name="IIR Filter" position="(900, 100)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="Lowpass IIR" uuid="de77edbb-338b-4488-91e7-750600bd841f" version="1.1.0" />
		<node id="7" name="Single Pole Filter" position="(700, 400)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owsinglepolefilter.OWSinglePoleFilter" title="Single Pole Filter" uuid="81701469-2811-4fda-9f4d-5371d1f7eae8" version="1.0.0" />
		<node id="8" name="Dejitter Timestamps" position="(200, 200)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="2ab7cd52-8172-4a9d-a36d-e13a4e657818" version="1.0.0" />
		<node id="9" name="Estimate Update Rate" position="(700, 500)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owestimateupdaterate.OWEstimateUpdateRate" title="Estimate Update Rate" uuid="7a0b36a8-5b47-4d68-ac64-f4ee9dc8d648" version="1.0.0" />
		<node id="10" name="Power Spectrum (Burg)" position="(600, 400)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owburgspectrum.OWBurgSpectrum" title="Power Spectrum (Burg)" uuid="9ccfc9b6-ffd5-4280-9c94-40df92726d67" version="1.0.0" />
		<node id="11" name="Strip Singleton Axis" position="(900, 400)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owstripsingletonaxis.OWStripSingletonAxis" title="Strip Frequency Axis" uuid="0c6be951-1eab-4d8f-83f4-d70915456f9c" version="1.0.0" />
		<node id="12" name="Concatenate Tensors" position="(1200, 300)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owconcatinputs.OWConcatInputs" title="Concatenate EOG and EEG" uuid="cb62336f-f6f2-4677-9b7b-791bca51bf2a" version="1.0.0" />
		<node id="13" name="Rename Channels" position="(800, 400)" project_name="NeuroPype" qualified_name="widgets.utilities.owrenamechannels.OWRenameChannels" title="Rename Channels" uuid="cbbf063a-8442-4184-a388-9f105233a887" version="1.0.0" />
		<node id="14" name="LSL Output" position="(1500, 300)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="7ea56791-b89a-4df7-8c21-ed886bae9246" version="1.0.0" />
		<node id="15" name="Segmentation" position="(500, 400)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="dca0ddd2-41bc-4cfc-98e8-1ab78be3291e" version="1.0.1" />
		<node id="16" name="Pick Times" position="(1100, 200)" project_name="NeuroPype" qualified_name="widgets.exo_nodes.owpicktimes.OWPickTimes" title="Pick Times" uuid="e7bb9091-7d5b-463f-a474-2dec098aa000" version="1.0.0" />
		<node id="17" name="LSL Input" position="(100, 200)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL from Streaming Data" uuid="60eb134a-ff39-46df-b202-140a78e3f738" version="1.0.0" />
		<node id="18" name="Select Range" position="(800, 100)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Extract EOG" uuid="b5d1cbe4-29c7-4972-b55a-bd0ef6b1c3ff" version="1.0.0" />
		<node id="19" name="Select Range" position="(800, 200)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Extract EEG" uuid="afb75377-ab0c-4597-a18d-90813147a313" version="1.0.0" />
		<node id="20" name="Override Sampling Rate" position="(1400, 300)" project_name="NeuroPype" qualified_name="widgets.utilities.owoverridesamplingrate.OWOverrideSamplingRate" title="Override Sampling Rate" uuid="dc0573e7-ef2c-46aa-9845-be92dd68cd51" version="1.0.0" />
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
		<properties format="pickle" node_id="4">gAN9cQAoWAoAAABDM193ZWlnaHRzcQF9cQIoWAIAAABDM3EDSwFYAgAAAEYzcQRHv9UeuFHrhR9Y
AgAAAEN6cQVHv9UeuFHrhR9YAgAAAFAzcQZHv9UeuFHrhR91WAoAAABDNF93ZWlnaHRzcQd9cQgo
WAIAAABDNHEJSwFYAgAAAEY0cQpHv9UeuFHrhR9YAgAAAEN6cQtHv9UeuFHrhR9YAgAAAFA0cQxH
v9UeuFHrhR91WAsAAABFT0dfd2VpZ2h0c3ENfXEOKFgCAAAAQzNxD0sBWAIAAABDNHEQSv////91
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRFjc2lwCl91bnBpY2tsZV90eXBlCnESWAwAAABQeVF0
NC5RdENvcmVxE1gKAAAAUUJ5dGVBcnJheXEUQy4B2dDLAAEAAAAABg8AAAJLAAAHiAAABBwAAAYY
AAACcQAAB38AAAQTAAAAAAAAcRWFcRaHcRdScRhYDgAAAHNldF9icmVha3BvaW50cRmJdS4=
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
cnJheXEMQy4B2dDLAAEAAAAAAwIAAAFAAAAEewAAApoAAAMLAAABZgAABHIAAAKRAAAAAAAAcQ2F
cQ6HcQ9ScRBYDgAAAHNldF9icmVha3BvaW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAwAAAByZXBsYWNlX2V4cHJxAVgEAAAAwrVcMXECWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQNjc2lwCl91bnBpY2tsZV90eXBlCnEEWAwAAABQeVF0NC5RdENvcmVxBVgKAAAAUUJ5dGVB
cnJheXEGQy4B2dDLAAEAAAAAAvQAAAFdAAAEigAAAn0AAAL9AAABgwAABIEAAAJ0AAAAAAAAcQeF
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
AFB5UXQ0LlF0Q29yZXEIWAoAAABRQnl0ZUFycmF5cQlDLgHZ0MsAAQAAAAAC9QAAATAAAASJAAAC
qwAAAv4AAAFWAAAEgAAAAqIAAAAAAABxCoVxC4dxDFJxDVgOAAAAc2VsZWN0X21hcmtlcnNxDlgN
AAAAKHVzZSBkZWZhdWx0KXEPWA4AAABzZXRfYnJlYWtwb2ludHEQiVgLAAAAdGltZV9ib3VuZHNx
EV1xEihLAEc/2ZmZmZmZmmVYBwAAAHZlcmJvc2VxE4l1Lg==
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAYAAABjaHVua3NxAV1xAlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEDY3NpcApfdW5w
aWNrbGVfdHlwZQpxBFgMAAAAUHlRdDQuUXRDb3JlcQVYCgAAAFFCeXRlQXJyYXlxBkMuAdnQywAB
AAAAAAMCAAABiwAABH8AAAJZAAADDQAAAbgAAAR0AAACTgAAAAAAAHEHhXEIh3EJUnEKWA4AAABz
ZXRfYnJlYWtwb2ludHELiXUu
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQIoWAIAAABGM3EDWAIAAABGNHEEWAIAAABDM3EF
WAIAAABDenEGWAIAAABDNHEHWAIAAABQM3EIWAIAAABQNHEJWAIAAABPenEKWAIAAABUMXELWAIA
AABUMnEMZVgLAAAAZGlhZ25vc3RpY3NxDYlYDAAAAG1hcmtlcl9xdWVyeXEOWAAAAABxD1gMAAAA
bWF4X2Jsb2NrbGVucRBNAARYCgAAAG1heF9idWZsZW5xEUsKWAwAAABtYXhfY2h1bmtsZW5xEksA
WAwAAABub21pbmFsX3JhdGVxE1gNAAAAKHVzZSBkZWZhdWx0KXEUWAUAAABxdWVyeXEVWCkAAAB0
eXBlPSdFRUcnIGFuZCBuYW1lPSdFRTQxMS0wMDAwMDAtMDAwOTk5J3EWWAcAAAByZWNvdmVycReI
WBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEYRz/gAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cRljc2lwCl91bnBpY2tsZV90eXBlCnEaWAwAAABQeVF0NC5RdENvcmVxG1gKAAAAUUJ5dGVB
cnJheXEcQy4B2dDLAAEAAAAAAuQAAAEBAAAEmQAAAtkAAALtAAABJwAABJAAAALQAAAAAAAAcR2F
cR6HcR9ScSBYDgAAAHNldF9icmVha3BvaW50cSGJdS4=
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
            "node13",
            "outdata",
            "node21",
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
            "uuid": "14086d9d-4ded-420e-8031-d9b860596891"
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
            "uuid": "7a0b36a8-5b47-4d68-ac64-f4ee9dc8d648"
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
            "uuid": "9ccfc9b6-ffd5-4280-9c94-40df92726d67"
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
            "uuid": "0c6be951-1eab-4d8f-83f4-d70915456f9c"
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
            "uuid": "cb62336f-f6f2-4677-9b7b-791bca51bf2a"
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
            "uuid": "cbbf063a-8442-4184-a388-9f105233a887"
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
            "uuid": "7ea56791-b89a-4df7-8c21-ed886bae9246"
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
            "uuid": "dca0ddd2-41bc-4cfc-98e8-1ab78be3291e"
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
            "uuid": "e7bb9091-7d5b-463f-a474-2dec098aa000"
        },
        "node18": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "F3",
                        "F4",
                        "C3",
                        "Cz",
                        "C4",
                        "P3",
                        "P4",
                        "Oz",
                        "T1",
                        "T2"
                    ]
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
                    "value": "type='EEG' and name='EE411-000000-000999'"
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
            "uuid": "60eb134a-ff39-46df-b202-140a78e3f738"
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
            "uuid": "b5d1cbe4-29c7-4972-b55a-bd0ef6b1c3ff"
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
            "uuid": "e460f646-a626-4cc8-ab06-f9512df99f59"
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
            "uuid": "afb75377-ab0c-4597-a18d-90813147a313"
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
            "uuid": "dc0573e7-ef2c-46aa-9845-be92dd68cd51"
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
            "uuid": "864cd650-fa19-47b9-a492-f3f7e780937e"
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
            "uuid": "8d408007-3267-4f6b-97b9-9c6050be2dad"
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
                        "Cz": -0.33,
                        "F3": -0.33,
                        "P3": -0.33
                    }
                },
                "C4_weights": {
                    "customized": true,
                    "type": "DictPort",
                    "value": {
                        "C4": 1,
                        "Cz": -0.33,
                        "F4": -0.33,
                        "P4": -0.33
                    }
                },
                "EOG_weights": {
                    "customized": true,
                    "type": "DictPort",
                    "value": {
                        "C3": 1,
                        "C4": -1
                    }
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "293dfc9d-ef5f-45e7-86aa-d3b1b950561b"
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
            "uuid": "a5ef95f2-4269-4ec9-b09a-fab52a2d3285"
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
            "uuid": "de77edbb-338b-4488-91e7-750600bd841f"
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
            "uuid": "81701469-2811-4fda-9f4d-5371d1f7eae8"
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
            "uuid": "2ab7cd52-8172-4a9d-a36d-e13a4e657818"
        }
    },
    "version": 1.1
}</patch>
</scheme>
