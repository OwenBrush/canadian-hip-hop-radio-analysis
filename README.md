# canadian-hip-hop-radio-analysis


### Goal:
- Analyze data for complex correlational insights
- Visualize the data to support a written thesis


### Data Cleaning Documentation:

- Strings
  - remove extra whitespaces
  - convert to lower cases
  - convert empty strings and '-' and '?' values to null
 
- Date Times:
  - convert ''3/2/1010' dates to '2010-03-02' (After inspecting the dataset, this appears to be a missing week)

- Station Data
  -  null values are matched to existing information for given station

- Clean Artist data
  - 1 record with no artist data is removed
  - 29 instances of artists named 'various' are grouped by shared lattitude/longitude and given unique names (various_1, various_2, etc)
  - 1478 instances of artists name 'various' do not have lattitude/longitude information
    - TODO: consider filling in lattitude/longitude based on country or city information where possible
    - these artists will be excluded from geographic visualization but included in statistical data
  - 13 artists with more than one lattitude/longitude are fixed to only have 1
    - artist names: birdman, rhymekeepers, john smith, m.i.a., the dirty sample, j57, justin bieber, roots manuva meets wrongtom, alias and tarsier, d-sisive, ghostface killah, bobby digital (rza), rick ross 
    - most appear to be the result of typos or small decimal differences, where multiple distinct locations exist the one with the most entries is chosen.
  - null values are matched to existing information for given artist
  - 3 named artists with missing lattitude/longitude are given that information based on city data
    - Geckoturner-> Madrid
    - Nas & Damian Marley -> New York
    - Non + Herrmutt Lobby -> Los Angeles
  - 1 instance of 'e' in the language of music column is replaced with 'english'

  - remaining null values in the MAPL columns are replaced with 'no'
  - any remaining null values in artist related columns are replaced with 'unknown'

- Album data
  - null values are matched to existing information for given album
  -  



