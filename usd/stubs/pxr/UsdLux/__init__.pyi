# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.Gf
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdShade
import typing
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class BoundableLightBase(pxr.UsdGeom.Boundable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDiffuseAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateEnableColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateExposureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFiltersRel(self) -> pxr.Usd.Relationship: ...
    def CreateIntensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSpecularAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BoundableLightBase: ...
    def GetColorAttr(self) -> pxr.Usd.Attribute: ...
    def GetColorTemperatureAttr(self) -> pxr.Usd.Attribute: ...
    def GetDiffuseAttr(self) -> pxr.Usd.Attribute: ...
    def GetEnableColorTemperatureAttr(self) -> pxr.Usd.Attribute: ...
    def GetExposureAttr(self) -> pxr.Usd.Attribute: ...
    def GetFiltersRel(self) -> pxr.Usd.Relationship: ...
    def GetIntensityAttr(self) -> pxr.Usd.Attribute: ...
    def GetNormalizeAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetSpecularAttr(self) -> pxr.Usd.Attribute: ...
    def LightAPI(self) -> LightAPI: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class CylinderLight(BoundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateLengthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTreatAsLineAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CylinderLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> CylinderLight: ...
    def GetLengthAttr(self) -> pxr.Usd.Attribute: ...
    def GetRadiusAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetTreatAsLineAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class DiskLight(BoundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DiskLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DiskLight: ...
    def GetRadiusAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class DistantLight(NonboundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateAngleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistantLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DistantLight: ...
    def GetAngleAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class DomeLight(NonboundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateGuideRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePortalsRel(self) -> pxr.Usd.Relationship: ...
    def CreateTextureFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTextureFormatAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight: ...
    def GetGuideRadiusAttr(self) -> pxr.Usd.Attribute: ...
    def GetPortalsRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetTextureFileAttr(self) -> pxr.Usd.Attribute: ...
    def GetTextureFormatAttr(self) -> pxr.Usd.Attribute: ...
    def OrientToStageUpAxis(self) -> None: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class DomeLight_1(NonboundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateGuideRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePoleAxisAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePortalsRel(self) -> pxr.Usd.Relationship: ...
    def CreateTextureFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTextureFormatAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight_1: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> DomeLight_1: ...
    def GetGuideRadiusAttr(self) -> pxr.Usd.Attribute: ...
    def GetPoleAxisAttr(self) -> pxr.Usd.Attribute: ...
    def GetPortalsRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetTextureFileAttr(self) -> pxr.Usd.Attribute: ...
    def GetTextureFormatAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class GeometryLight(NonboundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateGeometryRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GeometryLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> GeometryLight: ...
    def GetGeometryRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class LightAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> LightAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI: ...
    def CreateColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDiffuseAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateEnableColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateExposureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFiltersRel(self) -> pxr.Usd.Relationship: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input: ...
    def CreateIntensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMaterialSyncModeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output: ...
    def CreateShaderIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSpecularAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightAPI: ...
    def GetColorAttr(self) -> pxr.Usd.Attribute: ...
    def GetColorTemperatureAttr(self) -> pxr.Usd.Attribute: ...
    def GetDiffuseAttr(self) -> pxr.Usd.Attribute: ...
    def GetEnableColorTemperatureAttr(self) -> pxr.Usd.Attribute: ...
    def GetExposureAttr(self) -> pxr.Usd.Attribute: ...
    def GetFiltersRel(self) -> pxr.Usd.Relationship: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]: ...
    def GetIntensityAttr(self) -> pxr.Usd.Attribute: ...
    def GetLightLinkCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    def GetMaterialSyncModeAttr(self) -> pxr.Usd.Attribute: ...
    def GetNormalizeAttr(self) -> pxr.Usd.Attribute: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetShaderId(self, renderContexts: list[str] | list[pxr.Ar.ResolvedPath]) -> str: ...
    def GetShaderIdAttr(self) -> pxr.Usd.Attribute: ...
    def GetShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath) -> pxr.Usd.Attribute: ...
    def GetShadowLinkCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    def GetSpecularAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class LightFilter(pxr.UsdGeom.Xformable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output: ...
    def CreateShaderIdAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightFilter: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightFilter: ...
    def GetFilterLinkCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetShaderId(self, renderContexts: list[str] | list[pxr.Ar.ResolvedPath]) -> str: ...
    def GetShaderIdAttr(self) -> pxr.Usd.Attribute: ...
    def GetShaderIdAttrForRenderContext(self, renderContext: str | pxr.Ar.ResolvedPath) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class LightListAPI(pxr.Usd.APISchemaBase):
    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    ComputeModeConsultModelHierarchyCache: ClassVar[LightListAPI.ComputeMode] = ...
    ComputeModeIgnoreCache: ClassVar[LightListAPI.ComputeMode] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> LightListAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ComputeLightList(self, arg2: LightListAPI.ComputeMode) -> list[pxr.Sdf.Path]: ...
    def CreateLightListCacheBehaviorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLightListRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> LightListAPI: ...
    def GetLightListCacheBehaviorAttr(self) -> pxr.Usd.Attribute: ...
    def GetLightListRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def InvalidateLightList(self) -> None: ...
    def StoreLightList(self, arg2: typing.Iterable[pxr.Sdf.Path | str]) -> None: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ListAPI(pxr.Usd.APISchemaBase):
    class ComputeMode(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        @staticmethod
        def GetValueFromName(name: object) -> Any: ...
    ComputeModeConsultModelHierarchyCache: ClassVar[LightListAPI.ComputeMode] = ...
    ComputeModeIgnoreCache: ClassVar[LightListAPI.ComputeMode] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ListAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ComputeLightList(self, arg2: LightListAPI.ComputeMode) -> list[pxr.Sdf.Path]: ...
    def CreateLightListCacheBehaviorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateLightListRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ListAPI: ...
    def GetLightListCacheBehaviorAttr(self) -> pxr.Usd.Attribute: ...
    def GetLightListRel(self) -> pxr.Usd.Relationship: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def InvalidateLightList(self) -> None: ...
    def StoreLightList(self, arg2: typing.Iterable[pxr.Sdf.Path | str]) -> None: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class MeshLightAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> MeshLightAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> MeshLightAPI: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class NonboundableLightBase(pxr.UsdGeom.Xformable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDiffuseAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateEnableColorTemperatureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateExposureAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFiltersRel(self) -> pxr.Usd.Relationship: ...
    def CreateIntensityAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSpecularAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> NonboundableLightBase: ...
    def GetColorAttr(self) -> pxr.Usd.Attribute: ...
    def GetColorTemperatureAttr(self) -> pxr.Usd.Attribute: ...
    def GetDiffuseAttr(self) -> pxr.Usd.Attribute: ...
    def GetEnableColorTemperatureAttr(self) -> pxr.Usd.Attribute: ...
    def GetExposureAttr(self) -> pxr.Usd.Attribute: ...
    def GetFiltersRel(self) -> pxr.Usd.Relationship: ...
    def GetIntensityAttr(self) -> pxr.Usd.Attribute: ...
    def GetNormalizeAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetSpecularAttr(self) -> pxr.Usd.Attribute: ...
    def LightAPI(self) -> LightAPI: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class PluginLight(pxr.UsdGeom.Xformable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLight: ...
    def GetNodeDefAPI(self) -> pxr.UsdShade.NodeDefAPI: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class PluginLightFilter(LightFilter):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLightFilter: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PluginLightFilter: ...
    def GetNodeDefAPI(self) -> pxr.UsdShade.NodeDefAPI: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class PortalLight(BoundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateWidthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PortalLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PortalLight: ...
    def GetHeightAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetWidthAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class RectLight(BoundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateHeightAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTextureFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateWidthAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RectLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> RectLight: ...
    def GetHeightAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetTextureFileAttr(self) -> pxr.Usd.Attribute: ...
    def GetWidthAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ShadowAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ShadowAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output: ...
    def CreateShadowColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShadowDistanceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShadowEnableAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShadowFalloffAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShadowFalloffGammaAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ShadowAPI: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetShadowColorAttr(self) -> pxr.Usd.Attribute: ...
    def GetShadowDistanceAttr(self) -> pxr.Usd.Attribute: ...
    def GetShadowEnableAttr(self) -> pxr.Usd.Attribute: ...
    def GetShadowFalloffAttr(self) -> pxr.Usd.Attribute: ...
    def GetShadowFalloffGammaAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class ShapingAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, connectable: pxr.UsdShade.ConnectableAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> ShapingAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def ConnectableAPI(self) -> pxr.UsdShade.ConnectableAPI: ...
    def CreateInput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Input: ...
    def CreateOutput(self, name: str | pxr.Ar.ResolvedPath, type: pxr.Sdf.ValueTypeName) -> pxr.UsdShade.Output: ...
    def CreateShapingConeAngleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShapingConeSoftnessAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShapingFocusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShapingFocusTintAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShapingIesAngleScaleAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShapingIesFileAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateShapingIesNormalizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> ShapingAPI: ...
    def GetInput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Input: ...
    def GetInputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Input]: ...
    def GetOutput(self, name: str | pxr.Ar.ResolvedPath) -> pxr.UsdShade.Output: ...
    def GetOutputs(self, onlyAuthored: bool = ...) -> list[pxr.UsdShade.Output]: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetShapingConeAngleAttr(self) -> pxr.Usd.Attribute: ...
    def GetShapingConeSoftnessAttr(self) -> pxr.Usd.Attribute: ...
    def GetShapingFocusAttr(self) -> pxr.Usd.Attribute: ...
    def GetShapingFocusTintAttr(self) -> pxr.Usd.Attribute: ...
    def GetShapingIesAngleScaleAttr(self) -> pxr.Usd.Attribute: ...
    def GetShapingIesFileAttr(self) -> pxr.Usd.Attribute: ...
    def GetShapingIesNormalizeAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class SphereLight(BoundableLightBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateRadiusAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTreatAsPointAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @staticmethod
    def Define(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphereLight: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> SphereLight: ...
    def GetRadiusAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    def GetTreatAsPointAttr(self) -> pxr.Usd.Attribute: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class Tokens(Boost.Python.instance):
    BoundableLightBase: ClassVar[str] = ...  # read-only
    CylinderLight: ClassVar[str] = ...  # read-only
    DiskLight: ClassVar[str] = ...  # read-only
    DistantLight: ClassVar[str] = ...  # read-only
    DomeLight: ClassVar[str] = ...  # read-only
    DomeLight_1: ClassVar[str] = ...  # read-only
    GeometryLight: ClassVar[str] = ...  # read-only
    LightAPI: ClassVar[str] = ...  # read-only
    LightFilter: ClassVar[str] = ...  # read-only
    LightListAPI: ClassVar[str] = ...  # read-only
    ListAPI: ClassVar[str] = ...  # read-only
    MeshLight: ClassVar[str] = ...  # read-only
    MeshLightAPI: ClassVar[str] = ...  # read-only
    NonboundableLightBase: ClassVar[str] = ...  # read-only
    PluginLight: ClassVar[str] = ...  # read-only
    PluginLightFilter: ClassVar[str] = ...  # read-only
    PortalLight: ClassVar[str] = ...  # read-only
    RectLight: ClassVar[str] = ...  # read-only
    ShadowAPI: ClassVar[str] = ...  # read-only
    ShapingAPI: ClassVar[str] = ...  # read-only
    SphereLight: ClassVar[str] = ...  # read-only
    VolumeLight: ClassVar[str] = ...  # read-only
    VolumeLightAPI: ClassVar[str] = ...  # read-only
    Y: ClassVar[str] = ...  # read-only
    Z: ClassVar[str] = ...  # read-only
    angular: ClassVar[str] = ...  # read-only
    automatic: ClassVar[str] = ...  # read-only
    collectionFilterLinkIncludeRoot: ClassVar[str] = ...  # read-only
    collectionLightLinkIncludeRoot: ClassVar[str] = ...  # read-only
    collectionShadowLinkIncludeRoot: ClassVar[str] = ...  # read-only
    consumeAndContinue: ClassVar[str] = ...  # read-only
    consumeAndHalt: ClassVar[str] = ...  # read-only
    cubeMapVerticalCross: ClassVar[str] = ...  # read-only
    filterLink: ClassVar[str] = ...  # read-only
    geometry: ClassVar[str] = ...  # read-only
    guideRadius: ClassVar[str] = ...  # read-only
    ignore: ClassVar[str] = ...  # read-only
    independent: ClassVar[str] = ...  # read-only
    inputsAngle: ClassVar[str] = ...  # read-only
    inputsColor: ClassVar[str] = ...  # read-only
    inputsColorTemperature: ClassVar[str] = ...  # read-only
    inputsDiffuse: ClassVar[str] = ...  # read-only
    inputsEnableColorTemperature: ClassVar[str] = ...  # read-only
    inputsExposure: ClassVar[str] = ...  # read-only
    inputsHeight: ClassVar[str] = ...  # read-only
    inputsIntensity: ClassVar[str] = ...  # read-only
    inputsLength: ClassVar[str] = ...  # read-only
    inputsNormalize: ClassVar[str] = ...  # read-only
    inputsRadius: ClassVar[str] = ...  # read-only
    inputsShadowColor: ClassVar[str] = ...  # read-only
    inputsShadowDistance: ClassVar[str] = ...  # read-only
    inputsShadowEnable: ClassVar[str] = ...  # read-only
    inputsShadowFalloff: ClassVar[str] = ...  # read-only
    inputsShadowFalloffGamma: ClassVar[str] = ...  # read-only
    inputsShapingConeAngle: ClassVar[str] = ...  # read-only
    inputsShapingConeSoftness: ClassVar[str] = ...  # read-only
    inputsShapingFocus: ClassVar[str] = ...  # read-only
    inputsShapingFocusTint: ClassVar[str] = ...  # read-only
    inputsShapingIesAngleScale: ClassVar[str] = ...  # read-only
    inputsShapingIesFile: ClassVar[str] = ...  # read-only
    inputsShapingIesNormalize: ClassVar[str] = ...  # read-only
    inputsSpecular: ClassVar[str] = ...  # read-only
    inputsTextureFile: ClassVar[str] = ...  # read-only
    inputsTextureFormat: ClassVar[str] = ...  # read-only
    inputsWidth: ClassVar[str] = ...  # read-only
    latlong: ClassVar[str] = ...  # read-only
    lightFilterShaderId: ClassVar[str] = ...  # read-only
    lightFilters: ClassVar[str] = ...  # read-only
    lightLink: ClassVar[str] = ...  # read-only
    lightList: ClassVar[str] = ...  # read-only
    lightListCacheBehavior: ClassVar[str] = ...  # read-only
    lightMaterialSyncMode: ClassVar[str] = ...  # read-only
    lightShaderId: ClassVar[str] = ...  # read-only
    materialGlowTintsLight: ClassVar[str] = ...  # read-only
    mirroredBall: ClassVar[str] = ...  # read-only
    noMaterialResponse: ClassVar[str] = ...  # read-only
    orientToStageUpAxis: ClassVar[str] = ...  # read-only
    poleAxis: ClassVar[str] = ...  # read-only
    portals: ClassVar[str] = ...  # read-only
    scene: ClassVar[str] = ...  # read-only
    shadowLink: ClassVar[str] = ...  # read-only
    treatAsLine: ClassVar[str] = ...  # read-only
    treatAsPoint: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...

class VolumeLightAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def Apply(prim: pxr.Usd.Prim) -> VolumeLightAPI: ...
    @staticmethod
    def CanApply(prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    @staticmethod
    def Get(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> VolumeLightAPI: ...
    @staticmethod
    def GetSchemaAttributeNames(includeInherited: bool = ...) -> list[str]: ...
    @staticmethod
    def _GetStaticTfType() -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def whyNot(self): ...

def BlackbodyTemperatureAsRgb(arg1: float) -> pxr.Gf.Vec3f: ...
