import Boost.Python
import pxr.Ndr
from typing import Any, ClassVar

class NodeContext(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def Displacement(self) -> Any: ...
    @property
    def Light(self) -> Any: ...
    @property
    def LightFilter(self) -> Any: ...
    @property
    def Pattern(self) -> Any: ...
    @property
    def PixelFilter(self) -> Any: ...
    @property
    def SampleFilter(self) -> Any: ...
    @property
    def Surface(self) -> Any: ...
    @property
    def Volume(self) -> Any: ...

class NodeMetadata(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def Category(self) -> Any: ...
    @property
    def Departments(self) -> Any: ...
    @property
    def Help(self) -> Any: ...
    @property
    def ImplementationName(self) -> Any: ...
    @property
    def Label(self) -> Any: ...
    @property
    def Pages(self) -> Any: ...
    @property
    def Primvars(self) -> Any: ...
    @property
    def Role(self) -> Any: ...
    @property
    def SdrDefinitionNameFallbackPrefix(self) -> Any: ...
    @property
    def SdrUsdEncodingVersion(self) -> Any: ...
    @property
    def Target(self) -> Any: ...

class NodeRole(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def Field(self) -> Any: ...
    @property
    def Math(self) -> Any: ...
    @property
    def Primvar(self) -> Any: ...
    @property
    def Texture(self) -> Any: ...

class PropertyMetadata(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def Colorspace(self) -> Any: ...
    @property
    def Connectable(self) -> Any: ...
    @property
    def DefaultInput(self) -> Any: ...
    @property
    def Help(self) -> Any: ...
    @property
    def Hints(self) -> Any: ...
    @property
    def ImplementationName(self) -> Any: ...
    @property
    def IsAssetIdentifier(self) -> Any: ...
    @property
    def IsDynamicArray(self) -> Any: ...
    @property
    def Label(self) -> Any: ...
    @property
    def Options(self) -> Any: ...
    @property
    def Page(self) -> Any: ...
    @property
    def RenderType(self) -> Any: ...
    @property
    def Role(self) -> Any: ...
    @property
    def SdrUsdDefinitionType(self) -> Any: ...
    @property
    def Tag(self) -> Any: ...
    @property
    def Target(self) -> Any: ...
    @property
    def ValidConnectionTypes(self) -> Any: ...
    @property
    def VstructConditionalExpr(self) -> Any: ...
    @property
    def VstructMemberName(self) -> Any: ...
    @property
    def VstructMemberOf(self) -> Any: ...
    @property
    def Widget(self) -> Any: ...

class PropertyRole(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class PropertyTypes(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def Color(self) -> Any: ...
    @property
    def Color4(self) -> Any: ...
    @property
    def Float(self) -> Any: ...
    @property
    def Int(self) -> Any: ...
    @property
    def Matrix(self) -> Any: ...
    @property
    def Normal(self) -> Any: ...
    @property
    def Point(self) -> Any: ...
    @property
    def String(self) -> Any: ...
    @property
    def Struct(self) -> Any: ...
    @property
    def Terminal(self) -> Any: ...
    @property
    def Unknown(self) -> Any: ...
    @property
    def Vector(self) -> Any: ...
    @property
    def Vstruct(self) -> Any: ...

class Registry(pxr.Ndr.Registry):
    def __init__(self, tupleargs, dictkwds) -> None: ...
    def GetShaderNodeByIdentifier(self, identifier: object, typePriority: object = ...) -> ShaderNode: ...
    def GetShaderNodeByIdentifierAndType(self, identifier: object, nodeType: object) -> ShaderNode: ...
    def GetShaderNodeByName(self, name: object, typePriority: object = ..., filter: object = ...) -> ShaderNode: ...
    def GetShaderNodeByNameAndType(self, name: object, nodeType: object, filter: object = ...) -> ShaderNode: ...
    def GetShaderNodeFromAsset(self, shaderAsset: pxr.Sdf.AssetPath, metadata: object = ..., subIdentifier: object = ..., sourceType: object = ...) -> ShaderNode: ...
    def GetShaderNodeFromSourceCode(self, sourceCode: object, sourceType: object, metadata: object = ...) -> ShaderNode: ...
    def GetShaderNodesByFamily(self, family: object = ..., filter: object = ...) -> ShaderNodeList: ...
    def GetShaderNodesByIdentifier(self, identifier: object) -> ShaderNodeList: ...
    def GetShaderNodesByName(self, name: object, filter: object = ...) -> ShaderNodeList: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class ShaderNode(pxr.Ndr.Node):
    def __init__(self, *args, **kwargs) -> None: ...
    def GetAdditionalPrimvarProperties(self) -> Any: ...
    def GetAllVstructNames(self) -> Any: ...
    def GetAssetIdentifierInputNames(self) -> list: ...
    def GetCategory(self) -> Any: ...
    def GetDefaultInput(self) -> ShaderProperty: ...
    def GetDepartments(self) -> Any: ...
    def GetHelp(self) -> str: ...
    def GetImplementationName(self) -> str: ...
    def GetLabel(self) -> Any: ...
    def GetPages(self) -> Any: ...
    def GetPrimvars(self) -> Any: ...
    def GetPropertyNamesForPage(self, arg2: object) -> Any: ...
    def GetRole(self) -> str: ...
    def GetShaderInput(self, arg2: object) -> ShaderProperty: ...
    def GetShaderOutput(self, arg2: object) -> ShaderProperty: ...
    def __reduce__(self) -> Any: ...

class ShaderNodeList(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def append(self, arg2: object) -> None: ...
    def extend(self, arg2: object) -> None: ...
    def __contains__(self, arg2: object) -> bool: ...
    def __delitem__(self, arg2: object) -> None: ...
    def __getitem__(self, arg2: object) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __reduce__(self) -> Any: ...
    def __setitem__(self, arg2: object, arg3: object) -> None: ...

class ShaderProperty(pxr.Ndr.Property):
    def __init__(self, *args, **kwargs) -> None: ...
    def GetDefaultValueAsSdfType(self) -> Any: ...
    def GetHelp(self) -> str: ...
    def GetHints(self) -> dict: ...
    def GetImplementationName(self) -> str: ...
    def GetLabel(self) -> Any: ...
    def GetOptions(self) -> list: ...
    def GetPage(self) -> Any: ...
    def GetVStructConditionalExpr(self) -> Any: ...
    def GetVStructMemberName(self) -> Any: ...
    def GetVStructMemberOf(self) -> Any: ...
    def GetValidConnectionTypes(self) -> Any: ...
    def GetWidget(self) -> Any: ...
    def IsAssetIdentifier(self) -> bool: ...
    def IsDefaultInput(self) -> bool: ...
    def IsVStruct(self) -> bool: ...
    def IsVStructMember(self) -> bool: ...
    def __reduce__(self) -> Any: ...