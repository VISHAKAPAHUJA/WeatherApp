from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk

window = Tk()
window.title("WEATHER APP")
window.geometry('800x700')
window.configure(bg="#F0F0F0")  # Light gray background

# Title Label
title_label = Label(window, text="WEATHER APP", font=("Brush Script MT", 40, "bold"), fg="#333333", bg="#F0F0F0")
title_label.place(x=200, y=20)

# Countries List
countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina",
             "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
             "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana",
             "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
             "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
             "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica", "Croatia", "Cuba",
             "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
             "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
             "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",
             "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
             "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
             "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",
             "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
             "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali",
             "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
             "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal",
             "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman",
             "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
             "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
             "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
             "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
             "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
             "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga",
             "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
             "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
             "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]

# City Selection Combobox
city_var = StringVar()
city_combobox = ttk.Combobox(window, textvariable=city_var, values=countries, font=("Arial", 14), width=40, state="readonly")
city_combobox.place(x=150, y=100)

# Weather Display Frame
weather_frame = Frame(window, bg="#FFFFFF", width=600, height=420)
weather_frame.place(x=100, y=150)

# Weather Icons
cloud_icon = Image.open(r"C:\Users\Aman\Desktop\python_AI\cloud.png")
cloud_icon = cloud_icon.resize((200, 200))
cloud_image = ImageTk.PhotoImage(cloud_icon)
cloud_label = Label(weather_frame, image=cloud_image, bg="#FFFFFF")
cloud_label.place(x=50, y=20)

sunrise_icon = Image.open(r"C:\Users\Aman\Desktop\python_AI\sunrise.png")
sunrise_icon = sunrise_icon.resize((50, 50))
sunrise_image = ImageTk.PhotoImage(sunrise_icon)
sunrise_label = Label(weather_frame, image=sunrise_image, bg="#FFFFFF")
sunrise_label.place(x=60, y=250)

sunset_icon = Image.open(r"C:\Users\Aman\Desktop\python_AI\sunset.png")
sunset_icon = sunset_icon.resize((50, 50))
sunset_image = ImageTk.PhotoImage(sunset_icon)
sunset_label = Label(weather_frame, image=sunset_image, bg="#FFFFFF")
sunset_label.place(x=60, y=320)

# Weather Details Labels
weather_labels = ["Climate", "Description", "Temperature", "Pressure", "Wind Speed", "Sunrise", "Sunset"]
for i, label in enumerate(weather_labels):
    lbl = Label(weather_frame, text=label, font=("Arial", 14, "bold"), bg="#FFFFFF", fg="#333333")
    lbl.place(x=250, y=20 + i * 50)

# Weather Data Labels
weather_data = [StringVar() for _ in range(len(weather_labels))]
for i, data in enumerate(weather_data):
    txt = Label(weather_frame, textvariable=data, font=("Arial", 14), bg="#FFFFFF", fg="#333333")
    txt.place(x=380, y=20 + i * 50)

# Get Weather Button
def get_weather():
    api_key = '52f741de75961956e7ed5b298199310d'
    city_name = city_var.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    data = requests.get(url).json()
    weather_data[0].set(data['weather'][0]['main'])
    weather_data[1].set(data['weather'][0]['description'])
    weather_data[2].set(f"{int(data['main']['temp'] - 273.15)} °C")
    weather_data[3].set(f"{data['main']['pressure']} hPa")
    weather_data[4].set(f"{data['wind']['speed']} m/s")
    weather_data[5].set(f"{data['sys']['sunrise']} UTC")
    weather_data[6].set(f"{data['sys']['sunset']} UTC")

get_weather_button = Button(window, text="GET WEATHER", bg="#336699", fg="#FFFFFF", font=("Arial", 14, "bold"), command=get_weather)
get_weather_button.place(x=300, y=600)

window.mainloop()
