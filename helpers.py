import pandas as pd
import numpy as np
from tqdm import tqdm
import plotly.graph_objects as go


from constants import *

def syncrhonize_data(X:pd.DataFrame, key_column:str, columns_to_sync:list) -> pd.DataFrame:
    """Ensures that each instance of a unique value in the key_column has the same values in the corresponding
        columns_to_sync

    Args:
        X (pd.DataFrame): DataFrame to clean
        key_column (str): Name of column used to sync columns to
        columns_to_sync (list): Columns to sync to the key_column

    Returns:
        pd.DataFrame: DataFrame with synchronized values.
    """
    X = X.copy()
    for key in tqdm(X[key_column].unique()):
        if not key in VALUE_EXCEPTIONS:        
            for column in columns_to_sync:        
                row_filter = X[key_column] == key
                mode =  X[row_filter][column].mode()
                if len(mode) > 0:
                    X.loc[row_filter, column] = mode[0] 
                else:
                    X.loc[row_filter, column] = np.nan 
    return X

def make_unique(X:pd.DataFrame, key_column:str, values_to_split:list, columns_to_match:list) -> pd.DataFrame:
    """Renames each instance of the values_to_split found in the key_column so that is unique and grouped by
    the values in columns_to_match.

    Args:
        X (pd.DataFrame): DataFrame to clean
        key_column (str): Name of column where values_to_split are found
        values_to_split (list): List of values to make unique
        columns_to_match (list): _List of columns to use as a reference when grouping the values to be split

    Returns:
        pd.DataFrame: Dataframe with values made unique
    """
    X = X.copy()
    for value in values_to_split:
        groups = X.loc[X[key_column]==value][columns_to_match[0]].astype(str)
        for c in columns_to_match[1:]:
            groups += X[c].astype(str)
        for i, g in enumerate(groups.unique()):
            row_filter = (X[key_column] == value) & (groups == g)
            X.loc[row_filter, key_column] = f'{value}_{i}'    
    return X

def assign_lat_long(X:pd.DataFrame, city:str, lat:float, long:float) -> pd.DataFrame:
    """assigns latitude and longitude to samples with the given city
    """
    X = X.copy()
    X.loc[X['artist_home_city'] == city, 'artist_home_latitude'] = lat
    X.loc[X['artist_home_city'] == city, 'artist_home_longitude'] = long
    return X

def haversine(lat1, lon1, lat2, lon2, to_radians=True, earth_radius=6371):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees or in radians)

    All (lat, lon) coordinates must have numeric dtypes and be of equal length.
    FROM: https://stackoverflow.com/questions/43577086/
    """
    if to_radians:
        lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    a = np.sin((lat2-lat1)/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2-lon1)/2.0)**2

    return earth_radius * 2 * np.arcsin(np.sqrt(a))



def chart_grouped_categorical_comparison(
                                            groupby:pd.Series, 
                                            to_compare:pd.Series, 
                                            groups:list=None, 
                                            categories:list=None, 
                                            color_dict:dict=None, 
                                            chart_width=1200,
                                            chart_height=600
                                            
                                        ) -> None:
    
    traces = []
    if categories is None:
        categories = to_compare.unique()
    if groups is None:
        groups = groupby.unique()
    for id in groups:
        values = []
        for x in categories:
            value_count = (to_compare.loc[groupby == id] == x).value_counts(normalize=True)
            if False in value_count.index:
                values.append(1- value_count[False])
            else:
                values.append(0)
           
        new_trace = go.Bar( 
                            name = id, 
                            x = categories, 
                            y = values,
                            # marker_color = COLOR_DICT[id]
                            )
        if not color_dict is None:
            if id in color_dict.keys():
                new_trace.update({'marker_color':color_dict[id]})
                
        traces.append(new_trace)
    
    averages = []
    for y, _ in enumerate(categories):
        value = np.mean([traces[id]['y'][y] for id in range(len(traces))])
        new_trace = go.Scatter(  
                            name = f'{_}_average',
                            mode = 'lines',
                            x = (y,y+1),
                            y = (value,value),
                            marker_color = '#303030',
                            showlegend=False,
                            xaxis='x2'
                            )
        
        averages.append(new_trace)
        
        
    fig = go.Figure()
    fig.add_traces(traces + averages)
    
    t1 = to_compare.name.replace('_',' ').capitalize()
    t2 = groupby.name.replace('_',' ')
    fig.update_layout(      
                            width= chart_width, 
                            height= chart_height,
                            plot_bgcolor= 'white', 
                            title = f'{t1} grouped by {t2}.',
                            barmode = 'group',
                            font=dict( size= 16)
                    )
    fig.update_yaxes(       
                            dtick=0.1,    
                            tickformat= '.0%',
                            range= [0,1], 
                            gridcolor='lightgray'
                    )               
    fig.layout.xaxis2 = go.layout.XAxis(
                                        overlaying='x',
                                        range=[0, len(categories)],
                                        showticklabels=False
                                        )
    fig.show()