STATION_COLUMNS = ['station_city',
                   'station_province',
                   'station_latitude',
                   'station_longitude']
ARTIST_COLUMNS = ['artist_country',
                  'artist_home_city',
                  'artist_home_latitude',
                  'artist_home_longitude',
                  'visible_ethnic_minority',
                  'census_race_classification', 
                  'artist_gender', 
                  'm_music', 
                  'a_artist',
                  'p_performance', 
                  'l_lyrics']
ALBUM_COLUMNS = ['label_name', 
                  'label_type',
                  'language_of_music']
PLACEHOLDERS = ['', '-', '?']  #Strings used to show null values in data
VALUE_EXCEPTIONS = ['unknown','various']  #Unspecified artists, or albums that should not be grouped together