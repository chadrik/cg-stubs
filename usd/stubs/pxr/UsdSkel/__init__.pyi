# mypy: disable_error_code = misc
import Boost.Python
import pxr.Ar
import pxr.Gf
import pxr.Sdf
import pxr.Tf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdShade
import pxr.Vt
import typing
from typing import Any, ClassVar, overload

__MFB_FULL_PACKAGE_NAME: str

class AnimMapper(Boost.Python.instance):
    @overload
    def __init__(self, sourceOrder: pxr.Vt.TokenArray | typing.Iterable[str], targetOrder: pxr.Vt.TokenArray | typing.Iterable[str]) -> None: ...
    @overload
    def __init__(self, arg2: int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def IsIdentity(self) -> bool: ...
    def IsNull(self) -> bool: ...
    def IsSparse(self) -> bool: ...
    def Remap(self, source: object, target: object = ..., elementSize: int = ..., defaultValue: object = ...) -> Any: ...
    @overload
    def RemapTransforms(self, source: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], target: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], elementSize: int = ...) -> pxr.Vt.Matrix4dArray: ...
    @overload
    def RemapTransforms(self, source: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], target: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], elementSize: int = ...) -> pxr.Vt.Matrix4fArray: ...
    def __len__(self) -> int: ...
    def __reduce__(self): ...

class AnimQuery(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def BlendShapeWeightsMightBeTimeVarying(self) -> bool: ...
    def ComputeBlendShapeWeights(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.FloatArray: ...
    def ComputeJointLocalTransformComponents(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> tuple: ...
    def ComputeJointLocalTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray: ...
    def GetBlendShapeOrder(self) -> pxr.Vt.TokenArray: ...
    def GetBlendShapeWeightTimeSamples(self) -> list[float]: ...
    def GetBlendShapeWeightTimeSamplesInInterval(self, interval: pxr.Gf.Interval) -> list[float]: ...
    def GetJointOrder(self) -> pxr.Vt.TokenArray: ...
    def GetJointTransformTimeSamples(self) -> list[float]: ...
    def GetJointTransformTimeSamplesInInterval(self, interval: pxr.Gf.Interval) -> list[float]: ...
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def JointTransformsMightBeTimeVarying(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self): ...

class Animation(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateBlendShapeWeightsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateBlendShapesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRotationsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateScalesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateTranslationsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Animation: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Animation: ...
    def GetBlendShapeWeightsAttr(self) -> pxr.Usd.Attribute: ...
    def GetBlendShapesAttr(self) -> pxr.Usd.Attribute: ...
    def GetJointsAttr(self) -> pxr.Usd.Attribute: ...
    def GetRotationsAttr(self) -> pxr.Usd.Attribute: ...
    def GetScalesAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray: ...
    def GetTranslationsAttr(self) -> pxr.Usd.Attribute: ...
    def SetTransforms(self, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self): ...

class Binding(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: Skeleton, arg3: list) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetSkeleton(self) -> Skeleton: ...
    def GetSkinningTargets(self) -> list: ...
    def __reduce__(self): ...

class BindingAPI(pxr.Usd.APISchemaBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Apply(cls, prim: pxr.Usd.Prim) -> BindingAPI: ...
    @classmethod
    def CanApply(cls, prim: pxr.Usd.Prim) -> _CanApplyResult: ...
    def CreateAnimationSourceRel(self) -> pxr.Usd.Relationship: ...
    def CreateBlendShapeTargetsRel(self) -> pxr.Usd.Relationship: ...
    def CreateBlendShapesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateGeomBindTransformAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointIndicesPrimvar(self, constant: bool, elementSize: int = ...) -> pxr.UsdGeom.Primvar: ...
    def CreateJointWeightsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointWeightsPrimvar(self, constant: bool, elementSize: int = ...) -> pxr.UsdGeom.Primvar: ...
    def CreateJointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateSkeletonRel(self) -> pxr.Usd.Relationship: ...
    def CreateSkinningMethodAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BindingAPI: ...
    def GetAnimationSource(self) -> pxr.Usd.Prim: ...
    def GetAnimationSourceRel(self) -> pxr.Usd.Relationship: ...
    def GetBlendShapeTargetsRel(self) -> pxr.Usd.Relationship: ...
    def GetBlendShapesAttr(self) -> pxr.Usd.Attribute: ...
    def GetGeomBindTransformAttr(self) -> pxr.Usd.Attribute: ...
    def GetInheritedAnimationSource(self) -> pxr.Usd.Prim: ...
    def GetInheritedSkeleton(self) -> Skeleton: ...
    def GetJointIndicesAttr(self) -> pxr.Usd.Attribute: ...
    def GetJointIndicesPrimvar(self) -> pxr.UsdGeom.Primvar: ...
    def GetJointWeightsAttr(self) -> pxr.Usd.Attribute: ...
    def GetJointWeightsPrimvar(self) -> pxr.UsdGeom.Primvar: ...
    def GetJointsAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetSkeleton(self) -> Skeleton: ...
    def GetSkeletonRel(self) -> pxr.Usd.Relationship: ...
    def GetSkinningMethodAttr(self) -> pxr.Usd.Attribute: ...
    def SetRigidJointInfluence(self, jointIndex: int, weight: float = ...) -> bool: ...
    @classmethod
    def ValidateJointIndices(cls, jointIndices: pxr.Vt.IntArray | typing.Iterable[int], numJoints: int) -> tuple: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self): ...

class BlendShape(pxr.Usd.Typed):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateInbetween(self, name: str | pxr.Ar.ResolvedPath) -> InbetweenShape: ...
    def CreateNormalOffsetsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateOffsetsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreatePointIndicesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BlendShape: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> BlendShape: ...
    def GetAuthoredInbetweens(self) -> list[InbetweenShape]: ...
    def GetInbetween(self, name: str | pxr.Ar.ResolvedPath) -> InbetweenShape: ...
    def GetInbetweens(self) -> list[InbetweenShape]: ...
    def GetNormalOffsetsAttr(self) -> pxr.Usd.Attribute: ...
    def GetOffsetsAttr(self) -> pxr.Usd.Attribute: ...
    def GetPointIndicesAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def HasInbetween(self, name: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def ValidatePointIndices(cls, pointIndices: pxr.Vt.IntArray | typing.Iterable[int], numPoints: int) -> tuple: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self): ...

class BlendShapeQuery(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: BindingAPI) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ComputeBlendShapePointIndices(self) -> list[pxr.Vt.IntArray]: ...
    def ComputeDeformedPoints(self, subShapeWeights: pxr.Vt.FloatArray | typing.Iterable[float], blendShapeIndices: pxr.Vt.UIntArray | typing.Iterable[int], subShapeIndices: pxr.Vt.UIntArray | typing.Iterable[int], blendShapePointIndices: typing.Iterable[pxr.Vt.IntArray | typing.Iterable[int]], subShapePointOffset: typing.Iterable[pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f]], points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f]) -> bool: ...
    def ComputeSubShapePointOffsets(self) -> list[pxr.Vt.Vec3fArray]: ...
    def ComputeSubShapeWeights(self, arg2: pxr.Vt.FloatArray | typing.Iterable[float]) -> tuple: ...
    def GetBlendShape(self, arg2: int) -> BlendShape: ...
    def GetBlendShapeIndex(self, arg2: int) -> int: ...
    def GetInbetween(self, arg2: int) -> InbetweenShape: ...
    def GetNumBlendShapes(self) -> int: ...
    def GetNumSubShapes(self) -> int: ...
    def __reduce__(self): ...

class Cache(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def Clear(self) -> None: ...
    def ComputeSkelBinding(self, skelRoot: Root, skel: Skeleton, predicate: pxr.Usd._PrimFlagsPredicate | pxr.Usd._Term) -> Binding: ...
    def ComputeSkelBindings(self, skelRoot: Root, predicate: pxr.Usd._PrimFlagsPredicate | pxr.Usd._Term) -> list[Binding]: ...
    @overload
    def GetAnimQuery(self, prim: pxr.Usd.Prim) -> AnimQuery: ...
    @overload
    def GetAnimQuery(self, anim: Animation) -> AnimQuery: ...
    def GetSkelQuery(self, arg2: Skeleton) -> SkeletonQuery: ...
    def GetSkinningQuery(self, arg2: pxr.Usd.Prim) -> SkinningQuery: ...
    def Populate(self, skelRoot: Root, predicate: pxr.Usd._PrimFlagsPredicate | pxr.Usd._Term) -> bool: ...
    def __reduce__(self): ...

class InbetweenShape(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateNormalOffsetsAttr(self, arg2: Any) -> pxr.Usd.Attribute: ...
    def GetAttr(self) -> pxr.Usd.Attribute: ...
    def GetNormalOffsets(self) -> pxr.Vt.Vec3fArray: ...
    def GetNormalOffsetsAttr(self) -> pxr.Usd.Attribute: ...
    def GetOffsets(self) -> pxr.Vt.Vec3fArray: ...
    def GetWeight(self) -> float: ...
    def HasAuthoredWeight(self) -> bool: ...
    def IsDefined(self) -> bool: ...
    @classmethod
    def IsInbetween(cls, attr: pxr.Usd.Attribute | pxr.UsdGeom.ConstraintTarget | pxr.UsdGeom.Primvar | pxr.UsdGeom.XformOp | pxr.UsdShade.Input | pxr.UsdShade.Output) -> bool: ...
    def SetNormalOffsets(self, offsets: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f]) -> bool: ...
    def SetOffsets(self, offsets: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f]) -> bool: ...
    def SetWeight(self, weight: float) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __reduce__(self): ...

class PackedJointAnimation(Animation):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PackedJointAnimation: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> PackedJointAnimation: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self): ...

class Root(pxr.UsdGeom.Boundable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Root: ...
    @classmethod
    def Find(cls, arg1: pxr.Usd.Prim) -> Root: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Root: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self): ...

class Skeleton(pxr.UsdGeom.Boundable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateBindTransformsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointNamesAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateJointsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateRestTransformsAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Skeleton: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Skeleton: ...
    def GetBindTransformsAttr(self) -> pxr.Usd.Attribute: ...
    def GetJointNamesAttr(self) -> pxr.Usd.Attribute: ...
    def GetJointsAttr(self) -> pxr.Usd.Attribute: ...
    def GetRestTransformsAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self): ...

class SkeletonQuery(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def ComputeJointLocalTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ..., atRest: bool = ...) -> pxr.Vt.Matrix4dArray: ...
    def ComputeJointRestRelativeTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray: ...
    def ComputeJointSkelTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ..., atRest: bool = ...) -> pxr.Vt.Matrix4dArray: ...
    def ComputeJointWorldTransforms(self, time: pxr.UsdGeom.XformCache = ..., atRest: bool = ...) -> pxr.Vt.Matrix4dArray: ...
    def ComputeSkinningTransforms(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Vt.Matrix4dArray: ...
    def GetAnimQuery(self) -> AnimQuery: ...
    def GetJointOrder(self) -> pxr.Vt.TokenArray: ...
    def GetJointWorldBindTransforms(self) -> pxr.Vt.Matrix4dArray: ...
    def GetMapper(self) -> AnimMapper: ...
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def GetSkeleton(self) -> Skeleton: ...
    def GetTopology(self) -> Topology: ...
    def HasBindPose(self) -> bool: ...
    def HasRestPose(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self): ...

class SkinningQuery(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @overload
    def ComputeExtentsPadding(self, skelRestXforms: SkinningQuery, boundable: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], time: pxr.UsdGeom.Boundable = ...) -> float: ...
    @overload
    def ComputeExtentsPadding(self, skelRestXforms: SkinningQuery, boundable: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], time: pxr.UsdGeom.Boundable = ...) -> float: ...
    def ComputeJointInfluences(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> tuple[pxr.Vt.IntArray, pxr.Vt.FloatArray]: ...
    @overload
    def ComputeSkinnedPoints(self, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    @overload
    def ComputeSkinnedPoints(self, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> bool: ...
    @overload
    def ComputeSkinnedTransform(self, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4d: ...
    @overload
    def ComputeSkinnedTransform(self, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4f: ...
    def ComputeVaryingJointInfluences(self, numPoints: int, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> tuple[pxr.Vt.IntArray, pxr.Vt.FloatArray]: ...
    def GetBlendShapeMapper(self) -> AnimMapper: ...
    def GetBlendShapeOrder(self) -> pxr.Vt.TokenArray: ...
    def GetBlendShapeTargetsRel(self) -> pxr.Usd.Relationship: ...
    def GetBlendShapesAttr(self) -> pxr.Usd.Attribute: ...
    def GetGeomBindTransform(self, time: pxr.Usd.TimeCode | float | pxr.Sdf.TimeCode = ...) -> pxr.Gf.Matrix4d: ...
    def GetGeomBindTransformAttr(self) -> pxr.Usd.Attribute: ...
    def GetInterpolation(self) -> str: ...
    def GetJointIndicesPrimvar(self) -> pxr.UsdGeom.Primvar: ...
    def GetJointMapper(self) -> AnimMapper: ...
    def GetJointOrder(self) -> pxr.Vt.TokenArray: ...
    def GetJointWeightsPrimvar(self) -> pxr.UsdGeom.Primvar: ...
    def GetMapper(self) -> AnimMapper: ...
    def GetNumInfluencesPerComponent(self) -> int: ...
    def GetPrim(self) -> pxr.Usd.Prim: ...
    def GetSkinningMethod(self) -> str: ...
    def GetSkinningMethodAttr(self) -> pxr.Usd.Attribute: ...
    def GetTimeSamples(self) -> list[float]: ...
    def GetTimeSamplesInInterval(self, arg2: pxr.Gf.Interval) -> list[float]: ...
    def HasBlendShapes(self) -> bool: ...
    def HasJointInfluences(self) -> bool: ...
    def IsRigidlyDeformed(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self): ...

class Tokens(Boost.Python.instance):
    BlendShape: ClassVar[Any] = ...  # read-only
    PackedJointAnimation: ClassVar[Any] = ...  # read-only
    SkelAnimation: ClassVar[Any] = ...  # read-only
    SkelBindingAPI: ClassVar[Any] = ...  # read-only
    SkelRoot: ClassVar[Any] = ...  # read-only
    Skeleton: ClassVar[Any] = ...  # read-only
    bindTransforms: ClassVar[Any] = ...  # read-only
    blendShapeWeights: ClassVar[Any] = ...  # read-only
    blendShapes: ClassVar[Any] = ...  # read-only
    classicLinear: ClassVar[Any] = ...  # read-only
    dualQuaternion: ClassVar[Any] = ...  # read-only
    jointNames: ClassVar[Any] = ...  # read-only
    joints: ClassVar[Any] = ...  # read-only
    normalOffsets: ClassVar[Any] = ...  # read-only
    offsets: ClassVar[Any] = ...  # read-only
    pointIndices: ClassVar[Any] = ...  # read-only
    primvarsSkelGeomBindTransform: ClassVar[Any] = ...  # read-only
    primvarsSkelJointIndices: ClassVar[Any] = ...  # read-only
    primvarsSkelJointWeights: ClassVar[Any] = ...  # read-only
    primvarsSkelSkinningMethod: ClassVar[Any] = ...  # read-only
    restTransforms: ClassVar[Any] = ...  # read-only
    rotations: ClassVar[Any] = ...  # read-only
    scales: ClassVar[Any] = ...  # read-only
    skelAnimationSource: ClassVar[Any] = ...  # read-only
    skelBlendShapeTargets: ClassVar[Any] = ...  # read-only
    skelBlendShapes: ClassVar[Any] = ...  # read-only
    skelJoints: ClassVar[Any] = ...  # read-only
    skelSkeleton: ClassVar[Any] = ...  # read-only
    translations: ClassVar[Any] = ...  # read-only
    weight: ClassVar[Any] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...

class Topology(Boost.Python.instance):
    @overload
    def __init__(self, arg2: object) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Vt.TokenArray | typing.Iterable[str]) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Vt.IntArray | typing.Iterable[int]) -> None: ...
    def GetNumJoints(self) -> int: ...
    def GetParent(self, arg2: int) -> int: ...
    def GetParentIndices(self) -> pxr.Vt.IntArray: ...
    def IsRoot(self, arg2: int) -> bool: ...
    def Validate(self) -> tuple: ...
    def __len__(self) -> int: ...
    def __reduce__(self): ...

class _CanApplyResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self): ...
    @property
    def whyNot(self) -> Any: ...

def ApplyBlendShape(weight: float, offsets: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], indices: pxr.Vt.IntArray | typing.Iterable[int], points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f]) -> bool: ...
@overload
def BakeSkinning(root: Root, interval: pxr.Gf.Interval = ...) -> bool: ...
@overload
def BakeSkinning(range: object, interval: pxr.Gf.Interval = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], inverseXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], inverseXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointLocalXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], rootInverseXform: pxr.Gf.Matrix4f = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointLocalXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], rootInverseXform: pxr.Gf.Matrix4f = ...) -> bool: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], inverseXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> pxr.Vt.Matrix4dArray: ...
@overload
def ComputeJointLocalTransforms(topology: Topology, xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootInverseXform: pxr.Gf.Matrix4d = ...) -> pxr.Vt.Matrix4dArray: ...
@overload
def ComputeJointsExtent(xforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], pad: float = ..., rootXform: pxr.Gf.Matrix4d = ...) -> pxr.Gf.Range3f: ...
@overload
def ComputeJointsExtent(xforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], pad: float = ..., rootXform: pxr.Gf.Matrix4f = ...) -> pxr.Gf.Range3f: ...
@overload
def ConcatJointTransforms(arg1: Topology, topology: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootXform: pxr.Gf.Matrix4d = ...) -> bool: ...
@overload
def ConcatJointTransforms(arg1: Topology, topology: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointLocalXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], rootXform: pxr.Gf.Matrix4f = ...) -> bool: ...
@overload
def ConcatJointTransforms(topology: Topology, jointLocalXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], rootXform: pxr.Gf.Matrix4d = ...) -> pxr.Vt.Matrix4dArray: ...
@overload
def DecomposeTransform(arg1: pxr.Gf.Matrix4d) -> tuple: ...
@overload
def DecomposeTransform(arg1: pxr.Gf.Matrix4f) -> tuple: ...
@overload
def DecomposeTransforms(arg1: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d]) -> tuple: ...
@overload
def DecomposeTransforms(arg1: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f]) -> tuple: ...
@overload
def ExpandConstantInfluencesToVarying(array: pxr.Vt.IntArray | typing.Iterable[int], size: int) -> bool: ...
@overload
def ExpandConstantInfluencesToVarying(array: pxr.Vt.FloatArray | typing.Iterable[float], size: int) -> bool: ...
def InterleaveInfluences(indices: pxr.Vt.IntArray | typing.Iterable[int], weights: pxr.Vt.FloatArray | typing.Iterable[float], interleavedInfluences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f]) -> bool: ...
def IsSkelAnimationPrim(prim: pxr.Usd.Prim) -> bool: ...
def IsSkinnablePrim(prim: pxr.Usd.Prim) -> bool: ...
def MakeTransform(translate: pxr.Gf.Vec3f | list[float] | tuple[float, float, float], rotate: pxr.Gf.Quatf | pxr.Gf.Quath, scale: pxr.Gf.Vec3h | list[float] | tuple[float, float, float]) -> pxr.Gf.Matrix4d: ...
def MakeTransforms(translations: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], rotations: pxr.Vt.QuatfArray | typing.Iterable[pxr.Gf.Quatf], scales: pxr.Vt.Vec3hArray | typing.Iterable[pxr.Gf.Vec3h]) -> pxr.Vt.Matrix4dArray: ...
def NormalizeWeights(weights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerComponent: int, eps: float = ...) -> bool: ...
@overload
def ResizeInfluences(array: pxr.Vt.IntArray | typing.Iterable[int], srcNumInfluencesPerComponent: int, newNumInfluencesPerComponent: int) -> bool: ...
@overload
def ResizeInfluences(array: pxr.Vt.FloatArray | typing.Iterable[float], srcNumInfluencesPerComponent: int, newNumInfluencesPerComponent: int) -> bool: ...
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormals(skinningMethod: str | pxr.Ar.ResolvedPath, geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3d, jointXforms: pxr.Vt.Matrix3dArray | typing.Iterable[pxr.Gf.Matrix3d], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinNormalsLBS(geomBindTransform: pxr.Gf.Matrix3f, jointXforms: pxr.Vt.Matrix3fArray | typing.Iterable[pxr.Gf.Matrix3f], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, normals: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPoints(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinPointsLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f], numInfluencesPerPoint: int, points: pxr.Vt.Vec3fArray | typing.Iterable[pxr.Gf.Vec3f], inSerial: bool = ...) -> bool: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4f: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransform(skinningMethod: object, geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f]) -> pxr.Gf.Matrix4f: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], jointIndices: pxr.Vt.IntArray | typing.Iterable[int], jointWeights: pxr.Vt.FloatArray | typing.Iterable[float]) -> pxr.Gf.Matrix4f: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4d, jointXforms: pxr.Vt.Matrix4dArray | typing.Iterable[pxr.Gf.Matrix4d], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f]) -> pxr.Gf.Matrix4d: ...
@overload
def SkinTransformLBS(geomBindTransform: pxr.Gf.Matrix4f, jointXforms: pxr.Vt.Matrix4fArray | typing.Iterable[pxr.Gf.Matrix4f], influences: pxr.Vt.Vec2fArray | typing.Iterable[pxr.Gf.Vec2f]) -> pxr.Gf.Matrix4f: ...
def SortInfluences(indices: pxr.Vt.IntArray | typing.Iterable[int], weights: pxr.Vt.FloatArray | typing.Iterable[float], numInfluencesPerComponent: int) -> bool: ...
