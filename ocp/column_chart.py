class ColumnChart:
    def __init__(self, data):
        self.data = data

    def check_data_is_valid(self):
        print("Os dados sao validos para o grafico coluna!")
        return True

    def render_column_chart(self):
       print("Desenhar grafico coluna com %s" % self.data) 