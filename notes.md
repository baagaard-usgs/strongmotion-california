# Dataset alternatives

## Dataset 1

* Raw waveforms from CESMD, SCEDC, NCEDC
* Use metadata from NGA West2 if available (Mw, Vs30, Z1.0, Z1.5)
* Metadata from COMCAT: origin time, lon/lat/depth, Mw, description, catalog

* Earthquakes
  * Pre-1999 (list from NGA with 4+ records and in COMCAT)
  * 1999+
    * within 4 deg of LA or SF
    * latitude > 32.00 degrees
    * only CI and NC events
    * must be moment magnitude

## Dataset 2

* Waveforms from NGA West2

# Flatfiles

## Earthquakes

## Stations

## Records

# Data Collection

1. Get earthquake catalogs from COMCAT

  * pre1999: list
  * 1999+ search
    * associate with NGA

2. Tabulate earthquakes into flatfile
