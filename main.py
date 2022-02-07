import argparse
import os
import subprocess
import pandas as pd
import crawling

parser = argparse.ArgumentParser()
parser.add_argument('--input', default='csv/example.csv', type=str) #input csv file
parser.add_argument('--name', default='data', type=str) #saved in result/[name]
opt = parser.parse_args()

data = pd.read_csv(opt.input, encoding='cp949')

eng_list = data['Folder_name']
eng_list = eng_list.values.tolist()

search = data['Search']
search = search.values.tolist()

if not os.path.isdir('result'):
    os.mkdir('result')

if not os.path.isdir('result/%s' %opt.name):
    os.mkdir('result/%s' %opt.name)
    
crawling.crawling(eng_list, search, opt.name)

