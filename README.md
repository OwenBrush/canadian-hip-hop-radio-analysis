# canadian-hip-hop-radio-analysis

## Outline

- This data was originally prepared to support a doctoral thesis by Deepak Mehmi
- I have created visualizations of the data in order to draw out insights based on the demographic qualities of artists and stations 


## Distribution and characteristic of data:

![Distribution of plays by station](/images/plays_by_station.png)

- #### Records of songs played at a given station are collected on a weekly basis, 10 at a time. (from a single radio show at that station)
- #### The frequency of the records vary greatly from station to station

![Distribution of plays by chart position](/images/plays_by_chart_position.png)

- #### Each selection of 10 songs from a radio station includes 1 song from each chart position
- #### April and May generally have better reporting
- #### There is rarely data from the holiday period at the end of december

![Distribution of plays by province](/images/plays_by_province.png)

- #### The data is heavily weighted towards Ontario
- #### Data from stations inNew Brunswick and Nova Scotia are mostly absent for the second half of the time period

## Insights:

![Distribution of gender by nationalitt](/images/chart_artist_gender_by_nationality.png)

- #### There is a signifigantly larger proportion of female artists from the UK than amongst other nationalities.

![Distribution of race by province](/images/chart_bipoc_by_province.png)

- #### Nova Scotia plays a signifigantly larger proportion of white artists.

![Distribution of canadian content by province](/images/chart_cancon_by_province.png)

- #### Nova Scotia also plays a signifigantly larger proportion of Canadian Artists.

![Distribution of race by nationality](/images/chart_station_plays_nationality.png)

- #### There is a signifigantly larger proportion of black artists from the USA than amongst other nationalities
- #### There is a signifigantly larger proportion of ethnically asian or middle eastern artists from the UK or internationally than from USA or Canada

![Correlation of artist data](/images/correlation_artist.png)

- #### There is a moderate negative correlation between artists qualifying as Canadian Content and belonging to a visable ethnic minority, meaning that Canadian artists within the dataset are more likely to be white.
- #### There is a light positive correlation between Canadian Content and total plays, meaning that Canadian artists tend to get played more often.

![Correlation of station data](/images/correlation_station.png)

- #### There is a strong negative correlation between Canadian Content and visable ethnic minority when it comes to songs getting air time, and it is worth noting that it is roughly twice as strong as the correlation that exists within the artist demographics, suggesting that there is a bias at the station level. (Nova Scotia is not a large enough factor in the data set to signifigantly influence the strength of this correlation)
- #### There is a strong positive correlation between the population of the station's city and the number of BIPOC artists that get played, meaning that stations in larger cities play more BIPOC artists.
- #### There is a moderate positive correlation between total plays and male artists, meaning that male artists get played more often.
- #### There is a moderate positive correlation between total plays and english songs, meaning that english songs get played more often.
- #### There is a moderate negative correlation between BIPOC artists and Male artists, meaning that the proportion of male artists is smaller within the selection of BIPOC artists.


![Comparison of BIPOC and can con](/images/bipoc_over_time.png)
- #### Looking at the data as a time series, a trend can be seen where Canadian Content is getting played more and BIPOC artists are getting played less over time.


## Tableau Dashboard for visualizing geographic distribution:

https://public.tableau.com/app/profile/owen6164/viz/CanadianRapBroadcasting/Dashboard


## Conclusions:

- Given the small size and inconsistent frequency of the sampling, as well as the equal distribution of chart positions, this data is not neccesarily reflective of day to day airtime that artists are getting at these radio stations.
- There appears to be less BIPOC Canadian artists compared to artists of other nationalities. Whether this is in part a result of the demographic make up of artists in Canada is not clear from this data, but it is clear that it is atleast in part a result of the programming decisions of radio stations.
- It also seems to be clear that this bias is closely connected to Canadian Content, as shown by the negative correlation that exists between cancon and BIPOC artists getting air time, when it should in theory be possible to increase Canadian Content without decreesing the number of bipoc artists geting air time.
- This begs the question:  **When asked to play canadian content, do programmers unconsciously choose white artists more frequently than they otherwise would?**

