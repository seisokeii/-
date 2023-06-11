import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    response = requests.get('https://www.ptwxz.com/html/7/7197/')
    response.encoding = 'gb2312'
    soup = BeautifulSoup(response.text, 'lxml')

    chap = soup.find_all('ul')

    for ul in chap:
        each = ul.find_all('a')
        for ee in each:
            with open("./novel_index.txt", 'a', encoding='utf-8') as f:
                f.write(ee.get('href') + "@" + ee.text + '\n')
    '''
        網站的章節標示有地方會漏掉或是奇怪的章節出現，出現較少就沒用程式排除了，已經整理成 novel_index.txt 了
    '''