
# バージョン: 111.0.5563.65（Official Build）
# "C:\Users\kenzo\マイドライブ\KENZO_個人フォルダ\03_Python\09_ノンプロ研Python中級講座2023Mar\chromedriver.exe"

# from selenium import webdriver
# driver_file = r'C:\Users\kenzo\マイドライブ\KENZO_個人フォルダ\03_Python\09_ノンプロ研Python中級講座2023Mar\chromedriver.exe'
# browser = webdriver.Chrome(driver_file)
# url = 'https://tonari-it.com'
# browser.get(url)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep

# driver_file = r'C:\Users\kenzo\マイドライブ\KENZO_個人フォルダ\03_Python\09_ノンプロ研Python中級講座2023Mar\chromedriver.exe'
# browser = webdriver.Chrome(driver_file)
# url = 'https://tonari-it.com'


# def fetch_titles(browser):
#     titles = browser.find_elements(By.CSS_SELECTOR, "h2.entry-card-title.card-title.e-card-title")
#     return [title.text for title in titles]


# def main():
#     browser.get(url)
#     sleep(1)  # Wait 処理
#     titles = fetch_titles(browser)
#     print(titles)
#     browser.quit()


# if __name__ == "__main__":
#     main()

#Seleneumバージョン
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver_file = r'C:\Users\kenzo\マイドライブ\KENZO_個人フォルダ\03_Python\09_ノンプロ研Python中級講座2023Mar\chromedriver.exe'
browser = webdriver.Chrome(driver_file)
url = 'https://tonari-it.com'


def fetch_titles(browser):
    titles = browser.find_elements(By.CSS_SELECTOR, "h2.entry-card-title.card-title.e-card-title")
    return [title.text for title in titles]


def find_next_page(browser):
    try:
        next_page = browser.find_element(By.CSS_SELECTOR, "a.page-numbers")
        return next_page.get_attribute("href")
    except:
        return None


def main():
    all_titles = []
    browser.get(url)
    page_count = 1

    while url and page_count <= 3:
        sleep(1)  # Wait 処理
        titles = fetch_titles(browser)
        all_titles.extend(titles)

        next_page_url = find_next_page(browser)
        if next_page_url:
            browser.get(next_page_url)
            page_count += 1
        else:
            break

    print(all_titles)
    browser.quit()


if __name__ == "__main__":
    main()



# BSバージョン
import requests
from bs4 import BeautifulSoup

base_url = 'https://tonari-it.com'


def fetch_titles(soup):
    titles = soup.select("h2.entry-card-title.card-title.e-card-title")
    return [title.text for title in titles]


def find_next_page(soup):
    next_page = soup.find("a", class_="page-numbers")
    return next_page["href"] if next_page else None


def main():
    all_titles = []
    page_count = 1
    current_url = base_url

    while current_url and page_count <= 3:
        response = requests.get(current_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        titles = fetch_titles(soup)
        all_titles.extend(titles)

        next_page_url = find_next_page(soup)
        if next_page_url:
            current_url = next_page_url
            page_count += 1
        else:
            break

    print(all_titles)


if __name__ == "__main__":
    main()


    



