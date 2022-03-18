import xml.etree.ElementTree as ET

settingRead = Krita.instance().readSetting('','ExportConfiguration-ANIMATION_EXPORT','')
tree = str(settingRead)
root = ET.fromstring(tree)


########################################

for x in root[0].iter():
    print (x.tag,x.attrib)

param {'type': 'string', 'name': 'basename'}

##################################
for x in root[0].iter():
    print (x.text)


020.00_FelixRunsToParents_001_


###############################
print(tree)


<!DOCTYPE params>
<params>
 <param type="string" name="basename"><![CDATA[020.00_FelixRunsToParents_001_]]></param>
 <param type="string" name="custom_ffmpeg_options"><![CDATA[-crf 23 -preset medium -profile:v baseline -pix_fmt yuv420p]]></param>
 <param type="internal" name="delete_sequence">false</param>
 <param type="string" name="directory"><![CDATA[E:/Onedrive/# School/Krabbel en Babbel/Preproduction/04_Storyboard/Demo/020.00_FelixRunsToParents/020.00_FelixRunsToParents_001]]></param>
 <param type="internal" name="encode_video">false</param>
 <param type="string" name="ffmpeg_path"><![CDATA[C:\FOSS\shotcut-win64-220130\ffmpeg.exe]]></param>
 <param type="string" name="filename"><![CDATA[./020.00_FelixRunsToParents_001.mp4]]></param>
 <param type="internal" name="first_frame">0</param>
 <param type="internal" name="frame_export/CICPCompatiblePrimaries">1</param>
 <param type="internal" name="frame_export/CICPCompatibleTransferFunction">2</param>
 <param type="string" name="frame_export/ColorDepthID"><![CDATA[U8]]></param>
 <param type="string" name="frame_export/ColorModelID"><![CDATA[RGBA]]></param>
 <param type="internal" name="frame_export/HDRSupported">false</param>
 <param type="internal" name="frame_export/ImageContainsTransparency">false</param>
 <param type="internal" name="frame_export/sRGB">true</param>
 <param type="string" name="frame_mimetype"><![CDATA[image/png]]></param>
 <param type="internal" name="framerate">24</param>
 <param type="internal" name="height">1789</param>
 <param type="internal" name="include_audio">true</param>
 <param type="string" name="last_document_path"><![CDATA[E:/Onedrive/# School/Krabbel en Babbel/Preproduction/04_Storyboard/Source/020.00_FelixRunsToParents/020.00_FelixRunsToParents_001.kra]]></param>
 <param type="internal" name="last_frame">100</param>
 <param type="internal" name="only_unique_frames">true</param>
 <param type="internal" name="sequence_start">0</param>
 <param type="string" name="video_mimetype"><![CDATA[video/mp4]]></param>
 <param type="internal" name="width">1960</param>
</params>

###############

for x in root.iterfind("param"):
parameters = x.text
print (parameters)


020.00_FelixRunsToParents_001_
-crf 23 -preset medium -profile:v baseline -pix_fmt yuv420p
false
E:/Onedrive/# School/Krabbel en Babbel/Preproduction/04_Storyboard/Demo/020.00_FelixRunsToParents/020.00_FelixRunsToParents_001
false
C:\FOSS\shotcut-win64-220130\ffmpeg.exe
./020.00_FelixRunsToParents_001.mp4
0
1
2
U8
RGBA
false
false
true
image/png
24
1789
true
E:/Onedrive/# School/Krabbel en Babbel/Preproduction/04_Storyboard/Source/020.00_FelixRunsToParents/020.00_FelixRunsToParents_001.kra
100
true
0
video/mp4
1960


##########################################


for x in root.iterfind("param"):
    paraname = x.attrib
    parainput = x.text
    print (paraname,parainput)

{'type': 'string', 'name': 'basename'} 020.00_FelixRunsToParents_001_
{'type': 'string', 'name': 'custom_ffmpeg_options'} -crf 23 -preset medium -profile:v baseline -pix_fmt yuv420p
{'type': 'internal', 'name': 'delete_sequence'} false
{'type': 'string', 'name': 'directory'} E:/Onedrive/# School/Krabbel en Babbel/Preproduction/04_Storyboard/Demo/020.00_FelixRunsToParents/020.00_FelixRunsToParents_001
{'type': 'internal', 'name': 'encode_video'} false
{'type': 'string', 'name': 'ffmpeg_path'} C:\FOSS\shotcut-win64-220130\ffmpeg.exe
{'type': 'string', 'name': 'filename'} ./020.00_FelixRunsToParents_001.mp4
{'type': 'internal', 'name': 'first_frame'} 0
{'type': 'internal', 'name': 'frame_export/CICPCompatiblePrimaries'} 1
{'type': 'internal', 'name': 'frame_export/CICPCompatibleTransferFunction'} 2
{'type': 'string', 'name': 'frame_export/ColorDepthID'} U8
{'type': 'string', 'name': 'frame_export/ColorModelID'} RGBA
{'type': 'internal', 'name': 'frame_export/HDRSupported'} false
{'type': 'internal', 'name': 'frame_export/ImageContainsTransparency'} false
{'type': 'internal', 'name': 'frame_export/sRGB'} true
{'type': 'string', 'name': 'frame_mimetype'} image/png
{'type': 'internal', 'name': 'framerate'} 24
{'type': 'internal', 'name': 'height'} 1789
{'type': 'internal', 'name': 'include_audio'} true
{'type': 'string', 'name': 'last_document_path'} E:/Onedrive/# School/Krabbel en Babbel/Preproduction/04_Storyboard/Source/020.00_FelixRunsToParents/020.00_FelixRunsToParents_001.kra
{'type': 'internal', 'name': 'last_frame'} 100
{'type': 'internal', 'name': 'only_unique_frames'} true
{'type': 'internal', 'name': 'sequence_start'} 0
{'type': 'string', 'name': 'video_mimetype'} video/mp4
{'type': 'internal', 'name': 'width'} 1960

#################################

for x in root.iterfind("param"):
    directory = ../../04_Storyboard/Demo/

################

from krita import *
import os
import xml.etree.ElementTree as ET

Krita.instance().action('save_incremental_version').trigger()
settingRead = Krita.instance().readSetting('','ExportConfiguration-ANIMATION_EXPORT','')
tree = str(settingRead)
root = ET.fromstring(tree)

for doc in Krita.instance().documents():
    basename = doc.fileName()
    print (os.path.basename(basename))


019.00_HardcutFelixDoorSkipping_011.kra
##returns the current file minus 1

#######################


from krita import *
import os
import xml.etree.ElementTree as ET



settingRead = Krita.instance().readSetting('','ExportConfiguration-ANIMATION_EXPORT','')
tree = str(settingRead)
root = ET.fromstring(tree)

for doc in Krita.instance().documents():
    #retrieve path
    filepath= doc.fileName()
    #retrieve name
    filename = os.path.basename(filepath)
    print(filename)
    size = len(filename)
    nokra = filename[:size - 4]
    print(nokra)

    #split text around '_'
    nokra = nokra.split('_')

    filenumber = int(nokra[-1])
    filenumber+= 1
    print(filenumber)

    incrementname = '_'.join(nokra[:-1])+"_"+str(filenumber).zfill(3)+".kra"
    print (incrementname)
    savedfolder = os.path.split(filepath)[0] + '\\'+ incrementname
    doc.saveAs(savedfolder)
    print (savedfolder)


#########################

        filepath= doc.fileName()
        #retrieve name
        path_split = os.path.split(filepath)
        filename = path_split[1]
        print(filename)
        nokra = filename.split(".")[0]
        print(nokra)
        #split text around '_'
        split_file_underscore = nokra.split('_')
        filenumber = int(split_file_underscore[-1])
        print(filenumber)
        filenumber+= 1
        filenumber_pad = str(filenumber).zfill(3)
        incrementname = f'{path_split[0]}\\{nokra[:-4]}_{filenumber_pad}.kra'
        print (incrementname)


for doc in Krita.instance().documents():
    filepath= doc.fileName()
    #retrieve name
    path_split = os.path.split(filepath)
    filename = path_split[1]
    print(filename)
    nokra = filename.split(".")[0]
    print(nokra)

    #split text around '_'
    split_file_underscore = nokra.split('_')

    filenumber = int(split_file_underscore[-1])
    print(filenumber)
    filenumber+= 1
    filenumber_pad = str(filenumber).zfill(3)
    incrementname = f'{path_split[0]}\\{nokra[:-4]}_{filenumber_pad}.kra'
    print (incrementname)


#########################

from krita import *
import os
import xml.etree.ElementTree as ET
settingRead = Krita.instance().readSetting('','ExportConfiguration-ANIMATION_EXPORT','')
tree = str(settingRead)
root = ET.fromstring(tree)

for doc in Krita.instance().documents():
    filepath= doc.fileName()
    #retrieve name
    path_split = os.path.split(filepath)
    filename = path_split[1]
    print(filename)
    nokra = filename.split(".")[0]
    print(nokra)

    #split text around '_'
    split_file_underscore = nokra.split('_')

    filenumber = int(split_file_underscore[-1])
    print(filenumber)
    filenumber+= 1
    filenumber_pad = str(filenumber).zfill(3)
    incrementname = f'{path_split[0]}\\{nokra[:-4]}_{filenumber_pad}.kra'
    print (incrementname)

######################

for doc in Krita.instance().documents():
    Krita.instance().action('save_incremental_version').trigger()

    settingRead = Krita.instance().readSetting('','ExportConfiguration-ANIMATION_EXPORT','')
    tree = str(settingRead)
    root = ET.fromstring(tree)
    print (os.path.basename(filename))
    elemList = []
    for x in root.iterfind("param"):
        paraname = x.attrib
        parainput = x.text
        elemList.append(paraname)
        elemList = list(set(elemList))
        print (paraname,parainput)

#################

from krita import *
import os
import xml.etree.ElementTree as ET

for doc in Krita.instance().documents():
    filepath= doc.fileName()
    #retrieve name
    path_split = os.path.split(str(filepath))
    filename = path_split[1]
    nokra = filename.split(".")[0]
    #split text around '_'
    split_file_underscore = nokra.split('_')
    #pad out incremented file number
    filenumber = int(split_file_underscore[-1]) + 1
    filenumber_pad = str(filenumber).zfill(3)
    #join path together with everything we've gathered
    incrementname = f'{path_split[0]}\\{nokra[:-3]}{filenumber_pad}.kra'
    doc.saveAs(incrementname)
    print (incrementname)

################

from krita import *
import os

def sleep_qt(value):
    """Do a sleep of `value` milliseconds
    use of python timer.sleep() method seems to be not recommanded in a Qt application.. ??
    """

    loop = QEventLoop()
    QTimer.singleShot(value, loop.quit)
    loop.exec()

def main():

    newpath = 'C:\\Users\\koter\\Desktop\\test\\test_002.kra'

    Krita.instance().action('save_incremental_version').trigger()
    while os.path.isfile(newpath) == False:
        sleep_qt(300)

    for docs in Krita.instance().documents():
        filename = docs.fileName()
        print (os.path.basename(filename))
main()


################################

from krita import *
import os

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
        nokra = filename.split(".")[0]
        #split text around '_'
        split_file_underscore = nokra.split('_')
        #pad out incremented file number
        filenumber = int(split_file_underscore[-1]) + 1
        filenumber_pad = str(filenumber).zfill(3)
        #join path together with everything we've gathered
        incrementname = f'{path_split[0]}\\{nokra[:-3]}{filenumber_pad}.kra'
        doc.saveAs(incrementname)
        print (incrementname)

    while os.path.isfile(incrementname == False:
        sleep_qt(200)

        docs = Krita.instance().openDocument(incrementname)
        Krita.instance().activeWindow().addView(docs)

main()


###############


from krita import *
import os

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
        nokra = filename.split(".")[0]
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

main()
