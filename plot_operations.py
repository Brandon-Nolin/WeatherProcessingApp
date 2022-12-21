"""
Contains the PlotOperations class, which contains functions to plot weather data.
"""
import logging
import matplotlib.pyplot as plot

class PlotOperations():
    """
    Contains functions to plot daily and monthly data.
    """

    logger = logging.getLogger("main." + __name__)

    def plot_monthly(self, weather_data, start_year, end_year):
        """
        Plots monthly temps in a given year range on a box plot.
        """
        try:
            monthly_data = {"01" : [], "02" : [], "03" : [], "04" : [], "05" : [],
            "06" : [], "07" : [], "08" : [], "09" : [], "10" : [], "11" : [], "12" : []}

            for date, temps in weather_data.items():
                try:
                    month = date.split("-")[1]
                    monthly_data[str(month)].append(float(temps["avg_temp"]))
                except Exception as exception:
                    print("plot_operations:plot_daily:loop:", exception)
                    self.logger.error(f"plot_operations:plot_daily:loop:{exception}")

            plot.boxplot(monthly_data.values())
            plot.title(f"Monthly Temperature Distribution for: {start_year} to {end_year}")
            plot.xlabel("Month")
            plot.ylabel("Temperature (Celcius)")
            plot.show()
        except Exception as exception:
            print("plot_operations:plot_monthly:", exception)
            self.logger.error(f"plot_operations:plot_monthly:{exception}")



    def plot_daily(self, weather_data):
        """
        Plots daily temps in a given month on a given year on a line plot.
        """
        try:
            daily_data = []
            date_ticks = []

            for dates, temps in weather_data.items():
                try:
                    date_ticks.append(dates)
                    daily_data.append(float(temps["avg_temp"]))
                except Exception as exception:
                    print("plot_operations:plot_daily:loop:", exception)
                    self.logger.error(f"plot_operations:plot_daily:loop:{exception}")

            plot.plot(daily_data)
            plot.title("Daily Avg Temperatures")

            plot.xticks(ticks= range(0, len(date_ticks)),labels= date_ticks,
            rotation=40, fontsize=7)

            plot.ylabel("Avg Daily Temp")
            plot.xlabel("Day of Month")
            plot.show()
        except Exception as exception:
            print("plot_operations:plot_daily:", exception)
            self.logger.error(f"plot_operations:plot_daily:{exception}")
