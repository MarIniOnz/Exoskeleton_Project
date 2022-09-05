<?xml version='1.0' encoding='utf-8'?>
<scheme description="Pipeline creating plots for the main Exo data processing pipeline.&#10;&#10;Plots:&#10;- raw data" title="Visuals" version="2.0">
	<nodes>
		<node id="0" name="Time Series Plot" position="(600, 500)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Plot Processed EEG" uuid="a047308a-b9a0-4dc1-92d4-77e37adb7762" version="1.0.1" />
		<node id="1" name="LSL Input" position="(300, 400)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="ca5ed861-9228-464c-a2ae-86e00841f0f4" version="1.0.0" />
		<node id="2" name="Dejitter Timestamps" position="(400, 400)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="997daf0c-cc52-4762-9827-99a5160469a9" version="1.0.0" />
		<node id="3" name="Select Range" position="(500, 300)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="f682b060-942e-4ece-af65-ed59658fe363" version="1.0.0" />
		<node id="4" name="Select Range" position="(498.0, 500.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="78fd7d69-a077-493d-98f9-4ccff74bc159" version="1.0.0" />
		<node id="5" name="Time Series Plot" position="(600, 300)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Plot Processed EOG" uuid="adb15479-3361-45ac-8b4b-b13922a33e08" version="1.0.1" />
		<node id="6" name="Dejitter Timestamps" position="(400, 200)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="55ea137a-a1db-4e56-9169-0b01bf99f233" version="1.0.0" />
		<node id="7" name="Time Series Plot" position="(600, 200)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Plot Raw Data" uuid="1018eb1d-cf47-4df4-82de-2a10d332f2b1" version="1.0.1" />
		<node id="8" name="LSL Input" position="(301.0, 200.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="fd3337f3-37bf-4597-bf6c-1bef925dea66" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="8" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiVgQAAAAYXV0b19saW5lX2NvbG9yc3EEiFgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqIWAwAAABpbml0aWFsX2RpbXNxC11xDChN4gRL
Mk1YAk30AWVYCgAAAGxpbmVfY29sb3JxDVgHAAAAIzAwMDAwMHEOWAoAAABsaW5lX3dpZHRocQ9H
P+gAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnEQWAcAAAAjRkYwMDAwcRFYDAAAAG5hbnNfYXNfemVy
b3ESiFgOAAAAbm9fY29uY2F0ZW5hdGVxE4lYDgAAAG92ZXJyaWRlX3NyYXRlcRRYDQAAACh1c2Ug
ZGVmYXVsdClxFVgMAAAAcGxvdF9tYXJrZXJzcRaJWAsAAABwbG90X21pbm1heHEXiFgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEYY3NpcApfdW5waWNrbGVfdHlwZQpxGVgMAAAAUHlRdDQuUXRDb3Jl
cRpYCgAAAFFCeXRlQXJyYXlxG0MuAdnQywABAAAAAAL1AAAAMgAABIwAAAOxAAADAAAAAF8AAASB
AAADpgAAAAAAAHEchXEdh3EeUnEfWAUAAABzY2FsZXEgRz+5mZmZmZmaWA4AAABzZXRfYnJlYWtw
b2ludHEhiVgMAAAAc2hvd190b29sYmFycSKIWAsAAABzdHJlYW1fbmFtZXEjWA0AAAAodXNlIGRl
ZmF1bHQpcSRYCgAAAHRpbWVfcmFuZ2VxJUdACAAAAAAAAFgFAAAAdGl0bGVxJlgNAAAAUHJvY2Vz
c2VkIEVFR3EnWAoAAAB6ZXJvX2NvbG9ycShYBwAAACNGRkZGRkZxKVgIAAAAemVyb21lYW5xKol1
Lg==
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
HlgMAAAAbWF4X2NodW5rbGVucQhLAFgMAAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVs
dClxClgFAAAAcXVlcnlxC1gmAAAAdHlwZT0nRUVHJyBhbmQgbmFtZT0nUHJlcHJvY2Vzc2VkRGF0
YSdxDFgHAAAAcmVjb3ZlcnENiFgUAAAAcmVzb2x2ZV9taW5pbXVtX3RpbWVxDkc/4AAAAAAAAFgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAAUHlRdDQu
UXRDb3JlcRFYCgAAAFFCeXRlQXJyYXlxEkMuAdnQywABAAAAAASIAAAArQAABkEAAAKOAAAEkwAA
ANoAAAY2AAACgwAAAAAAAHEThXEUh3EVUnEWWA4AAABzZXRfYnJlYWtwb2ludHEXiXUu
</properties>
		<properties format="literal" node_id="2">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAC2gAAAV0AAASnAAACrAAAAuUA
AAGKAAAEnAAAAqEAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ1YCwAAAGJpcG9s
YXIgRU9HcQ5hWA4AAABzZXRfYnJlYWtwb2ludHEPiVgEAAAAdW5pdHEQWAUAAABuYW1lc3ERdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAC2gAAAV0AAASnAAAChgAAAuUA
AAGKAAAEnAAAAnsAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ0oWAQAAADCtUMz
cQ5YBAAAAMK1QzRxD2VYDgAAAHNldF9icmVha3BvaW50cRCJWAQAAAB1bml0cRFYBQAAAG5hbWVz
cRJ1Lg==
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiVgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqIWAwAAABpbml0aWFsX2RpbXNxC11xDChNigJL
Mk1YAk30AWVYCgAAAGxpbmVfY29sb3JxDVgHAAAAIzAwMDAwMHEOWAoAAABsaW5lX3dpZHRocQ9H
P+gAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnEQWAcAAAAjRkYwMDAwcRFYDAAAAG5hbnNfYXNfemVy
b3ESiFgOAAAAbm9fY29uY2F0ZW5hdGVxE4lYDgAAAG92ZXJyaWRlX3NyYXRlcRRYDQAAACh1c2Ug
ZGVmYXVsdClxFVgMAAAAcGxvdF9tYXJrZXJzcRaJWAsAAABwbG90X21pbm1heHEXiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEYY3NpcApfdW5waWNrbGVfdHlwZQpxGVgMAAAAUHlRdDQuUXRDb3Jl
cRpYCgAAAFFCeXRlQXJyYXlxG0MuAdnQywABAAAAAAL1AAAAMgAABIwAAAOxAAADAAAAAF8AAASB
AAADpgAAAAAAAHEchXEdh3EeUnEfWAUAAABzY2FsZXEgRz90euFHrhR7WA4AAABzZXRfYnJlYWtw
b2ludHEhiVgMAAAAc2hvd190b29sYmFycSKIWAsAAABzdHJlYW1fbmFtZXEjWA0AAAAodXNlIGRl
ZmF1bHQpcSRYCgAAAHRpbWVfcmFuZ2VxJUdACAAAAAAAAFgFAAAAdGl0bGVxJlgLAAAAQmlwb2xh
ciBFT0dxJ1gKAAAAemVyb19jb2xvcnEoWAcAAAAjRkZGRkZGcSlYCAAAAHplcm9tZWFucSqJdS4=
</properties>
		<properties format="literal" node_id="6">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiVgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqIWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TVgCTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKIWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFolYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAAAvUAAAAyAAAEjAAAA7EAAAMAAAAAXwAABIEA
AAOmAAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP/AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNoFVgKAAAAdGltZV9y
YW5nZXEkR0AIAAAAAAAAWAUAAAB0aXRsZXElWAgAAABSYXcgRGF0YXEmWAoAAAB6ZXJvX2NvbG9y
cSdYBwAAACNGRkZGRkZxKFgIAAAAemVyb21lYW5xKYh1Lg==
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
HlgMAAAAbWF4X2NodW5rbGVucQhLFFgMAAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVs
dClxClgFAAAAcXVlcnlxC1gfAAAAdHlwZT0nRUVHJyBhbmQgbmFtZT0nU291cmNlRUVHJ3EMWAcA
AAByZWNvdmVycQ2IWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEORz/gAAAAAAAAWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVx
EVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEAAAAAAQ0AAACRAAACxgAAAnIAAAEYAAAAvgAAArsA
AAJnAAAAAAAAcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJdS4=
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
            "node3",
            "data"
        ],
        [
            "node3",
            "data",
            "node5",
            "data"
        ],
        [
            "node3",
            "data",
            "node4",
            "data"
        ],
        [
            "node5",
            "data",
            "node1",
            "data"
        ],
        [
            "node4",
            "data",
            "node6",
            "data"
        ],
        [
            "node7",
            "data",
            "node8",
            "data"
        ],
        [
            "node9",
            "data",
            "node7",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        1250,
                        50,
                        600,
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
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "plot_minmax": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.1
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
                    "value": 3.0
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Processed EEG"
                },
                "zero_color": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "zeromean": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a047308a-b9a0-4dc1-92d4-77e37adb7762"
        },
        "node2": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "bipolar EOG",
                        "\u00b5C3",
                        "\u00b5C4"
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
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
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
                    "value": "type='EEG' and name='PreprocessedData'"
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
            "uuid": "ca5ed861-9228-464c-a2ae-86e00841f0f4"
        },
        "node3": {
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
            "uuid": "997daf0c-cc52-4762-9827-99a5160469a9"
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
            "uuid": "f682b060-942e-4ece-af65-ed59658fe363"
        },
        "node5": {
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
                        "\u00b5C3",
                        "\u00b5C4"
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
            "uuid": "78fd7d69-a077-493d-98f9-4ccff74bc159"
        },
        "node6": {
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        650,
                        50,
                        600,
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
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.005
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
                    "value": 3.0
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Bipolar EOG"
                },
                "zero_color": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "zeromean": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "adb15479-3361-45ac-8b4b-b13922a33e08"
        },
        "node7": {
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
            "uuid": "55ea137a-a1db-4e56-9169-0b01bf99f233"
        },
        "node8": {
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        600,
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
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 3.0
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Raw Data"
                },
                "zero_color": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "1018eb1d-cf47-4df4-82de-2a10d332f2b1"
        },
        "node9": {
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
                        "C4",
                        "P3",
                        "P4",
                        "F7",
                        "F8",
                        "T7",
                        "T8",
                        "Cz"
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
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 20
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
            "uuid": "fd3337f3-37bf-4597-bf6c-1bef925dea66"
        }
    },
    "version": 1.1
}</patch>
</scheme>
