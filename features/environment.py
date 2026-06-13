from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ### USED FOR CHROME TESTING
    context.driver = webdriver.Chrome()

    ### USED FOR FIREFOX TESTING
    # context.driver = webdriver.Firefox()

    ### USED FOR SAFARI TESTING
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE CHROME
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #     options=options
    # )

    ### HEADLESS MODE FIREFOX
    # options = webdriver.FirefoxOptions()
    # options.add_argument("-headless")
    # context.driver = webdriver.Firefox(options=options)

    ### BROWSERSTACK ###
    # bs_user = 'borisnunez_Exd0YS'
    # bs_key = 'fFqsRpuERpbHMiGxGAqz'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "10",
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15) #added
    context.app = Application(context.driver) #added

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.delete_all_cookies() #added
    context.driver.quit()