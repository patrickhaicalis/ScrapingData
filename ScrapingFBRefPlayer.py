import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def ScrapePlayerStats(name, url, table_type):


    res = requests.get(url)
    comm = re.compile('<!--|-->')
    soup = BeautifulSoup(comm.sub('', res.text), 'lxml')

    all_tables = soup.findAll('tbody')
    standard_table = all_tables[0]
    shooting_table = all_tables[1]
    passing_table = all_tables[2]
    pass_type_table = all_tables[3]
    goal_and_shot_creation_table = all_tables[4]
    defensive_action_table = all_tables[5]
    possession_table = all_tables[6]
    playing_time_table = all_tables[7]
    miscellaneous_table = all_tables[8]
    summary_table = all_tables[9]

    if table_type == 'shooting':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', 'minutes_90s', 'goals', 'shots_total', 'shots_on_target',
                            'shots_on_target_pct', "shots_total_per90", "shots_on_target_per90", "goals_per_shot",
                            "goals_per_shot_on_target", "shots_free_kicks", "pens_made", "pens_att", "xg", "npxg",
                            "npxg_per_shot", "xg_net",  "npxg_net"}

        rows = shooting_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/ShootingStats/{name}PlayerShootingStats.csv')

    elif table_type == 'standard':
        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', 'games', 'games_starts', 'minutes', 'goals', 'assists', 'pens_made', 'pens_att',
                           'cards_yellow', 'cards_red', 'goals_per90', 'assists_per90', 'goals_assists_per90',
                           'goals_pens_per90', 'goals_assists_pens_per90', 'xg', 'npxg', 'xa', 'xg_per90', 'xa_per90',
                           'xg_xa_per90', 'npxg_per90', 'npxg_xa_per90'}

        rows = standard_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/StandardStats/{name}PlayerStandardStats.csv')

    elif table_type == 'passing':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', 'minutes_90s', 'passes_completed', 'passes', 'passes_pct',
                           'passes_total_distance', 'passes_progressive_distance', 'passes_completed_short',
                           'passes_short', 'passes_pct_short', 'passes_completed_medium', 'passes_medium',
                           'passes_pct_medium', 'passes_completed_long', 'passes_long', 'passes_pct_long', 'assists',
                           'xa', 'xa_net', 'assisted_shots', 'passes_into_final_third', 'passes_into_penalty_area',
                           'crosses_into_penalty_area', 'progressive_passes'}

        rows = passing_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/PassingStats/{name}PlayerPassingStats.csv')

    elif table_type == 'pass_types':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', 'minutes_90s', 'passes_completed', 'passes', 'passes_live',
                           "passes_dead", "passes_free_kicks", "through_balls", "passes_pressure", "passes_switches",
                           "crosses", "corner_kicks", "corner_kicks_in", "corner_kicks_out", "corner_kicks_straight",
                           "passes_ground", "passes_low", "passes_high", "passes_left_foot", "passes_right_foot",
                           "passes_head", "throw_ins", "passes_other_body", "passes_completed", "passes_offsides",
                           "passes_oob", 'passes_intercepted', "passes_blocked"}

        rows = pass_type_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/PassTypeStats/{name}PlayerPassTypeStats.csv')

    elif table_type == 'goal_shot_creation':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', 'minutes_90s', "sca", "sca_per90", "sca_passes_live",
                           "sca_passes_dead", "sca_dribbles", "sca_shots", "sca_fouled", "gca", "gca_per90",
                           "gca_passes_live", "gca_passes_dead", "gca_dribbles", "gca_shots", "gca_fouled",
                           "gca_og_for"}

        rows = goal_and_shot_creation_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/GoalShotCreationStats/{name}PlayerGoalShotCreationStats.csv')

    elif table_type == 'defense':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', 'minutes_90s', "tackles", "tackles_won", "tackles_def_3rd",
                           "tackles_mid_3rd", "tackles_att_3rd", "dribble_tackles", "dribbles_vs","dribble_tackles_pct",
                           "dribbled_past", "pressures", "pressure_regains", "pressure_regain_pct", "pressures_def_3rd",
                           "pressures_mid_3rd", "pressures_att_3rd", "blocks", "blocked_shots", "blocked_shots_saves",
                           "blocked_passes", "interceptions", "tackles_interceptions", "clearances", "errors"}

        rows = defensive_action_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/DefensiveActionStats/{name}PlayerDefensiveActionStats.csv')

    elif table_type == 'possession':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', 'minutes_90s', "touches", "touches_def_pen_area",
                           "touches_def_3rd", "touches_mid_3rd", "touches_att_3rd", "touches_att_pen_area",
                           "touches_live_ball", "dribbles_completed", "dribbles", "dribbles_completed_pct",
                           "players_dribbled_past", "nutmegs", "carries", "carry_distance",
                           "carry_progressive_distance", "pass_targets", "passes_received", "passes_received_pct",
                           "miscontrols", "dispossessed"}

        rows = possession_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/PossessionStats/{name}PlayerPossessionStats.csv')

    elif table_type == 'playing_time':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', "games", "minutes", "minutes_per_game", "minutes_pct",
                           "minutes_90s", "games_starts", "minutes_per_start", "games_subs", "minutes_per_sub",
                           "unused_subs", "points_per_match", "on_goals_for", "on_goals_against", "plus_minus",
                           "plus_minus_per90", "plus_minus_wowy", "on_xg_for", "on_xg_against", "xg_plus_minus",
                           "xg_plus_minus_per90", "xg_plus_minus_wowy"}

        rows = playing_time_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/PlayingTimeStats/{name}PlayerPlayingTimeStats.csv')

    elif table_type == 'misc':

        pre_df = dict()
        features_wanted = {'age', 'squad', 'lg_finish', "minutes_90s", "cards_yellow", "cards_red",
                           "cards_yellow_red", "fouls", "fouled", "offsides", "crosses", "interceptions", "tackles_won",
                           "pens_won", "pens_conceded", "own_goals", "ball_recoveries", "aerials_won", "aerials_lost",
                           "aerials_won_pct"}

        rows = miscellaneous_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/MiscellaneousStats/{name}PlayerMiscellaneousStats.csv')

    elif table_type == 'summary':

        pre_df = dict()
        features_wanted = {'age', 'squad', "dom_lg_games", "dom_lg_minutes", "dom_lg_goals", "dom_lg_assists",
                           "dom_cup_games", "dom_cup_minutes", "dom_cup_goals", "dom_cup_assists", "intl_cup_games",
                           "intl_cup_minutes", "intl_cup_goals", "intl_cup_assists", "all_games", "all_minutes",
                           "all_goals", "all_assists"}

        rows = summary_table.find_all('tr')
        for row in rows:
            if (row.find('th', {"scope": "row"}) != None):
                for f in features_wanted:
                    cell = row.find("td", {"data-stat": f})
                    a = cell.text.strip().encode()
                    text = a.decode("utf-8")
                    if f in pre_df:
                        pre_df[f].append(text)
                    else:
                        pre_df[f] = [text]

        df_squad = pd.DataFrame.from_dict(pre_df)
        df_squad.to_csv(f'PlayerStats/SummaryStats/{name}PlayerSummaryStats.csv')

name = 'Mount'
url = 'https://fbref.com/en/players/9674002f/Mason-Mount'

ScrapePlayerStats(name, url, table_type='standard')
ScrapePlayerStats(name, url, table_type='shooting')
ScrapePlayerStats(name, url, table_type='passing')
ScrapePlayerStats(name, url, table_type='pass_types')
ScrapePlayerStats(name, url, table_type='goal_shot_creation')
ScrapePlayerStats(name, url, table_type='defense')
ScrapePlayerStats(name, url, table_type='possession')
ScrapePlayerStats(name, url, table_type='playing_time')
ScrapePlayerStats(name, url, table_type='misc')
ScrapePlayerStats(name, url, table_type='summary')

