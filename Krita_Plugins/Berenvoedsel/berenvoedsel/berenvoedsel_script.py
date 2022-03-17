# BBD's Krita Script Starter Feb 2018

from krita import Extension
from krita import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg, uic
import sip
import pprint
import time
from contextlib import redirect_stdout
import io
import re
import json
import pprint
from datetime import datetime
import sys

EXTENSION_ID = 'pykrita_biggenvlees'
MENU_ENTRY = 'biggenvlees_run'


class Biggenvlees(Extension):

    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(EXTENSION_ID, MENU_ENTRY, "tools/scripts")
        # parameter 1 = the name that Krita uses to identify the action
        # parameter 2 = the text to be added to the menu entry for this script
        # parameter 3 = location of menu entry
        action.triggered.connect(self.action_triggered)

    def action_triggered(self):
        qdock = next((w for w in Krita.instance().dockers() if w.objectName() == 'StoryboardDocker'), None)
        wobj = qdock.findChild(QToolButton,'btnCreateScene')
        wobj.click()
        Krita.instance().action('paste_columns_from_clipboard').trigger()
        pass  # your active code goes here.
