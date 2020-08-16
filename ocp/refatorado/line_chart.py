from .chart_abstract import Chart

class LineChart(Chart):
    def check_data_is_valid(self, data):
        print("Os dados sao validos para o grafico linha!")
        return True

    def render(self, data):
        print("Desenhar grafico linha com %s" % data)