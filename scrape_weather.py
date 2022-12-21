"""
Scrapes winnipeg weather data from the government of canada website from the current date
to as far back as it goes.
"""
import logging
import urllib.request
from html.parser import HTMLParser
from datetime import date
from pubsub import pub

class WeatherScraper(HTMLParser):
    """
    Scrapes weather data from the government of Canada website, storing all data in a dict.
    """

    logger = logging.getLogger("main." + __name__)

    def __init__(self, last_date=None):
        """
        Initializes the WeatherScraper object with an empty dict to store the weather data in
        along with other variables to help with scraping.
        """
        try:
            HTMLParser.__init__(self)
            self.last_date = last_date
            self.day = 1
            self.year = date.today().year
            self.month = date.today().month
            self.months = {1 : "January", 2 : "February", 3 : "March",
            4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August",
            9 : "September", 10 : "October", 11 : "November", 12 : "December"}
            self.weather = {}
            self.pos = 0
            self.data_found = False
            self.more_data = True
            self.final_month = False
        except Exception as exception:
            print("WeatherScraper:__init__:", exception)
            self.logger.error("WeatherScraper:__init__:%s", exception)


    def handle_starttag(self, tag, attrs):
        """
        Checks for the the date we are currently on,
        when found sets data_found to true to scrape it.
        """
        try:
            for attr in attrs:
                try:
                    if (self.months[self.month] + " " +
                    str(self.day).lstrip('0') + ", " + str(self.year)) in attr:
                        self.data_found = True
                        self.pos = 0
                except Exception as exception:
                    print("WeatherScraper:handle_starttag:for:", exception)
        except Exception as exception:
            print("WeatherScraper:handle_starttag:", exception)
            self.logger.error("WeatherScraper:handle_starttag:%s", exception)


    def handle_data(self, data):
        """
        Checks if the month and year are correct and adds the correct data to the weather dict.
        """

        try:
            if "Daily Data Report" in data:
                if f"{self.months[self.month]} {self.year}" not in data:
                    self.more_data = False

            if f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}" == self.last_date:
                self.final_month = True

            if self.more_data and self.data_found and "E" not in data:
                if "LegendM" not in data:
                    self.pos += 1
                if self.pos == 1:
                    self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"] = {}
                elif self.pos == 4:
                    try:
                        self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"]["max_temp"] = float(data)
                    except ValueError:
                        self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"]["max_temp"] = None
                elif self.pos == 6:
                    try:
                        self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"]["min_temp"] = float(data)
                    except ValueError:
                        self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"]["min_temp"] = None
                elif self.pos == 8:
                    try:
                        self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"]["avg_temp"] = float(data)
                    except ValueError:
                        self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"]["avg_temp"] = None

                    if None in self.weather[f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"]:
                        self.weather.pop(f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}")
                    self.data_found = False
                    self.day += 1
        except Exception as exception:
            print("WeatherScraper:handle_data:", exception)
            self.logger.error("WeatherScraper:handle_data:%s", exception)

    def scrape(self):
        """
        Continuously scrape data from the website, starting at the current date,
        reducing the months and year as it goes and
        stopping when the data returned is not of the correct date.
        """
        try:
            while self.more_data:
                with urllib.request.urlopen(
                    "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID" +
                    "=27174&timeframe=2&StartYear=1840&EndYear=2018&" +
                    f"Day=1&Year={self.year}&Month={self.month}") as response:
                    html = str(response.read())
                self.day = 1

                print(f"scraping {self.year}-{str(self.month).zfill(2)}")

                status = f"scraping {self.year}-{str(self.month).zfill(2)}"
                pub.sendMessage("progress", progress=status)

                self.logger.info("scraping %s-%s", self.year, str(self.month).zfill(2))
                self.feed(html)
                if self.final_month:
                    self.more_data = False
                self.month -= 1
                if self.month == 0:
                    self.year -= 1
                    self.month = 12
            pub.sendMessage("data", weather_data=self.weather)
        except Exception as exception:
            print("WeatherScraper:scrape:", exception)
            self.logger.error("WeatherScraper:scrape:%s", exception)
