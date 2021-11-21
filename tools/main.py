import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.neighbors import KernelDensity

SOLAR_IRRADIANCE = "GHI"


def filter_data(df, thresh=1 / 50):
    df = df.loc[
        df[SOLAR_IRRADIANCE] > thresh * df[SOLAR_IRRADIANCE].max(),
    ]
    return df


def kernel_density_from_df(df):
    data_vec = df[SOLAR_IRRADIANCE].values.reshape(-1, 1)
    kde = KernelDensity(kernel="gaussian", bandwidth=50).fit(data_vec)
    return kde


def hist_from_df_and_kde(df, kde):
    # x_vals = np.arange(df[SOLAR_IRRADIANCE].min(), df[SOLAR_IRRADIANCE].max(), 0.1).reshape(-1, 1)
    x_vals = np.arange(0, df[SOLAR_IRRADIANCE].max(), 0.1)
    # Returns the log value; needs to be re-exponentiated
    kde_vals = np.exp(kde.score_samples(x_vals.reshape(-1, 1)))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    sns.histplot(
        df[SOLAR_IRRADIANCE], kde=False, bins=30, stat="density", ax=ax
    )
    sns.lineplot(x=x_vals, y=kde_vals, color="red", linewidth=2.5, ax=ax)
    # TODO Make plot save(?)
    plt.show()
    return None


def time_of_day_plot(df):
    plt.scatter(df["Hour"], df[SOLAR_IRRADIANCE], s=0.05)
    # TODO Make plot save(?)
    plt.show()
    return None


def main():
    df = pd.read_csv("../data/irradiance_full.csv")
    df = filter_data(df)
    kde = kernel_density_from_df(df)
    hist_from_df_and_kde(df, kde)
    time_of_day_plot(df)


if __name__ == "__main__":
    main()
