# test_module.py
import os
import matplotlib
matplotlib.use("Agg")  # backend sem interface
from sea_level_predictor import draw_plot

def test_draw_plot_saves_file():
    # Gera o gráfico e salva a figura
    ax = draw_plot()
    assert os.path.exists("sea_level_plot.png"), "O arquivo 'sea_level_plot.png' não foi gerado."

def test_labels_and_title():
    ax = draw_plot()
    assert ax.get_xlabel() == "Year", "xlabel deve ser 'Year'"
    assert ax.get_ylabel() == "Sea Level (inches)", "ylabel deve ser 'Sea Level (inches)'"
    assert ax.get_title() == "Rise in Sea Level", "title deve ser 'Rise in Sea Level'"

def test_has_two_fit_lines():
    ax = draw_plot()
    # Deve haver pelo menos duas linhas (fits)
    lines = ax.get_lines()
    assert len(lines) >= 2, "Devem existir pelo menos 2 linhas de regressão no gráfico."
