# BBD's Krita Script Starter Feb 2018

from krita import *
import pprint
import os
import sys
import xml.etree.ElementTree as ET

EXTENSION_ID = 'pykrita_berenvoedsel'
MENU_ENTRY = 'berenvoedsel_run'


class Berenvoedsel(Extension):

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
        # parameter 3 = location of menu entryW
        action.triggered.connect(self.action_triggered)

def sleep_qt(value):
    """Do a sleep of `value` milliseconds

    use of python timer.sleep() method seems to be not recommanded in a Qt application.. ??
    """
    loop = QEventLoop()
    QTimer.singleShot(value, loop.quit)
    loop.exec()


def main():

    for doc in Krita.instance().documents():
        filepath= doc.fileName()
        #retrieve name
        path_split = os.path.split(str(filepath))
        filename = path_split[1]
        size = len(filename)
        nokra = filename[:size - 4]
        #split text around '_'
        split_file_underscore = nokra.split('_')
        #pad out incremented file number
        filenumber = int(split_file_underscore[-1]) + 1
        filenumber_pad = str(filenumber).zfill(3)
        #join path together with everything we've gathered
        incrementname = f'{path_split[0]}\\{nokra[:-3]}{filenumber_pad}.kra'
        doc.saveAs(incrementname)
        doc.close()

        print (incrementname)

        while os.path.isfile(incrementname) == False:
            sleep_qt(200)

        docs = Krita.instance().openDocument(incrementname)
        Krita.instance().activeWindow().addView(docs)
        frame_end = Krita.instance().activeDocument().animationLength()


    settingRead = Krita.instance().readSetting('','ExportConfiguration-ANIMATION_EXPORT','')



    tree = str(settingRead)
    root = ET.fromstring(tree)

    render_split = os.path.split(str(incrementname))
    rendername = render_split[1]
    print (rendername)
    rsize = len(rendername)
    kraless = rendername[:rsize - 4]
    print (kraless)

    path_name = render_split[1]
    psize = len(path_name)
    path_name = path_name[:psize - 8]

    #parameters written in variables

    basename = kraless + '_'
    basename = str(basename)

    directory = f"../../Demo/{path_name}/{kraless}"

    for x in root[5].iter():
        ffmpeg_path = x.text
        ffmpeg_path = str(ffmpeg_path)

    video_name = f"{kraless}.mp4"
    video_path = f"{directory}/{video_name}"

    frame_end = str(frame_end)
    last_document_path = str(incrementname)

    width = 1960
    width = str(width)
    height = 1789
    height = str(height)
    framerate = 24
    framerate = str(framerate)

    storedict = {
    'basename': basename,
    'custom_ffmpeg_options': '-crf 23 -preset medium -profile:v baseline -pix_fmt yuv420p',
    'delete_sequence': 'false',
    'directory': directory,
    'encode_video': 'true',
    'ffmpeg_path': ffmpeg_path,
    'filename': video_path,
    'first_frame': '0',
    'frame_export/CICPCompatiblePrimaries': '1',
    'frame_export/CICPCompatibleTransferFunction': '2',
    'frame_export/ColorDepthID': 'U8',
    'frame_export/ColorModelID': 'RGBA',
    'frame_export/HDRSupported': 'false',
    'frame_export/ImageContainsTransparency': 'false',
    'frame_export/sRGB': 'true',
    'frame_mimetype': 'image/png',
    'framerate': framerate,
    'height': height,
    'include_audio': 'false',
    'last_document_path': last_document_path,
    'last_frame': frame_end,
    'only_unique_frames': 'true',
    'sequence_start': '0',
    'video_mimetype': 'video/mp4',
    'width': width
    }

    for element in root.iterfind("param"):

        current_type = element.attrib["type"]
        current_key = element.attrib["name"]
        dict_value = storedict[current_key]

        if (current_type == "string"):
            dict_value = f"<![CDATA[{dict_value}]]>"

        element.text = dict_value

    str_xml = str(ET.tostring(root, encoding='unicode',method="xml"))
    #include header
    str_xml = f"<!DOCTYPE params>\n{str_xml}"
    #fix fucked up unicode representations of characters
    str_xml = str_xml.replace("&lt;","<")
    str_xml = str_xml.replace("&gt;",">")

    Krita.instance().writeSetting('','ExportConfiguration-ANIMATION_EXPORT',str_xml)

    sleep_qt(200)
    Krita.instance().action('render_animation').trigger()

    def action_triggered(self):
        main()
        pass  # your active code goes here.
