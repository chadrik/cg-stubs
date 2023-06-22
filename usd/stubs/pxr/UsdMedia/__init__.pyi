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
    def GetAssetDefaultPreviews(cls, layerPath: object) -> AssetPreviewsAPI: ...
    def GetDefaultThumbnails(self) -> Any: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def SetDefaultThumbnails(self, thumbnails: Thumbnails) -> None: ...
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
    def CreateAuralModeAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateEndTimeAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFilePathAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateGainAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMediaOffsetAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePlaybackModeAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateStartTimeAttr(self, defaultValue: object = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
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
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list: ...
    def GetStartTimeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def AssetPreviewsAPI(self) -> Any: ...
    @property
    def SpatialAudio(self) -> Any: ...
    @property
    def auralMode(self) -> Any: ...
    @property
    def defaultImage(self) -> Any: ...
    @property
    def endTime(self) -> Any: ...
    @property
    def filePath(self) -> Any: ...
    @property
    def gain(self) -> Any: ...
    @property
    def loopFromStage(self) -> Any: ...
    @property
    def loopFromStart(self) -> Any: ...
    @property
    def loopFromStartToEnd(self) -> Any: ...
    @property
    def mediaOffset(self) -> Any: ...
    @property
    def nonSpatial(self) -> Any: ...
    @property
    def onceFromStart(self) -> Any: ...
    @property
    def onceFromStartToEnd(self) -> Any: ...
    @property
    def playbackMode(self) -> Any: ...
    @property
    def previewThumbnails(self) -> Any: ...
    @property
    def previewThumbnailsDefault(self) -> Any: ...
    @property
    def previews(self) -> Any: ...
    @property
    def spatial(self) -> Any: ...
    @property
    def startTime(self) -> Any: ...
    @property
    def thumbnails(self) -> Any: ...

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