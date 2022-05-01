import maya.cmds as cmds


def createUI(windowTitle):
    window = 'OC_Window'
    size = (600, 450)
    # create new window
    cmds.window(window, title=windowTitle, widthHeight=size,
                resizeToFitChildren=True, sizeable=True)
    cmds.showWindow()

    cmds.rowColumnLayout()
    cmds.text('FixingTexturePath', width=50, height=50,
              font='boldLabelFont', bgc=[0.2, 0.2, 0.2])

    cmds.rowColumnLayout(numberOfColumns=2, columnAttach=(
        (1, 'right', 2), (2, 'both', 2)), columnOffset=[(1, 'left', 5), (2, 'both', 5)])
    cmds.text(label='Output Directory :', height=20, font='boldLabelFont')
    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=2, columnOffset=[
                         (1, 'both', 1), (2, 'both', 1)], columnWidth=[(1, 200)])
    cmds.textField()
    cmds.button(label='Choose', h=20, w=80)
    cmds.setParent('..')
    cmds.button(label='Set Path', h=30, w=80, bgc=[0.7, 0.8, 0.1])


if __name__ == "__main__":
    createUI('setTexture')
