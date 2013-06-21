import bge
import mathutils
import math

sce = bge.logic.getCurrentScene()
cont = bge.logic.getCurrentController()
obj = cont.owner
target_ob = sce.objects[obj["target"]]

##### Extra visual stuff
rot = sce.objects["rot"]
angle = mathutils.Vector((target_ob.worldPosition[0], target_ob.worldPosition[1], 0)).angle((mathutils.Vector((0,1,0))))
rot.alignAxisToVect(mathutils.Vector((target_ob.worldPosition[0], target_ob.worldPosition[1], 0)), 1, 1.0)


target_position = target_ob.localPosition
handle = obj.channels["handle"]


Target_to_me = mathutils.Vector((target_ob.worldPosition - obj.worldPosition))
orientation_Y = mathutils.Vector((Target_to_me[0], Target_to_me[1], 0)).normalized()
orientation_X = mathutils.Vector((orientation_Y[1], -orientation_Y[0], 0))

base_rotation = orientation_Y.angle(obj.channels["base_rot"].pose_head)

if orientation_X.dot((obj.channels["base_rot"].pose_head).normalized()) > 0:
    base_rotation = base_rotation
else:
    base_rotation = -base_rotation

new_base_rotation = obj.channels["B"].joint_rotation
dest = target_position - obj.channels["handle"].bone.head - obj.localPosition
dist = dest.magnitude
new_EE_position = obj.channels["handle"].location
add = (dest - new_EE_position)*obj["coarse"]


if (dest - new_EE_position).magnitude < 0.7:
    obj["prec"] = True   
else:
    obj["prec"] = False   


if obj["snap_translate"] == True: 
    add = (dest - new_EE_position)
else:
    if obj["prec"] == True:
        add = (dest - new_EE_position)*obj["precise"]
    else:
        add = (add/add.magnitude)*obj["coarse"]
        

if obj["snap_rotate"] == True:
    new_base_rotation += mathutils.Vector((0.0, 0.0, base_rotation))
else:
    if abs(base_rotation) < math.pi/16:
        new_base_rotation += mathutils.Vector((0.0, 0.0, base_rotation*obj["rotate_fine"]))
    else:
        new_base_rotation += mathutils.Vector((0.0, 0.0, math.copysign(1.0, base_rotation)*obj["rotate_coarse"]))


new_EE_position = new_EE_position + add
obj.channels["B"].joint_rotation = new_base_rotation    

if new_EE_position[2] < -obj.channels["handle"].bone.head[2]:
    new_EE_position[2] = -obj.channels["handle"].bone.head[2]
  
obj.channels["handle"].location = new_EE_position