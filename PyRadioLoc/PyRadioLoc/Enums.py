from enum import Enum
from collections import namedtuple
class LeeAreaType(Enum):
    """description of class"""
    FreeSpace = (2.0,5.0),
    OpenArea = (4.35,49),
    SubUrban = (3.84,61.7),
    Philadelphia=(3.68,70.0),
    Newark=(4.31, 64),
    Tokyo=(3.05, 84.0),
    NewYorkCity=(4.80,77.0)

class AreaKind(Enum):
    Rural = 1,
    Suburban = 2,
    Urban = 3
class CityKind(Enum):
    Small = 1,
    Medium = 2,
    Large = 3

class TerrainKind(Enum):
    A = 1, # hilly terrain with moderate-to-heavy tree densities
    B = 2, # hilly environment but rare vegetation, or high vegetation but flat terrain
    C = 3  # mostly flat terrain with light tree densities
