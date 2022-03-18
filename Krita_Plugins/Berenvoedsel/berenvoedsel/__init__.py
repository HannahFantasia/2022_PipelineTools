from .berenvoedsel import Berenvoedsel

app = Krita.instance()
# Instantiate your class:
extension = Berenvoedsel(parent = app)
app.addExtension(extension)
