import plotly.graph_objects as go
import numpy as np

delta = 0.2

fig = go.Figure(data=[
    go.Mesh3d(
        # 8 vertices of a cube
        x=[0, 0, 1, 1, 0, 0, 1, 1],
        y=[0, 1, 1, 0, 0, 1, 1, 0],
        z=[0, 0, 0, 0, 1, 1, 1, 1],
        # Intensity of each vertex, which will be interpolated and color-coded
        i = [7, 0, 0, 0, 4, 4, 6, 1, 4, 0, 3, 6],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k =[0, 7, 2, 3, 6, 7, 1, 6, 5, 5, 7, 2],
        name='y',
        #showscale=True,
        opacity=0.4
    ),
    go.Mesh3d(
        # 8 vertices of a cube
        x=[  0,   0,   1,   1,   0,   0,   1,   1],
        y=[0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
        z=[  0,   0,   0,   0,   1,   1,   1,   1],
        # Intensity of each vertex, which will be interpolated and color-coded
        i = [7, 0, 0, 0, 4, 4, 6, 1, 4, 0, 3, 6],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k =[0, 7, 2, 3, 6, 7, 1, 6, 5, 5, 7, 2],
        name='y',
        #showscale=True,
        opacity=0.2
    ),
    go.Mesh3d(
        # 8 vertices of a cube
        x=[0.8 - delta, 0.8- delta,   1- delta,   1- delta, 0.8- delta, 0.8- delta,   1- delta,   1- delta],
        y=[0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
        z=[0.8- delta, 0.8- delta, 0.8- delta, 0.8- delta,   1- delta,   1- delta,   1- delta,   1- delta],
        # Intensity of each vertex, which will be interpolated and color-coded
        i = [7, 0, 0, 0, 4, 4, 6, 1, 4, 0, 3, 6],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k =[0, 7, 2, 3, 6, 7, 1, 6, 5, 5, 7, 2],
        name='y',
        #showscale=True,
        opacity=0.2
    )
])
fig.show()
