#%% 실행 전 사전준비
from urllib.parse import quote_plus
from selenium import webdriver
from bs4 import BeautifulSoup

headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38'}
url_bs='http://g.bns.plaync.com/ingame/bs/character/profile?c='

options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')


#%% 캐릭정보 호출 함수
def info_call(char_name) : 
 driver=webdriver.Chrome('chromedriver', options=options)
 
 cn=quote_plus(char_name)
 driver.get(url_bs + cn)
 soup_bs=BeautifulSoup(driver.page_source, 'html.parser')
 
 atk=soup_bs.find('span', id='total-int_attack_power_value').text
 boss_atk=soup_bs.find('span', id='total-boss_attack_power_value').text
 acc=soup_bs.find('span', id='total-int_attack_hit_value').text
 acc_rate=soup_bs.find('span', id='total-attack_hit_rate').text
 crt_rate=soup_bs.find('span', id='total-attack_critical_rate').text
 crt_dam=soup_bs.find('span', id='total-attack_critical_damage_value').text
 attr=soup_bs.find('span', id='total-attack_attribute_value').text

 print('{} 님의 캐릭터 정보'.format(char_name))
 print('공격력 :', atk)
 print('항마공 :', boss_atk)
 print('명중 :', acc)
 print('명중률 :', acc_rate)
 print('치명타율 :', crt_rate)
 print('치명피해 :', crt_dam)
 print('공력 :', attr)
 print('치피공합 :', int(crt_dam)+int(attr))
# %%
name=input('캐릭터명 입력 :')
info_call(name)
# %%
