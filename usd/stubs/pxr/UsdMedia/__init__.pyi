import Boost.Python
import pxr.UsdGeom
from typing import Any, ClassVar, overload

class AssetPreviewsAPI(pxr.Usd.APISchemaBase):
    class Thumbnails(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        defaultImage: Any
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, defaultImage: pxr.Sdf.AssetPath = ...) -> None: ...
        def __reduce__(self) -> Any: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> AssetPreviewsAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ClearDefaultThumbnails(self) -> None: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> AssetPreviewsAPI: ...
    @overload
    @classmethod
    def GetAssetDefaultPreviews(cls, layer: pxr.Sdf.Layer) -> AssetPreviewsAPI: ...
    @overload
    @classmethod
    def GetAssetDefaultPreviews(cls, layerPath: str) -> AssetPreviewsAPI: ...
    def GetDefaultThumbnails(self) -> bool: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def SetDefaultThumbnails(self, thumbnails: AssetPreviewsAPI.Thumbnails) -> None: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class SpatialAudio(pxr.UsdGeom.Xformable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateAuralModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateEndTimeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFilePathAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateGainAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMediaOffsetAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePlaybackModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateStartTimeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> SpatialAudio: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> SpatialAudio: ...
    def GetAuralModeAttr(self) -> pxr.Usd.Attribute: ...
    def GetEndTimeAttr(self) -> pxr.Usd.Attribute: ...
    def GetFilePathAttr(self) -> pxr.Usd.Attribute: ...
    def GetGainAttr(self) -> pxr.Usd.Attribute: ...
    def GetMediaOffsetAttr(self) -> pxr.Usd.Attribute: ...
    def GetPlaybackModeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetStartTimeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    AssetPreviewsAPI: ClassVar[Any] = ...  # read-only
    SpatialAudio: ClassVar[Any] = ...  # read-only
    auralMode: ClassVar[Any] = ...  # read-only
    defaultImage: ClassVar[Any] = ...  # read-only
    endTime: ClassVar[Any] = ...  # read-only
    filePath: ClassVar[Any] = ...  # read-only
    gain: ClassVar[Any] = ...  # read-only
    loopFromStage: ClassVar[Any] = ...  # read-only
    loopFromStart: ClassVar[Any] = ...  # read-only
    loopFromStartToEnd: ClassVar[Any] = ...  # read-only
    mediaOffset: ClassVar[Any] = ...  # read-only
    nonSpatial: ClassVar[Any] = ...  # read-only
    onceFromStart: ClassVar[Any] = ...  # read-only
    onceFromStartToEnd: ClassVar[Any] = ...  # read-only
    playbackMode: ClassVar[Any] = ...  # read-only
    previewThumbnails: ClassVar[Any] = ...  # read-only
    previewThumbnailsDefault: ClassVar[Any] = ...  # read-only
    previews: ClassVar[Any] = ...  # read-only
    spatial: ClassVar[Any] = ...  # read-only
    startTime: ClassVar[Any] = ...  # read-only
    thumbnails: ClassVar[Any] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    @overload
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    @overload
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def whyNot(self) -> Any: ...