class ChartOC:

    @staticmethod
    def render(chart, data):
        if chart.check_data_is_valid(data):
            chart.render(data)