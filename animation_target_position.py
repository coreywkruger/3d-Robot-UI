import bge
import mathutils
from math import*

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    
    target = sce.objects[obj["target"]]
    tar_name = target.name + "_"
    bez_points = tar_name + "bez_points"
    
    count = target["key_count"]

    if count > 1:
        points = bge.logic.globalDict[bez_points]
        if count == 0:
            obj.worldPosition = bge.logic.globalDict[bez_points][0]
        if obj["place"] >= len(points) - 2:
            obj.worldPosition = bge.logic.globalDict[bez_points][0]
            obj["place"] = 0
            
        i = obj["place"]
        vec = points[i]
        dif = points[i + 1] - points[i]
        space = points[i + 1] - obj.worldPosition
        
        if space.magnitude >  0.1:
            obj.worldPosition = points[i].lerp(points[i + 1], obj["slice"]/obj["slice_divider"])
            obj["slice"] += 1
            if obj["slice"] >= obj["slice_divider"]:
                obj["slice"] = 0
                obj["place"] += 1
        else:
            obj["slice"] = 0
            obj["place"] += 1
           
main()