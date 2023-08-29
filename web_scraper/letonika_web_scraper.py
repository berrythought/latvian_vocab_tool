import pandas as pd
import requests
from bs4 import BeautifulSoup

from vocab_tool_functions import import_and_clean_data, create_study_df

pd.set_option('display.max_columns', None)

df_unique = import_and_clean_data('enter_text.txt')
study_df, unique_word_df = create_study_df(df_unique)
search_words = unique_word_df['word']
search_words = search_words[17192:]

total_set = set()
df = pd.read_csv('total_df.csv')

for i in range(len(df)):
    word = df['0'][i]
    conjugations = tuple(df['1'][i].replace('(', '').replace(')', '').replace("'", "").replace(' ', '').split(','))
    new_list = [word, conjugations]
    new_tuple = tuple(new_list)
    total_set.add(new_tuple)

for idx, search_word in enumerate(search_words):
    print(idx)
    oh_dear = 1
    page_no = 0
    while oh_dear == 1:
        url = 'https://www.letonika.lv/groups/default.aspx?r=1100&q=' + search_word + '&title=' + search_word + '/' + str(
            page_no) + '&g=5'
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)
        soup_txt = str(soup)
        if 'apstākļa vārds' in soup_txt:
            words = soup_txt.split('Entrytext">')
            if len(words) >= 4:
                words = words[1:4]
                for i in range(3):
                    words[i] = words[i].split('<')[0]
                words = set(words)
            else:
                words = []
        else:
            words = soup_txt.split('spelling')
            words = words[1::2]
            words = set([w.replace('>', '').replace('<', '').replace('/', '') for w in words])
        if len(words) > 0:
            pamatforma = soup_txt.split('pamatforma: <i>')[1].split('<')[0]
            words.add(pamatforma)
            words = tuple([pamatforma, tuple(words)])
            print(pamatforma)
            total_set.add(words)
            page_no = page_no + 1
        else:
            oh_dear = 0
            # if idx % 100 == 99:
            #   total_list = list(total_set)
            #  df = pd.DataFrame(total_list)
            df.to_csv('total_df.csv', index=False, encoding='utf-8')

total_list = list(total_set)
df = pd.DataFrame(total_list)
df.to_csv('total_df.csv', index=False, encoding='utf-8')
print('Done')
