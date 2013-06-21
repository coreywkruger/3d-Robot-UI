import bge
import mathutils
import math

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    
    name = obj.name + "_"
    cont_keys = name + "cont_keys"
    bez_points = name + "bez_points"
    
    key = cont.sensors['key1']
    mouse = cont.sensors["Mouse"]
    res = obj["res"]
    
    #key.status == bge.logic.KX_INPUT_JUST_ACTIVATED or     
    if obj["new_key"] == True:
        print(obj["key_count"])
        if obj["key_count"] == 1:
            c = bge.logic.globalDict[cont_keys]
            bge.logic.globalDict[bez_points] = [c[0]]
            
        if obj["key_count"] >= 2:
            print("hello")
            list = bge.logic.globalDict[cont_keys]

            bez_points_list = []
            i = (obj["key_count"] - 1)
            kon = 3
            kn1 = list[i*kon - 3]
            ha1 = list[i*kon - 2]
            ha2 = list[i*kon - 1]
            kn2 = list[i*kon]
        
            resDy = int((kn1 - kn2).magnitude*1.5)
            
            if resDy < 2:
                resDy = 2
            
            points = mathutils.geometry.interpolate_bezier(kn1, ha1, ha2, kn2, 10)
            bez_points_list = points[1:]
            bge.logic.globalDict[bez_points] += bez_points_list
        obj["new_key"] = False
        
    if obj["key_change"] == True:
        bge.logic.globalDict[bez_points] = []
        i = 0
        
        while i <= obj["key_count"] - 1:
                                    
            if i == 1:
                bge.logic.globalDict[bez_points] = [bge.logic.globalDict[cont_keys][0]]
            
            if i >= 1:
                list = bge.logic.globalDict[cont_keys]
                bez_points_list = []
                kon = 3
                
                kn1 = list[i*kon - 3]
                ha1 = list[i*kon - 2]
                ha2 = list[i*kon - 1]
                kn2 = list[i*kon]
            
                resDy = int((kn1 - kn2).magnitude*1.5)
                
                if resDy < 2:
                    resDy = 2
                
                points = mathutils.geometry.interpolate_bezier(kn1, ha1, ha2, kn2, resDy)
                bez_points_list = points[1:]
                bge.logic.globalDict[bez_points] += bez_points_list
            
            i += 1
    
main()
