# Dataset alternatives

## Dataset 1

* Raw waveforms from CESMD, SCEDC, NCEDC
* Use metadata from NGA West2 if available (Mw, Vs30, Z1.0, Z1.5)
* Metadata from COMCAT: origin time, lon/lat/depth, Mw (prefer over NGA), description, catalog

* Earthquakes
  * Pre-1999 (list from NGA with 4+ records and in COMCAT)
  * 1999+
    * within 4 deg of LA or SF
    * latitude > 32.00 degrees
    * only CI and NC events
    * must be moment magnitude

## Dataset 2

* Waveforms from NGA West2

# Metadata (flat) files

## Earthquakes

* COMCAT id
* CESMD id
* NGA West2 id
* Origin Time
* Moment Magnitude
* Longitude
* Latitude
* Depth
* Strike
* Dip
* Rake
* Min. Depth
* Catalog
* Description

## Stations

* Network.StationCode
* Name
* Longitude
* Latitude
* Elevation
* Channels
* Locataion Code
* Data Source (CESMD, SCEDC, NCEDC, IRIS)
* NGA id
* Vs30
* Vs30 Source
* Z1.0
* Z1.0 Source
* Z2.5
* Z2.5 Source

## Records

* Network.StationCode
* COMCAT id
* NGA West2 RSN
* Source [NGAWest2, CESMD, SCEDC, NCEDC, IRIS]

# Data files

Store waveforms in HDF5 files

COMCAT id / Network.StationCode / Dataset

* Datasets
  * acc (unprocessed and processed)
  * vel (processed only)
  * disp (processed only)
* Station attributes
  * toffset (from origin time)
  * azimuth0 (azimuth of component 0)
  * azimuth1 (azimuth of component 1)


# Data Collection

1. Get earthquake catalog from COMCAT

./collect --fetch-earthquakes

  * pre1999: list
  * 1999+ search COMCAT
      * Within 4 degrees of LA or SF
      * Since Jan 1, 19999
	  * Magnitude > 4
	  * Only CI and NC events
	  * Latitude > 32.00 degrees
    * Remove duplicates
    * associate with NGA

2. Tabulate earthquakes into flatfile

./collect --tabulate-earthquakes

Read XML files and tabulate

3. Fetch raw records from CESMD for pre-1999 earthquakes

./collect --fetch-waveforms-cesmd

Read list, construct URL, save zip file.

4. Read CESMD records and associate with NGA records

./collect --load-waveforms-cesmd

* Read records
* Associate with NGA records
* Save into HDF5

5. Fetch records from SCEDC, NCEDC, IRIS

./collect --fetch-stations-fdsn
./collect --fetch-waveforms-fdsn
./collect --load-waveforms-fdsn

* Fetch stations
 * HL?,HN? channels
 * start before origin time
	* end after origin time
	* Ignore structures
	* Select channels with maximum elevation (minimum depth) and
   maximum sampling rate
 * Ignore duplicates
* Fetch records
* Associate with NGA records
* Save into HDF5

# Data processing

./collect --process-waveforms

* Remove noise
* Baseline correction

# Plotting

* Earthquakes (circle, marker size by magnitude, color by number of records)
* Stations (triangle, color by number of records)
* Stations for each earthquake
* Records for each earthquake
  + Record section (R,T,Z)
  + Magnitude versus distance
  + Amplitude (PGA, PGV, PGD?, etc versus distance)

