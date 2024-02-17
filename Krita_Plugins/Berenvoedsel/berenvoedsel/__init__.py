from .Animatic_Export import Animatic_Export

app = Krita.instance()
# Instantiate your class:
extension = Animatic_Export(parent = app)
app.addExtension(extension)
