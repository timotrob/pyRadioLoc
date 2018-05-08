import numpy as np
from math import log10
from PyRadioLoc.Enums import LeeAreaType
from PyRadioLoc.Enums import AreaKind
from PyRadioLoc.Enums import CityKind
from PyRadioLoc.Enums import TerrainKind
__all__ = ['FreeSpaceModel',
          'OkumuraHataModel',
          'LeeModel',
          'EricssonModel']

class FreeSpaceModel(object):
    """Free Space path loss Model"""
    def __init__(self, freq):
        self.freq = freq
    """Path loss Free Space path loss Model"""
    def pathloss(self,dist):
        return 32.44 + 20*np.log10(dist) + 20*np.log10(self.freq)

class FlatEarthModel(object):
    """FlatEarthModel Model"""
    def __init__(self, freq):
        self.freq = freq
        self.txH = 50.0
        self.rxH = 1.5
    def pathloss(self,dist):
        return 120 + (40*np.log10(dist))-(20*np.log10(self.txH))-(20*np.log10(self.rxH))

class LeeModel(object):
    """Lee Point-to-Point Model"""
    def __init__(self, freq):
        self.freq = freq
        self.n0 = LeeAreaType.SubUrban.value[0][0]
        self.p0 = LeeAreaType.SubUrban.value[0][1]
        self.txH = 50.0
        self.rxH = 1.5
    def pathloss(self,dist):
        nf = 3 if self.freq > 850 else 2
        X2 = 2 if self.rxH > 3 else 1
        L1 = -20*np.log10(self.txH/30)
        L2 = -10*X2*np.log10(self.rxH/3)
        Lo = 50.3 + self.p0 - 10*self.n0*np.log10(1.61)-10*nf*np.log10(900)
        L = Lo + 10*self.n0*np.log10(dist)+10*nf*np.log10(self.freq)+L1+L2
        return L

class EricssonModel(object):
    """Ericcson Model"""
    def __init__(self, freq):
        self.freq = freq
        self.cityKind = CityKind.Medium
        self.areaKind = AreaKind.Urban
        self.checkFreq = True
        self.txH = 50.0
        self.rxH = 1.5
    def pathloss(self,dist):
        if (self.checkFreq):
            if (self.freq<=500 or self.freq>=2000):
                raise ValueError('The frequency range for Ericcson Model is 500MHz-1500Mhz')
        f, d, hm, hb = self.freq, dist, self.rxH, self.txH
        g = 44.49*np.log10(f)-4.78*(np.log10(f)**2)
        a2= 12
        a3= 0.1
        if (self.cityKind== CityKind.Large):
            a0,a1 = 36.2,30.2
        elif (self.cityKind== CityKind.Medium):
            a0,a1 = 43.2,68.9
        else:
            a0,a1=45.9,100.6
        PL=a0+a1*np.log10(d)+a2*np.log10(hb)+a3*(np.log10(hb))*(np.log10(d))-3.2*np.log10((11.75*hm)**2)+g
        return PL
class Cost231Model(object):
    """COST 231- Cost-Waldrosch-Ikegami Model"""
    def __init__(self, freq):
        self.freq = freq
        self.txH = 50.0
        self.rxH = 1.5
        self.ws = 15.0
        self.bs =0.5
        self.hr =3.0
        self.areaKind = AreaKind.Urban
        self.cityKind =  CityKind.Medium
        self.checkFreq = True
    def pathloss(self,dist):
        if (self.checkFreq):
            if (self.freq<=150 or self.freq>=2000):
                raise ValueError('The frequency range for Ecc-33 Model is 150MHz-2000Mhz')
        f, d, hm, hb,hr,ws,bs = self.freq, dist, self.rxH, self.txH,self.hr,self.ws,self.bs
        deltaH = hm/hb #relaction between heighths
        Lbsh= 18*np.log10(1+deltaH) # Loss due to difference of heights
        Ka=54.0  #Coefficient of proximity Buildings
        Kd=18.0  #Coeficiente of proximidade Edifica??es
        Kf=4.0  #Coeficient of environment(urban or not)
        #Coeficient's calculate
        if (hr > hb):
            Lbsh=0.0
        if (hb<=hr and d>=0.5):
            Ka = Ka - 0.8*deltaH
        elif (hb<=hr and d<0.5):
            Ka = Ka - 0.8*deltaH*(d/0.5)
        if (hb < hr):
            Kd=Kd-15*(hb-hr)/(hr-hm)
        if (self.cityKind==CityKind.Small):
            Kf = Kf +0.7*(f/925-1)
        else:
            Kf = Kf +1.5*(f/925-1)
        #path loss's calculate
        Lo = 32.4+20*np.log10(d)+20*np.log10(f)                     #free space path loss
        Lrts = 8.2+10*np.log(ws) + 10*np.log10(f) + 10*np.log(deltaH) # roofTop loss
        Lmsd =Lbsh+ Ka+ Kd*np.log10(d)+Kf*np.log10(f)-9*np.log10(bs)    #Multpath loss
        #final path loss
        PL = Lo + Lrts + Lmsd;
        return PL

class Cost231HataModel(object):
    """COST 231-Cost-Hata Extension Model"""
    def __init__(self, freq):
       self.freq = freq
       self.rxH =1.5
       self.txH = 50.0
       self.areaKind = AreaKind.Urban
       self.checkFreq = True
    def pathloss(self,dist):
        if (self.checkFreq):
            if (self.freq<=150 or self.freq>=2000):
                raise ValueError('The frequency range for Cost-Hata Extension Model is 150MHz-2000Mhz')
        f,hm,hb,d = self.freq,self.rxH,self.txH,dist    
        ar=(1.1*np.log10(f)-0.7)*hm-(1.56*np.log10(f)-0.8)
        C = 3 if  (self.areaKind==AreaKind.Urban) else 0
        L= 46.3 +33.9*np.log10(f)-13.82*np.log10(hb)-ar+(44.9-6.55*np.log10(hb))*np.log10(d)+C
        return L
class OkumuraHataModel(object):
    """Okumura-Hata Model"""
    def __init__(self, freq):
       self.freq = freq
       self.rxH =1.5
       self.txH = 50.0
       self.areaKind = AreaKind.Urban
       self.cityKind = CityKind.Large
       self.checkFreq = True

    def pathloss(self,dist):
        if (self.checkFreq):
            if (self.freq<=500 or self.freq>=1500):
                raise ValueError('The frequency range for Okumura-Hata Model is 500MHz-1500Mhz')
        hm,hb,f = self.rxH,self.txH,self.freq
        # a Calc
        if (f<=200 and self.cityKind==CityKind.Large):
            a = 8.29*(np.log10(1.54*hm))**2-1.1
        elif (f>=400 and self.cityKind==CityKind.Large):
            a = 3.2*(np.log10(11.75*hm)**2)-4.97
        else:
            a = (1.1*np.log10(f-0.7))*hm -(1.56*np.log10(f-0.8))
        # Pathloss Calc
        lossUrban = 69.55 +(26.16)*np.log10(f)-13.82*np.log10(hb) - a + (44.9-6.55*np.log10(hb))*np.log10(dist)
        if (self.areaKind==AreaKind.Rural):
            lossOpen = lossUrban - 4.78*((np.log10(f))^2)+18.33*np.log10(f)-40.94
            return lossOpen
        elif (self.areaKind==AreaKind.Suburban):
            lossSubUrban= lossUrban  - 2*(np.log10(f/28.0))^2 - 5.4
            return lossSubUrban
        else:
            return lossUrban

class Ecc33Model(object):
    def __init__(self, freq):
       self.freq = freq
       self.rxH =1.5
       self.txH = 50.0
       self.areaKind = AreaKind.Urban
       self.cityKind = CityKind.Large
       self.checkFreq = True

    def pathloss(self,dist):
        if (self.checkFreq):
            if (self.freq<=500 or self.freq>=1500):
                raise ValueError('The frequency range for Ecc33 Model is 500MHz-1500Mhz')
        hm,hb,f,d = self.rxH,self.txH,self.freq,dist
        PLfs = 92.4+20*np.log10(d)+20*np.log10(f/1000)
        PLbm = 20.41+9.83*np.log10(d)+7.894*(np.log10(f/1000))+9.56*(np.log10(f/1000))**2
        Gb = np.log10(hb/200)*(13.98+5.8*(np.log10(d))**2)
        Gm =(42.57+13.7*np.log10(f/1000))*(np.log10(hm)-0.585)
        PL= PLfs+PLbm-Gb-Gm
        return PL

class SuiModel(object):
    def __init__(self, freq):
       self.freq = freq
       self.rxH =1.5
       self.txH = 50.0
       self.terrainKind = TerrainKind.A
       self.checkFreq = True
       self.shadowFading = 8.2

    def pathloss(self,dist):
        if (self.checkFreq):
            if (self.freq<=1900 or self.freq>=11000):
                raise ValueError('The frequency range for SUI Model is 1900 MHz-11.000 Mhz')
        txH, rxH, f,d = self.txH, self.rxH, self.freq, np.multiply(dist,1000)
        coef_a = (4.6,0.0075,12.6,-10.8)
        coef_b = (4.0,0.0065,17.1,-10.8)
        coef_c = (3.6,0.005,20,-20)
        s = self.shadowFading
        # Terrain Mode  B
        if (self.terrainKind == TerrainKind.A):
            a, b, c, XhCF = coef_a
        elif (self.terrainKind == TerrainKind.B):
            a, b, c, XhCF = coef_b
        else:
            a, b, c, XhCF = coef_c
        d0 = 100
        A = 20 *np.log10((4 *np.pi * d0) / (300 / f))
        y = (a - b * txH) + c / txH
        Xf = 6 * np.log10(f / 2000)
        Xh = XhCF * np.log10(rxH / 2)
        dr = np.multiply(d,1/d0)
        return (10 * y * np.log10(dr)) + Xf + Xh + s+ A







