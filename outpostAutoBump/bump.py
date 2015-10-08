from splinter import Browser
import log, config, time

def run():
    browser = Browser('firefox', profile=config.FIREFOX_PROFILE_PATH)
    browser.visit('http://www.tf2outpost.com/trades')

    buttonList = browser.find_by_css(".trade_bump")
    listSize = len(buttonList)
    log.logMessage("Bumping " + str(listSize) + " items")

    for i in range(listSize):
        buttonList[i].click()

    browser.quit()

def execute(minutes):
    run()
    time.sleep(minutes*60)

if __name__ == "__main__":
    while True:
        execute(1)