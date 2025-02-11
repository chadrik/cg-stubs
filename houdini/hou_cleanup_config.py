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
        "def voxelRangeAsBool(self, range: BoundingBox) -> Tuple[bool, ...]",
        "def voxelRangeAsInt(self, range: BoundingBox) -> Tuple[int, ...]",
        "def voxelRangeAsFloat(self, range: BoundingBox) -> Tuple[float, ...]",
        "def voxelRangeAsVector3(self, range: BoundingBox) -> Tuple[Vector3, ...]",
    ],
    "Geometry": [
        "def pointAttribs(self, scope: EnumValue) -> Tuple[Attrib, ...]",
        "def primAttribs(self, scope: EnumValue) -> Tuple[Attrib, ...]",
        "def vertexAttribs(self, scope: EnumValue) -> Tuple[Attrib, ...]",
        "def globalAttribs(self, scope: EnumValue) -> Tuple[Attrib, ...]",
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
    "_ik_Skeleton": {
        "addJoint",
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
# FIXME: Audit functions that take *args and add the remaining functions here.
#   Searching for `(?<!__init__)\((self(, )?)?\*args` will return
#   the ~381 remaining functions that need to be explicitly fixed and defined by us here.
#   We need to pull out the argspec from the docstring and do our best to determine the types
#   Of the arguments, which is a bit time consuming, but not difficult.
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
        "removeAnimationLayer": "(layermixer: ChopNode, layername: str, merge_down: bool = False) -> bool",
        "applicationVersion": "(include_patch: bool = False) -> Tuple[int, int, int]",
        "createAnimationClip": "(path: str = ..., set_export: bool = False) -> ChopNode",
        "createAnimationLayers": "(path: str = ...) -> ChopNode",
        # FIXME: The type annotation and default value for precision are being stripped out.
        #   Possible that it is being stripped out because it is `Literal`, but even
        #   when we declare it as a string, the default is also pulled out.
        "runVex": "(vex_file: str, inputs: dict[str, Any], precision: Literal['32', '64'] = '32') -> dict[str, Any]",
        "startHoudiniEngineDebugger": "(portOrPipeName: Union[int, str]) -> None",
    },
    "_StringMapDoubleTuple": {
        "__iter__": "(self) -> Iterator[str]",
    },
    "AgentMetadata": {
        "data": "(self) -> dict[str, Any]",
        "setData": "(self, data: dict[str, Any]) -> None",
        "setMetadata": "(self, item_id: str, metadata: dict[str, Any]) -> None",
    },
    "Attrib": {
        "option": "(self, option_name: str) -> Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Tuple[int, ...], Tuple[float, ...]]",
        "options": "(self) -> Dict[str, Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Tuple[int, ...], Tuple[float, ...]]]",
    },
    "Bookmark": {
        "setEndFrame": "(self, end: float) -> None",
        "setStartFrame": "(self, start: float) -> None",
        "metadata": "(self, key: str, default_value: Any = None) -> Any"
    },
    "ChannelGraph": {
        "selectedKeyframes": "(self) -> dict[Parm, Tuple[BaseKeyframe, ...]]",
    },
    "DataParmTemplate": {
        "__init__": "(self, name: , label: , num_components: int, look: EnumValue = parmLook.Regular, naming_scheme: EnumValue = parmNamingScheme.XYZW, unknown_str: Optional[str] = None, disable_when: Optional[str] = None, is_hidden: bool = False, is_label_hidden: bool = False, join_with_next: bool = False, help: Optional[str] = None, script_callback: Optional[str] = None, script_callback_language: EnumValue = scriptLanguage.Hscript, tags: dict[str, str] = {}, unknown_dict: dict[EnumValue, str] = {}, default_expression: Sequence[str] = (), default_expression_language: Sequence[EnumValue] = ()) -> DataParmTemplate",
    },
    "Desktop": {
        "createFloatingPanel": "(self, pane_tab_type: EnumValue, position: Sequence[float] = ..., size: Sequence[float] = ..., python_panel_interface: Optional[PythonPanelInterface] = ..., immediate: bool = False) -> FloatingPanel",
    },
    "Face": {
        "attribValueAt": "(self, attrib_or_name: str, u: float, du: int = 0) -> Any"
    },
    "FolderSetParmTemplate": {
        "folderNames": "(self) -> list[str]",
        "setFolderNames": "(self, folder_names: Sequence[str]) -> None",
    },
    "Geometry": {
        "addAttrib": "(self, type: EnumValue, name: str, default_value: Any, transform_as_normal: bool = True, create_local_variable: bool = True) -> Attrib",
        "deletePoints": "(self, points: Union[Iterable[Point], PointGroup]) -> None",
        "deletePrims": "(self, prims: Union[Iterable[Prim], PrimGroup], keep_points: bool = False) -> None",
        "transformPrims": "(self, prims: Union[Iterable[Prim], PrimGroup], matrix: Matrix4) -> None",
        "setGlobalAttribValue": "(self, name_or_attrib: Union[str, Attrib], attrib_value: Any) -> None",
    },
    "GeometryViewport": {
        "changeType": "(self, type: EnumValue) -> None",
    },
    "Keyframe": {
        "__init__": "(self, value: Optional[float] = None, time: Optional[float] = None) -> None",
    },
    "LopNode": {
        "activeLayer": "(self, output_index: int = 0, ignore_errors: bool = False, use_last_cook_context_options: bool = True, frame: Optional[float] = None, context_options: Dict[str, Any] = ...) -> pxr.Sdf.Layer",
        "displayNode": "(self) -> LopNode",
        "setLastModifiedPrims": "(self, primPaths: Sequence[str]) -> None",
        "sourceLayer": "(self, layer_index: int = 0, output_index: int = 0, use_last_cook_context_options: bool = True, frame: Optional[float] = None, context_options: Dict[str, Any] = ...) -> pxr.Sdf.Layer",
        "stage": "(self, output_index: int = 0, apply_viewport_overrides: bool = False, ignore_errors: bool = False, use_last_cook_context_options: bool = True, apply_post_layers: bool = True, frame: Optional[float] = None, context_options: Dict[str, Any] = ...) -> pxr.Sdf.Stage",
    },
    "Matrix2": {
        "__init__": "(self, values: Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]] = 0) -> Matrix2",
    },
    "Matrix3": {
        "__init__": "(self, values: Union[int, float, Iterable[Union[int, float]], Iterable[Iterable[Union[int, float]]]] = 0) -> Matrix3",
    },
    "Matrix4": {
        "__init__": "(self, values: Union[int, float, Sequence[Union[int, float]], Sequence[Sequence[Union[int, float]]]] = 0) -> Matrix4",
    },
    "MenuParmTemplate": {
        "setDefaultExpressionLanguage": "(self, default_expression_language: EnumValue) -> None",
    },
    "NetworkEditor": {
        "flashMessage": "(self, image: Optional[str], message: Optional[str], duration: float) -> None",
        "registerPref": "(self, pref: str, value: str, _global: bool) -> None",
    },
    "NetworkMovableItem": {
        "shiftPosition": "(self, vector2: Union[Sequence[float], Vector2]) -> None",
    },
    "NetworkDot": {
        "setInput": "(self, input_index: int, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
    },
    "Node": {
        "input": "(self, input_index: int) -> Optional[Self]",
        "inputFollowingOutputs": "(self, input_index: int) -> Optional[Self]",
        "inputs": "(self) -> Tuple[Self, ...]",
        "layoutChildren": "(self, items: Sequence[NetworkMovableItem] = ..., horizontal_spacing: float = 1.0, vertical_spacing: float = 1.0) -> None",
        "outputs": "(self) -> Tuple[Self, ...]",
    },
    "NodeInfoTree": {
        "__init__": "(self, tree_root: Any, tree: Any) -> None",
    },
    "OpNode": {
        "setFirstInput": "(self, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
        "setInput": "(self, input_index: int, item_to_become_input: Optional[NetworkMovableItem], output_index: int = 0) -> None",
        "cookCodeGeneratorNode": "(self, check_parent: bool = False) -> Node",
    },
    "OperationFailed": {
        "__init__": "(self, message: Optional[str] = ...) -> None",
    },
    "Parm": {
        "eval": "(self) -> Union[int, float, str]",
        "evalAtFrame": "(self, frame: float) -> Union[int, float, str]",
        "evalAtTime": "(self, frame: float) -> Union[int, float, str]",
        "pressButton": "(self, arguments: Dict[str, Union[int, bool, float, str]] = ...) -> None",
        "set": "(self, value: Union[int, float, str, Parm, Ramp], language: Optional[EnumValue] = None, follow_parm_reference: bool = True) -> None",
    },
    "ParmTemplate": {
        "conditionals": "(self) -> dict[EnumValue, str]",
        "setTags": "(self, tags: dict[str, str]) -> None",
    },
    "ParmTemplateGroup": {
        "containingFolder": "(self, name_or_parm_template: Union[str, ParmTemplate]) -> FolderParmTemplate",
    },
    "ParmTuple": {
        "eval": "(self) -> Union[Tuple[int, ...], Tuple[float, ...], Tuple[str, ...], Ramp]",
        "evalAtFrame": "(self, frame: float) -> Union[Tuple[int, ...], Tuple[float, ...], Tuple[str, ...], Ramp]",
        "evalAtTime": "(self, frame: float) -> Union[Tuple[int, ...], Tuple[float, ...], Tuple[str, ...], Ramp]",
        "node": "(self) -> OpNode",
    },
    "PerfMonProfile": {
        "stats": "(self) -> dict[str, Any]",
    },
    "PointGroup": {
        "option": "(self, option_name: str) -> Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Tuple[int, ...], Tuple[float, ...]]",
        "options": "(self) -> Dict[str, Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Tuple[int, ...], Tuple[float, ...]]]",
    },
    "Prim": {
        "setIntrinsicValue": "(self, intrinsic_name: str, value: Union[int, float, str, Iterable[int], Iterable[float], Iterable[str]]) -> None",
        "voxelRange": "(self, range: BoundingBox) -> Union[Tuple[bool, ...], Tuple[int, ...], Tuple[float, ...], Tuple[Vector3, ...]]",
        "primuConvert": "(self, u: float, mode: int, tol: Optional[float] = ...) -> float",
        "primuvConvert": "(self, uv: Union[Sequence[float], Vector2], mode: int, tol: Optional[float] = ...) -> Vector2",
    },
    "PrimGroup": {
        "option": "(self, option_name: str) -> Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Tuple[int, ...], Tuple[float, ...]]",
        "options": "(self) -> Dict[str, Union[bool, int, float, str, Vector2, Vector3, Vector4, Quaternion, Matrix3, Matrix4, Tuple[int, ...], Tuple[float, ...]]]",
    },
    "SceneViewer": {
        "groupListMask": "(self) -> str",
        "isGroupPicking": "(self) -> bool",
        "selectGeometry": "(self, prompt: str = 'Select geometry', sel_index: int = 0, allow_drag: bool = False, quick_select: bool = False, use_existing_selection: bool = True, initial_selection: Optional[str] = None, initial_selection_type: Optional[EnumValue] = None, ordered: bool = False, geometry_types: Sequence[EnumValue] = ..., primitive_types: Sequence[EnumValue] = ..., allow_obj_sel: bool = True, icon: Optional[str] = None, label: Optional[str] = None, prior_selection_paths: list = ..., prior_selection_ids: list = ..., prior_selections: list = ..., allow_other_sops: bool = True, consume_selections: bool = True) -> GeometrySelection",
    },
    "ScriptEvalContext": {
        "__init__": "(self, node_or_parm: Union[OpNode, Parm]) -> None"
    },
    "Selection": {
        "numSelected": "(self) -> int",
    },
    "StickyNote": {
        "setSize": "(self, size: Union[Sequence[float], Vector2]) -> None",
    },
    "StringKeyframe": {
        "__init__": "(self, expression: Optional[str] = None, time: Optional[float] = None, language: Optional[EnumValue] = exprLanguage.Python) -> None",
    },
    "SwigPyIterator": {
        "__sub__": "(self, n: int) -> Any",
    },
    "Take": {
        "name": "(self) -> str",
        "loadChildTakeFromFile": "(self, filename: str) -> Tuple[Take, ...]",
    },
    "ViewerState": {
        "parmTemplates": "(self) -> ParmTemplateGroup",
    },
    "ViewportVisualizer": {
        "setParm": "(self, parm_name: str, value: Union[int, float, str]) -> None",
    },
    "anim": {
        "newBookmark": "(name: str, start: float, end: float) -> Bookmark",
    },
    "hmath": {
        "buildTranslate": "(tx: Union[float, Vector3], ty: float = ..., tz: float = ...) -> Matrix4",
        "buildRotate": "(rx: Union[float, Vector3], ry: float = ..., rz: float = ..., order: str = 'xyz') -> Matrix4",
        "buildScale": "(sx: Union[float, Vector3], sy: float = ..., sz: float = ...) -> Matrix4",
        "buildShear": "(shearx: Union[float, Vector3], sheary: float = ..., shearz: float = ...) -> Matrix4",
        "buildTransform": "(values_dict: dict[str, Union[Vector3, Sequence[float]]], transform_order: str = 'srt', rotate_order: str = 'xyz') -> Matrix4",
    },
    "hotkeys": {
        "assignments": "(hotkey_symbol: str) -> list[str]",
    },
    "playbar": {
        "setChannelList": "(arg: ChannelList) -> None",
    },
    "ui": {
        "getDragSourceData": "(label: str, index: int = 0) -> Any",
        "hasDragSourceData": "(label: str, index: int) -> bool",
    },
    "viewportVisualizer": {
        "createVisualizer": "(type: EnumValue, category: EnumValue = viewportVisualizerCategory.Common, node: Optional[Node] = None) -> ViewportVisualizer",
    },
}
