import Boost.Python
import pxr.Usd
from typing import Any, ClassVar, overload

class Backdrop(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    def CreateDescriptionAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Backdrop: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> Backdrop: ...
    def GetDescriptionAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class NodeGraphNodeAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> NodeGraphNodeAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateDisplayColorAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateExpansionStateAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateIconAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePosAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSizeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateStackingOrderAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> NodeGraphNodeAPI: ...
    def GetDisplayColorAttr(self) -> pxr.Usd.Attribute: ...
    def GetExpansionStateAttr(self) -> pxr.Usd.Attribute: ...
    def GetIconAttr(self) -> pxr.Usd.Attribute: ...
    def GetPosAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetSizeAttr(self) -> pxr.Usd.Attribute: ...
    def GetStackingOrderAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class SceneGraphPrimAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> SceneGraphPrimAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateDisplayGroupAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateDisplayNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path) -> SceneGraphPrimAPI: ...
    def GetDisplayGroupAttr(self) -> pxr.Usd.Attribute: ...
    def GetDisplayNameAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    Backdrop: ClassVar[Any] = ...  # read-only
    NodeGraphNodeAPI: ClassVar[Any] = ...  # read-only
    SceneGraphPrimAPI: ClassVar[Any] = ...  # read-only
    closed: ClassVar[Any] = ...  # read-only
    minimized: ClassVar[Any] = ...  # read-only
    open: ClassVar[Any] = ...  # read-only
    uiDescription: ClassVar[Any] = ...  # read-only
    uiDisplayGroup: ClassVar[Any] = ...  # read-only
    uiDisplayName: ClassVar[Any] = ...  # read-only
    uiNodegraphNodeDisplayColor: ClassVar[Any] = ...  # read-only
    uiNodegraphNodeExpansionState: ClassVar[Any] = ...  # read-only
    uiNodegraphNodeIcon: ClassVar[Any] = ...  # read-only
    uiNodegraphNodePos: ClassVar[Any] = ...  # read-only
    uiNodegraphNodeSize: ClassVar[Any] = ...  # read-only
    uiNodegraphNodeStackingOrder: ClassVar[Any] = ...  # read-only
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