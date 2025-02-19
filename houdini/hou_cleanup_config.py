"""Configuration hou stub generation clean up.

The constants in this module act as overrides for the automatic type annotations we get from
the C++ type analysis.
"""

# Define functions that are missing entirely from hou.py
# WARNING: Try not to redefine functions that are deprecated and have been removed from hou.py
MISSING_DEFINITIONS = {
    # Missing module level imports are sorted into the `None` class.
    None: [
        # NOTE: These are left as an example of deprecated functions that should not be added.
        # "def expandString(text: str) -> str",
        # "def expandStringAtFrame(text: str, frame_number: float) -> str",
    ],
    "NetworkItem": [
        "def __lt__(self, other: object) -> bool",
        "def __le__(self, other: object) -> bool",
        "def __gt__(self, other: object) -> bool",
        "def __ge__(self, other: object) -> bool",
        "def __eq__(self, other: object) -> bool",
        "def __ne__(self, other: object) -> bool",
    ],
    "Node": [
        "def createOutputNode(self, node_type_name: str, node_name: Optional[str] = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> Self",
        "def createInputNode(self, input_index: int, node_type_name: str, node_name: Optional[str] = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> Self",
        "def creationTime(self) -> datetime.datetime",
        "def modificationTime(self) -> datetime.datetime",
    ],
    "OpNode": [
        "def setParmExpressions(self, parm_dict: Dict[str, Any], language: Optional[EnumValue] = None, replace_expressions: bool = True) -> None",
    ],
    "Parm": [
        "def set(self, value: Union[int, float, str, Parm, Ramp], language: Optional[EnumValue] = None, follow_parm_reference: bool = True) -> None",
    ],
    "ParmTuple": [
        "def __iter__(self) -> Iterator[Parm]",
        "def set(self, value: Union[Iterable[int], Iterable[float], Iterable[str], Iterable[Parm], ParmTuple], language: Optional[EnumValue] = None, follow_parm_reference: bool = True) -> None",
    ],
    "Prim": [
        "def voxelRangeAsBool(self, range: BoundingBox) -> Sequence[bool]",
        "def voxelRangeAsInt(self, range: BoundingBox) -> Sequence[int]",
        "def voxelRangeAsFloat(self, range: BoundingBox) -> Sequence[float]",
        "def voxelRangeAsVector3(self, range: BoundingBox) -> Sequence[Vector3]",
    ],
    "Geometry": [
        "def pointAttribs(self, scope: EnumValue) -> Sequence[Attrib]",
        "def primAttribs(self, scope: EnumValue) -> Sequence[Attrib]",
        "def vertexAttribs(self, scope: EnumValue) -> Sequence[Attrib]",
        "def globalAttribs(self, scope: EnumValue) -> Sequence[Attrib]",
    ],
    "Vector2": [
        "def __iter__(self) -> Iterator[float]",
    ],
    "Vector3": [
        "def __iter__(self) -> Iterator[float]",
    ],
    "Vector4": [
        "def __iter__(self) -> Iterator[float]",
    ],
    "hda": [
        "@staticmethod\ndef reloadHDAModule(hda_module: HDAModule) -> None",
    ],
    "qt": [
        "@staticmethod\ndef mainWindow() -> QtWidgets.QMainWindow",
        "@staticmethod\ndef Icon(icon_name: str, width: Optional[int] = None, height: Optional[int] = None) -> QtGui.QIcon",
    ],
    "ui": [
        "@staticmethod\ndef displayConfirmation(text: str, severity: EnumValue = severityType.Message, help: Optional[str] = None, title: Optional[str] = None, details: Optional[str] = None, destails_label: Optional[str] = None, destails_expanded: bool = False) -> bool",
        "@staticmethod\ndef selectFile(start_directory: Optional[str] = None, title: Optional[str] = None, collapse_sequences: bool = False, file_type: EnumValue = fileType.Any, pattern: Optional[str] = None, default_value: Optional[str] = None, multiple_select: bool = False, image_chooser: bool = False, chooser_mode: EnumValue = fileChooserMode.ReadAndWrite, width: int = 0, height: int = 0) -> str",
    ],
}


# Functions that return these types are never optional.
NON_OPTIONAL_RETURN_TYPES = {
    "EnumValue",
    "Iterator",
    "Matrix2",
    "Matrix3",
    "Matrix4",
    "Quaternion",
    "Tuple",
    "Vector2",
    "Vector3",
    "Vector4",
    "std.vector",
    "tuple",
}


# Functions that are not Optional returns, even though they are pointers.
NON_OPTIONAL_RETURN_FUNCTIONS = {
    None: {
        "root",
        "pwd",
        "phm",
        "currentDopNet",
        "createApexRootNode",
        "nodeTypeCategories",
        "addNodeBundle",
    },
    "_clone_Connection": {
        "duplicate",
        "lopNode",
    },
    "_ik_Target": {
        "joint",
    },
    "Face": {
        "addVertex",
        "vertex",
    },
    "Agent": {
        "collisionLayer",
        "currentLayer",
        "definition",
    },
    "AgentClip": {
        "freeze",
    },
    "AgentDefinition": {
        "freeze",
        "metadata",
        "rig",
        "shapeLibrary",
    },
    "AgentMetadata": {
        "freeze",
    },
    "AgentRig": {
        "freeze",
    },
    "AgentShape": {
        "freeze",
        "geometry",
    },
    "AgentShapeBinding": {
        "deformer",
        "shape",
    },
    "AgentShapeLibrary": {
        "addShape",
        "data",
        "freeze",
    },
    "Attrib": {
        "dataId",
        "geometry",
    },
    "ChannelGraphSelection": {
        "animBar",
        "channelList",
        "graph",
        "parm",
    },
    "ChannelPrim": {
        "addVertex",
        "vertex",
    },
    "ChopNode": {
        "addVertex",
        "clip",
    },
    "Color": {
        "ocio_transform",
        "ocio_viewTransform",
    },
    "ConstructionPlane": {
        "sceneViewer",
        "transform",
    },
    "DataParmTemplate": {
        "defaultExpressionLanguage",
    },
    "Desktop": {
        "createFloatingPane",
        "createFloatingPaneTab",
        "shelfDock",
    },
    "DopData": {
        "createSubData",
        "freeze",
        "options",
        "simulation",
    },
    "DopNode": {
        "pythonSolverData",
        "simulation",
    },
    "DopSimulation": {
        "dopNetNode",
    },
    "Edge": {
        "geometry",
    },
    "EdgeGroup": {
        "dataId",
        "geometry",
    },
    "FlipbookSettings": {
        "stash",
    },
    "Gallery": {
        "createEntry",
    },
    "GalleryEntry": {
        "createChildNode",
    },
    "Geometry": {
        "addArrayAttrib",
        "createBezierCurve",
        "createBezierSurface",
        "createChannelPrim",
        "createEdgeGroup",
        "createHexahedron",
        "createHexahedronInPlace",
        "createMeshSurface",
        "createNURBSCurve",
        "createNURBSCurve",
        "createNURBSSurface",
        "createPacked",
        "createPoint",
        "createPointGroup",
        "createPolygon",
        "createPrimGroup",
        "createTetrahedron",
        "createTetrahedronInPlace",
        "createVertexGroup",
        "createVolume",
        "freeze",
        "primitiveIntrinsicsDataId",
        "selection",
        "topologyDataId",
        "unpackFromFolder",
    },
    "GeometryDrawable": {
        "geometry",
    },
    "GeometryDrawableGroup": {
        "drawable",
        "geometry",
    },
    "GeometrySelection": {
        "drawable",
        "geometry",
    },
    "GeometryViewport": {
        "camera",
        "defaultCamera",
        "settings",
    },
    "GeometryViewportCamera": {
        "stash",
    },
    "GeometryViewportSettings": {
        "backgroundImage",
        "displaySet",
    },
    "HDADefinition": {
        "addSection",
        "nodeType",
        "options",
        "parmTemplateGroup",
    },
    "HDASection": {
        "definition",
    },
    "IndexPairPropertyTable": {
        "attrib",
        "propertyDataType",
    },
    "InterruptableOperation": {
        "__enter__",
    },
    "LopNetwork": {
        "viewportOverrides",
        "viewportLoadMasks",
        "loadNamedViewportLoadMasks",
        "editablePostLayer",
    },
    "LopNode": {
        "loadMasks",
        "selectionRule",
        "viewerNode",
    },
    "LopPostLayer": {
        "__enter__",
    },
    "LopViewportOverrides": {
        "__enter__",
    },
    "NodeConnection": {
        "outputItem",
    },
    "Node": {
        "childTypeCategory",
        "collapseIntoSubnet",
        "copyNetworkBox",
        "copyStickyNote",
        "createInputNode",
        "createNetworkBox",
        "createNetworkDot",
        "createNode",
        "createOutputNode",
        "createStickyNote",
        "creator",
        "moveToGoodPosition",
        "type",
    },
    "NodeGroup": {
        "parent",
    },
    "NodeType": {
        "parmTemplateGroup",
    },
    "OpNode": {
        "addNodeGroup",
        "hdaModule",
        "hm",
        "parmTemplateGroup",
        "expressionLanguage",
        "simulation",
    },
    "OpNodeTypeCategory": {
        "createDigitalAsset",
    },
    "PackedGeometry": {
        "getEmbeddedGeometry"
    },
    "PackedPrim": {
        "vertex",
    },
    "Pane": {
        "createTab",
        "currentTab",
        "splitHorizontally",
        "splitVertically",
    },
    "PaneTab": {
        "clone",
        "setType",
    },
    "Parm": {
        "evalAsRamp",
        "evalAsRampAtFrame",
        "expressionLanguage",
        "getReferencedParm",
        "parmTemplate",
        "tuple",
        "uiBackgroundColor",
    },
    "ParmTemplate": {
        "clone",
    },
    "ParmTemplateGroup": {
        "entryAtIndices",
    },
    "ParmTuple": {
        "__getitem__",
        "parmTemplate",
    },
    "PathBasedPaneTab": {
        "currentNode",
        "pwd",
    },
    "PerfMonEvent": {
        "__enter__",
    },
    "Point": {
        "geometry",
    },
    "PointGroup": {
        "dataId",
    },
    "Prim": {
        "geometry",
    },
    "PrimGroup": {
        "dataId",
    },
    "Quadric": {
        "vertex",
    },
    "RadialMenu": {
        "categories",
        "createScriptItem",
        "createSubmenu",
        "item",
        "items",
        "label",
        "root",
        "shortcut",
        "sourceFile",
    },
    "RadialScriptItem": {
        "check",
        "icon",
        "label",
        "script",
        "shortcut",
    },
    "RadialSubmenu": {
        "createScriptItem",
        "createSubmenu",
        "items",
        "label",
        "shortcut",
    },
    "RedrawBlock": {
        "__enter__",
    },
    "ReferencePlane": {
        "sceneViewer",
    },
    "SceneViewer": {
        "constructionPlane",
        "curViewport",
        "flipbookSettings",
        "referencePlane",
        "selectGeometry",
        "selectedViewport",
    },
    "ScriptEvalContext": {
        "__enter__",
    },
    "Selection": {
        "freeze",
    },
    "Selector": {
        "nodeType",
    },
    "SimpleDrawable": {
        "geometry"
    },
    "SopNode": {
        "curPoint",
        "curPrim",
        "curVertex",
    },
    "SopNodeType": {
        "addSelector",
    },
    "StyleSheet": {
        "clone",
        "cloneWithAddedStyleSheet",
        "cloneWithObject",
        "cloneWithPrim",
        "cloneWithShape",
    },
    "Surface": {
        "vertex",
    },
    "Take": {
        "addChildTake",
        "insertTakeAbove",
    },
    "Track": {
        "clip",
    },
    "UndosDisabler": {
        "__enter__",
    },
    "UndosGroup": {
        "__enter__",
    },
    "VDB": {
        "vertex",
    },
    "Vertex": {
        "geometry",
        "point",
        "prim",
    },
    "VertexGroup": {
        "dataId",
        "geometry",
    },
    "VexContext": {
        "nodeTypeCategory",
    },
    "ViewerDragger": {
        "curViewport",
        "viewport",
    },
    "ViewerState": {
        "nodeType",
    },
    "ViewportVisualizer": {
        "evalParmAsRamp",
        "type",
    },
    "Volume": {
        "vertex",
    },
    "VopNetNode": {
        "definedType",
        "vexContext",
    },
    "VopNode": {
        "insertParmGenerator",
    },
    "anim": {
        "newBookmark",
    },
    "clone": {
        "createClone",
    },
    "galleries": {
        "createGalleryEntry",
    },
    "lop": {
        "createConnectionParmsForProperty",
        "createParmsForParameter",
        "createParmsForProperty",
        "outputProcessorParms",
        "shaderNodeType",
    },
    "perfMon": {
        "loadProfile",
        "startCookEvent",
        "startEvent",
        "startPaneEvent",
        "startProfile",
        "startTimedCookEvent",
        "startTimedEvent",
    },
    "playbar": {
        "animBar",
        "channelList",
        "channelListFromNodes",
        "channelListFromParmTuples",
        "channelListFromParms",
        "channelListFromSelection",
        "frameRange",
        "playbackRange",
        "selectionRanges",
        "timeRange",
        "timelineRange",
    },
    "properties": {
        "parmTemplate",
    },
    "shelves": {
        "newShelf",
        "newShelfSet",
        "newTool",
    },
    "takes": {
        "currentTake",
        "rootTake",
    },
    "ui": {
        "createDialog",
        "createRadialItem",
        "createRadialMenu",
        "curDesktop",
        "device",
        "sharedAssetGalleryDataSource",
        "showFloatingParameterEditor",
    },
    "undos": {
        "disabler",
        "group",
    },
    "viewportVisualizer": {
        "copyVisualizer",
    },
}

# Functions for which we want to declare a specific return type.
EXPLICIT_RETURN_TYPES = {
    None: {},
    "DopData": {
        "creator": "OpNode",
        "dopNetNode": "OpNode",
    },
    "DopNode": {
        "dopNetNode": "OpNode",
        "displayNode": "Optional[OpNode]",
        "renderNode": "Optional[OpNode]",
    },
    "GeometrySelection": {
        "mergedNode": "SopNode",
    },
    "LopNode": {
        "editableLayer": "pxr.Sdf.Layer",
        "editableStage": "pxr.Sdf.Stage",
        "inputPrims": "Tuple[pxr.Sdf.Path, ...]",
        "lastModifiedPrims": "Tuple[pxr.Sdf.Path, ...]",
        "network": "OpNode",
        "uneditableStage": "pxr.Sdf.Stage",
    },
    "LopSelectionRule": {
        "sourceNode": "Optional[LopNode]",
    },
    "OpNode": {
        "changeNodeType": "ChopNode",
        "createDigitalAsset": "OpNode",
        "findOrCreateMotionEffectsNetwork": "OpNode",
    },
    "Parm": {
        "createClip": "ChopNode",
        "node": "OpNode",
    },
    "ParmTuple": {
        "createClip": "ChopNode",
        "node": "OpNode",
    },
    "ScriptEvalContext": {
        "node": "Optional[OpNode]",
    },
    "ViewerState": {
        "categoryNode": "Optional[OpNode]",
    },
    "ViewportVisualizer": {
        "evalParm": "Union[int, float, str]",
    },
    "dop": {
        "scriptSolverNetwork": "Optional[OpNode]"
    },
}

# Completely redefine function definitions that are wrong or did not come with C++ type hints.
# WARNING: Anything that is set to return `Sequence[T]` actually returns `tuple[T, ...]`,
#  but the `...` is throwing the stubgen off and it does not apply the override.
# WARNING: Any methods that take transform_order or rotate_order should have the annotations below,
#  however, since Literals are stripped out during the override, I have left them as `str`:
#   transform_order: Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs'] = 'srt'
#   rotate_order: Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'] = 'xyz'

EXPLICIT_DEFINITIONS = {
    None: {
        # signatures for these special methods include many inaccurate overloads
        "__ne__": "(self, other: object) -> bool",
        "__eq__": "(self, other: object) -> bool",
        "__lt__": "(self, other: object) -> bool",
        "__le__": "(self, other: object) -> bool",
        "__gt__": "(self, other: object) -> bool",
        "__ge__": "(self, other: object) -> bool",
        "addAnimationLayer": "(layermixer: ChopNode, layername: str = "") -> ChopNode",
        "applicationVersion": "(include_patch: bool = False) -> Sequence[int, int]",
        "createAnimationClip": "(path: str = ..., set_export: bool = False) -> ChopNode",
        "createAnimationLayers": "(path: str = ...) -> ChopNode",
        "fileReferences": "(project_dir_variable: str = 'HIP', include_all_refs: bool = true) -> Sequence[Tuple[Parm, str]]",
        "loadImageDataFromFile": "(file_name: str, arg: EnumValue = ...) -> bytes",
        "nodeType": "(category_or_name: Union[NodeTypeCategory, str], internal_name: Optional[str] = None) -> Optional[NodeType]",
        "registerOpdefPath": "(path: str, server_name: str, port: str = '')",
        "removeAnimationLayer": "(layermixer: ChopNode, layername: str, merge_down: bool = False) -> bool",
        # FIXME: runVex should have the following annotations:
        #   precision: Literal['32', '64'] = '32'
        "runVex": "(vex_file: str, inputs: dict[str, Any], precision: str = '32') -> dict[str, Any]",
        "saveImageDataToFile": "(color_and_alpha_data: Union[Sequence[float], bytes], width: int, height: int, file_name: str) -> None",
        "setContextOption": "(option: str, value: Optional[Union[str, float]]) -> None",
        "startHoudiniEngineDebugger": "(portOrPipeName: Union[int, str]) -> None",
    },
    "_StringMapDoubleTuple": {
        "__iter__": "(self) -> Iterator[str]",
    },
    "_ik_Skeleton": {
        "addJoint": "(self, world_transform: Matrix4 = ..., parent: Optional[_ik_Joint] = None, rotation_weights: Vector3 = ..., translation_weights: Vector3 = ..., mass: float = 1.0, local_com: Vector3 = ...) -> _ik_Joint",
    },
    "_ik_Target": {
        "__init__": "(joint: Optional[_ik_Joint] = None, goal_transform: Matrix4 = ..., joint_offset: Matrix4 = ..., target_type: EnumValue = _ik_targetType.Position, weight: float = 1.0, priority: int = 0, depth: int = -1) -> None",
    },
    "AdvancedDrawable": {
        "draw": "(self, handle: Incomplete, params: Optional[Dict[str, Any]] = None) -> None",
        "setParams": "(self, params: Optional[Dict[str, Any]] = None) -> None",
    },
    "AgentClip": {
        "__init__": "(name: str, stage: pxr.Usd.Stage, prim_path: str, rig: AgentRig) -> None",
    },
    "AgentLayer": {
        "__init__": "(name: str, rig: AgentRig, shapelib: AgentShapeLibrary, shape_bindings: Sequence[AgentShapeBinding], source_layer: Optional[AgentLayer] = None) -> None",
        "bindings": "(self, transform: Optional[int] = None) -> Sequence[AgentShapeBinding]",
    },
    "AgentMetadata": {
        "__init__": "(data: Dict[str, Any]) -> None",
        "data": "(self) -> dict[str, Any]",
        "setData": "(self, data: dict[str, Any]) -> None",
        "setMetadata": "(self, item_id: str, metadata: dict[str, Any]) -> None",
    },
    "AgentRig": {
        "__init__": "(name: str, transform_names: Sequence[str], hierarchy: Sequence[int]) -> None",
    },
    "AgentShapeBinding": {
        "__init__": "(shape: AgentShape, deformer: AgentShapeDeformer, bounds_scale: float = 1.0) -> None",
    },
    "AgentShapeDeformer": {
        "__init__": "(name: Union[str, EnumValue]) -> None",
    },
    "AgentShapeLibrary": {
        "__init__": "(filename: str, keep_external_ref: bool = True) -> None",
    },
    "AgentTransformGroup": {
        "__init__": "(name: str, transforms: Sequence[int], rig: AgentRig, weights: Sequence[float], channels: Sequence[int]) -> None",
    },
    "AssetGalleryDataSource": {
        "addItem": "(self, label: str, file_path: Optional[str] = None, thumbnail: bytes = b'', type_name: str = 'asset', blind_data: bytes = b'', creation_date: int = 0) -> str",
    },
    "Attrib": {
        "option": "(self, option_name: str) -> Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]",
        "options": "(self) -> Dict[str, Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]]",
        "setOption": "(self, name: str, value: Union[int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[float], Sequence[int]], type_hint: EnumValue = ...) -> None",
    },
    "Bookmark": {
        "metadata": "(self, key: str, default_value: Any = None) -> Any",
        "setEndFrame": "(self, end: float) -> None",
        "setMetadata": "(self, key: str, value: Any, type_hint: EnumValue = ...) -> None",
        "setStartFrame": "(self, start: float) -> None",
    },
    "BoundingBox": {
        "__init__": "(self, bbox_or_xmin: Union[float, BoundingBox] = 0.0, ymin: float = 0.0, zmin: float = 0.0, xmax: float = 0.0, ymax: float = 0.0, zmax: float = 0.0) -> None",
        "enlargeToContain": "(self, point_or_bbox: Union[Sequence[float], BoundingBox]) -> None",
    },
    "BoundingRect": {
        "__init__": "(self, brect_or_p1_or_xmin: Union[BoundingRect, Vector2, float], p2_or_ymin: Union[Vector2, float], xmax: float = 0.0, ymax: float = 0.0) -> None",
        "enlargeToContain": "(self, point_or_rect: Union[Sequence[float], BoundingRect]) -> None",
        "intersects": "(self, rect: BoundingRect) -> bool",
        "contains": "(self, rect: BoundingRect) -> bool",
    },
    "ButtonParmTemplate": {
        "__init__": "(self, name: str, label: str, disable_when: Optional[str] = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help=None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Dict[str, str] = ...) -> None",
    },
    "ChannelGraph": {
        "selectedKeyframes": "(self) -> dict[Parm, Sequence[BaseKeyframe]]",
    },
    "ChannelGraphSelection": {
        "__init__": "(self, path: Optional[str] = None, flags: Sequence[int] = ...) -> None",
    },
    "ChannelList": {
        "addGeometryChannels": "(self, geometry: Geometry, collection_name: Optional[str] = None, pattern: Optional[str] = None, selected: bool = True, pinned: bool = False, valueselected: bool = False) -> str",
        "addNodeGeometryChannels": "(self, node: SopNode, pattern: Optional[str] = None, selected: bool = True, pinned: bool = False, valueselected: bool = False) -> str",
        "asCode": "(self, var_name: str = 'chanlist') -> str",
        "containsGeometryChannel": "(self, collection_name: str, channel: Optional[str] = None) -> bool",
        "deselect": "(self, parm: Union[Parm, Sequence[Parm]]) -> None",
        "deselectGeometryChannel": "(self, collection_name: str, channel: Optional[str] = None) -> str",
        "deselectGeometryChannelValue": "(self, collection_name: str, channel: Optional[str] = None) -> str",
        "deselectValue": "(self, parm: Union[Parm, Sequence[Parm]]) -> None",
        "pin": "(self, parm: Union[Parm, Sequence[Parm]]) -> None",
        "pinGeometryChannel": "(self, collection_name: str, channel: Optional[str] = None) -> str",
        "remove": "(self, parm: Union[Parm, Sequence[Parm]]) -> None",
        "select": "(self, parm: Union[Parm, Sequence[Parm]]) -> None",
        "selectGeometryChannel": "(self, collection_name: str, channel: Optional[str] = None) -> str",
        "selectGeometryChannelValue": "(self, collection_name: str, channel: Optional[str] = None) -> str",
        "selectValue": "(self, parm: Union[Parm, Sequence[Parm]]) -> None",
        "unpin": "(self, parm: Union[Parm, Sequence[Parm]]) -> None",
        "unpinGeometryChannel": "(self, collection_name: str, channel: Optional[str] = None) -> str",
    },
    "ChopNode": {
        "clipData": "(self, binary: Any) -> bytes",
        "saveClip": "(self, file_name: str) -> bool",
    },
    "Color": {
        "__init__": "(self, rgb_tuple: Sequence[float] = ...) -> None",
    },
    "Cop2Node": {
        "allPixels": "(self, plane: str = 'C', component: Optional[str] = None, interleaved: bool = True, time: float = -1.0) -> Sequence[float]",
        "allPixelsAsString": "(self, plane: str = 'C', component: Optional[str] = None, interleaved: bool = True, time: float = -1.0) -> bytes",
        "imageBounds": "(self, plane: str = 'C') -> Sequence[int, int, int]",
        "saveImage": "saveImage(self, file_name: str, frame_range: Sequence[float] = ...) -> None",
    },
    "DataParmTemplate": {
        "__init__": "(self, name: , label: , num_components: int, look: EnumValue = parmLook.Regular, naming_scheme: EnumValue = parmNamingScheme.XYZW, unknown_str: Optional[str] = None, disable_when: Optional[str] = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: dict[str, str] = {}, unknown_dict: dict[EnumValue, str] = {}, default_expression: Sequence[str] = (), default_expression_language: Sequence[EnumValue] = ()) -> DataParmTemplate",
    },
    "Desktop": {
        "createFloatingPane": "(self, pane_tab_type: EnumValue, position: Sequence[float] = ..., size: Sequence[float] = ..., python_panel_interface: Optional[PythonPanelInterface] = ..., immediate: bool = False) -> PaneTab",
        "createFloatingPaneTab": "(self, pane_tab_type: EnumValue, position: Sequence[float] = ..., size: Sequence[float] = ..., python_panel_interface: Optional[PythonPanelInterface] = ..., immediate: bool = False) -> PaneTab",
        "createFloatingPanel": "(self, pane_tab_type: EnumValue, position: Sequence[float] = ..., size: Sequence[float] = ..., python_panel_interface: Optional[PythonPanelInterface] = ..., immediate: bool = False) -> FloatingPanel",
    },
    "Dialog": {
        "setValue": "(self, name: str, value: Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4]) -> None",
        "waitForValueToChangeTo": "(self, name: str, new_value: Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4]) -> None",
    },
    "DopData": {
        "createSubData": "(self, data_name: str, data_type: str = ..., avoid_name_collisions: bool = False) -> DopData",
    },
    "DopRecord": {
        "setField": "(self, field_name: str, value: Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4]) -> None",
    },
    "EdgeGroup": {
        "add": "(self, edge_or_list_or_edge_group: Union[Edge, Sequence[Edge], EdgeGroup]) -> None",
        "remove": "(self, edge_or_list_or_edge_group: Union[Edge, Sequence[Edge], EdgeGroup]) -> None",
    },
    "Face": {
        "attribValueAt": "(self, attrib_or_name: Union[Attrib, str], u: float, du: float = 0) -> Union[int, float, str, Sequence[int], Sequence[float]]"
    },
    "FlipbookSettings": {
        # FIXME: Most of these methods are both setters and getters, where it will set the value if
        #  one is provided and return None, or will return the current value if none is provided.
        #  We would have better results if we overloaded each of these.
        "LUT": "(self, value: Optional[str] = None) -> Optional[str]",
        "antialias": "(self, value: Optional[EnumValue] = None) -> Optional[EnumValue]",
        "aperture": "(self, value: Optional[float] = None) -> Optional[float]",
        "appendFramesToCurrent": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "audioFilename": "(self, audio_file: Optional[str] = None) -> Optional[str]",
        "audioFrameStart": "(self, audio_file: Optional[float] = None) -> Optional[float]",
        "audioTimeOffset": "(self, value: Optional[float] = None) -> Optional[float]",
        "backgroundImage": "(self, value: Optional[str] = None) -> Optional[str]",
        "beautyPassOnly": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "blockEditing": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "cropOutMaskOverlay": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "depthOfFieldFromCamera": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "depthOfFieldQuality": "(self, value: Optional[float] = None) -> Optional[float]",
        "fStop": "(self, value: Optional[float] = None) -> Optional[float]",
        "focusDistance": "(self, value: Optional[float] = None) -> Optional[float]",
        "frameIncrement": "(self, value: Optional[float] = None) -> Optional[float]",
        "frameRange": "(self, value: Optional[Sequence[float]] = None) -> Optional[Tuple[float, float]]",
        "fromAudioPanel": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "gamma": "(self, value: Optional[float] = None) -> Optional[float]",
        "initializeSimulations": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "leaveFrameAtEnd": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "motionBlurFrameRange": "(self, value: Optional[EnumValue] = None) -> Optional[EnumValue]",
        "motionBlurSegments": "(self, value: Optional[int] = None) -> Optional[int]",
        "output": "(self, value: Optional[str] = None) -> Optional[str]",
        "outputToMPlay": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "outputZoom": "(self, value: Optional[int] = None) -> Optional[int]",
        "overrideGamma": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "overrideLUT": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "renderAllViewports": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "resolution": "(self, value: Optional[Tuple[int, int]] = None) -> Optional[Tuple[int, int]]",
        "scopeChannelKeyframesOnly": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "sessionLabel": "(self, value: Optional[str] = None) -> Optional[str]",
        "sheetSize": "(self, value: Optional[Sequence[int]] = None) -> Optional[Tuple[int, int]]",
        "shutter": "(self, value: Optional[float] = None) -> Optional[float]",
        "shutterFromCamera": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "useDepthOfField": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "useMotionBlur": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "useResolution": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "useSheetSize": "(self, value: Optional[bool] = None) -> Optional[bool]",
        "visibleObjects": "(self, value: Optional[str] = None) -> Optional[str]",
        "visibleTypes": "(self, value: Optional[EnumValue] = None) -> Optional[EnumValue]",
    },
    "FloatParmTemplate": {
        "__init__": "(self, name: str, label: str, num_components: int, default_value: Sequence[float] = ..., min: float = 0.0, max: float = 10.0, min_is_strict: bool = False, max_is_strict: bool = False, look: EnumValue = parmLook.Regular, naming_scheme: EnumValue = parmNamingScheme.XYZW, disable_when: Optional[str] = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Dict[str, str] = ..., default_expression: Sequence[str] = ..., default_expression_language: Sequence[EnumValue] = ...) -> None",
    },
    "FolderParmTemplate": {
        "__init__": "(self, name: str, label: str, parm_templates: Sequence[ParmTemplate] = ..., folder_type: EnumValue = folderType.Tabs, is_hidden: bool = False, ends_tab_group: bool = False, tags: Dict[str, str] = ..., conditionals: Dict[EnumValue, str] = ..., tab_conditionals: Dict[EnumValue, str] = ...) -> None",
    },
    "FolderSetParmTemplate": {
        "__init__": "(self, name: str, folder_names: Sequence[str], folder_type: EnumValue, tags: Dict[str, str] = ...) -> None",
        "folderNames": "(self) -> list[str]",
        "setFolderNames": "(self, folder_names: Sequence[str]) -> None",
    },
    "Geometry": {
        "addAttrib": "(self, type: EnumValue, name: str, default_value: Any, transform_as_normal: bool = True, create_local_variable: bool = True) -> Attrib",
        "attribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Union[int, float, str, Sequence[float], Sequence[int], Dict[str, Any]]",
        "containsPrimType": "(self, type_or_name: Union[EnumValue, str]) -> bool",
        "countPrimType": "(self, type_or_name: Union[EnumValue, str]) -> int",
        "createPoints": "(self, point_positions: Sequence[Sequence[float]]) -> Sequence[Point]",
        "createPolygons": "(self, point_positions: Sequence[Union[Point, Sequence[int]]], is_closed: bool = True) -> Sequence[Polygon]",
        "deletePoints": "(self, points: Union[Iterable[Point], PointGroup]) -> None",
        "deletePrims": "(self, prims: Union[Sequence[Prim], PrimGroup], keep_points: bool = False) -> None",
        "dictAttribValue": "(self, attrib: Union[Attrib, str]) -> dict[str, Any]",
        "dictListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[dict[str, Any]]",
        "edgeGroups": "(self, scope: EnumValue = groupScope.Public) -> Sequence[EdgeGroup]",
        "edgeLoop": "(self, edges: Sequence[Edge], loop_type: EnumValue, full_loop_per_edge: bool, force_ring: bool, allow_ring: bool) -> Sequence[Edge]",
        "findEdgeGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> Optional[EdgeGroup]",
        "findGlobalAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Optional[Attrib]",
        "findPointAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Optional[Attrib]",
        "findPointGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> Optional[PointGroup]",
        "findPrimAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Optional[Attrib]",
        "findPrimGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> Optional[PrimGroup]",
        "findVertexAttrib": "(self, name: str, scope: EnumValue = attribScope.Public) -> Optional[Attrib]",
        "findVertexGroup": "(self, name: str, scope: EnumValue = groupScope.Public) -> Optional[VertexGroup]",
        "floatAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> float",
        "floatListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[float]",
        "generateAttribMenu": "(self, attrib_type: Optional[EnumValue] = None, data_type: Optional[EnumValue] = None, min_size: int = 1, max_size: int = -1, array_type: bool = True, scalar_type: bool = True, case_sensitive: bool = True, pattern: str = '*', decode_tokens: bool = False) -> Sequence[str]",
        "importLop": "(self, lopnode: LopNode, selectionrule: LopSelectionRule, purpose: Optional[str] = None, traversal: Optional[str] = None, path_attrib_name: Optional[str] = None, name_attrib_name: Optional[str] = None, strip_layers: bool = False, frame: Optional[float] = None) -> LopLockedStage",
        "importUsdStage": "(self, stage: pxr.Usd.Stage, selectionrule: LopSelectionRule, purpose: Optional[str] = None, traversal: Optional[str] = None, path_attrib_name: Optional[str] = None, name_attrib_name: Optional[str] = None, frame: Optional[float] = None) -> None",
        "intAttribValue": "(self, attrib: Union[Attrib, str]) -> int",
        "intListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[int]",
        "pointFloatAttribValuesAsString": "(self, name: str, float_type: EnumValue = numericData.Float32) -> bytes",
        "pointGroups": "(self, scope: EnumValue = groupScope.Public) -> Sequence[PointGroup]",
        "pointIntAttribValuesAsString": "(self, name: str, int_type: EnumValue = numericData.Int32) -> bytes",
        "pointLoop": "(self, points: Sequence[Point], loop_type: EnumValue) -> Sequence[Point]",
        "pointNormals": "(self, points: Union[Sequence[Point], PointGroup]) -> Sequence[Vector3]",
        "primFloatAttribValuesAsString": "(self, name: str, float_type: EnumValue = numericData.Float32) -> bytes",
        "primGroups": "(self, scope: EnumValue = groupScope.Public) -> Sequence[PrimGroup]",
        "primIntAttribValuesAsString": "(self, name: str, int_type: EnumValue = numericData.Int32) -> bytes",
        "primLoop": "(self, prims: Sequence[Prim], loop_type: EnumValue) -> Sequence[Prim]",
        "setGlobalAttribValue": "(self, name_or_attrib: Union[str, Attrib], attrib_value: Any) -> None",
        "setIntrinsicValue": "(self, intrinsic_name: str, value: Union[int, float, str, Sequence[float], Sequence[int], Dict[str, Any]]) -> None",
        "setPointFloatAttribValuesFromString": "(self, name: str, values: bytes, float_type: EnumValue = numericData.Float32) -> None",
        "setPointIntAttribValuesFromString": "(self, name: str, values: bytes, int_type: EnumValue = numericData.Float32) -> None",
        "setPrimFloatAttribValuesFromString": "(self, name: str, values: bytes, float_type: EnumValue = numericData.Float32) -> None",
        "setPrimIntAttribValuesFromString": "(self, name: str, values: bytes, int_type: EnumValue = numericData.Float32) -> None",
        "setVertexFloatAttribValuesFromString": "(self, name: str, values: bytes, float_type: EnumValue = numericData.Float32) -> None",
        "setVertexIntAttribValuesFromString": "(self, name: str, values: bytes, int_type: EnumValue = numericData.Float32) -> None",
        "stringAttribValue": "(self, attrib: Union[Attrib, str]) -> str",
        "stringListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[str]",
        "transformPrims": "(self, prims: Union[Sequence[Prim], PrimGroup], matrix: Matrix4) -> None",
        "vertexFloatAttribValuesAsString": "(self, name: str, float_type: EnumValue = numericData.Float32) -> bytes",
        "vertexGroups": "(self, scope: EnumValue = groupScope.Public) -> Sequence[VertexGroup]",
        "vertexIntAttribValuesAsString": "(self, name: str, int_type: EnumValue = numericData.Int32) -> bytes",
    },
    "GeometryDelta": {
        "setPointPositionsFromString": "(self, positions: bytes, float_type: EnumValue = numericData.Float32) -> None",
    },
    "GeometryDrawable": {
        "__init__": "(self, scene_viewer: SceneViewer, geo_type: EnumValue, name: str, label: Optional[str] = None, geometry: Optional[Geometry] = None, params: Optional[Dict[str, Any]] = None) -> None",
    },
    "GeometryDrawableGroup": {
        "__init__": "(self, name: str, label: Optional[str] = None) -> None",
    },
    "GeometrySelection": {
        "__init__": "(self) -> None",
    },
    "GeometryViewport": {
        "changeType": "(self, type: EnumValue) -> None",
        "setCamera": "(self, camera_node: ObjNode) -> None",
        "queryWorldPositionAndNormal": "(self, x: int, y: int, selectionRestriction: bool = False) -> Tuple[Vector3, Vector3, bool]",
    },
    "GeometryViewportSettings": {
        "allowParticleSprites": "(self) -> bool",
        "autoGenerateVertexNormals": "(self) -> bool",
        "closureSelection": "(self, arg: EnumValue) -> EnumValue",
        "geometryInfo": "(self, arg: EnumValue) -> EnumValue",
        "guideFontSize": "(self) -> EnumValue",
        "handleHighlight": "(self, arg: EnumValue) -> EnumValue",
        "instanceStandInGeometry": "(self) -> EnumValue",
        "interiorWireAlpha": "(self) -> float",
        "levelOfDetail": "(self) -> float",
        "orientDiscToNormal": "(self) -> bool",
        "particleDiscSize": "(self) -> float",
        "particleDisplayType": "(self) -> EnumValue",
        "particlePointSize": "(self) -> float",
        "pointInstancing": "(self) -> bool",
        "pointInstancingLimit": "(self) -> int",
        "pointInstancingPercent": "(self) -> float",
        "polygonConvexQuality": "(self) -> bool",
        "selectWireframeAsSolid": "(self) -> bool",
        "setCamera": "(self, camera_node: ObjNode) -> None",
        "shadeOpenCurves": "(self) -> bool",
        "spriteTextureLimit": "(self) -> Sequence[int]",
        "subdivsionLimit": "(self) -> int",
        "vertexNormalCuspAngle": "(self) -> float",
        "vertexNormalLimit": "(self) -> int",
        "volumeAmbientShadows": "(self) -> float",
        "volumeBSplines": "(self) -> EnumValue",
        "volumeQuality": "(self) -> EnumValue",
        "volumeWireAsPoints": "(self) -> bool",
        "wireBlend": "(self) -> float",
        "wireWidth": "(self) -> float",
    },
    "Handle": {
        "disableParms": "(self, parm_names: Sequence[str]) -> None",
        "enableParms": "(self, parm_names: Sequence[str]) -> None",
    },
    "HDADefinition": {
        "addSection": "(self, name: str, contents: str = '', compression_type: EnumValue = compressionType.NoCompression) -> HDASection",
        "setExtraFileOption": "(self, name, value: Union[int, float, str, Vector2, Vecto3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[float]], type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "HDASection": {
        "binaryContents": "(self, compressionType: EnumValue = compressionType.NoCompression) -> bytes",
        "contents": "(self, compressionType: EnumValue = compressionType.NoCompression) -> str",
        "setContents": "(self, contents: str, compressionType: EnumValue = compressionType.NoCompression) -> None",
    },
    "IntParmTemplate": {
        "__init__": "(self, name: str, label: str, num_components: int, default_value: Sequence[int] = ..., min: int = 0, max: int = 10, min_is_strict=False, max_is_strict: bool = False, look: EnumValue = parmLook.Regular, naming_scheme: EnumValue = parmNamingScheme.XYZW, menu_items: Sequence[str] = ..., menu_labels: Sequence[str] = ..., icon_names: Sequence[str] = ..., item_generator_script: Optional[str] = None, item_generator_script_language: Optional[EnumValue] = None, menu_type: EnumValue = menuType.Normal, disable_when: Optional[str] = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Dict[str, str] = ..., default_expression: Sequence[str] = ..., default_expression_language: Sequence[str] = ...) -> None",
    },
    "IPRViewer": {
        "saveFrame": "(self, file_path: str, snapshot: int = 0, xres: int = -1, yres: int = -1, color: str = 'C', alpha: str = 'C', scope: str = '*', lut: str = '', gamma: float = 1.0, convert: bool = True) -> bool",
    },
    "Keyframe": {
        "__init__": "(self, value: Optional[float] = None, time: Optional[float] = None) -> None",
    },
    "LabelParmTemplate": {
        "__init__": "(self, name: str, label: str, column_labels: Sequence[str] = ..., is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, tags: Dict[str, str] = ...) -> None",
    },
    "LopNetwork": {
        "viewportOverridesLayer": "(self, layer_id: EnumValue) -> pxr.Sdf.Layer",
    },
    "LopNode": {
        "activeLayer": "(self, output_index: int = 0, ignore_errors: bool = False, use_last_cook_context_options: bool = True, frame: Optional[float] = None, context_options: Dict[str, Any] = ...) -> pxr.Sdf.Layer",
        "addLockedGeometry": "(self, identifier: str, geo: Geometry, args: Optional[Dict[str, str]] = None) -> str",
        "displayNode": "(self) -> LopNode",
        "layersAboveLayerBreak": "(self, output_index: int = 0, use_last_cook_context_options: bool = True, frame: Optional[float] = None, context_options: Optional[Dict[str, Union[str, float]]] = None) -> Sequence[str]",
        "loadMasks": "(self, output_index: int = 0, force_cook: bool = False, use_last_cook_context_options: bool = True, frame: Optional[float] = None, context_options: Optional[Dict[str, Union[str, float]]] = None) -> LopViewportLoadMasks",
        "setLastModifiedPrims": "(self, primPaths: Sequence[str]) -> None",
        "sourceLayer": "(self, layer_index: int = 0, output_index: int = 0, use_last_cook_context_options: bool = True, frame: Optional[float] = None, context_options: Dict[str, Any] = ...) -> pxr.Sdf.Layer",
        "sourceLayerCount": "(self, output_index: int = 0, use_last_cook_context_options: bool = True, frame: Optional[float] = None, context_options: Optional[Dict[str, Union[str, float]]] = None) -> LopViewportLoadMasks",
        "stage": "(self, output_index: int = 0, apply_viewport_overrides: bool = False, ignore_errors: bool = False, use_last_cook_context_options: bool = True, apply_post_layers: bool = True, frame: Optional[float] = None, context_options: Dict[str, Any] = ...) -> pxr.Sdf.Stage",
        "stagePrimStats": "(self, primpath: Optional[str] = None, output_index: int = 0, apply_viewport_overrides: bool = False, ignore_errors: bool = False, do_geometry_counts: bool = False, do_separate_purposes: bool = False, use_last_cook_context_options: bool = True, apply_post_layers: bool = True, frame: Optional[float] = None, context_options: Optional[Dict[str, Union[str, float]]] = None) -> Dict[str, int]",
    },
    "Matrix2": {
        "__init__": "(self, values: Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]] = 0) -> Matrix2",
        "__mul__": "(self, matrix2_or_scalar: Union[Matrix2, float]) -> Matrix2",
        "setTo": "(self, value: Sequence[float]) -> None",
    },
    "Matrix3": {
        "__init__": "(self, values: Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]] = 0) -> Matrix3",
        "__mul__": "(self, matrix3_or_scalar: Union[Matrix3, float]) -> Matrix4",
        "setTo": "(self, value: Sequence[float]) -> None",
        "removeScalesAndShears": "(self, transform_order: str = 'srt') -> Tuple[Vector3, Vector3]",
        "extractRotates": "(self, rotate_order: str = 'xyz') -> Vector3",
    },
    "Matrix4": {
        "__init__": "(self, values: Union[int, float, Sequence[Union[int, float]], Sequence[Sequence[Union[int, float]]]] = 0) -> Matrix4",
        "__mul__": "(self, matrix4_or_scalar: Union[Matrix4, float]) -> Matrix4",
        "explode": "(self, transform_order: str = 'srt', rotate_order: str = 'xyz', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> dict[str, Vector3]",
        "extractRotates": "(self, transform_order: str = 'srt', rotate_order: str = 'xyz', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "extractScales": "(self, transform_order: str = 'srt', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "extractShears": "(self, transform_order: str = 'srt', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "extractTranslates": "(self, transform_order: str = 'srt', pivot: Vector3 = ..., pivot_rotate: Vector3 = ...) -> Vector3",
        "setTo": "(self, value: Sequence[float]) -> None",
    },
    "MenuParmTemplate": {
        "__init__": "(self, name: str, label: str, menu_items: Sequence[str], menu_labels: Sequence[str] = ..., default_value: int = 0, icon_names: Sequence[str] = ..., item_generator_script: str = '', item_generator_script_language: Optional[EnumValue] = None, disable_when: Optional[str] = None, menu_type: EnumValue = menuType.Normal, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Dict[str, str] = ..., default_expression: str = '', default_expression_language: EnumValue = scriptLanguage.Hscript, store_default_value_as_string: bool = False, menu_use_token: bool = False, is_button_strip: bool = False, strip_uses_icons: bool = False) -> None",
        "setDefaultExpressionLanguage": "(self, default_expression_language: EnumValue) -> None",
    },
    "NetworkAnimValue": {
        # FIXME: The value_start and value_end types must be the same, so some overloads are
        #  in order to make this type annotation correct.
        "__init__": "(self, duration: Union[float, Vector2, Vector3, Vector4, NetworkAnimValue], value_start: Union[float, Vector2, Vector3, Vector4] = ..., value_end: Union[float, Vector2, Vector3, Vector4] = ...) -> None",
    },
    "NetworkEditor": {
        "flashMessage": "(self, image: Optional[str], message: Optional[str], duration: float) -> None",
        "openNodeMenu": "(self, node: Optional[Node] = None, items: Optional[Sequence[NetworkMovableItem]] = None) -> None",
        "openTabMenu": "(self, key: Optional[str] = None, auto_place: bool = False, branch: bool = False, src_item: Optional[NetworkMovableItem] = None, src_connector_index: int = -1, dest_item: Optional[NetworkMovableItem] = None, dest_connector_index: int = -1, node_position: Optional[Vector2] = None, src_items: Optional[Sequence[NetworkMovableItem]] = None, src_indexes: Optional[Sequence[int]] = None, dest_items: Optional[Sequence[NetworkMovableItem]] = None, dest_indexes: Optional[Sequence[int]] = None) -> None",
        "registerPref": "(self, pref: str, value: str, _global: bool) -> None",
        "setParmFilterCriteria": "(self, mode: EnumValue) -> None",
        "setParmFilterMode": "(self, mode: EnumValue) -> None",
    },
    "NetworkFootprint": {
        "__init__": "(self, condition: Union[EnumValue, str], color: Color, ring: int, use_minimum_size: bool) -> None",
    },
    "NetworkImage": {
        "__init__": "(self, path: str, rect: BoundingRect) -> None",
    },
    "NetworkMovableItem": {
        "shiftPosition": "(self, vector2: Union[Sequence[float], Vector2]) -> None",
    },
    "NetworkDot": {
        "setInput": "(self, input_index: int, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
    },
    "NetworkShapeConnection": {
        "__init__": "(self, input_pos: Vector2, input_dir: Vector2, output_pos: Vector2, output_dir: Vector2, color: Color = ..., alpha: float = 1.0, fade_factor: float = 0.0, smooth: bool = True, dashed: bool = False) -> None",
    },
    "NetworkShapeLine": {
        "__init__": "(self, start: Vector2, end: Vector2, color: Color = ..., alpha: float = 1.0, width: float = 1.0, screen_space: bool = True, smooth: bool = True, dashed: bool = False) -> None",
    },
    "NetworkShapeBox": {
        "__init__": "(self, rect: BoundingRect, color: Color = ..., alpha: float = 1.0, fill: bool = True, screen_space: bool = True, smooth: bool = True) -> None",
    },
    "NetworkShapeNodeShape": {
        "__init__": "(self, rect: BoundingRect, shape: str, color: Color = ..., alpha: float = 1.0, fill: bool = True, screen_space: bool = True, smooth: bool = True) -> None",
    },
    "Node": {
        "copyItemsToClipboard": "(self, items: Iterable[NetworkMovableItem]) -> None",
        "deleteItems": "(self, items: Iterable[NetworkMovableItem], disable_safety_checks: bool = False) -> None",
        "input": "(self, input_index: int) -> Optional[Self]",
        "inputFollowingOutputs": "(self, input_index: int) -> Optional[Self]",
        "inputs": "(self) -> Sequence[Self]",
        "layoutChildren": "(self, items: Sequence[NetworkMovableItem] = ..., horizontal_spacing: float = 1.0, vertical_spacing: float = 1.0) -> None",
        "outputs": "(self) -> Sequence[Self]",
        "recursiveGlob": "(self, pattern: str, filter: EnumValue = nodeTypeFilter.NoFilter, include_subnets: bool = True) -> Sequence[Node]",
        "setNamedInput": "(self, input_name: str, item_to_become_input: NetworkMovableItem, output_name_or_index: Union[str, int]) -> None",
    },
    "NodeInfoTree": {
        "__init__": "(self, tree_root: Any, tree: Any) -> None",
    },
    "ObjNode": {
        # FIXME: material should have the following annotations:
        #   operation: Literal['override', 'select', 'remove', 'rmdefault', 'sync', 'revert', 'addlist']
        "material": "(self, operation: str, parameter: Optional[Sequence[str]] = None) -> None",
    },
    "OpNode": {
        "addError": "(self, message: str, severity: EnumValue = ...) -> None",
        "cook": "(self, force: bool = False, frame_range: Sequence[float] = ...) -> None",
        "cookCodeGeneratorNode": "(self, check_parent: bool = False) -> Node",
        "fileReferences": "(self, recurse: bool = True, project_dir_variable: str = 'HIP', include_all_refs: bool = True) -> Sequence[Tuple[Parm, str]]",
        "needsToCook": "(self, time: float = ...) -> bool",
        "setDeleteScript": "(self, script_text: str, language: EnumValue = ...) -> None",
        "setFirstInput": "(self, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
        "setInput": "(self, input_index: int, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
        "stampValue": "(self, parm_name: str, default_value: Union[float, str]) -> str",
    },
    "OperationFailed": {
        "__init__": "(self, message: Optional[str] = ...) -> None",
    },
    "OrientedBoundingBox": {
        "__init__": "(self, oriented_bbox: OrientedBoundingBox = ...) -> None",
    },
    "PaneTab": {
        "displayRadialMenu": "(self, menu: Union[str, RadialScriptItem]) -> None",
    },
    "ParameterEditor": {
        "setFilterCriteria": "(self, criteria: EnumValue) -> None",
        "setFilterMode": "(self, mode: EnumValue) -> None",
    },
    "Parm": {
        "eval": "(self) -> Union[int, float, str]",
        "evalAtFrame": "(self, frame: float) -> Union[int, float, str]",
        "evalAtTime": "(self, frame: float) -> Union[int, float, str]",
        "keyframesRefit": "(self, refit: bool, refit_tol: float, refit_preserve_extrema: bool, refit_bezier: bool, resample: bool, resample_rate: float, resample_tol: float, range_: bool, range_start: float, range_end: bool, bake_chop: EnumValue, refit_smooth: bool) -> None",
        "pressButton": "(self, arguments: Dict[str, Union[int, bool, float, str]] = ...) -> None",
        "set": "(self, value: Union[int, float, str, Parm, Ramp], language: Optional[EnumValue] = None, follow_parm_reference: bool = True) -> None",
    },
    "ParmTemplate": {
        "conditionals": "(self) -> dict[EnumValue, str]",
        "setTags": "(self, tags: dict[str, str]) -> None",
    },
    "ParmTemplateGroup": {
        "__init__": "(self, parm_templates: Sequence[ParmTemplate] = ...) -> None",
        "appendToFolder": "(self, label_or_labels_or_parm_template_or_indices: Union[str, Sequence[str], ParmTemplate, Sequence[int]], parm_template: ParmTemplate) -> None",
        "asDialogScript": "(self, rename_conflicting_parms: bool = False, full_info: bool = False, script_name: Optional[str] = None, script_label: Optional[str] = None, script_tags: Dict[str, str] = ...) -> str",
        "containingFolder": "(self, name_or_parm_template: Union[str, ParmTemplate]) -> FolderParmTemplate",
        "containingFolderIndices": "(self, name_or_parm_template_or_indices: Union[str, ParmTemplate, Sequence[int]]) -> Sequence[int]",
        "findFolder": "(self, label_or_labels: Union[str, Sequence[str]]) -> Optional[ParmTemplate]",
        "findIndices": "(self, name_or_parm_template: Union[ParmTemplate, str]) -> Sequence[int]",
        "findIndicesForFolder": "(self, name_or_parm_template: Union[ParmTemplate, str]) -> Sequence[int]",
        "hide": "(self, name_or_parm_template_or_indices: Union[str, ParmTemplate, Sequence[int]], on: bool) -> None",
        "hideFolder": "(self, label_or_labels: Union[str, Sequence[str]], on: bool) -> None",
        "insertAfter": "(self, name_or_parm_template_or_indices: Union[str, ParmTemplate, Sequence[int]], parm_template: ParmTemplate) -> None",
        "insertBefore": "(self, name_or_parm_template_or_indices: Union[str, ParmTemplate, Sequence[int]], parm_template: ParmTemplate) -> None",
        "isFolderHidden": "(self, label_or_labels: Union[str, Sequence[str]]) -> bool",
        "isHidden": "(self, name_or_parm_template_or_indices: Union[str, ParmTemplate, Sequence[int]]) -> bool",
        "remove": "(self, name_or_parm_template_or_indices: Union[str, ParmTemplate, Sequence[int]]) -> None",
        "replace": "(self, name_or_parm_template_or_indices: Union[str, ParmTemplate, Sequence[int]], parm_template: ParmTemplate) -> None",
    },
    "ParmTuple": {
        "eval": "(self) -> Union[Sequence[int], Sequence[float], Sequence[str], Ramp]",
        "evalAtFrame": "(self, frame: float) -> Union[Sequence[int], Sequence[float], Sequence[str], Ramp]",
        "evalAtTime": "(self, frame: float) -> Union[Sequence[int], Sequence[float], Sequence[str], Ramp]",
        "lock": "(self, bool_values: Sequence[bool]) -> None",
        "node": "(self) -> OpNode",
        "setPending": "(self, values: Sequence[Union[float, str]]) -> None",
    },
    "PerfMonProfile": {
        "stats": "(self) -> dict[str, Any]",
    },
    "PluginHotkeyDefinitions": {
        "addDefaultBinding": "(self, context: str, command: str, assignments: Sequence[str], apply_platform_modifier_mappings: bool = True)",
    },
    "Point": {
        "attribValue": "(self, attrib: Union[Attrib, str]) -> Union[int, float, str, Sequence[int], Sequence[float], Dict[str, Any]]",
        "dictAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> dict[str, Any]",
        "dictListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[dict[str, Any]]",
        "floatAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> float",
        "floatListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[float]",
        "intAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> int",
        "intListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[int]",
        "setAttribValue": "(self, name_or_attrib: Union[str, Attrib], attrib_value: Union[int, float, str, Dict[str, Any]]) -> None",
        "stringAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> str",
        "stringListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[str]",
    },
    "PointGroup": {
        "add": "(self, point_or_list_or_point_group: Union[Point, Sequence[Point], PointGroup]) -> None",
        "option": "(self, option_name: str) -> Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]",
        "options": "(self) -> Dict[str, Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]]",
        "remove": "(self, point_or_list_or_point_group: Union[Point, Sequence[Point], PointGroup]) -> None",
        "setOption": "(self, name: str, value: Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]], type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "Prim": {
        "attribValue": "(self, attrib: Union[Attrib, str]) -> Union[int, float, str, Sequence[int], Sequence[float], Dict[str, Any]]",
        "attribValueAtInterior": "(self, attrib: Union[Attrib, str], u: float, v: float, w: float = 0.0) -> Union[int, float, str, Sequence[int], Sequence[float]]",
        "dictAttribValue": "(self, attrib: Union[Attrib, str]) -> Dict[str, Any]",
        "dictListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[dict[str, Any]]",
        "floatAttribValue": "(self, attrib: Union[Attrib, str]) -> float",
        "floatListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[float]",
        "intAttribValue": "(self, attrib: Union[Attrib, str]) -> int",
        "intListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[int]",
        "primuConvert": "(self, u: float, mode: int, tol: Optional[float] = ...) -> float",
        "primuvConvert": "(self, uv: Union[Sequence[float], Vector2], mode: int, tol: Optional[float] = ...) -> Vector2",
        "setAttribValue": "(self, name_or_attrib: Union[Attrib, str], attrib_value: Union[int, float, str, Dict[str, Any]]) -> None",
        "setIntrinsicValue": "(self, intrinsic_name: str, value: Union[int, float, str, Iterable[int], Iterable[float], Iterable[str]]) -> None",
        "stringAttribValue": "(self, attrib: Union[Attrib, str]) -> str",
        "stringListAttribValue": "(self, name_or_attrib: Union[Attrib, str]) -> Sequence[str]",
        "voxelRange": "(self, range: BoundingBox) -> Union[Sequence[bool], Sequence[int], Sequence[float], Sequence[Vector3]]",
    },
    "PrimGroup": {
        "add": "(self, prim_or_list_or_prim_group: Union[Prim, Sequence[Prim], PrimGroup]) -> None",
        "option": "(self, option_name: str) -> Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]",
        "options": "(self) -> Dict[str, Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]]",
        "remove": "(self, prim_or_list_or_prim_group: Union[Prim, Sequence[Prim], PrimGroup]) -> None",
        "setOption": "(self, name: str, value: Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]], type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "Quaternion": {
        "__init__": "(self, x: Union[Sequence[float], float, Matrix3, Matrix4], y: Union[Sequence[float], float], z: float = ..., w: float = ...) -> None",
        "__mul__": "(self, quaternion_or_scalar: Union[Quaternion, float]) -> Quaternion",
        "extractEulerRotates": "(self, rotate_order: str = 'xyz') -> Vector3",
        "setToEulerRotates": "(self, angles_in_deg: float, rotate_order: str = 'xyz') -> None",
        "setToRotationMatrix": "(self, matrix3_or_matrix4: Union[Matrix3, Matrix4]) -> None",
    },
    "Ramp": {
        "__init__": "(self, basis: Sequence[EnumValue], keys: Sequence[float], values: Union[Sequence[float], Sequence[Tuple[float, float, float]]]) -> None",
    },
    "RampParmTemplate": {
        "__init__": "(self, name: str, label: str, ramp_parm_type: EnumValue, default_value: int = 2, default_basis: Optional[EnumValue] = None, show_controls: bool = True, color_type: Optional[EnumValue] = None, disable_when: Optional[str] = None, is_hidden: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Dict[str, str] = ..., default_expression_language: EnumValue = scriptLanguage.Hscript) -> None",
    },
    "RopNode": {
        "render": "(self, frame_range: Optional[Sequence[float]] = None, res: Optional[Sequence[int]] = None, output_file: Optional[str] = None, output_format=None, to_flipbook: bool = False, quality: int = 2, ignore_inputs: bool = False, method=RopByRop, ignore_bypass_flags: bool = False, ignore_lock_flags: bool = False, verbose: bool = False, output_progress: bool = False) -> None",
    },
    "SceneViewer": {
        "bindViewerHandle": "(self, handle_type: str, name: str, settings: Optional[str] = None, cache_previous_parms: bool = False, handle_parms: Optional[Sequence[str]] = None) -> None",
        "bindViewerHandleStatic": "(self, handle_type: str, name: str, bindings: Sequence[str], settings: Optional[str] = None) -> None",
        "groupListMask": "(self) -> str",
        "isGroupPicking": "(self) -> bool",
        "locateSceneGraphPrim": "(self, x: int, y: int) -> Tuple[float, str]",
        "selectDrawableGeometry": "(self, drawable_selection: Dict[str, Incomplete], selection_modifier: EnumValue = pickModifier.Replace) -> None",
        "selectDynamics": "(self, prompt: str = 'Select objects', sel_index: int = 0, allow_objects: bool = True, allow_modifiers: bool = False, quick_select: bool = False, use_existing_selection: bool = True, allow_multisel: bool = True, icon: Optional[str] = None, label: Optional[str] = None, prior_selection_paths: Optional[Sequence[str]] = ..., prior_selection_ids: Optional[int] = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: Optional[str] = None, toolbox1_templategroupOptional[str] = None, select_parm: str = '') -> Sequence[DopData]",
        "selectDynamicsPoints": "(self, prompt: str = 'Select objects', sel_index: int = 0, quick_select: bool = False, use_existing_selection: bool = True, allow_multisel: bool = True, only_select_points: bool = True, object_based_point_selection: bool = False, use_last_selected_object: bool = False, icon: Optional[str] = None, label: Optional[str] = None, prior_selection_paths: Optional[Sequence[str]] = ..., prior_selection_ids: Optional[int] = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: Optional[str] = None, toolbox1_templategroupOptional[str] = None, select_parm: str = '') -> Sequence[tuple[DopData, GeometrySelection]]",
        "selectDynamicsPolygons": "(self, prompt: str = 'Select objects', sel_index: int = 0, quick_select: bool = False, use_existing_selection: bool = True, object_based_point_selection: bool = False, use_last_selected_object: bool = False, icon: Optional[str] = None, label: Optional[str] = None, prior_selection_paths: Optional[Sequence[str]] = ..., prior_selection_ids: Optional[int] = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: Optional[str] = None, toolbox1_templategroupOptional[str] = None, select_parm: str = '') -> Sequence[tuple[DopData, GeometrySelection]]",
        "selectGeometry": "(self, prompt: str = 'Select geometry', sel_index: int = 0, allow_drag: bool = False, quick_select: bool = False, use_existing_selection: bool = True, initial_selection: Optional[str] = None, initial_selection_type: Optional[EnumValue] = None, ordered: bool = False, geometry_types: Sequence[EnumValue] = ..., primitive_types: Sequence[EnumValue] = ..., allow_obj_sel: bool = True, icon: Optional[str] = None, label: Optional[str] = None, prior_selection_paths: list = ..., prior_selection_ids: list = ..., prior_selections: list = ..., allow_other_sops: bool = True, consume_selections: bool = True) -> GeometrySelection",
        "selectObjects": "(self, prompt: str = 'Select objects', sel_index: int = 0, allow_drag: bool = False, quick_select: bool = False, use_existing_selection: bool = True, allow_multisel: bool = True, allowed_types: Sequence[str] = ..., icon: Optional[str] = None, label: Optional[str] = None, prior_selection_paths: Optional[Sequence[str]] = ..., prior_selection_ids: Optional[int] = ..., prior_selections: Sequence[str] = ..., toolbox_templategroup: Optional[str] = None, toolbox1_templategroupOptional[str] = None, select_parm: str = '') -> Sequence[Node]",
        "selectOrientedPositions": "(self, prompt: str = 'Click to specify a position', number_of_positions: int = 1, min_number_of_positions: int = -1, connect_positions: bool = True, show_coordinates: bool = True, bbox: BoundingBox = ..., icon: Optional[str] = None, label: Optional[str] = None, toolbox_templategroup: Optional[str] = None, toolbox1_templategroup: Optional[str] = None, select_parm: str = '') -> Sequence[tuple[Vector3, Matrix3]]",
        "selectPositions": "(self, prompt: str = 'Click to specify a position', number_of_positions: int = 1, min_number_of_positions: int = -1, connect_positions: bool = True, show_coordinates: bool = True, bbox: BoundingBox = ..., position_type: EnumValue = positionType.WorldSpace, icon: Optional[str] = None, label: Optional[str] =None, toolbox_templategroup: Optional[str] = None, toolbox1_templategroup: Optional[str] = None, select_parm: str ='') -> Sequence[Vector3]",
        "selectSceneGraph": "(self, prompt: str ='Select primitives', preselection: Sequence[str] = ..., prim_mask: EnumValue = scenePrimMask.ViewerSetting, quick_select: bool = False, use_existing_selection: bool = True, confirm_existing: bool = False, allow_multisel: bool = True, allow_drag: bool = True, propagate_selection: bool = True, path_prefix_mask: str = '', prim_kind: str = '', validate_selection_for_node: Incomplete = ..., select_parm: str = '', allow_kind_mismatch: EnumValue = optionalBool.NoOpinion, allow_instance_proxies: EnumValue = optionalBool.NoOpinion, fix_preselection_paths=True) -> Sequence[str]",
        "selectSceneGraphInstances": "(self, prompt: str = 'Select point instances', preselection: Sequence[str] = ..., quick_select: bool = False, use_existing_selection: bool = True, confirm_existing: bool = False, allow_multisel: bool = True, allow_drag: bool = True, path_prefix_mask: str = '', instance_level: int = 0, instance_indices_only: bool = False, validate_selection_for_node: Incomplete = ..., select_parm: str = '') -> Sequence[str]",
        "setCurrentState": "(self, state: EnumValue, wait_for_exit: bool = False, generate: EnumValue = stateGenerateMode.Insert, request_new_on_generate: bool = True, ex_situ_generate: bool = False) -> None",
        "setPromptMessage": "(self, msg: str, msg_type: EnumValue = promptMessageType.Prompt) -> None",
        "triggerStateSelector": "(self, action: EnumValue, name: Optional[str] = None) -> None",
    },
    "ScriptEvalContext": {
        "__init__": "(self, node_or_parm: Union[OpNode, Parm]) -> None"
    },
    "Selection": {
        "__init__": "(self, selection: Union[EnumValue, Geometry, Sequence[Prim], Sequence[Point], Sequence[Vertex], Sequence[Edge]], geometry_type: Union[EnumValue, Sequence[EnumValue]] = ..., selection_string: str = ...) -> None",
        "numSelected": "(self) -> int",
    },
    "SeparatorParmTemplate": {
        "__init__": "(self, name: str, is_hidden: bool = False, tags: Dict[str, str] = ...) -> None",
    },
    "ShopNode": {
        "shaderCode": "(self, shader_type: Optional[EnumValue] = None) -> str",
        "shaderString": "(self, render_type: Optional[str] = None) -> str",
    },
    "SimpleDrawable": {
        "__init__": "(self, scene_viewer: SceneViewer, geometry: Union[Geometry, EnumValue], name: str) -> None",
        "setOutlineColor": "(self, color: Union[Color, Vector4]) -> None",
    },
    "SopNodeType": {
        "addSelector": "(self, name: str, selector_type: str, prompt: str = 'Select components', primitive_types: Sequence[EnumValue] = ..., group_parm_name: Optional[str] = None, group_type_parm_name: Optional[str] = None, input_index: int = 0, input_required: bool = True, allow_dragging: bool = False, empty_string_selects_all: bool = True) -> Selector",
        "selectors": "(self, selector_indices: Sequence[int] = ...) -> Sequence[Selector]",
    },
    "StickyNote": {
        "setSize": "(self, size: Union[Sequence[float], Vector2]) -> None",
    },
    "StringKeyframe": {
        "__init__": "(self, expression: Optional[str] = None, time: Optional[float] = None, language: Optional[EnumValue] = exprLanguage.Python) -> None",
    },
    "StringParmTemplate": {
        "__init__": "(self, name: str, label: str, num_components: int, default_value: Sequence[str] = ..., naming_scheme: EnumValue = parmNamingScheme.Base1, string_type: EnumValue = stringParmType.Regular, file_type: EnumValue = fileType.Any, menu_items: Sequence[str] = ..., menu_labels: Sequence[str] = ..., icon_names: Sequence[str] = ..., item_generator_script: Optional[str] = None, item_generator_script_language: Optional[EnumValue] = None, menu_type: EnumValue = menuType.Normal, disable_when: Optional[str] = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Dict[str, str] = ..., default_expression: Sequence[str] = ..., default_expression_language: Sequence[EnumValue] = ...) -> None",
    },
    "StyleSheet": {
        "__init__": "(self, json_text: str = ...) -> None",
        "cloneWithAddedStyleSheet": "(self, stylesheet: StyleSheet, target: Optional[str] = ...) -> StyleSheet",
    },
    "Surface": {
        "attribValueAt": "(self, attrib_or_name: Union[Attrib, str], u: float, v: float, du: float = 0, dv: float = 0) -> Union[int, float, str, Sequence[int], Sequence[float]]"
    },
    "SwigPyIterator": {
        "__sub__": "(self, n: int) -> Any",
    },
    "Take": {
        "loadChildTakeFromFile": "(self, filename: str) -> Sequence[Take]",
        "name": "(self) -> str",
    },
    "TextDrawable": {
        "__init__": "(self, scene_viewer: SceneViewer, name: str, label: Optional[str] = None, params: Optional[Dict[str, Any]] = None) -> None",
    },
    "ToggleParmTemplate": {
        "__init__": "(self, name: str, label: str, default_value: bool = False, disable_when: Optional[str]  =None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: Dict[str, str] = ..., default_expression: str = '', default_expression_language: EnumValue = scriptLanguage.Hscript) -> None",
    },
    "Tool": {
        "setData": "(self, script: str = '', language: EnumValue = scriptLanguage.Python, icon: str = '', help: str = '', help_url: str = '', network_categories: Sequence[NodeTypeCategory] = ..., viewer_categories: Sequence[NodeTypeCategory] = ..., cop_viewer_categories: Sequence[NodeTypeCategory] = ..., network_op_type: str = '', viewer_op_type: str = '', locations: Sequence[str] = ...) -> None",
    },
    "TopNode": {
        "cookWorkItems": "(self, block: bool = False, generate_only: bool = False, tops_only: bool = False, save_prompt: bool = False, nodes: Sequence[TopNode] = ...) -> None",
        "generateStaticWorkItems": "(self, block: bool = False, nodes: Sequence[TopNode] = ...) -> None",
    },
    "Vector2": {
        "__init__": "(self, x: Union[Sequence[float], float] = ..., y: float = ...) -> None",
        "__mul__": "(self, scalar_or_matrix2: Union[float, Matrix2]) -> Vector2",
    },
    "Vector3": {
        "__init__": "(self, x: Union[Sequence[float], float] = ..., y: float = ..., z: float = ...) -> None",
        "__mul__": "(self, scalar_or_matrix3_or_matrix4: Union[float, Matrix3, Matrix4]) -> Vector3",
        "smoothRotation": "(self, reference: Vector3, rotate_order: str = 'xyz') -> Vector3",
    },
    "Vector4": {
        "__init__": "(self, x: Union[Sequence[float], float] = ..., y: float = ..., z: float = ..., w: float = ...) -> None",
        "__mul__": "(self, scalar_or_matrix4: Union[float,  Matrix4]) -> Vector4",
    },
    "Vertex": {
        "attribValue": "(self, attrib: Union[Attrib, str]) -> Union[int, float, str, Sequence[int], Sequence[float], Dict[str, Any]]",
        "dictAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> dict[str, Any]",
        "dictListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[dict[str, Any]]",
        "floatAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> float",
        "floatListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[float]",
        "intAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> int",
        "intListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[int]",
        "setAttribValue": "(self, name_or_attrib: Union[str, Attrib], attrib_value: Union[int, float, str, Dict[str, Any]]) -> None",
        "stringAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> str",
        "stringListAttribValue": "(self, name_or_attrib: Union[str, Attrib]) -> Sequence[str]",
    },
    "VertexGroup": {
        "add": "(self, vertex_or_list_or_vertex_group: Union[Vertex, Sequence[Vertex], VertexGroup]) -> None",
        "option": "(self, option_name: str) -> Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]",
        "options": "(self) -> Dict[str, Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]]]",
        "remove": "(self, vertex_or_list_or_vertex_group: Union[Vertex, Sequence[Vertex], VertexGroup]) -> None",
        "setOption": "(self, name: str, value: Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Sequence[int], Sequence[float]], type_hint: EnumValue = fieldType.NoSuchField) -> None",
    },
    "ViewerHandleContext": {
        "scaleFactor": "(self, ref_position: Sequence[float] = ...) -> float",
    },
    "ViewerHandleTemplate": {
        "__init__": "(self, name: str, label: str, categories: Sequence[EnumValue]) -> None",
        "bindGadget": "(self, drawable_type: EnumValue, gadget_name: str , gadget_label: Optional[str] = None, parms: Optional[Sequence[str]] = None) -> None",
        "bindParameter": "(self, param_type: EnumValue, name: str , label: Optional[str] = None, default_value: Optional[Union[int, float, str]] = None, num_components: int = 1, min_limit: int = 0, max_limit: int = 1, visible: bool = True) -> None",
        "bindSetting": "(self, param_type: EnumValue, name: str , label: Optional[str] = None, menu_as_button_strip: bool = False, menu_items: Optional[Sequence[Union[Tuple[str, str], Tuple[str, str, str]]]] = None, num_components: int = 1, default_value: Optional[Union[int, float, str]] = None, min_limit: int = 0, max_limit: int = 1, align: bool = False) -> None",
    },
    "ViewerState": {
        "parmTemplates": "(self) -> ParmTemplateGroup",
    },
    "ViewerStateDragger": {
        "__init__": "(self, name: str, xform: Matrix4 = ..., inv_xform: Matrix4 = ...) -> None",
    },
    "ViewerStateMenu": {
        "addActionItem": "(self, id,: str label: str, hotkey: str = '') -> None",
        "addRadioStripItem": "(self, strip_id: str, id: str label: str, hotkey: str = '') -> None",
        "addToggleItem": "(self, id,: str label: str, default: bool, hotkey: str = '') -> None",
    },
    "ViewerStateTemplate": {
        "__init__": "(self, state_name: str, state_label: str, node_type_category: NodeTypeCategory, contexts: Optional[Sequence[NodeTypeCategory]] = None)",
        "bindDrawableSelector": "(self, prompt: str, auto_start: bool = True, toolbox: bool = True, drawable_mask=[], hotkey: str = '', name: str = '') -> None",
        "bindDynamicsPointSelector": "(self, prompt: str, allow_objects: bool = True, allow_modifiers: bool = False, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, allow_multisel: bool = True, only_select_points: bool = True, object_based_point_selection: bool = False, use_last_selected_object: bool = False, hotkey: str = '', name: str = '') -> None",
        "bindDynamicsPolygonSelector": "(self, prompt: str, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, object_based_point_selection: bool = False, secure_selection: EnumValue = secureSelectionOption.Obey, use_last_selected_object: bool = False, hotkey: str = '', name: str = '') -> None",
        "bindDynamicsSelector": "(self, prompt: str, allow_objects: bool = True, allow_modifiers: bool = False, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, allow_multisel: bool = True, hotkey: str = '', name: str = '') -> None",
        "bindGadget": "(self, drawable_type: EnumValue, gadget_name: str, gadget_label: Optional[str] = None) -> None",
        "bindGeometrySelector": "(self, prompt: str, allow_drag: bool = False, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, consume_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, initial_selection: str = '', initial_selection_type: EnumValue = geometryType.Primitives, ordered: bool = False, geometry_types: Sequence[EnumValue] = ..., primitive_types: Sequence[EnumValue] = ..., allow_other_sops: bool = False, hotkey: str = '', name: str = '') -> None",
        "bindHandle": "(self, handle_type: str, name: str, settings: Optional[str] = None) -> None",
        "bindHandleStatic": "(self, handle_type: str, name: str, bindings: Sequence[str] , settings: Optional[str] = None) -> None",
        "bindObjectSelector": "(self, prompt: str, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, allow_multisel: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, allowed_types: Sequence[str] = ..., hotkey: str = '', name: str = '') -> None",
        "bindParameter": "(self, param_type: EnumValue, name: Optional[str] = None, label: Optional[str] = None, menu_as_button_strip: bool = False, menu_items: Optional[Sequence[Union[Tuple[str, str], Tuple[str, str, str]]]] = None, num_components: int = 1, default_value=None, min_limit: int = 0, max_limit: int = 1, align: bool = False, toolbox: bool = True) -> None",
        "bindSceneGraphSelector": "(self, prompt: str, allow_drag: bool = True, quick_select: bool = True, auto_start: bool = True, toolbox: bool = True, use_existing_selection: bool = True, secure_selection: EnumValue = secureSelectionOption.Obey, consume_selection: bool = False, allow_multisel: bool = True, prior_selection_paths=None, prim_mask=None, path_prefix_mask=None, prim_kind=None, hotkey: str = '', name: str = '') -> None",
        "bindSelector": "(self, name, selector_type, prompt: str, primitive_types=None, group_parm_name=None, input_index=0, input_required: bool = True, allow_dragging: bool = True) -> None",
    },
    "ViewportVisualizer": {
        "setParm": "(self, parm_name: str, value: Union[int, float, str]) -> None",
    },
    "VopNode": {
        "shaderCode": "(self, shader_type: Optional[EnumValue] = None) -> str",
        "shaderString": "(self, render_type: Optional[str] = None, shader_type: EnumValue = shaderType.Surface, as_encapsulated: bool = False) -> str",
    },
    "anim": {
        "getGeometryChannels": "(collection_name: str, geometry: Geometry, channel_names: Optional[Sequence[str]] = None) -> None",
        "isGeometryChannelPinned": "(collection_name: str, channel_names: Optional[str] = None) -> bool",
        "mergeGeometryChannels": "(collection_name: str, geometry: Geometry, channel_names: Optional[Sequence[str]] = None) -> None",
        "newBookmark": "(name: str, start: float, end: float) -> Bookmark",
        "saveBookmarks": "(filename: str, bookmarks: Optional[Sequence[Bookmark]] = None, include_temporary: bool = False) -> bool",
        "saveBookmarksToString": "(bookmarks: Optional[Sequence[Bookmark]] = None, include_temporary: bool = False, binary: bool = True) -> bytes",
        "setGeometryChannelsFromPattern": "(collection_name: str, geometry: Geometry, pattern: str) -> None",
    },
    "crowds": {
        "findAgentDefinitions": "(geometry: Geometry, group: str = '', group_type: EnumValue = geometryType.Primitives) -> Sequence[AgentDefinition]",
        "replaceAgentDefinitions": "(geometry: Geometry, new_definition_map: Dict[AgentDefinition, AgentDefinition], group: str = '', group_type: EnumValue = geometryType.Primitives) -> None",
        "setBlendshapeDeformerParms": "(base_shape_geo: Geometry, attribs: str = 'P N', point_id_attrib: str = 'id', prim_id_attrib: str = 'id') -> None",
    },
    "hipFile": {
        "collisionNodesIfMerged": "(file_name: str, node_pattern: str = '*') -> Sequence[OpNode]",
        "importFBX": "(file_name: str, suppress_save_prompt: bool = False, merge_into_scene: bool = True, import_cameras: bool = True, import_joints_and_skin: bool = True, import_geometry: bool = True, import_lights: bool = True, import_animation: bool = True, import_materials: bool = True, resample_animation: bool = False, resample_interval: float = 1.0, override_framerate: bool = False, framerate: int = -1, hide_joints_attached_to_skin: bool = True, convert_joints_to_zyx_rotation_order: bool = False, material_mode: EnumValue = fbxMaterialMode.FBXShaderNodes, compatibility_mode: EnumValue = fbxCompatibilityMode.Maya, single_precision_vertex_caches: bool = False, triangulate_nurbs: bool = False, triangulate_patches: bool = False, import_global_ambient_light: bool = False, import_blend_deformers_as_blend_sops: bool = False, segment_scale_already_baked_in: bool = True, convert_file_paths_to_relative: bool = True, unlock_geometry: bool = False, unlock_deformations: bool = False, import_nulls_as_subnets: bool = False, import_into_object_subnet: bool = True, convert_into_y_up_coordinate_system: bool = False, create_sibling_bones: bool = True, override_scene_frame_range: bool = False, convert_units: bool = False) -> Sequence[ObjNode]",
        "merge": "(file_name: str, node_pattern: str = '*', overwrite_on_conflict: bool = False, ignore_load_warnings: bool = False) -> None",
    },
    "hmath": {
        "buildRotate": "(rx: Union[float, Vector3], ry: float = ..., rz: float = ..., order: str = 'xyz') -> Matrix4",
        "buildScale": "(sx: Union[float, Vector3], sy: float = ..., sz: float = ...) -> Matrix4",
        "buildShear": "(shearx: Union[float, Vector3], sheary: float = ..., shearz: float = ...) -> Matrix4",
        "buildTransform": "(values_dict: dict[str, Union[Vector3, Sequence[float]]], transform_order: str = 'srt', rotate_order: str = 'xyz') -> Matrix4",
        "buildTranslate": "(tx: Union[float, Vector3], ty: float = ..., tz: float = ...) -> Matrix4",
        "combineLocalTransform": "(local: Matrix4, world: Matrix4, parent_local: Optional[Matrix4] = None, mode: EnumValue = scaleInheritanceMode.Default) -> Matrix4",
        "extractLocalTransform": "(local: Matrix4, world: Matrix4, parent_local: Matrix4, mode: EnumValue = scaleInheritanceMode.Default, effective_local: Optional[Matrix4] = None) -> Matrix4",
    },
    "hotkeys": {
        "addAssignment": "(context: str, hotkey_symbol: str, key: str) -> bool",
        "addCommand": "(hotkey_symbol: str, label: str, description: str, assignments: Sequence[str]) -> bool",
        "assignments": "(hotkey_symbol: str) -> Sequence[str]",
        "availableKeycodes": "(context: str, hotkey_symbol: str, layout_keys: Optional[Sequence[str]] = None, modifiers: int = 0) -> Sequence[int]",
        "clearAssignments": "(context: str, hotkey_symbol: str) -> bool",
        "findConflicts": "(context: str, hotkey_symbol: str, key: Optional[str] = None) -> Sequence[str]",
        "removeAssignment": "(context: str, hotkey_symbol: str, key: str) -> bool",
        "revertToDefaults": "(context: str, hotkey_symbol: str, one_level_only: bool) -> None",
    },
    "ik": {
        "solveFBIK": "(skeleton: Sequence[_ik_Skeleton], targets: Sequence[_ik_Target], iters: int = 30, tolerance: float = 1e-5, pin_root: bool = False) -> None",
        "solvePhysFBIK": "(skeleton: Sequence[_ik_Skeleton], targets: Sequence[_ik_Target], com_target: Optional[_ik_Target] = None, iters: int = 30, damping: float = 0.5, tolerance: float = 1e-5) -> None",
    },
    "lop": {
        "addLockedGeometry": "(identifier: str, geo: Geometry, args: Optional[Dict[str, str]] = None) -> str",
        "createConnectionParmsForProperty": "(source: Union[LopNode, str], primpath: str, propertyname: str, parametername: Optional[str] = None, prepend_control_parm: bool = ...) -> ParmTemplateGroup",
        "createParmsForProperty": "(source: Union[LopNode, str], primpath: str, propertyname: str, parametername: Optional[str] = None, prepend_control_parm: bool = ..., prefix_xform_parms: bool = ...) -> ParmTemplateGroup",
        "setParmTupleFromProperty": "(parmtuple: ParmTuple, source: Union[LopNode, str], primpath: str, propertyname: str) -> None",
        "translateShader": "(node: Node, node_output_name: str, material_prim_path: str, container_prim_path: str, shader_prim_name: Optional[str] = None, frame: Optional[float] = None) -> str",
    },
    "playbar": {
        "setChannelList": "(arg: ChannelList) -> None",
    },
    "properties": {
        "classes": "(tags: Optional[Sequence[str]] = None) -> Sequence[str]",
    },
    "shelves": {
        "newTool": "(file_path: Optional[str] = None, name: Optional[str] = None, label: Optional[str] = None, script: Optional[str] = None, language: EnumValue = scriptLanguage.Python, icon: Optional[str] = None, help: Optional[str] = None, help_url: Optional[str] = None, network_categories: Sequence[NodeTypeCategory] = ..., viewer_categories: Sequence[NodeTypeCategory] = ..., cop_viewer_categories: Sequence[NodeTypeCategory] = ..., network_op_type: Optional[str] = None, viewer_op_type: Optional[str] = None, locations: Sequence[str] = ..., hda_definition: Optional[HDADefinition] = None) -> Tool",
    },
    "text": {
        "collapseCommonVars": "(path: str, vars: Sequence[str] = ...) -> str",
    },
    "ui": {
        "displayConfirmation": "(text: str, severity_type: EnumValue = ..., help: Optional[str] = None, title: Optional[str] = None, details: Optional[str] = None, details_label: Optional[str] = None, details_expanded: bool = False, suppress: EnumValue = ...) -> bool",
        "displayCustomConfirmation": "(text: str, buttons: Sequence[str] = ..., severity_type: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: Optional[str] = None, title: Optional[str] = None, details: Optional[str] = None, details_label: Optional[str] = None, details_expanded: bool = False, suppress: EnumValue = ...) -> int",
        "displayFileDependencyDialog": "(rop_node: Optional[RopNode] = None, uploaded_files: Sequence[str] = ..., forced_unselected_patterns: Sequence[str] = ..., project_dir_variable: str = 'HIP', is_standalone: bool = true) -> Tuple[bool, Sequence[Tuple[Parm, str]]]",
        "displayMessage": "(text: str, buttons: Sequence[str] = ..., severity_type: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: Optional[str] = None, title: Optional[str] = None, details: Optional[str] = None, details_label: Optional[str] = None, details_expanded: bool = False, suppress: EnumValue = ...) -> int",
        "getDragSourceData": "(label: str, index: int = 0) -> Any",
        "hasDragSourceData": "(label: str, index: int) -> bool",
        "loadPackageArchive": "(file_path: str, extract_path: Optional[str] = None) -> Sequence[str]",
        "openFileEditor": "(title: str, file_path: str, action_callback: Optional[Callable[[Dict[str, Union[int, float, bool, str]]], None]] = None, params: Optional[Dict[str, Union[int, float, bool, str]]] =None) -> None",
        "openValueLadder": "(initial_value: float, value_changed_callback: Callable[[float], None], type: EnumValue = valueLadderType.Generic, data_type: EnumValue = valueLadderDataType.Float) -> None",
        "openViewerStateCodeGenDialog": "(category: NodeTypeCategory, action_callback: Callable[[Dict[str, Union[int, float, bool, str]]], None], operator_name: Optional[str] = None) -> None",
        "packageInfo": "(file_paths: Sequence[str]) -> str",
        "printResourceMessage": "(resource_type: EnumValue, message: str, message_type: EnumValue = ...) -> None",
        "readInput": "(text: str, buttons: Sequence[str] = ..., severity_type: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: Optional[str] = None, title: Optional[str] = None, initial_contents: Optional[str] = None) -> Tuple[int, str]",
        "readMultiInput": "(text: str, input_labels: Sequence[str], password_input_indices: Sequence[int] = ..., buttons: Sequence[str] = ..., severity_type: EnumValue = ..., default_choice: int = 0, close_choice: int = -1, help: Optional[str] = None, title: Optional[str] = None, initial_contents: Sequence[str] = ...) -> Tuple[int, Sequence[str]]",
        "reloadViewerStates": "(state_names: Optional[Sequence[str]] = None) -> None",
        "selectFromList": "(choices: Sequence[str], default_choices: Sequence[int] = ..., exclusive: bool = False, message: Optional[str] = None, title: Optional[str] = None, column_header: str = 'Choices', num_visible_rows: int = 10, clear_on_cancel: bool = False, width: int = 0, height: int = 0, sort: bool = False, condense_paths: bool = False) -> Sequence[int]",
        "selectFromTree": "(choices: Sequence[str], picked: Sequence[int] = ..., exclusive: bool = False, message: Optional[str] = None, title: Optional[str] = None, clear_on_cancel: bool = False, width: int = 0, height: int = 0) -> Sequence[str]",
        "selectParm": "(category: NodeTypeCategory = ..., bound_parms_only: bool = False, relative_to_node: Optional[OpNode] = None, message: Optional[str] = None, title: Optional[str] = None, initial_parms: Sequence[Parm] = ..., multiple_select: bool = True, width: int = 0, height: int = 0) -> Sequence[str]",
        "selectParmTuple": "(category: NodeTypeCategory = ..., bound_parms_only: bool = False, relative_to_node: Optional[OpNode] = None, message: Optional[str] = None, title: Optional[str] = None, initial_parm_tuples: Sequence[ParmTuple] = ..., multiple_select: bool = True, width: int = 0, height: int = 0) -> Sequence[str]",
        "setStatusMessage": "(message: str, severity: EnumValue = ...) -> None",
        "viewerHandleInfo": "(handle_names: Sequence[str] = ...) -> str",
        "viewerStateInfo": "(state_names: Sequence[str] = ...) -> str",
    },
    "viewportVisualizers": {
        # FIXME: The Callables provided to the callback system for viewport visualizers take
        #  different argument types and numbers of arguments according to the event type associated
        #  with the callback.  To avoid an overload nightmare and to avoid fully articulating code
        #  that is likely to be out of date at some stage, I'm going to leave them as `Callable`
        #  with no subscript annotation.
        #  See the documentation of hou.viewportVisualizerEventType for more information.
        "addEventCallback": "(self, event_types: EnumValue, callback: Callable, category: EnumValue = viewportVisualizerCategory.Common, node: Optional[Node] = None) -> None",
        "createVisualizer": "(type: EnumValue, category: EnumValue = viewportVisualizerCategory.Common, node: Optional[Node] = None) -> ViewportVisualizer",
        "eventCallbacks": "(category=hou.viewportVisualizerCategory.Common, node=None) -> Sequence[tuple[Sequence[EnumValue], Callable]]",
        "removeAllEventCallbacks": "(self, category: EnumValue = viewportVisualizerCategory.Common, node: Optional[Node] = None) -> None",
        "removeEventCallback": "(self, event_types: Sequence[EnumValue], callback: Callable, category: EnumValue = viewportVisualizerCategory.Common, node: Optional[Node] = None) -> None",
        "visualizers": "(category: EnumValue = viewportVisualizerCategory.Common, node: Optional[Node] = None) -> Sequence[ViewportVisualizer]",
    },
}
