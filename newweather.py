# -*- coding: utf-8
from tkinter import (
    StringVar,
    Radiobutton,
    W,
    Button,
    Label,
    Checkbutton,
    IntVar,
    END,
    Entry,
    E,
    N,
    S,
)
from PIL import ImageTk, Image
import tkinter as tk
import requests
import json
from datetime import timedelta, date
import array as arr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


root = tk.Tk()
root.title("Here is the Weather!")
#root.iconbitmap(".\partlycloudy.ico")
# root.geometry("700x600")

degree_symbol = "\xb0"


def submit_weather_view():
    current_weather_button.grid_forget()
    historical_weather_button.grid_forget()
    submit_weather_view_button.grid_forget()
    if weather_view.get() == "current":

        def clear_buttons():
            metric_button.grid_forget()
            scientific_button.grid_forget()
            fahrenheit_button.grid_forget()

            entry_type_checkbox.grid_forget()
            exact_entry_checkbox.grid_forget()
            latitude_checkbox.grid_forget()
            longitude_checkbox.grid_forget()
            city_checkbox.grid_forget()
            current_temp_checkbox.grid_forget()
            current_time_checkbox.grid_forget()
            weather_description_checkbox.grid_forget()
            wind_speed_checkbox.grid_forget()
            humidity_checkbox.grid_forget()
            feels_like_checkbox.grid_forget()
            humidity_checkbox.grid_forget()
            feels_like_checkbox.grid_forget()
            visibility_checkbox.grid_forget()
            select_all_checkbox.grid_forget()

        def api_set():
            global api, api_request, params, response_entry_type, response_exact_entry, response_latitude
            global response_longitude, response_city, response_current_temp, response_current_time
            global response_weather_description, response_wind_speed, response_humidity, response_feels_like
            global response_visibility

            # api request
            params = {
                "access_key": api_key_lookup.get(),
                "query": city_lookup.get(),
                "units": unit.get(),
            }

            api_request = requests.get("http://api.weatherstack.com/current", params)
            api = api_request.json()

            # Setting Response Variables
            response_entry_type = api["request"]["type"]
            response_exact_entry = api["request"]["query"]
            response_latitude = api["location"]["lat"]
            response_longitude = api["location"]["lon"]
            response_city = api["location"]["name"]
            response_current_temp = api["current"]["temperature"]
            response_current_time = api["location"]["localtime"]
            response_weather_description = api["current"]["weather_descriptions"]
            response_wind_speed = api["current"]["wind_speed"]
            response_humidity = api["current"]["humidity"]
            response_feels_like = api["current"]["feelslike"]
            response_visibility = api["current"]["visibility"]

        def submit():
            api_key_lookup.grid_forget()
            try:
                api_set()
                clear_buttons()

                if select_all_checkbox_var.get() == 1:
                    entry_type_checkbox.select()
                    exact_entry_checkbox.select()
                    latitude_checkbox.select()
                    longitude_checkbox.select()
                    city_checkbox.select()
                    current_temp_checkbox.select()
                    current_time_checkbox.select()
                    weather_description_checkbox.select()
                    wind_speed_checkbox.select()
                    humidity_checkbox.select()
                    feels_like_checkbox.select()
                    visibility_checkbox.select()

                # Set labels
                if entry_type_checkbox_var.get() == 1:
                    entry_type_label.config(text=f"Entry Type: {response_entry_type}")
                    entry_type_label.grid(row=1, column=0)

                if exact_entry_checkbox_var.get() == 1:
                    exact_entry_label.config(
                        text=f"Exact Entry: {response_exact_entry}"
                    )
                    exact_entry_label.grid(row=1, column=1)

                if latitude_checkbox_var.get() == 1:
                    latitude_label.config(text=f"Latitude: {response_latitude}")
                    latitude_label.grid(row=3, column=1)

                if longitude_checkbox_var.get() == 1:
                    longitude_label.config(text=f"Longitude: {response_longitude}")
                    longitude_label.grid(row=4, column=1)

                if city_checkbox_var.get() == 1:
                    city_label.config(text=f"City: {response_city}")
                    city_label.grid(row=2, column=0)

                if current_temp_checkbox_var.get() == 1:
                    current_temp_label.grid(row=3, column=0)
                    if unit.get() == "m":
                        temperature_symbol = "C"
                        current_temp_label.config(
                            text=f"Current Temperature: {response_current_temp}{degree_symbol}{temperature_symbol}"
                        )
                    elif unit.get() == "s":
                        temperature_symbol = "K"
                        current_temp_label.config(
                            text=f"Current Temperature: {response_current_temp}{temperature_symbol}"
                        )
                    elif unit.get() == "f":
                        temperature_symbol = "F"
                        current_temp_label.config(
                            text=f"Current Temperature: {response_current_temp}{degree_symbol}{temperature_symbol}"
                        )

                if current_time_checkbox_var.get() == 1:
                    current_time_label.config(
                        text=f"Current Time: {response_current_time}"
                    )
                    current_time_label.grid(row=2, column=1)

                if weather_description_checkbox_var.get() == 1:
                    weather_description_label.config(
                        text=f"Weather Description: {response_weather_description}"
                    )
                    weather_description_label.grid(row=1, column=2)

                if wind_speed_checkbox_var.get() == 1:
                    if unit.get() == "m" or unit.get() == "s":
                        wind_speed_label.config(
                            text=f"Wind Speed: {response_wind_speed}km/h"
                        )
                    elif unit.get() == "f":
                        wind_speed_label.config(
                            text=f"Wind Speed: {response_wind_speed}mph"
                        )
                    wind_speed_label.grid(row=2, column=2)

                if humidity_checkbox_var.get() == 1:
                    humidity_label.config(text=f"Humidity: {response_humidity}%")
                    humidity_label.grid(row=3, column=2)

                if feels_like_checkbox_var.get() == 1:
                    feels_like_label.config(
                        text=f"Feels Like: {response_feels_like}{degree_symbol}{temperature_symbol}"
                    )
                    feels_like_label.grid(row=4, column=0)

                if visibility_checkbox_var.get() == 1:
                    if unit.get() == "m" or unit.get() == "s":
                        visibility_label.config(
                            text=f"Visibility: {response_visibility}km"
                        )
                    elif unit.get() == "f":
                        visibility_label.config(
                            text=f"Visibility: {response_visibility}miles"
                        )
                    visibility_label.grid(row=4, column=2)

                city_lookup.delete(0, END)

            except:
                clear_buttons()
                city_lookup.grid_forget()
                my_button.grid_forget()
                error_label = Label(root, text="Error...", font="Helvetica")
                error_label.grid(row=0, column=0)

        # Set Labels
        entry_type_label = Label(root, font="Helvetica")
        exact_entry_label = Label(root, font="Helvetica", padx=10)
        latitude_label = Label(root, font="Helvetica")
        longitude_label = Label(root, font="Helvetica")
        city_label = Label(root, font="Helvetica")
        current_temp_label = Label(root, font="Helvetica")
        current_time_label = Label(root, font="Helvetica")
        weather_description_label = Label(root, font="Helvetica", padx=10)
        wind_speed_label = Label(root, font="Helvetica")
        humidity_label = Label(root, font="Helvetica")
        feels_like_label = Label(root, font="Helvetica")
        visibility_label = Label(root, font="Helvetica")

        # Radio Buttons
        unit = StringVar()
        unit.set("f")
        metric_button = Radiobutton(root, text="Metric", variable=unit, value="m")
        scientific_button = Radiobutton(
            root, text="Scientific", variable=unit, value="s"
        )
        fahrenheit_button = Radiobutton(
            root, text="Fahrenheit", variable=unit, value="f"
        )

        # Radio Button grid
        scientific_button.grid(row=3, column=2, stick=W)
        fahrenheit_button.grid(row=4, column=2, stick=W)
        metric_button.grid(row=5, column=2, stick=W)

        # Checkbox variables
        entry_type_checkbox_var = IntVar()
        exact_entry_checkbox_var = IntVar()
        latitude_checkbox_var = IntVar()
        longitude_checkbox_var = IntVar()
        city_checkbox_var = IntVar()
        current_temp_checkbox_var = IntVar()
        current_time_checkbox_var = IntVar()
        weather_description_checkbox_var = IntVar()
        wind_speed_checkbox_var = IntVar()
        humidity_checkbox_var = IntVar()
        feels_like_checkbox_var = IntVar()
        visibility_checkbox_var = IntVar()
        select_all_checkbox_var = IntVar()

        # Checkboxes
        entry_type_checkbox = Checkbutton(
            root, text="Entry Type", variable=entry_type_checkbox_var
        )
        exact_entry_checkbox = Checkbutton(
            root, text="Exact Entry", variable=exact_entry_checkbox_var
        )
        latitude_checkbox = Checkbutton(
            root, text="Latitude", variable=latitude_checkbox_var
        )
        longitude_checkbox = Checkbutton(
            root, text="Longitude", variable=longitude_checkbox_var
        )
        city_checkbox = Checkbutton(root, text="City", variable=city_checkbox_var)
        current_temp_checkbox = Checkbutton(
            root, text="Current Temperature", variable=current_temp_checkbox_var
        )
        current_time_checkbox = Checkbutton(
            root, text="Current Time", variable=current_time_checkbox_var
        )
        weather_description_checkbox = Checkbutton(
            root, text="Weather Description", variable=weather_description_checkbox_var
        )
        wind_speed_checkbox = Checkbutton(
            root, text="Wind Speed", variable=wind_speed_checkbox_var
        )
        humidity_checkbox = Checkbutton(
            root, text="Humidity", variable=humidity_checkbox_var
        )
        feels_like_checkbox = Checkbutton(
            root, text="Feels Like", variable=feels_like_checkbox_var
        )
        visibility_checkbox = Checkbutton(
            root, text="Visibility", variable=visibility_checkbox_var
        )
        select_all_checkbox = Checkbutton(
            root, text="Select All", variable=select_all_checkbox_var
        )

        # Checkbox grid
        entry_type_checkbox.grid(row=3, column=0, stick=W)
        exact_entry_checkbox.grid(row=4, column=0, stick=W)
        latitude_checkbox.grid(row=5, column=0, stick=W)
        longitude_checkbox.grid(row=6, column=0, stick=W)
        city_checkbox.grid(row=7, column=0, stick=W)
        current_temp_checkbox.grid(row=8, column=0, stick=W)
        current_time_checkbox.grid(row=3, column=1, stick=W)
        weather_description_checkbox.grid(row=4, column=1, stick=W)
        wind_speed_checkbox.grid(row=5, column=1, stick=W)
        humidity_checkbox.grid(row=6, column=1, stick=W)
        feels_like_checkbox.grid(row=7, column=1, stick=W)
        visibility_checkbox.grid(row=8, column=1, stick=W)
        select_all_checkbox.grid(row=9, column=0, columnspan=2)

        city_lookup = Entry(root)
        city_lookup.grid(row=0, column=0, stick=W + E + N + S)
        city_lookup.insert(END, "Enter a city or zipcode")

        my_button = Button(root, text="Submit", command=submit)
        my_button.grid(row=0, column=1, stick=W)

        api_key_lookup = Entry(root)
        api_key_lookup.grid(row=1, column=0, stick=W + E + N + S)
        api_key_lookup.insert(END, "afcf823a27c3bdabfe2a1e7e108a60d4")
    else:

        def api_set():
            global response_temp, response_date_time, city, response_high_temp, response_low_temp, df, number_of_days
            response_date_time = []
            response_temp = []
            response_high_temp = []
            response_low_temp = []
            city = city_lookup.get()
            number_of_days = 5
            for i in range(number_of_days):
                params = {
                    "key": "d0da5088f19041ce854543731a901d17",
                    "city": city_lookup.get(),
                    "start_date": date.today() - timedelta(days=number_of_days - i),
                    "end_date": date.today() - timedelta(days=number_of_days - 1 - i),
                    "units": unit.get(),
                }
                api_request = requests.get(
                    "http://api.weatherbit.io/v2.0/history/daily", params
                )
                api = api_request.json()
                response_temp.append(api["data"][0]["temp"])
                response_date_time.append(api["data"][0]["datetime"])
                response_high_temp.append(api["data"][0]["max_temp"])
                response_low_temp.append(api["data"][0]["min_temp"])
            df = pd.DataFrame()
            df["Date"] = response_date_time
            df["Average Temp"] = response_temp

        def submit():
            api_set()
            metric_button.grid_forget()
            scientific_button.grid_forget()
            fahrenheit_button.grid_forget()
            city_lookup.grid_forget()
            submit_city_button.grid_forget()

            x = []
            x.extend(range(number_of_days))
            y_avg = response_temp
            z_avg = np.polyfit(x, y_avg, 1)
            p_avg = np.poly1d(z_avg)
            plt.plot(x, p_avg(x), "--", label="y=%.6fx+(%.6f)" % (z_avg[0], z_avg[1]))
            y_high = response_high_temp
            z_high = np.polyfit(x, y_high, 1)
            p_high = np.poly1d(z_high)
            plt.plot(
                x, p_high(x), "--", label="y=%.6fx+(%.6f)" % (z_high[0], z_high[1])
            )
            y_low = response_low_temp
            z_low = np.polyfit(x, y_low, 1)
            p_low = np.poly1d(z_low)
            plt.plot(x, p_low(x), "--", label="y=%.6fx+(%.6f)" % (z_low[0], z_low[1]))
            plt.plot(df["Date"], df["Average Temp"])
            plt.plot(response_high_temp)
            plt.plot(response_low_temp)
            plt.ylabel("Average Temp(" + degree_symbol + "F)")
            plt.title(label="Average Temperature of " + city)
            plt.legend()
            plt.show()

        city_lookup = Entry(root)
        city_lookup.grid(row=0, column=0, stick=W + E + N + S)
        city_lookup.insert(END, "Dallas")

        submit_city_button = Button(root, text="Submit", command=submit)
        submit_city_button.grid(row=0, column=1, stick=W)

        # Radio Buttons
        unit = StringVar()
        unit.set("I")
        metric_button = Radiobutton(root, text="Metric", variable=unit, value="M")
        scientific_button = Radiobutton(
            root, text="Scientific", variable=unit, value="S"
        )
        fahrenheit_button = Radiobutton(
            root, text="Fahrenheit", variable=unit, value="I"
        )

        # Radio Button grid
        scientific_button.grid(row=1, column=0, stick=W)
        fahrenheit_button.grid(row=2, column=0, stick=W)
        metric_button.grid(row=3, column=0, stick=W)


weather_view = StringVar()
weather_view.set("current")
current_weather_button = Radiobutton(
    root, text="Current Weather", variable=weather_view, value="current"
)
historical_weather_button = Radiobutton(
    root, text="Historical Weather", variable=weather_view, value="historical"
)

current_weather_button.grid(row=0, column=0, stick=W)
historical_weather_button.grid(row=1, column=0, stick=W)

submit_weather_view_button = Button(root, text="Submit", command=submit_weather_view)
submit_weather_view_button.grid(row=2, column=0)


root.mainloop()