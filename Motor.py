import math

class PMMotor:

  def __init__(self,Kt,Ke,phi,Ra):
    self.Kt = Kt
    self.Ke = Ke
    self.phi = phi
    self.Ra = Ra

  def GetTorque(self,omega,Va):
    k1 = self.Kt*self.Ke*self.phi*self.phi/self.Ra
    k2 = self.Kt*self.phi/self.Ra
    return - k1*omega + k2*Va

