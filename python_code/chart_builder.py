import pygal
from pygal.style import LightSolarizedStyle


class ChartBuilder:
    @staticmethod
    def pyramid(*, chart_title, series_titles, series_data, style=LightSolarizedStyle):
        pyramid_chart = pygal.Pyramid(
            human_readable=True, legend_at_bottom=True, style=style
        )
        pyramid_chart.title = chart_title
        for title, data in zip(series_titles, series_data):
            pyramid_chart.add(title, data)
        pyramid_chart.render_to_file(f"charts/{str(chart_title).replace(' ', '')}.svg")

    @staticmethod
    def horizontal_bar(
        *, chart_title, series_titles, series_data, style=LightSolarizedStyle
    ):
        horz_bar = pygal.HorizontalBar(human_readable=True, style=style)
        horz_bar.title = chart_title
        for title, data in zip(series_titles, series_data):
            horz_bar.add(title, data)
        horz_bar.render_to_file(f"charts/{str(chart_title).replace(' ', '')}.svg")

    @staticmethod
    def bar(*, chart_title, series_titles, series_data, style=LightSolarizedStyle):
        bar = pygal.Bar(
            title=chart_title,
            human_readable=True,
            style=style,
            legend_at_bottom=True,
            legend_at_bottom_columns=4,
        )
        for title, data in zip(series_titles, series_data):
            bar.add(title, data)
        bar.render_to_file(f"charts/{str(chart_title).replace(' ', '')}.svg")
