import numpy as np
from geographiclib.geodesic import Geodesic,Math
class GeoUtils(object):
    """description of class"""
    
    @staticmethod
    def distanceGeoLibArr(lat1,lon1,lat2,lon2,extract):
        if (np.isscalar(lat1) and np.isscalar(lat2)):
            return GeoUtils.distanceGeoLib(lat1,lon1,lat2,lon2,extract)
        elif (np.isscalar(lat1) and (not np.isscalar(lat2))):
            resp=[]
            for i in range(len(lat2)):
                r = GeoUtils.distanceGeoLib(lat1,lon1,lat2[i],lon2[i],extract)
                resp.append(r)
            return resp
        elif (not np.isscalar(lat1) and (not np.isscalar(lat2))):
            resp=[]
            for i in range(len(lat1)):
                r = GeoUtils.distanceGeoLib(lat1[i],lon1[i],lat2[i],lon2[i],extract)
                resp.append(r)
            return resp
    @staticmethod
    def distanceGeoLib(lat1,lon1,lat2,lon2,extract):
        MASK=Geodesic.DISTANCE|Geodesic.AZIMUTH|Geodesic.REDUCEDLENGTH
        gab=Geodesic.WGS84.Inverse(lat1,lon1,lat2,lon2,MASK)
        resp = extract(gab)
        return resp

    @staticmethod
    def distanceInKm(lat1,lon1,lat2,lon2):
       return GeoUtils.distanceGeoLibArr(lat1,lon1,lat2,lon2,lambda g:g['s12']/1000)

    @staticmethod
    def AzimuthAtoB(lata,lona,latb,lonb):
       return GeoUtils.distanceGeoLibArr(lata,lona,latb,lonb,lambda g:g['azi1'])
    
    