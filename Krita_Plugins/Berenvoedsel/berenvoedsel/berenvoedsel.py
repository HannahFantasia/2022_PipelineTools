#BBD's Krita Script Starter Feb 2018
from krita import DockWidget, DockWidgetFactory, DockWidgetFactoryBase
from PyQt5.QTWidgets import *
from Krita import *
import berenvoedsel_script

DOCKER_NAME = 'Berenvoedsel'
DOCKER_ID = 'pykrita_berenvoedsel'


class Berenvoedsel(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Berenvoedsel")
        mainWidget = Qwidget(self)
        self.setWidget(mainWidget)

        Render = QPushButton("Render a Demo", mainWidget)
        renderButton.click.connect(berenvoedsel_script.main())

        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(renderButton)


    def canvasChanged(self, canvas):
        pass


instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockRight,
                                        Berenvoedsel)

instance.addDockWidgetFactory(dock_widget_factory)
