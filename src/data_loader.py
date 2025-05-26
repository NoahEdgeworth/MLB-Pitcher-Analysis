from pybaseball import playerid_lookup, statcast_pitcher
import pandas as pd
import os

def get_pitcher_id(first_name, last_name):
    return playerid_lookup(last=last_name, first=first_name)['key_mlbam'].values[0]

def get_statcast_pitching_data(pitcher_id, start_date, end_date):
    df = statcast_pitcher(player_id=pitcher_id, start_dt=start_date, end_dt=end_date)
    return df

def save_data(df, name):
    path = os.path.join('data', 'raw', f'{name}.csv')
    df.to_csv(path, index=False)