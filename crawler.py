"""Main file that interacts with the specified URLs."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import config, mail, time

def crawl(product_name, size, product_url):
	"""Interact with the internet. The main logic flow is as follows:

	First ensure that the site URL is correct.
	If so, search for the item using the searchbar.
	If no items are returned, assume the item no longer exists.
	Else, try to go to the product URL.
		If this works, interact with the size dropdown menu.
			Try to select the size. 
				If it doesn't let you, it's not in stock and try again later.
				If it is, then email!
		If not, assume the item is gone. 

	"""

	found = False
	driver = webdriver.Chrome()
	driver.get(config.SITE_URL)

	if config.SITE_NAME not in driver.title:
		mail.err(config.SITE_NAME)

	else:
		while not found:
			elem = driver.find_element_by_name(config.SEARCHBAR)
			elem.clear()
			elem.send_keys(product_name)
			elem.send_keys(Keys.RETURN)

			if config.NOT_FOUND in driver.page_source:
				mail.gone(config.SITE_NAME, product_name)
				break

			else:
				try:
					driver.get(product_url)
					select = Select(driver.find_element_by_name(config.SELECT_BAR_NAME))

					if config.NO_EXIST in driver.page_source:
						mail.gone(config.SITE_NAME, product_NAME)
						break

					try:
						select.select_by_visible_text(size.upper())
						mail.restocked(config.SITE_NAME, product_name, driver.current_url)
						found = True

					except:
						time.sleep(TIME_TO_SLEEP)

				except:
					mail.gone(config.SITE_NAME, product_name)
					break

