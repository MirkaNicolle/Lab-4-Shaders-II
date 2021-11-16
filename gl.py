'''
Source: https://github.com/churly92/RendererOpenGL

Mirka Monzon 18139
Lab 4: Shaders II

'''
import glm
from OpenGL.GL import * 
from OpenGL.GL.shaders import compileProgram, compileShader
from pygame import image
from numpy import array, float32
import obj

class Model(object):
    def __init__(self, objName, textureName):

        self.model = obj.Obj(objName)

        self.createVertexBuffer()

        self.position = glm.vec3(0,0,0)
        self.rotation = glm.vec3(0,0,0)
        self.scale = glm.vec3(1,1,1)

        self.textureSurface = image.load(textureName)
        self.textureData = image.tostring(self.textureSurface, "RGB", True)
        self.texture = glGenTextures(1)