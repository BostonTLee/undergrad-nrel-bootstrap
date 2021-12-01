import pandas as pd

from astronomical_adjustment import AstronomicalAdjustment as aa
from power_processor import PowerProcessor as pp
from pv_module import PVModule as pvm


def main():
    SOLAR_IRRADIANCE = "irradiance_eff"
    CURRENT_OUTPUT = "current_out"
    RAW_CSV = "../data/raw/irradiance_full_raw.csv"
    PROCESSED_CSV =  "../data/final/irradiance_full_final.csv"


    df = pd.read_csv(RAW_CSV)

    lat = 34.05
    lon = 28.24
    utc = -8

    df[SOLAR_IRRADIANCE] = df.apply(
        lambda row: aa.effective_solar_radiance(
            row["DHI"],
            row["Month"],
            row["Day"],
            row["Hour"],
            row["Minute"],
            lat,
            lon,
            utc,
        ),
        axis=1,
    )

    df[CURRENT_OUTPUT] = df.apply(
        lambda row: pp.estimated_power(
            ideality=1.5,
            temperature=row["Temperature"],
            sc_current_module=5,
            i_eff=row[SOLAR_IRRADIANCE],
            n_parallel=6,
            n_series=6,
            oc_voltage=1.8,
            efficiency=0.211,
        ),
        axis=1,
    )

    df.to_csv(PROCESSED_CSV)

if __name__ == "__main__":
    main()
