# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import pxr.CameraUtil
import pxr.Gf
import pxr.Glf
import pxr.Sdf
import pxr.Usd
import std
import typing
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

ALL_INSTANCES: int
__MFB_FULL_PACKAGE_NAME: str

class CullStyle(Boost.Python.enum):
    CULL_STYLE_BACK: ClassVar[CullStyle] = ...
    CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED: ClassVar[CullStyle] = ...
    CULL_STYLE_FRONT: ClassVar[CullStyle] = ...
    CULL_STYLE_NOTHING: ClassVar[CullStyle] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class DrawMode(Boost.Python.enum):
    DRAW_GEOM_FLAT: ClassVar[DrawMode] = ...
    DRAW_GEOM_ONLY: ClassVar[DrawMode] = ...
    DRAW_GEOM_SMOOTH: ClassVar[DrawMode] = ...
    DRAW_POINTS: ClassVar[DrawMode] = ...
    DRAW_SHADED_FLAT: ClassVar[DrawMode] = ...
    DRAW_SHADED_SMOOTH: ClassVar[DrawMode] = ...
    DRAW_WIREFRAME: ClassVar[DrawMode] = ...
    DRAW_WIREFRAME_ON_SURFACE: ClassVar[DrawMode] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class Engine(Boost.Python.instance):
    class Parameters(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        allowAsynchronousSceneProcessing: Incomplete
        driver: Incomplete
        excludedPaths: Incomplete
        gpuEnabled: Incomplete
        invisedPaths: Incomplete
        rendererPluginId: Incomplete
        rootPath: Incomplete
        sceneDelegateID: Incomplete
        def __init__(self) -> None: ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: pxr.Sdf.Path | str, arg3: object, arg4: object) -> None: ...
    @overload
    def __init__(self, arg2: Engine.Parameters) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def AddSelected(self, arg2: pxr.Sdf.Path | str, arg3: int) -> None: ...
    def ClearSelected(self) -> None: ...
    @staticmethod
    def GetAvailableRenderSettingsPrimPaths(arg1: pxr.Usd.Prim) -> list[pxr.Sdf.Path]: ...
    def GetCurrentRendererId(self) -> str: ...
    def GetRenderStats(self) -> dict: ...
    def GetRendererAovs(self) -> list[str]: ...
    def GetRendererCommandDescriptors(self) -> list: ...
    @staticmethod
    def GetRendererDisplayName(arg1: str | pxr.Ar.ResolvedPath) -> str: ...
    @staticmethod
    def GetRendererPlugins() -> list[str]: ...
    def GetRendererSetting(self, arg2: str | pxr.Ar.ResolvedPath) -> Any: ...
    def GetRendererSettingsList(self) -> list: ...
    def InvokeRendererCommand(self, command: str | pxr.Ar.ResolvedPath, args: HdCommandArgs = ...) -> bool: ...
    @staticmethod
    def IsColorCorrectionCapable() -> bool: ...
    def IsConverged(self) -> bool: ...
    def IsPauseRendererSupported(self) -> bool: ...
    def IsStopRendererSupported(self) -> bool: ...
    def PauseRenderer(self) -> bool: ...
    def PollForAsynchronousUpdates(self) -> bool: ...
    def Render(self, arg2: pxr.Usd.Prim, arg3: RenderParams) -> None: ...
    def RestartRenderer(self) -> bool: ...
    def ResumeRenderer(self) -> bool: ...
    def SetActiveRenderSettingsPrimPath(self, arg2: pxr.Sdf.Path | str) -> None: ...
    def SetCameraPath(self, arg2: pxr.Sdf.Path | str) -> None: ...
    def SetCameraState(self, arg2: pxr.Gf.Matrix4d, arg3: pxr.Gf.Matrix4d) -> None: ...
    def SetColorCorrectionSettings(self, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: str | pxr.Ar.ResolvedPath, arg6: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetFraming(self, arg2: pxr.CameraUtil.Framing) -> None: ...
    def SetLightingState(self, arg2: object, arg3: pxr.Glf.SimpleMaterial, arg4: pxr.Gf.Vec4f | list[float] | tuple[float, float, float, float]) -> None: ...
    def SetOverrideWindowPolicy(self, arg2: std.optional[pxr.CameraUtil.ConformWindowPolicy]) -> None: ...
    def SetRenderBufferSize(self, arg2: pxr.Gf.Vec2i | list[int] | pxr.Gf.Size2 | tuple[int, int]) -> None: ...
    def SetRenderViewport(self, arg2: pxr.Gf.Vec4d | list[float] | tuple[float, float, float, float]) -> None: ...
    def SetRendererAov(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetRendererPlugin(self, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def SetRendererSetting(self, arg2: str | pxr.Ar.ResolvedPath, arg3: Any) -> None: ...
    def SetSelected(self, arg2: typing.Iterable[pxr.Sdf.Path | str]) -> None: ...
    def SetSelectionColor(self, arg2: pxr.Gf.Vec4f | list[float] | tuple[float, float, float, float]) -> None: ...
    def SetWindowPolicy(self, arg2: pxr.CameraUtil.ConformWindowPolicy) -> None: ...
    def StopRenderer(self) -> bool: ...
    def TestIntersection(self, arg2: pxr.Gf.Matrix4d, arg3: pxr.Gf.Matrix4d, arg4: pxr.Usd.Prim, arg5: RenderParams) -> tuple: ...

class RenderParams(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    applyRenderState: Incomplete
    bboxLineColor: Incomplete
    bboxLineDashSize: Incomplete
    bboxes: Incomplete
    clearColor: Incomplete
    clipPlanes: Incomplete
    colorCorrectionMode: Incomplete
    complexity: Incomplete
    cullStyle: Incomplete
    drawMode: Incomplete
    enableIdRender: Incomplete
    enableLighting: Incomplete
    enableSampleAlphaToCoverage: Incomplete
    enableSceneLights: Incomplete
    enableSceneMaterials: Incomplete
    enableUsdDrawModes: Incomplete
    forceRefresh: Incomplete
    frame: Incomplete
    gammaCorrectColors: Incomplete
    highlight: Incomplete
    ocioColorSpace: Incomplete
    ocioDisplay: Incomplete
    ocioLook: Incomplete
    ocioView: Incomplete
    overrideColor: Incomplete
    showGuides: Incomplete
    showProxy: Incomplete
    showRender: Incomplete
    wireframeColor: Incomplete
    def __init__(self) -> None: ...

class RendererCommandArgDescriptor(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def argName(self): ...
    @property
    def defaultValue(self): ...

class RendererCommandDescriptor(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def commandArgs(self): ...
    @property
    def commandDescription(self): ...
    @property
    def commandName(self): ...

class RendererSetting(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    @property
    def defValue(self): ...
    @property
    def key(self): ...
    @property
    def name(self): ...
    @property
    def type(self): ...

class RendererSettingType(Boost.Python.enum):
    FLAG: ClassVar[RendererSettingType] = ...
    FLOAT: ClassVar[RendererSettingType] = ...
    INT: ClassVar[RendererSettingType] = ...
    STRING: ClassVar[RendererSettingType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
