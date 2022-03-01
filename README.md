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
  - remaining null values in the MAPL columns are replaced with 'no'
  - any remaining null values in artist related columns are replaced with 'unknown'

- Album data
  - null values are matched to existing information by album name
  - in language of music column
    - replace 'e' with 'english'
    - replace 'yes' with 'other'
 
- Label data
  -  null values are matched to existing information by label name

- Chart Position
  - NOTE: Distribution of chart positions is almost exactly equal:
    - 1   =   3561
    - 2   =   3586
    - 3   =   3586
    - 4   =   3585
    - 5   =   3586
    - 6   =   3586
    - 7   =   3586
    - 8   =   3586
    - 9   =   3586
    - 10  =   3585
    - NaN =     25
  - 25 null chart positions are filled with the average chart position of the given artist.
    - artist names (1 missing value each): psyche origami, aceyalone, dilated peoples, jay bizzy, ok cobra, iam, pharoahe monch, jesse dangerously, othello, cadence weapon, guilty simpson, atmosphere, invincible, j'davey, factor, art of fresh, josh martinez, art of fresh, ghettosocks, p.o.s., k'naan, le klub des 7, various_19, the roots, dj brace

- Artist Distance
  - recalculate the haversine distance between station and artist for every record 

- Add Canadian content
  - rename MAPL columns 
  - add new column 'CANADIAN CONTENT' 
    - 2 or more MAPL = 'yes'
    - less than 2 MAPL = 'no'

