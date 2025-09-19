# sea_level_predictor.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def _fit_and_project(x, y, xmin, xmax):
    """Ajusta regressão linear com linregress e projeta de xmin..xmax (inclusive)."""
    fit = linregress(x, y)
    years = np.arange(int(xmin), int(xmax) + 1, dtype=int)
    pred = fit.slope * years + fit.intercept
    return years, pred

def draw_plot():
    # === Carregar dados ===
    data = pd.read_csv("epa-sea-level.csv")
    x_year = data["Year"].to_numpy()
    sea_csiro = data["CSIRO Adjusted Sea Level"].to_numpy()

    # === Figura base (dispersão) ===
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x_year, sea_csiro, s=18, alpha=0.7)

    # === Regressão completa (1880..2014) estendida até 2050 ===
    yrs_full, yhat_full = _fit_and_project(x_year, sea_csiro, xmin=1880, xmax=2050)
    ax.plot(yrs_full, yhat_full, linewidth=2.0, label="Best fit: 1880–2014")

    # === Regressão recente (>=2000) estendida até 2050 ===
    mask_recent = x_year >= 2000
    yrs_recent, yhat_recent = _fit_and_project(x_year[mask_recent], sea_csiro[mask_recent],
                                               xmin=2000, xmax=2050)
    ax.plot(yrs_recent, yhat_recent, linewidth=2.0, label="Best fit: 2000–2014")

    # === Rótulos e título exigidos ===
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    ax.grid(True, alpha=0.25)

    # === Salvar figura com o nome esperado pelos testes ===
    plt.savefig("sea_level_plot.png")
    return ax
