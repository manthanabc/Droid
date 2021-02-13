from time import sleep
import youtubefunctions as t
import speech_recognition as sr



r=sr.Recognizer()
def listen():
	with sr.Microphone() as source:
		print("speck:")
		audio=r.listen(source)
		try:
			ans=r.recognize_google(audio)
			'''
			.recognize_bing .recognizer_
			sr.adjust_for_ambient_noise()

			'''
			print(ans)
			return ans
		except sr.UnknownValueError:
			print('error')
		except sr.RequestError as e:
			print(format(e))
		return False

ans=listen()
if(ans):

	t.search(ans)
	#t.search('once i was 7')
	t.load()
	p=t.play()
	sleep(5)
	ans2=listen()
	if (ans2):
		t.change(ans)
	
	while t in t.lst :
		t.play()

		'''

		sleep(2)
		print('playing')
		sleep(3)
		print('pausing')  
		t.change('pause')
		sleep(3)
		print('resuming')
		t.change('pause')
		sleep(3)
		print('test done')

        '''

       