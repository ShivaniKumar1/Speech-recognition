# Beginner python speech recognition program
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
	print("Say something!")
	audio = recognizer.listen(source)

print("Google thinks you said:")
print(recognizer.recognize_google(audio))

words = recognizer.recognize_google(audio)

if "hello" in words:
    print("Hello to you too!")
elif "how are you" in words:
    print("I'm good")
elif "bye" in words:
    print("goodbye")
    
matches = re.search("my name is (.*)", words)

if matches:
	print(f"Hey, {matches}.")
else:
	print("Hey, you.")
