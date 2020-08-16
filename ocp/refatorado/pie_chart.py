from .chart_abstract import Chart

class PieChart(Chart):
    def check_data_is_valid(self, data):
        print("Os dados sao validos para o grafico torta!")
        return True

    def render(self, data):
        print("Desenhar grafico torta com %s" % data)