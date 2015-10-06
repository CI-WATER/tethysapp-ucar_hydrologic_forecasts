from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tethys_sdk.gizmos import MapView, MVDraw, MVView, MVLayer, MVLegendClass

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    # Define view options
    view_options = MVView(
        projection='EPSG:4326',
        center=[-60, 40],
        zoom=3.5,
        maxZoom=18,
        minZoom=2
    )

    map_view_options = MapView(
        height='100%',
        # height='619px',
        width='100%',
        controls=['ZoomSlider', 'Rotate', 'FullScreen',
                  {'MousePosition': {'projection': 'EPSG:4326'}},
                  {'ZoomToExtent': {'projection': 'EPSG:4326', 'extent': [-130, 22, -10, 54]}}],
        layers=[],
        view=view_options,
        basemap='OpenStreetMap',
        draw=None,
        legend=True
)


    context = {'map_view_options': map_view_options}

    return render(request, 'ucar_hydrologic_forecasts/home.html', context)