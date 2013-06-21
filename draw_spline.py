import bge
import mathutils

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    
    name = obj.name + "_"
    bez_points = name + "bez_points"
    cont_keys = name + "cont_keys"

    if obj["key_count"] > 1 and obj["draw"] == True:
        p = bge.logic.globalDict[bez_points]
        c = bge.logic.globalDict[cont_keys]
        
        j = 0
        
        while j < (len(p) - 1):
            bge.render.drawLine(p[j], p[j + 1], [1,1,0])
            j += 1
        
main()