from playwright.sync_api import sync_playwright, Playwright
import json
import os
import requests

def sendmessage(message):
    topic = "northwesternjobboardalert"
    requests.post(f"https://ntfy.sh/{topic}", data=message.encode('utf-8'))



def run(playwright: Playwright):
    #Check if we have a last job available, and load it as prev
    if os.path.exists("last_job.json"):
        with open("last_job.json", "r") as f:
            data = json.load(f)
            prev = data.get("last_id", "")
    else:
        prev = ""
    #Get to the Microsoft Power BI page
    chrome = playwright.chromium
    browser = chrome.launch()
    page = browser.new_page()
    page.goto("https://app.powerbi.com/view?r=eyJrIjoiMmUwNDhmNjEtMGRhMS00OTlhLWE1NjQtM2VkZjFlYTg3MzNhIiwidCI6IjdkNzZkMzYxLTgyNzctNDcwOC1hNDc3LTY0ZTgzNjZjZDFiYyIsImMiOjN9&pageName=ReportSection")
    page.wait_for_selector('[role="gridcell"]')
    id = page.locator('[role="gridcell"][column-index="8"]').first
    #If the id is different than what we already had, then we send a notification
    if id.text_content() != prev:
        deptname = page.locator('[role="gridcell"][column-index="2"]').first
        jobrole = page.locator('[role="gridcell"][column-index="4"]').first
        location = page.locator('[role="gridcell"][column-index="7"]').first
        #send notification
        message = f"""New Work-Study
        {deptname.text_content()}, {jobrole.text_content()}
        {location.text_content()}
        """
        sendmessage(message)
        currentid = id.text_content()
        #Change prev to the job we just notified
        with open("last_job.json", "w") as f:
            json.dump({"last_id": currentid}, f)   
with sync_playwright() as playwright:
    run(playwright)



