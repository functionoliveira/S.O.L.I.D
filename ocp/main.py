from charts import Chart, ChartTypes

chart_instance = Chart()

chart_instance.render(ChartTypes.COLUMN_CHART, "dados para grafico coluna")
chart_instance.render(ChartTypes.LINE_CHART, "dados para grafico linha")
chart_instance.render(ChartTypes.PIE_CHART, "dados para grafico torta")

print("\n\n\nAplicando OCP\n")
from refatorado import ChartOC, ColumnChart, LineChart, PieChart

instance_column_chart = ColumnChart()
instance_line_chart = LineChart()
instance_pie_chart = PieChart()

ChartOC.render(instance_column_chart, "dados para grafico coluna")
ChartOC.render(instance_line_chart, "dados para grafico linha")
ChartOC.render(instance_pie_chart, "dados para grafico torta")