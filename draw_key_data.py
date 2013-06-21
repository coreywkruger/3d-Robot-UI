import bge
import mathutils

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    
    d = cont.sensors["d"]
    
    if d.status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        if obj["draw"] == True:
            obj["draw"] = False
        else:
            obj["draw"] = True
    
main()