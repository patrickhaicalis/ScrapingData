import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys, getopt
import csv


def ScrapeTeamPlayerStats(team, url):


    res = requests.get(url)
    comm = re.compile('<!--|-->')
    soup = BeautifulSoup(comm.sub('', res.text), 'lxml')

    all_tables = soup.findAll('tbody')
    player_table = all_tables[0]

    pre_df = dict()
    features_wanted = {'position', 'age', 'games', 'games_starts', 'minutes', 'goals', 'assists', 'pens_made', 'pens_att',
                       'cards_yellow', 'cards_red', 'goals_per90', 'assists_per90', 'goals_assists_per90',
                       'goals_pens_per90', 'goals_assists_pens_per90', 'xg', 'npxg', 'xa', 'xg_per90', 'xa_per90',
                       'xg_xa_per90', 'npxg_per90', 'npxg_xa_per90'}

    rows = player_table.find_all('tr')
    for row in rows:
        if (row.find('th', {"scope": "row"}) != None):
            name = row.find('th', {"data-stat": "player"}).text.strip().encode().decode("utf-8")
            if 'player' in pre_df:
                pre_df['player'].append(name)
            else:
                pre_df['player'] = [name]
            for f in features_wanted:
                cell = row.find("td", {"data-stat": f})
                a = cell.text.strip().encode()
                text = a.decode("utf-8")
                if f in pre_df:
                    pre_df[f].append(text)
                else:
                    pre_df[f] = [text]



    df_squad = pd.DataFrame.from_dict(pre_df)
    df_squad.to_csv(f'TeamPlayerStats/{team}SquadStats.csv')
