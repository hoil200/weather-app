import tkinter as tk
from tkinter import *
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800

#548d5d295d26db34a190cdfa81b618b6
#api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}

def test_function(entry):
    print( "This is the entry: ", entry)

def get_weather(city):
    weather_key = '548d5d295d26db34a190cdfa81b618b6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q' : city,'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
    
    
    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])
    label['text'] = format_response(weather)
    #print(response.json())
def format_response(weather):
    
    try:
        name = (weather['name'])
        desc = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])
        final_str = 'City: %s \nConditions: %s \nTemperature °F: %s' %(name,desc,temp)
        #str(name) + ' ' + str(desc) + ' ' + str(temp)
      
    except:
       
        final_str = 'There was a problem retrieving that information'
       
    return final_str
    
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH)
canvas.pack()


background_image = tk.PhotoImage(file='clouds.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame = tk.Frame(root, bg = '#cef5df', bd=5)
frame.place(relx = 0.5, rely=0.1,relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame,text="Get Weather",bg='#ffe2cf',fg='black', font = ('Courier', 15), command=lambda:get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth =0.3, relheight=1)


entry = tk.Entry(frame, font = ('Courier', 30))
entry.place( relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg = '#cef5df', bd=10)
lower_frame.place(relx = 0.5, rely=0.25,relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = ('Courier', 25), anchor='nw',justify='left', bd=4, wraplength = 500 )
label.place(relwidth=1, relheight=1)

#print (tk.font.families())
root.mainloop()