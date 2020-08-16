from .chart_abstract import Chart

class ColumnChart(Chart):
    def check_data_is_valid(self, data):
        print("Os dados sao validos para o grafico coluna!")
        return True

    def render(self, data):
        print("Desenhar grafico coluna com %s" % data)