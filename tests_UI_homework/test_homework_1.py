from selenium.webdriver import Chrome


def test_browser_open():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw")
        print(f"current url {browser.current_url}")
        browser.quit()
