import Boost.Python
import pxr.Usd
from typing import Any, ClassVar, overload

class GenerativeProceduralAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> GenerativeProceduralAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateProceduralSystemAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateProceduralTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> GenerativeProceduralAPI: ...
    def GetProceduralSystemAttr(self) -> pxr.Usd.Attribute: ...
    def GetProceduralTypeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    HwPrimvar_1: ClassVar[Any] = ...  # read-only
    HwPtexTexture_1: ClassVar[Any] = ...  # read-only
    HwUvTexture_1: ClassVar[Any] = ...  # read-only
    HydraGenerativeProceduralAPI: ClassVar[Any] = ...  # read-only
    black: ClassVar[Any] = ...  # read-only
    clamp: ClassVar[Any] = ...  # read-only
    displayLookBxdf: ClassVar[Any] = ...  # read-only
    faceIndex: ClassVar[Any] = ...  # read-only
    faceOffset: ClassVar[Any] = ...  # read-only
    frame: ClassVar[Any] = ...  # read-only
    hydraGenerativeProcedural: ClassVar[Any] = ...  # read-only
    infoFilename: ClassVar[Any] = ...  # read-only
    infoVarname: ClassVar[Any] = ...  # read-only
    linear: ClassVar[Any] = ...  # read-only
    linearMipmapLinear: ClassVar[Any] = ...  # read-only
    linearMipmapNearest: ClassVar[Any] = ...  # read-only
    magFilter: ClassVar[Any] = ...  # read-only
    minFilter: ClassVar[Any] = ...  # read-only
    mirror: ClassVar[Any] = ...  # read-only
    nearest: ClassVar[Any] = ...  # read-only
    nearestMipmapLinear: ClassVar[Any] = ...  # read-only
    nearestMipmapNearest: ClassVar[Any] = ...  # read-only
    primvarsHdGpProceduralType: ClassVar[Any] = ...  # read-only
    proceduralSystem: ClassVar[Any] = ...  # read-only
    repeat: ClassVar[Any] = ...  # read-only
    textureMemory: ClassVar[Any] = ...  # read-only
    useMetadata: ClassVar[Any] = ...  # read-only
    uv: ClassVar[Any] = ...  # read-only
    wrapS: ClassVar[Any] = ...  # read-only
    wrapT: ClassVar[Any] = ...  # read-only
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