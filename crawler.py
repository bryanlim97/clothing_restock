"""Main file that interacts with the specified URLs."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import config, mail, time

def crawl(product_name, my_size, product_url):
	"""Interact with the internet. The main logic flow is as follows:

	First ensure that the site URL is correct.
		If so, search for the item using the searchbar.
			If no items are returned, assume the item no longer exists.
			Else, try to go to the product URL.
				If this works, try to create a list of the unreachable sizes.
					Check if your size is in this unreachable list. 
						If it is, sleep.
						Else, your item has been restocked!
				If the list is empty, all sizes are available and send a restock email!
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
				except:
					mail.err(config.SITE_URL)
				try:
					not_stocked = driver.find_elements_by_xpath(config.XPATH)
				except:
					mail.restocked(config.SITE_NAME, product_name, driver.current_url)
					break

				if config.NO_EXIST in driver.page_source:
					mail.gone(config.SITE_NAME, product_NAME)
					break

				found = True

				for sizes in not_stocked:
					if sizes.text == my_size.upper():
						found = False

				if found:
					mail.restocked(config.SITE_NAME, product_name, driver.current_url)
					break
				else:
					print("Sleeping...")
					time.sleep(config.TIME_TO_SLEEP)


