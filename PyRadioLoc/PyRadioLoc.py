from PyRadioLoc.Utils.GeoUtils import GeoUtils
from PyRadioLoc.Pathloss.Models import FreeSpaceModel
from PyRadioLoc.Pathloss.Models import FlatEarthModel
from PyRadioLoc.Pathloss.Models import LeeModel
from PyRadioLoc.Pathloss.Models import EricssonModel
from PyRadioLoc.Pathloss.Models import Cost231Model
from PyRadioLoc.Pathloss.Models import Cost231HataModel
from PyRadioLoc.Pathloss.Models import OkumuraHataModel
from PyRadioLoc.Pathloss.Models import Ecc33Model
from PyRadioLoc.Pathloss.Models import SuiModel

m1 = FreeSpaceModel(900)
m2 = FlatEarthModel(900)
m3 = LeeModel(900)
m4 = EricssonModel(900)
m5 =  Cost231Model(900)
m6 = Cost231HataModel(900)
m7 = OkumuraHataModel(900)
m8 = Ecc33Model(900)
m9 = SuiModel(2100)
print("FreeSapce:{}".format(m1.pathloss(0.8)))
print("FlatEarthModel:{}".format(m2.pathloss([0.8,0.5])))
print("LeeModel:{}".format(m3.pathloss([0.8,0.5])))
print("EricssonModel:{}".format(m4.pathloss([0.8,0.5])))
print("Cost231Model:{}".format(m5.pathloss([0.8,0.5])))
print("Cost231HataModel:{}".format(m6.pathloss([0.8,0.5])))
print("OkumuraHataModel:{}".format(m7.pathloss([0.8,0.5])))
print("Ecc33Model:{}".format(m8.pathloss([0.8,0.5])))
print("SuiModel:{}".format(m9.pathloss([0.8,0.5])))
#GeoUtils.teste()
lat1 =[41.49008,41.49008,41.49008,41.49008]
lon1=[-71.312796,-71.312796,-71.312796,-71.312796]
lat2 =[41.499498,41.499498,41.499498,41.499498]
lon2 =[-81.695391,-81.695391,-81.695391,-81.695391]
r = GeoUtils.distanceInKm(-8.055741, -34.951575,-8.052032, -34.951791)
a = GeoUtils.AzimuthAtoB(-8.055741, -34.951575,-8.052032, -34.951791)

r_m = GeoUtils.distanceInKm(-8.055741, -34.951575,[-8.053195,-8.055292,-8.057730], [-34.951778,-34.948435,-34.951484])
a_m = GeoUtils.AzimuthAtoB(-8.055741, -34.951575,[-8.053195,-8.055292,-8.057730], [-34.951778,-34.948435,-34.951484])

print(r)
 



