# mypy: disable_error_code = misc
import pxr.Usdviewq.usdviewContextMenuItem
from pxr.Usdviewq.usdviewContextMenuItem import UsdviewContextMenuItem as UsdviewContextMenuItem

class ActiveMenuItem(PrimContextMenuItem):
    def GetText(self): ...
    def RunCommand(self): ...

class CopyModelPathMenuItem(PrimContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class CopyPrimPathMenuItem(PrimContextMenuItem):
    def GetText(self): ...
    def RunCommand(self): ...

class IsolateAssetMenuItem(PrimContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class IsolateCopyPrimMenuItem(PrimContextMenuItem):
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class JumpToEnclosingModelItem(PrimContextMenuItem):
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class LoadOrUnloadMenuItem(PrimContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class PrimContextMenuItem(pxr.Usdviewq.usdviewContextMenuItem.UsdviewContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def IsSeparator(self): ...
    def RunCommand(self): ...

class RemoveVisMenuItem(PrimContextMenuItem):
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class SelectBoundFullMaterialMenuItem(PrimContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class SelectBoundPreviewMaterialMenuItem(PrimContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class SeparatorMenuItem(PrimContextMenuItem):
    def IsSeparator(self): ...

class SetAsActiveCamera(PrimContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class ToggleVisibilityMenuItem(PrimContextMenuItem):
    def __init__(self, appController, item): ...
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

class VisOnlyMenuItem(PrimContextMenuItem):
    def GetText(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

def _GetContextMenuItems(appController, item): ...
