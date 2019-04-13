# Example effect
import providad
import moviepy
import numpy as np
import providad.asset_effects_Letters_Base

from moviepy import editor


################## ARRIVE #########################

class LetterArriveFromLeft(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([1,0])
        d = lambda t : max(0, 3-3*t)
        return lambda t: screenpos-400*v*d(t-0.2*i)

    def name(self):
        return "LetterArriveFromLeft"

class LetterArriveFromRight(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([-1,0])
        d = lambda t : max(0, 3-3*t)
        return lambda t: screenpos-400*v*d(t-0.2*i)

    def name(self):
        return "LetterArriveFromRight"

class LetterArriveFromTop(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([0,1])
        d = lambda t : max(0, 3-3*t)
        return lambda t: screenpos-400*v*d(t-0.2*i)

    def name(self):
        return "LetterArriveFromTop"

class LetterArriveFromBottom(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([0,-1])
        d = lambda t : max(0, 3-3*t)
        return lambda t: screenpos-400*v*d(t-0.2*i)

    def name(self):
        return "LetterArriveFromBottom"

################## Cascade #########################

class LetterCascadeFromLeft(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([1,0])
        d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1+t**4))
        return lambda t: screenpos+v*400*d(t-0.15*i)
        
    def name(self):
        return "LetterCascadeFromLeft"

class LetterCascadeFromRight(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([-1,0])
        d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1+t**4))
        return lambda t: screenpos+v*400*d(t-0.15*i)

    def name(self):
        return "LetterCascadeFromRight"

class LetterCascadeFromTop(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([0,-1])
        d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1+t**4))
        return lambda t: screenpos+v*400*d(t-0.15*i)

    def name(self):
        return "LetterCascadeFromTop"

class LetterCascadeFromBottom(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        v = np.array([0,1])
        d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1+t**4))
        return lambda t: screenpos+v*400*d(t-0.15*i)

    def name(self):
        return "LetterCascadeFromBottom"
################## Vortex #########################

class LetterVortexIn(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        rotMatrix = lambda a: np.array( [[np.cos(a),np.sin(a)], [-np.sin(a),np.cos(a)]] )
        d = lambda t : 1.0/(0.3+t**8) #damping
        a = i*np.pi/ nletters # angle of the movement
        v = rotMatrix(a).dot([-1,0])
        if i%2 : v[1] = -v[1]
        return lambda t: screenpos+400*d(t)*rotMatrix(0.5*d(t)*a).dot(v)

    def name(self):
        return "LetterVortexIn"

class LetterVortexOut(providad.asset_effects_Letters_Base.LetterMove):
    def move(self, screenpos,i,nletters):
        rotMatrix = lambda a: np.array( [[np.cos(a),np.sin(a)], [-np.sin(a),np.cos(a)]] )
        d = lambda t : max(0,t) #damping
        a = i*np.pi/ nletters # angle of the movement
        v = rotMatrix(a).dot([-1,0])
        if i%2 : v[1] = -v[1]
        return lambda t: screenpos+400*d(t-0.1*i)*rotMatrix(-0.2*d(t)*a).dot(v)

    def name(self):
        return "LetterVortexOut"