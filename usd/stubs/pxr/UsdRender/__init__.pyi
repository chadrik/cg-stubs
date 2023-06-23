import Boost.Python
import pxr.Usd
from typing import Any, ClassVar, overload

class DenoisePass(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> DenoisePass: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> DenoisePass: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Pass(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateCommandAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDenoiseEnableAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDenoisePassRel(self) -> pxr.Usd.Relationship: ...
    def CreateFileNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateInputPassesRel(self) -> pxr.Usd.Relationship: ...
    def CreatePassTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRenderSourceRel(self) -> pxr.Usd.Relationship: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Pass: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Pass: ...
    def GetCommandAttr(self) -> pxr.Usd.Attribute: ...
    def GetDenoiseEnableAttr(self) -> pxr.Usd.Attribute: ...
    def GetDenoisePassRel(self) -> pxr.Usd.Relationship: ...
    def GetFileNameAttr(self) -> pxr.Usd.Attribute: ...
    def GetInputPassesRel(self) -> pxr.Usd.Relationship: ...
    def GetPassTypeAttr(self) -> pxr.Usd.Attribute: ...
    def GetRenderSourceRel(self) -> pxr.Usd.Relationship: ...
    def GetRenderVisibilityCollectionAPI(self) -> pxr.Usd.CollectionAPI: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Product(SettingsBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateOrderedVarsRel(self) -> pxr.Usd.Relationship: ...
    def CreateProductNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateProductTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Product: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Product: ...
    def GetOrderedVarsRel(self) -> pxr.Usd.Relationship: ...
    def GetProductNameAttr(self) -> pxr.Usd.Attribute: ...
    def GetProductTypeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Settings(SettingsBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateIncludedPurposesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateMaterialBindingPurposesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateProductsRel(self) -> pxr.Usd.Relationship: ...
    def CreateRenderingColorSpaceAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Settings: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Settings: ...
    def GetIncludedPurposesAttr(self) -> pxr.Usd.Attribute: ...
    def GetMaterialBindingPurposesAttr(self) -> pxr.Usd.Attribute: ...
    def GetProductsRel(self) -> pxr.Usd.Relationship: ...
    def GetRenderingColorSpaceAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def GetStageRenderSettings(cls, arg1: pxr.Usd.Stage) -> Settings: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class SettingsBase(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateAspectRatioConformPolicyAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateCameraRel(self) -> pxr.Usd.Relationship: ...
    def CreateDataWindowNDCAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDisableMotionBlurAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateInstantaneousShutterAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePixelAspectRatioAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateResolutionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> SettingsBase: ...
    def GetAspectRatioConformPolicyAttr(self) -> pxr.Usd.Attribute: ...
    def GetCameraRel(self) -> pxr.Usd.Relationship: ...
    def GetDataWindowNDCAttr(self) -> pxr.Usd.Attribute: ...
    def GetDisableMotionBlurAttr(self) -> pxr.Usd.Attribute: ...
    def GetInstantaneousShutterAttr(self) -> pxr.Usd.Attribute: ...
    def GetPixelAspectRatioAttr(self) -> pxr.Usd.Attribute: ...
    def GetResolutionAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    RenderDenoisePass: ClassVar[Any] = ...  # read-only
    RenderPass: ClassVar[Any] = ...  # read-only
    RenderProduct: ClassVar[Any] = ...  # read-only
    RenderSettings: ClassVar[Any] = ...  # read-only
    RenderSettingsBase: ClassVar[Any] = ...  # read-only
    RenderVar: ClassVar[Any] = ...  # read-only
    adjustApertureHeight: ClassVar[Any] = ...  # read-only
    adjustApertureWidth: ClassVar[Any] = ...  # read-only
    adjustPixelAspectRatio: ClassVar[Any] = ...  # read-only
    aspectRatioConformPolicy: ClassVar[Any] = ...  # read-only
    camera: ClassVar[Any] = ...  # read-only
    collectionRenderVisibilityIncludeRoot: ClassVar[Any] = ...  # read-only
    color3f: ClassVar[Any] = ...  # read-only
    command: ClassVar[Any] = ...  # read-only
    cropAperture: ClassVar[Any] = ...  # read-only
    dataType: ClassVar[Any] = ...  # read-only
    dataWindowNDC: ClassVar[Any] = ...  # read-only
    denoiseEnable: ClassVar[Any] = ...  # read-only
    denoisePass: ClassVar[Any] = ...  # read-only
    disableMotionBlur: ClassVar[Any] = ...  # read-only
    expandAperture: ClassVar[Any] = ...  # read-only
    fileName: ClassVar[Any] = ...  # read-only
    full: ClassVar[Any] = ...  # read-only
    includedPurposes: ClassVar[Any] = ...  # read-only
    inputPasses: ClassVar[Any] = ...  # read-only
    instantaneousShutter: ClassVar[Any] = ...  # read-only
    intrinsic: ClassVar[Any] = ...  # read-only
    lpe: ClassVar[Any] = ...  # read-only
    materialBindingPurposes: ClassVar[Any] = ...  # read-only
    orderedVars: ClassVar[Any] = ...  # read-only
    passType: ClassVar[Any] = ...  # read-only
    pixelAspectRatio: ClassVar[Any] = ...  # read-only
    preview: ClassVar[Any] = ...  # read-only
    primvar: ClassVar[Any] = ...  # read-only
    productName: ClassVar[Any] = ...  # read-only
    productType: ClassVar[Any] = ...  # read-only
    products: ClassVar[Any] = ...  # read-only
    raster: ClassVar[Any] = ...  # read-only
    raw: ClassVar[Any] = ...  # read-only
    renderSettingsPrimPath: ClassVar[Any] = ...  # read-only
    renderSource: ClassVar[Any] = ...  # read-only
    renderVisibility: ClassVar[Any] = ...  # read-only
    renderingColorSpace: ClassVar[Any] = ...  # read-only
    resolution: ClassVar[Any] = ...  # read-only
    sourceName: ClassVar[Any] = ...  # read-only
    sourceType: ClassVar[Any] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class Var(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSourceNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSourceTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Var: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Var: ...
    def GetDataTypeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetSourceNameAttr(self) -> pxr.Usd.Attribute: ...
    def GetSourceTypeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...