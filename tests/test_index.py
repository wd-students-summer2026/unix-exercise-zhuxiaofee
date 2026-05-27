"""
Tests of an assignment to set up a skeleton of a web page and publish it online on a web server.

Requires Selenium 4.6+ (uses Selenium Manager to auto-manage chromedriver)
and a recent installation of Google Chrome.
"""

import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Tests:

  @pytest.fixture(scope="class")
  def site_settings(self):
    settings = json.load(open('./settings.json', 'r'))
    yield settings

  @pytest.fixture(scope="class")
  def web_driver(self):
    """
    Pop open a web browser and make it available to the tests.
    """
    settings = json.load(open('./settings.json', 'r'))
    print(settings["site_url"])

    # set up the fixture
    driver = webdriver.Chrome()
    driver.get(settings["site_url"]) # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_title(self, web_driver, site_settings):
    """
    Check the title tag for the correct text
    """
    assert site_settings["name"] in web_driver.title

  def test_h1(self, web_driver, site_settings):
    """
    Check the h1 tag for the correct text
    """
    elem = web_driver.find_element(By.TAG_NAME, "h1")

    assert site_settings["name"] in elem.text

  def test_mobile_width(self, web_driver):
    """
    Check the width of a responsive heading at browser width of 500px
    """
    web_driver.set_window_size(500, 800)
    elem = web_driver.find_element(By.TAG_NAME, "h1")
    # check that the h1 element is appropriate for mobile
    assert 500 > elem.size["width"]

  def test_desktop_width(self, web_driver):
    """
    Check the width of a responsive heading at browser width of 1200px
    """
    web_driver.set_window_size(1200, 800)
    elem = web_driver.find_element(By.TAG_NAME, "h1")
    # check that the h1 element is appropriate for desktop
    assert 1200 > elem.size["width"] > 500
