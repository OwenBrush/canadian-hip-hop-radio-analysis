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
    - switched name of remaining 'various' artists to 'unkown'
  - 13 artists with more than one lattitude/longitude are fixed to only have 1
    - artist names: birdman, rhymekeepers, john smith, m.i.a., the dirty sample, j57, justin bieber, roots manuva meets wrongtom, alias and tarsier, d-sisive, ghostface killah, bobby digital (rza), rick ross 
    - most appear to be the result of typos or small decimal differences, where multiple distinct locations exist the one with the most entries is chosen.
  - null values are matched to existing information for given artist
  - remaining null values in the MAPL columns are replaced with 'no'
  - demographic classification consolodated into fewer options
    - ARTIST GENDER
      - 'female group' -> 'female' (97 instances)
      - 'male group' -> 'male' (11756 instances)
    - VISIBLE ETHNIC MINORITY
      - 'black' -> 'yes'  (1 instance)
    - CENSUS RACE CLASSIFICATION
      - 'asian other','other asian', 'east asian' -> 'asian'
      - 'asian indian','indian asian' -> 'indian'
      - 'native canadian' -> 'native american' (159 instances)
      - 'inuit' -> 'native american' (19 instances)
      - 'metis' -> 'native american' (7 instances)
      
  - any remaining null values in artist related columns are replaced with 'unknown'
  - filled in missing latitude / longitude data by matching to city name
    - also matched all latitude / longitude to city names, so there is only one set per city 
  - 1771 records between 45 different named artists and various unknown artists remain without lat / long or city information
    - names of artists without this information: 'dreddy kruger', '12seven', 'e.v.o', 'prz', 'con quest', 'existero and barfly', 'janelle', 'versus', 'lyric 1', 'the champions', 'rapscallion', 'reality sandwich', 'deepspace 5', 'free thinkers society', 'silk fire', 'awol one, josh martinez & moves', 'similar differences', 'c.e.o.', 'life sentences', 'shalom & moziz', 'c-k', 'teargas & plateglass', terrill jerome cook', 'felony', 'beware of dear', 'flex', 'assholes & whitties', 'pryde messiah', 'longstory', 'grown man bidness', 'tag digs', 'flo flo', 'taalam acey', 'swiss', 'two fingers', 'booker t.', "str8 trippin'", 'soul assassins', 'martin cradick & the baka at gbine', 'the slew', 'young money', 'price', 'radar', 'choicemakerz', 'tree'

- Album data
  - null values are matched to existing information by album name
  - in language of music column
    - replace 'e' with 'english'
    - replace 'yes' with 'other'
    - replace null with 'unknown'
 
- Label data
  -  null values are matched to existing information by label name
  -  5 labels are missing types, replaced with 'unknown'
     - Label names: 'hr', 'carhartt/because', 'homegrown inc.', 'the hip hop company',
       'word supremacy press'  

- Chart Position
  - 25 null chart positions are filled with the average chart position of the given artist.
    - artist names (1 missing value each): psyche origami, aceyalone, dilated peoples, jay bizzy, ok cobra, iam, pharoahe monch, jesse dangerously, othello, cadence weapon, guilty simpson, atmosphere, invincible, j'davey, factor, art of fresh, josh martinez, art of fresh, ghettosocks, p.o.s., k'naan, le klub des 7, various_19, the roots, dj brace

- Artist Distance
  - recalculate the haversine distance between station and artist for every record 

- Add Canadian content
  - rename MAPL columns 
  - add new column 'CANADIAN CONTENT' 
    - 2 or more MAPL = 'yes'
    - less than 2 MAPL = 'no'
    
- TODO:
  - account for demographic information of unknown artists instead of grouping them all together with the most common freatures


### Notes about data:

- Distribution of chart positions is precisely equal (Should null values be changed to 1 to fit this pattern?):
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

- Artists are almsot never played more than once per week at any given station
- There is a relatively small sampling size of artists played for a weeklong period at any given station.

### Thoughts about data:

- The distribution of chart positions indicate that this data is not randomly sampled and the demographic information it holds can't be assumed to be representive of real world trends in broadcasting unless, perhaps, a single chart position is isolated and looked at individually.

- The lack of any artists being played more than once per week per station also seems unlikely to be the result of random sampling.  It could be a result of the small sampling size on a per week per station basis but is worth questioning whether the data has been filtered in this regard aswell.

- Given the small sampling size of data on the per week / per station level, even if it is randomly sampled it still is not enough data to give an accurate impression of what is being played when looking at only a single station on a single week.
