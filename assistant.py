import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Language Option
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


# Hear micorphone and convert as a text
def transform_audio_into_text():

    # store recognizer in variable

    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:
        # waiting time
        r.pause_threshold = 0.5

        # report that recording has began
        print("You can now speak")

        # Save what you hear as audio
        audio = r.listen(source)

        try:
            # Serach on google
            request = r.recognize_google(audio , language="en-gb")

            # test in text
            print("You said " + request)

            # Return request
            return request
        # In case it does not recoginze audio
        except sr.UnknownValueError:
            print("OOPS! I did not understand")
            return "I am still waiting"

        # In case request can not be resolved
        except sr.RequestError:
            print("OOPS! there is no service")
            return "I am still waiting"

        # Unexpected error
        except:
            print("OOPS! Something Went Wrong")
            return "I am still waiting"

# Function so the assistant can be heard
def speak(message):
    # Start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Deliver message
    engine.say(message)
    engine.runAndWait()

engine = pyttsx3.init()


for voice in engine.getProperty('voices'):
    print(voice)

# Inform the day of the week
def ask_day():
    day = datetime.date.today()
    print(day)

    week_day = day.weekday()
    print(week_day)

    # Calander
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    speak(f'Today is {calendar[week_day]}')


# Inform what time is it

def ask_time():
    time = datetime.datetime.now()
    time = f'At this moment it is {time.hour} hours and {time.minute} minutes'
    print(time)

    # Speak the time
    speak(time)


# Create Initial Greetings

def initial_greeting():

    speak("Hi I am your assistant! how can i help you")

# main function of the assistant
def my_assistant():
    # Activate initial greetings
    initial_greeting()

    # cut off variable
    go_one = True

    # main loop
    while go_one:


        # activate microphone and save request
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak("sure i am opening youtube")
            webbrowser.open('https://www.youtube.com/')
            continue

        elif 'open browser' in my_request:
            speak("off course I am on it ")
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue

        elif 'what date it is' in my_request:
            ask_time()
            continue

        elif 'do a wikipedia search for' in my_request:
            speak("I am looking for it")
            my_request = my_request.replace('do a wikipedia serch for', '')
            answer = wikipedia.summary(my_request , sentences=1)
            speak('according to wikipedia ')
            speak(answer)
            continue

        elif 'search the internet search for' in my_request:
            speak("OK! I am on it")
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak("This is What i found")
            continue

        elif 'play' in my_request:
            speak("oh! what a great idea. I will play it right now")
            pywhatkit.playonyt(my_request)
            continue

        elif 'joke' in my_request:
            speak(pyjokes.get_joke())
            continue

        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {'apple': 'APPL',
                         'amazon': 'AMZN',
                         'google': 'GOOGL'
                         }
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info('regularMarketPrice')
                speak(f'I found the price of {share} is the {price}')
                continue
            except:
                speak('Sorry I did not find it')
                continue

        elif 'goodbye' in my_request:
            speak("I am going to rest. if you need anything call me again")
            break


my_assistant()




