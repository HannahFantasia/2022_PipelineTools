##A davinci resolve studio (not free version)
##incremental timeline/sequence saver made by Sas van Gulik

import DaVinciResolveScript as dvr_script
resolve = dvr_script.scriptapp("Resolve")
projman = resolve.GetProjectManager()
proj = projman.GetCurrentProject()
timeline = proj.GetCurrentTimeline()
dup_timeline = timeline.DuplicateTimeLine()
#retrieve name
dup_name = dup_timeline.GetName()
#modifying numbers
#remove copy part
dup_name = dup_name.replace(" copy","")
#split text around '_'
dup_name = dup_name.split("_")
#timeline number
timeline_number = int(dup_name[1])
timeline_number += 1
dup_name = dup_name[0]+"_"+str(timeline_number).zfill(3)
dup_timeline.SetName(dup_name)
