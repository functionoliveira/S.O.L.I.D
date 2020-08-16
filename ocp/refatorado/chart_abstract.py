from abc import ABC, abstractmethod

class Chart:

    def __init__(self):
        super().__init__()

    @abstractmethod
    def check_data_is_valid(data):
        print("Os dados sao validos para o grafico!")
        return True
    
    @abstractmethod
    def render(data):
        print("Desenhar grafico", data)