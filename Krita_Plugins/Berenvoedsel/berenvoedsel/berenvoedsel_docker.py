#BBD's Krita Script Starter Feb 2018
from krita import DockWidget, DockWidgetFactory, DockWidgetFactoryBase

DOCKER_NAME = 'Berenvoedsel'
DOCKER_ID = 'pykrita_berenvoedsel'


class Berenvoedsel(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_NAME)

    def canvasChanged(self, canvas):
        pass


instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockRight,
                                        Berenvoedsel)

instance.addDockWidgetFactory(dock_widget_factory)
