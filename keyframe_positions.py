import bge
import mathutils
#import GameKeys
#import GameLogic
    
def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    
    obj = cont.owner
    
    name = obj.name + "_"
    cont_keys = name + "cont_keys"
    keys = name + "keys"
    
    act = cont.actuators["add"]
    key = cont.sensors['key1']
    
    if key.status == bge.logic.KX_INPUT_JUST_ACTIVATED:
        
        kn1 = []
        kn2 = []
        c = obj["key_count"] 
        if c == 0:
            bge.logic.globalDict[cont_keys] = [mathutils.Vector((obj.worldPosition[0], obj.worldPosition[1], obj.worldPosition[2]))]
            bge.logic.globalDict[keys] = [mathutils.Vector((obj.worldPosition[0], obj.worldPosition[1], obj.worldPosition[2]))]
            
        if c > 0:
            bge.logic.globalDict[keys] += [mathutils.Vector((obj.worldPosition[0], obj.worldPosition[1], obj.worldPosition[2]))]
            
            if c >= 1:
                i = obj["key_count"]
                j = obj["cont_key_count"]
                list = bge.logic.globalDict[keys]
                
                if c > 1:
                    kn1 = list[i]
                    kn2 = list[i - 1]
                    ha1 = ((bge.logic.globalDict[cont_keys][j - 1] - bge.logic.globalDict[cont_keys][j - 2]) + bge.logic.globalDict[cont_keys][j - 1])
                    ha2 = (kn1 - ha1)/2 + ha1
                
                else:
                    kn1 = list[i]
                    kn2 = list[i - 1]
                    ha1 = (kn1 - kn2)/3 + kn2
                    ha2 = 2*((kn1 - kn2)/3) + kn2
                
                bge.logic.globalDict[cont_keys] += [ha1, ha2, kn1]
                j = len(bge.logic.globalDict[cont_keys])
        
        obj["cont_key_count"] = len(bge.logic.globalDict[cont_keys])
        obj["key_count"] += 1
        obj["new_key"] = True
    
main()


