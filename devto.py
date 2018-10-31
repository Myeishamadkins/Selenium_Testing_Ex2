from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def headers(browser):
    headers = browser.find_elements_by_css_selector(
        "#sidebar-additional div.widget header")
    for header in headers:
        print(header.get_attribute("innerText"))


def main():
    options = Options()
    options.headless = True
    browser = Firefox(options=options)
    browser.get("https://dev.to")

    select_sidebar = browser.find_elements_by_css_selector(
        '#sidebar-additional div.widget')
    select_sidebar.remove(select_sidebar[0])

    while True:

        headers(browser)
        inputs = input("Section: ")

        for div in select_sidebar:
            header = div.find_element_by_css_selector("header").get_attribute(
                "innerText")
            if inputs in header:
                print(header)
                links = div.find_elements_by_css_selector(
                    ".widget-link-list a")
                for link in links:
                    print("\t" + link.get_attribute("innerText"))
                    print("\t\t" + link.get_attribute("href"))
        if inputs not in header:
            print("No matches.")
            print("------------------")

    browser.quit()


if __name__ == '__main__':
    main()
