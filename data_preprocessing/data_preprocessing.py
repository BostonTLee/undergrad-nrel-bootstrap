import time

import pandas as pd
import toml


def pull_nrel_data_single_year(lat, lon, year, config_path):
    config_dict = toml.load("config.toml")
    attributes = "ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle"
    # Set leap year to true or false. True will return leap day data if present, false will not.
    leap_year = "false"
    # Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 30 & 60.
    interval = "30"
    # Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
    # NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
    # local time zone.
    utc = "true"
    # Please join our mailing list so we can keep you up-to-date on new developments.
    mailing_list = "false"

    # Declare url string
    url = "https://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}".format(
        year=year,
        lat=lat,
        lon=lon,
        leap=leap_year,
        interval=interval,
        utc=utc,
        name=config_dict["name"],
        email=config_dict["email"],
        mailing_list=mailing_list,
        affiliation=config_dict["affiliation"],
        reason=config_dict["reason"],
        api=config_dict["api_key"],
        attr=attributes,
    )
    df = pd.read_csv(url, low_memory=False, skiprows=2)
    return df


def pull_nrel_data_multiple_years(
    lat, lon, config_path, years=range(2001, 2011)
):
    df_list = []
    for year in years:
        try:
            print("Downloading data for year: {}".format(year))
            temp_df = pull_nrel_data_single_year(lat, lon, year, "config.toml")
            df_list.append(temp_df)
        except Exception as e:
            print("Could not download data for year: {}".format(year))
            print(e)
        time.sleep(60)

    df = pd.concat(df_list)
    return df


def main():
    # LA coordinates
    lat, lon = 34.0522, -118.2437
    data = pull_nrel_data_multiple_years(lat, lon, "config.toml")
    data.to_csv("../data/irradiance_full.csv")


if __name__ == "__main__":
    main()