# encoding=utf-8
from connectdb import *
from miner import Miner


url_info_list = get_url_list()
for url in url_info_list:
    project_name = str(url[0])
    mining_url = url[1]
    Miner(project_name, mining_url)
