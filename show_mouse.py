import bge
import Rasterizer

obj = bge.logic.getCurrentScene().objects["sph"]

if obj["start"] == 0:
    bge.render.setMousePosition(int(bge.render.getWindowWidth() / 2), int(bge.render.getWindowHeight() / 2))
    obj["start"] = 1
    
Rasterizer.showMouse(True)