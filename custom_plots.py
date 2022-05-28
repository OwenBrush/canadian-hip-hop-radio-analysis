import plotly.graph_objects as go
import pandas as pd
import numpy as np

DEFAULT_COLOR_SCALE =   [
                        [0.0, "#84145C"],
                        [0.5, "rgb(255,255,255)"],
                        [1.0, "#276B36"]
                        ]

def plot_categorical_comparison(
                                            categories:pd.Series, 
                                            compare_by:pd.Series, 
                                            category_filter:list=None, 
                                            comparison_filter:list=None, 
                                            color_dict:dict=None, 
                                            chart_width=1200,
                                            chart_height=600
                                        ):
    
    title_string_1 = categories.name.replace('_',' ')
    title_string_2 = compare_by.name.replace('_',' ')
    category_filter = categories.unique() if category_filter is None else category_filter
    comparison_filter = compare_by.unique() if comparison_filter is None else comparison_filter

    traces = []
    for id in comparison_filter:
        values = []
        for x in category_filter:
            value_count = (categories.loc[compare_by == id] == x).value_counts(normalize=True)
            if False in value_count.index:
                values.append(1- value_count[False])
            else:
                values.append(0)  
        new_trace = go.Bar( 
                            name = id, 
                            x = category_filter, 
                            y = values,
                            )
        if not color_dict is None:
            if id in color_dict.keys():
                new_trace.update({'marker_color':color_dict[id]})        
        traces.append(new_trace)
    
    averages = []
    for y, x in enumerate(category_filter):
        value = np.mean([traces[id]['y'][y] for id in range(len(traces))])
        new_trace = go.Scatter(  
                            name = f'{x}_average',
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
    
    fig.update_layout(      
                            width= chart_width, 
                            height= chart_height,
                            plot_bgcolor= 'white', 
                            title = f'Distribution of {title_string_1} by {title_string_2}.',
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
                                        range=[0, len(category_filter)],
                                        showticklabels=False
                                        )
    fig.show()


def plot_correlation_matrix(df:pd.DataFrame, color_scale=DEFAULT_COLOR_SCALE):
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    df_mask = corr.mask(mask)

    fig = go.Figure()

    trace = go.Heatmap(
                        z=df_mask.to_numpy(), 
                        x=df_mask.columns.tolist(),
                        y=df_mask.columns.tolist(),
                        zmin=-1,
                        zmax=1,
                        colorscale= color_scale
                        )
    fig.add_trace(trace)
    axis_template = dict(showgrid = False, zeroline = False)    
    fig.update_layout(
        title_text='Heatmap', 
        title_x=0.5, 
        width=1000, 
        height=1000,
        yaxis = axis_template,
        xaxis = axis_template,
        yaxis_autorange = 'reversed',
        template='plotly_white'
    )
    fig.show()