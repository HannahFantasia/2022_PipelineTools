from .CopyPaste_Frame_Board import CopyPaste_Frame_Board

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = CopyPaste_Frame_Board(parent = app)
app.addExtension(extension)
