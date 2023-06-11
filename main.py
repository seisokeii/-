import re
from threading import Thread
import requests

def get_content(response_text):
    maintxt = """&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br />"""
    texts = re.findall(maintxt, response_text, re.DOTALL)
    str = texts[len(texts) - 1]
    head = str.partition('<')
    texts[len(texts) - 1] = head[0]
    return texts


def write_to_file(file_name, novel_title, novel_contents):
    with open("./novel/"+file_name, 'w', encoding='utf-8') as f:
        f.write(novel_title + '\n')
        for c in novel_contents:
            f.write(c + '\n')
    print("Writing " + file_name + " Finish!")


def req_web(url, file_name, title):
    response = requests.get(url)
    response.encoding = 'gb2312'
    contents = get_content(response.text)
    write_to_file(file_name, title, contents)


if __name__ == '__main__':

    with open('./novel_index.txt', 'r', encoding="utf-8") as f:
        all_lines = f.readlines()
        index_count = 0

        for line in all_lines:
            link, title = line.split('@')
            index_count += 1

            full_url = 'https://www.ptwxz.com/html/7/7197/' + link
            filename = "No." + str(index_count) + ".txt"

            req_thread = Thread(target=req_web, args=(full_url, filename, title))
            req_thread.start()
