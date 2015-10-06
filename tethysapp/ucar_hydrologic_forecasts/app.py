from tethys_sdk.base import TethysAppBase, url_map_maker


class UcarHydrologicForecasts(TethysAppBase):
    """
    Tethys app class for UCAR Hydrologic Forecasts.
    """

    name = 'UCAR Hydrologic Forecasts'
    index = 'ucar_hydrologic_forecasts:home'
    icon = 'ucar_hydrologic_forecasts/images/icon.png'
    package = 'ucar_hydrologic_forecasts'
    root_url = 'ucar-hydrologic-forecasts'
    color = '#1A334C'
        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='ucar-hydrologic-forecasts',
                           controller='ucar_hydrologic_forecasts.controllers.home'),
        )

        return url_maps