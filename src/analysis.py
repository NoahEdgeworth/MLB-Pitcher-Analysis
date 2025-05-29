import pandas as pd

def add_pitch_count(df):
    df = df.sort_values(by=['game_pk', 'inning', 'at_bat_number', 'pitch_number'])
    df['pitch_count'] = df.groupby('game_pk').cumcount() + 1
    return df

def add_pitch_buckets(df, bins=[0, 25, 50, 75, 100, 125]):
    labels = ['0–25', '26–50', '51–75', '76–100', '101+']
    df['pitch_bucket'] = pd.cut(df['pitch_count'], bins=bins, labels=labels)
    return df