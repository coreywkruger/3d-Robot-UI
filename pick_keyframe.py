import bge
import mathutils
import math

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    
    obj = cont.owner
    name = obj.name + "_"
    cont_keys = name + "cont_keys"
    mouse_prev = name + "mouse_prev"
    below_prev = name + "below_prev"
    above_prev = name + "above_prev"
    selected_key_index = name + "selected_key_index"

    cam = sce.active_camera
    mouse = cont.sensors["Mouse"]

    # Position of the mouse on the screen.
    x = mouse.position[0]/bge.render.getWindowWidth()
    z = mouse.position[1]/bge.render.getWindowHeight()

    # The position of the mouse relative to the center of the screen is found here.
    px = 0.5 + x
    pz = 0.5 + z
    mvec = mathutils.Vector((px, 0, pz))
    fact = mvec.magnitude
    m_vect = -10000*cam.getScreenVect(x, z)
    
    if obj["key_count"] > 0:
        
        i = 0
        list = bge.logic.globalDict[cont_keys]
        matches = []
        
        ##### Decides if a key is under the cursor and collects key indexes in a list (matches).
        while i < len(bge.logic.globalDict[cont_keys]):
            
            check = mathutils.geometry.intersect_point_line(list[i], cam.worldPosition, m_vect)
            
            if (check[0] - list[i]).magnitude < 0.5:
                matches += [list[i][0], list[i][1], list[i][2], i]
            
            i += 1
 
        front = (cam.far, cam.far, cam.far, 0)
        cam_point = mathutils.Vector((front[0], front[1], front[2]))
        k = 0
        
        ##### If multiple keys are under the cursor, decides which key is closest to the camera (in front).
        while k < len(matches):
            
            # The list matches is interated through, three entries at a time.
            spot = mathutils.Vector((matches[0],matches[1],matches[2]))
            
            #The closes point to the camera is gradually selected. The vector "front" is replaced by this progressively more accurate selection.
            if (spot - cam.worldPosition).magnitude < cam_point.magnitude:
                front = (spot[k + 0], spot[k + 1], spot[k + 2], matches[k + 3])
                cam_point = mathutils.Vector((front[0], front[1], front[2]))
            
            k += 4
            
        differ = mathutils.Vector((0,0,0))   
        cam_distance = mathutils.Vector((0,0,0))
        add_me = mathutils.Vector((0,0,0))
        
        ##### Decides if a key is elligible for selection (is the mouse clicked, and hovering over a key)
        if mouse.status == bge.logic.KX_INPUT_JUST_ACTIVATED and cam_point.magnitude < mathutils.Vector((cam.far, cam.far, cam.far)).magnitude:
            
            bge.logic.globalDict[mouse_prev] = bge.logic.globalDict[cont_keys][front[3]]    
            
            # Checking if the keyframe is normal.   
            if front[3] > 0:
                bge.logic.globalDict[below_prev] = bge.logic.globalDict[cont_keys][front[3] - 1]
            
            # Checking if the keyframe is the last keyframe in the list (a special case).
            if front[3] < len(bge.logic.globalDict[cont_keys]) - 1:
                bge.logic.globalDict[above_prev] = bge.logic.globalDict[cont_keys][front[3] + 1]
            
            bge.logic.globalDict[selected_key_index] = front[3]
            
            # If a key is elligible, the okay is given for the whole bezier curve to be recalculated.
            obj["key_change"] = True
            
        ##### Here, actual keyframes (not bezier control handles) are moved through space if elligible.
        if mouse.status == bge.logic.KX_INPUT_ACTIVE and obj["key_change"] == True:
            
            cam_distance = mathutils.geometry.intersect_point_line(bge.logic.globalDict[mouse_prev], cam.worldPosition, cam.far*m_vect)
            add_me = -bge.logic.globalDict[mouse_prev] + (mathutils.Vector((cam_distance[0])))
            index = bge.logic.globalDict[selected_key_index]
            bge.logic.globalDict[cont_keys][index] = bge.logic.globalDict[mouse_prev] + add_me
            
            # Every third entry in the cont_keys list is a keyframe.
            if (index)%3 == 0:
                
                # Checking if the keyframe is normal.
                if index > 0:
                    bge.logic.globalDict[cont_keys][index - 1] = bge.logic.globalDict[below_prev] + add_me
                
                # Checking if the keyframe is the last keyframe in the list (a special case).
                if index < len(bge.logic.globalDict[cont_keys]) - 1:
                    bge.logic.globalDict[cont_keys][index + 1] = bge.logic.globalDict[above_prev] + add_me
            
            cont_keys_list = bge.logic.globalDict[cont_keys]
            
            ##### Bezier control handles have to rotate around the central keyframe. This is where those rotations are calculated.
            # Lower control handle (between two knots on the bezier curve) is repositioned.
            if (index)%3 == 1 and index > 3:
                handle_1 = cont_keys_list[index - 1] - (cont_keys_list[index] - cont_keys_list[index - 1])
                bge.logic.globalDict[cont_keys][index - 2] = handle_1
               
           # Uppser control handle (between two knots on the bezier curve) is repositioned.
            if (index)%3 == 2 and index < len(bge.logic.globalDict[cont_keys]) - 3:
                handle_2 = cont_keys_list[index + 1] - (cont_keys_list[index] - cont_keys_list[index + 1])
                bge.logic.globalDict[cont_keys][index + 2] = handle_2
         
        ##### The mouse's current position is saved for the next tick.   
        if mouse.status == bge.logic.KX_SENSOR_JUST_DEACTIVATED and obj["key_change"] == True:
            bge.logic.globalDict[mouse_prev] = bge.logic.globalDict[cont_keys][bge.logic.globalDict[selected_key_index]]
            obj["key_change"] = False

main()