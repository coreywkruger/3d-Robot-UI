import bge

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner

    anim_target = sce.objects[obj["anim_target_name"]]
    key = cont.sensors["q"]
    
    arm = sce.objects[obj["armature_follow_target"]]
    
    if key.status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        
        if obj["follow_anim_target"] == False:
            obj["follow_anim_target"] = True
        else:
            obj["follow_anim_target"] = False
        
        if arm["snap_translate"] == False:
            arm["snap_translate"] = True
        else:
            arm["snap_translate"] = False
        
        if arm["snap_rotate"] == False:
            arm["snap_rotate"] = True
        else:
            arm["snap_rotate"] = False
            
    if obj["follow_anim_target"] == True:
        obj.worldPosition = anim_target.worldPosition

           
main()