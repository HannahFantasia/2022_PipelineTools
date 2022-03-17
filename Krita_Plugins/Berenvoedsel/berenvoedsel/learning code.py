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

###############################

for x in root.iterfind("param"):
    directory = ../../04_Storyboard/Demo/

################
