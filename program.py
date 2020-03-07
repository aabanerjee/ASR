#Python 2.x program for Speech Recognition 
  
import speech_recognition as sr
import webbrowser as wb
import speech

#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer()

#use the microphone as source for input.

with sr.Microphone(device_index = 0, sample_rate = sample_rate, chunk_size = chunk_size) as source: 
    #wait for a second to let the recognizer adjust the  
    #energy threshold based on the surrounding noise level 
    r.adjust_for_ambient_noise(source) 
    while(1):
	print("Listning....")
	audio=r.listen(source)
	try: 
                s = r.recognize_google(audio)
                if(s.lower()=="jarvis"):
                        print("Say Something...")
                        s = r.recognize_google(audio)
                        wb.open("https://www.google.com/search?q="+s.lower().replace("search ",""))
                        speech.say("Showing Result For "+s.lower().replace("search ",""))
                elif(s.lower()=="bye bye" or s.lower()=="bye-bye" or s.lower()=="bye"):
                        print("Good Bye")
                        speech.say("Good Bye")
                        break
      
    #error occurs when google could not understand what was said 
      
        except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 
      
        except sr.RequestError as e: 
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


