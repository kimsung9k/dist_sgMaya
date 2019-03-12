
from maya import OpenMayaMPx


# initialize the script plug-in
def initializePlugin(mobject):

    mplugin = OpenMayaMPx.MFnPlugin(mobject, "sg", "1.0", "Any")
    import sg_menu
    sg_menu.load_menu_controller()



# Uninitialize the script plug-in
def uninitializePlugin(mobject):

    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    import sg_menu
    sg_menu.unload_menu_controller()
