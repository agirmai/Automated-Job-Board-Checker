print("Hello World")
print("Testing testing")

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chrome = playwright.chromium
    browser = chrome.launch()
    page = browser.new_page()
    page.goto("https://abemgirmai.pages.dev/")
    answer = page.locator("h1").first
    print(answer.text_content())

with sync_playwright() as playwright:
    run(playwright)



