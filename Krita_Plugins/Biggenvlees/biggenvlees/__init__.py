from .biggenvlees import Biggenvlees

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = Biggenvlees(parent = app)
app.addExtension(extension)
