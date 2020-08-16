class PieChart:
    def __init__(self, data):
        self.data = data

    def check_data_is_valid(self):
        print("Os dados sao validos para o grafico torta!")
        return True

    def render_pie_chart(self):
        print("Desenhar grafico torta com %s" % self.data)