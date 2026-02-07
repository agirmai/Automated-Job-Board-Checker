from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    prev = None
    chrome = playwright.chromium
    browser = chrome.launch()
    page = browser.new_page()
    page.goto("https://app.powerbi.com/view?r=eyJrIjoiMmUwNDhmNjEtMGRhMS00OTlhLWE1NjQtM2VkZjFlYTg3MzNhIiwidCI6IjdkNzZkMzYxLTgyNzctNDcwOC1hNDc3LTY0ZTgzNjZjZDFiYyIsImMiOjN9&pageName=ReportSection")
    # firstrow = page.get_by_role("rowheader")
    # date = page.locator("cell-selectedpivotTableCellWrap cell-interactive main-cell")
    deptname = page.locator('[role="gridcell"][column-index="2"]').first
    jobrole = page.locator('[role="gridcell"][column-index="4"]').first
    location = page.locator('[role="gridcell"][column-index="7"]').first
    id = page.locator('[role="gridcell"][column-index="8"]').first
    print(deptname.text_content())
    print(jobrole.text_content())
    print(location.text_content())
    print(id.text_content())
    

with sync_playwright() as playwright:
    run(playwright)



