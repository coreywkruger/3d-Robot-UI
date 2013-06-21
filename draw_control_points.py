import bge
import mathutils  as m
import math

def main():
    
    sce = bge.logic.getCurrentScene()
    cont = bge.logic.getCurrentController()
    
    obj = cont.owner
    name = obj.name + "_"
    cont_keys = name + "cont_keys"
    
    cam = sce.active_camera
    
    if obj["key_count"] > 0:
        points = bge.logic.globalDict[cont_keys]
        j = 0
        
        while j < len(points) and obj["draw"] == True:
            
            if (j)%3 == 0:
                vec = points[j]
                mul = 0.005*(vec - cam.worldPosition).magnitude
                col = [0,0.7,1]
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1, 1))), (vec + mul*m.Vector(( 1, 1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1, 1, 1))), (vec + mul*m.Vector((-1, 1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1,-1, 1))), (vec + mul*m.Vector(( 1,-1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1,-1, 1))), (vec + mul*m.Vector((-1,-1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1, 1))), (vec + mul*m.Vector(( 1, 1, 1)) + mul*m.Vector(( 0,-2, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1,-1))), (vec + mul*m.Vector(( 1, 1,-1)) + mul*m.Vector(( 0,-2, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1, 1, 1))), (vec + mul*m.Vector((-1, 1, 1)) + mul*m.Vector(( 0,-2, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1, 1,-1))), (vec + mul*m.Vector((-1, 1,-1)) + mul*m.Vector(( 0,-2, 0))), col)
                
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1, 1))), (vec + mul*m.Vector(( 1, 1, 1)) + mul*m.Vector((-2, 0, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1,-1))), (vec + mul*m.Vector(( 1, 1,-1)) + mul*m.Vector((-2, 0, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1,-1, 1))), (vec + mul*m.Vector(( 1,-1, 1)) + mul*m.Vector((-2, 0, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1,-1,-1))), (vec + mul*m.Vector(( 1,-1,-1)) + mul*m.Vector((-2, 0, 0))), col)

            else:
                vec = points[j]
                mul = 0.004*(vec - cam.worldPosition).magnitude
                col = [1,1,0.6]
                handle_color = [1,0.5,0]
                
                if (j - 1)%3 == 0:
                    bge.render.drawLine( points[j], points[j - 1], handle_color)
                if (j + 1)%3 == 0:
                    bge.render.drawLine( points[j], points[j + 1], handle_color)
                    
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1, 1))), (vec + mul*m.Vector(( 1, 1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1, 1, 1))), (vec + mul*m.Vector((-1, 1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1,-1, 1))), (vec + mul*m.Vector(( 1,-1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1,-1, 1))), (vec + mul*m.Vector((-1,-1, 1)) + mul*m.Vector(( 0, 0,-2))), col)
                
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1, 1))), (vec + mul*m.Vector(( 1, 1, 1)) + mul*m.Vector(( 0,-2, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1,-1))), (vec + mul*m.Vector(( 1, 1,-1)) + mul*m.Vector(( 0,-2, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1, 1, 1))), (vec + mul*m.Vector((-1, 1, 1)) + mul*m.Vector(( 0,-2, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector((-1, 1,-1))), (vec + mul*m.Vector((-1, 1,-1)) + mul*m.Vector(( 0,-2, 0))), col)
                
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1, 1))), (vec + mul*m.Vector(( 1, 1, 1)) + mul*m.Vector((-2, 0, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1, 1,-1))), (vec + mul*m.Vector(( 1, 1,-1)) + mul*m.Vector((-2, 0, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1,-1, 1))), (vec + mul*m.Vector(( 1,-1, 1)) + mul*m.Vector((-2, 0, 0))), col)
                bge.render.drawLine( (vec + mul*m.Vector(( 1,-1,-1))), (vec + mul*m.Vector(( 1,-1,-1)) + mul*m.Vector((-2, 0, 0))), col)
            
            j += 1
    
    
main()