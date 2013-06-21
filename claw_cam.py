import bge
from bge import texture
from bge import logic

cont = logic.getCurrentController()
scene = logic.getCurrentScene()
claw_cam = scene.objects["claw_cam"]
obj = cont.owner

if not hasattr(logic, 'video'):

    # identify a static texture by name
    matID = 0

    # create a dynamic texture that will replace the static texture
    logic.video = texture.Texture(obj, matID)

    # define a source of image for the texture, here a movie
    movie = bge.texture.ImageRender(scene, claw_cam)
    logic.video.source = movie

logic.video.refresh(True)