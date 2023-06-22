import Boost.Python
import pxr.Tf
from typing import Any, overload

class Notice(Boost.Python.instance):
    class Base(pxr.Tf.Notice):
        def __init__(self, *args, **kwargs) -> None: ...
        def __reduce__(self) -> Any: ...
    class DidRegisterPlugins(Base):
        def __init__(self, *args, **kwargs) -> None: ...
        def GetNewPlugins(self) -> list: ...
        def __reduce__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class Plugin(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def DeclaresType(self, type: Type, includeSubclasses: bool = ...) -> bool: ...
    def FindPluginResource(self, path: str, verify: bool = ...) -> str: ...
    def GetMetadataForType(self, arg2: Type) -> dict: ...
    def Load(self) -> bool: ...
    def MakeResourcePath(self, arg2: str) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...
    @property
    def isLoaded(self) -> type: ...
    @property
    def isPythonModule(self) -> type: ...
    @property
    def isResource(self) -> type: ...
    @property
    def metadata(self) -> type: ...
    @property
    def name(self) -> type: ...
    @property
    def path(self) -> type: ...
    @property
    def resourcePath(self) -> type: ...

class Registry(Boost.Python.instance):
    def __init__(self, tupleargs, dictkwds) -> None: ...
    @classmethod
    def FindDerivedTypeByName(cls, arg1: Type, arg2: str) -> Type: ...
    @classmethod
    def FindTypeByName(cls, arg1: str) -> Type: ...
    @classmethod
    def GetAllDerivedTypes(cls, arg1: Type) -> tuple: ...
    def GetAllPlugins(self) -> list[Plugin]: ...
    @classmethod
    def GetDirectlyDerivedTypes(cls, arg1: Type) -> tuple: ...
    def GetPluginForType(self, arg2: Type) -> Plugin: ...
    def GetPluginWithName(self, arg2: str) -> Plugin: ...
    def GetStringFromPluginMetaData(self, arg2: Type, arg3: str) -> str: ...
    @overload
    def RegisterPlugins(self, arg2: str) -> list[Plugin]: ...
    @overload
    def RegisterPlugins(self, arg2: list[str]) -> list[Plugin]: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase1(Boost.Python.instance):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: str) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase2(Boost.Python.instance):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: str) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase3(Boost.Python.instance):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: str) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestPlugBase4(Boost.Python.instance):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: str) -> None: ...
    def GetTypeName(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

def _LoadPluginsConcurrently(predicate: object, numThreads: int = ..., verbose: bool = ...) -> None: ...