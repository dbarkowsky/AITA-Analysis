import pygal
from pygal.style import LightSolarizedStyle


class ChartBuilder:
    @staticmethod
    def pyramid(
        *,
        chart_title,
        series_titles,
        series_data,
        y_title,
        style=LightSolarizedStyle,
        x_labels=None,
    ):
        pyramid_chart = pygal.Pyramid(
            human_readable=True, legend_at_bottom=True, style=style
        )
        pyramid_chart.title = chart_title
        pyramid_chart.y_title = y_title
        if x_labels != None:
            pyramid_chart.x_labels = x_labels
        # pyramid_chart.show_x_labels = False
        for title, data in zip(series_titles, series_data):
            pyramid_chart.add(title, data)
        pyramid_chart.render_to_file(
            f"charts/pyramid_{str(chart_title).replace(' ', '')}.svg"
        )

    @staticmethod
    def horizontal_bar(
        *, chart_title, series_titles, series_data, style=LightSolarizedStyle
    ):
        horz_bar = pygal.HorizontalBar(
            human_readable=True,
            style=style,
            print_values=True,
            print_labels=True,
            show_legend=False,
        )
        horz_bar.title = chart_title
        for title, data in zip(series_titles, series_data):
            horz_bar.add(title, [{"value": data, "label": title}])
        horz_bar.render_to_file(
            f"charts/horizontal_bar_{str(chart_title).replace(' ', '')}.svg"
        )

    @staticmethod
    def bar(
        *,
        chart_title,
        series_titles,
        series_data,
        style=LightSolarizedStyle,
        x_labels=None,
    ):
        bar = pygal.Bar(
            title=chart_title,
            human_readable=True,
            style=style,
            legend_at_bottom=True,
            legend_at_bottom_columns=4,
        )
        if x_labels != None:
            bar.x_labels = x_labels
        for title, data in zip(series_titles, series_data):
            bar.add(title, data)
        bar.render_to_file(f"charts/bar_{str(chart_title).replace(' ', '')}.svg")

    @staticmethod
    def stacked_bar(
        *,
        chart_title,
        series_titles,
        series_data,
        style=LightSolarizedStyle,
        x_labels=None,
    ):
        bar = pygal.StackedBar(
            title=chart_title,
            human_readable=True,
            style=style,
            legend_at_bottom=True,
            legend_at_bottom_columns=4,
        )
        if x_labels != None:
            bar.x_labels = x_labels
        for title, data in zip(series_titles, series_data):
            bar.add(title, data)
        bar.render_to_file(
            f"charts/stacked_bar_{str(chart_title).replace(' ', '')}.svg"
        )

    @staticmethod
    def scatterplot(
        *,
        chart_title,
        series_titles,
        series_data,
        style=LightSolarizedStyle,
        x_title=None,
    ):
        scatter = pygal.XY(
            stroke=False, title=chart_title, style=style, legend_at_bottom=True
        )
        scatter.title = chart_title
        if x_title != None:
            scatter.x_title = x_title
        for title, data in zip(series_titles, series_data):
            scatter.add(title, data)
        scatter.render_to_file(
            f"charts/scatterplot_{str(chart_title).replace(' ', '')}.svg"
        )

    @staticmethod
    def line(
        *,
        chart_title,
        series_titles,
        series_data,
        style=LightSolarizedStyle,
        x_labels=None,
    ):
        line = pygal.Line(title=chart_title, style=style, legend_at_bottom=True)
        line.title = chart_title
        if x_labels != None:
            line.x_labels = x_labels
        for title, data in zip(series_titles, series_data):
            line.add(title, data)
        line.render_to_file(f"charts/line_{str(chart_title).replace(' ', '')}.svg")
