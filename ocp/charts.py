from enum import Enum
from column_chart import ColumnChart
from line_chart import LineChart
from pie_chart import PieChart

class ChartTypes(Enum):
    COLUMN_CHART = 1
    PIE_CHART = 2
    LINE_CHART = 3

class Chart:
    def render(self, type, data):
        if type == ChartTypes.COLUMN_CHART:
            instance = ColumnChart(data)
            if instance.check_data_is_valid(): 
                instance.render_column_chart()
        elif type == ChartTypes.PIE_CHART:
            instance = PieChart(data)
            if instance.check_data_is_valid(): 
                instance.render_pie_chart()
        elif type == ChartTypes.LINE_CHART:
            instance = LineChart(data)
            if instance.check_data_is_valid(): 
                instance.render_line_chart()
        else:
            print("Tipo de grafico invalido")
