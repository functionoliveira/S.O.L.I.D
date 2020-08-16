class LineChart:
    def __init__(self, data):
        self.data = data

    def check_data_is_valid(self):
        print("Os dados sao validos para o grafico linha!")
        return True

    def render_line_chart(self):
        print("Desenhar grafico linha com %s" % self.data)