import nuke
import os

nuke.pluginAddPath('./tools')
nuke.pluginAddPath('./icons')

##########################################################################################################################################

toolbar = nuke.toolbar('Nodes') # The default nuke nodes toolbaron the left hand side of screen
p_tools = toolbar.addMenu('Peter Tools', icon = 'p.png') # add menu for Peter Tools

##########################################################################################################################################

# Draw
# Colour

p_tools.addCommand('GradeAOV', 'nuke.createNode(\'GradeAOV.nk\')', icon = 'p.png')
p_tools.addCommand('HueCorrect Soft', 'nuke.createNode(\'HueCorrectSoft.nk\')', icon = 'p.png')
p_tools.addCommand('HueVsHue', 'nuke.createNode(\'HueVsHue.nk\')', icon = 'p.png')
p_tools.addCommand('LogSat', 'nuke.createNode(\'LogSat.nk\')', icon = 'p.png')
p_tools.addCommand('Soft Crush Highlights', 'nuke.createNode(\'SoftCrushHighlights.nk\')', icon = 'p.png')
p_tools.addSeparator()
# Filter

p_tools.addCommand('Bump Displace', 'nuke.createNode(\'BumpDisplace.nk\')', icon = 'BumpDisplace.png')
p_tools.addCommand('Edge Inpaint', 'nuke.createNode(\'Edge_Inpaint.nk\')', icon = 'p.png')
p_tools.addCommand('Edge Push', 'nuke.createNode(\'EdgePush.nk\')', icon = 'EdgePush.png')
p_tools.addCommand('Glass', 'nuke.createNode(\'Glass.nk\')', icon = 'p.png')
p_tools.addCommand('Guided Blur Fast', 'nuke.createNode(\'GuidedBlurFast.nk\')', icon = 'p.png')
p_tools.addCommand('DualPassGuidedBlur', 'nuke.createNode(\'DualPassGuidedBlur.nk\')', icon = 'p.png')
p_tools.addCommand('Lens Juice', 'nuke.createNode(\'Lens_Juice.nk\')', icon = 'p.png')
p_tools.addCommand('RSMB Ghetto', 'nuke.createNode(\'RSMB_Ghetto.nk\')', icon = 'p.png')
p_tools.addCommand('Sharpie', 'nuke.createNode(\'Sharpie.nk\')', icon = 'p.png')
p_tools.addCommand('Vignette', 'nuke.createNode(\'Vignette.nk\')', icon = 'p.png')
p_tools.addSeparator()

# Keying

# Tansform

# Other

p_tools.addCommand('Fuse', 'nuke.createNode(\'Fuse.nk\')', icon = 'p.png')