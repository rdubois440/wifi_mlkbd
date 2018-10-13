'''
Todo
====

Esperanto - bepo - amharique - ousseau (musique) - custom alphabet Gabriel - 
Use the Esperanto kbd on Android
IMplement the AZERTY
Identify the keyboard layout from the program

Done
Use a cheaper ESP8266 + micropro instead of Yun (faster boot as well)
Temporarily, ask the user for the kbd layout

Runtime environment setup - esp8266 + micropro3
===============================================

Connect combo board (esp8266 + micropro3) to the laptop (power + hid emulation + wifi server)
Boot time 10 seconds

Connect the mobile phone to the esp8266 wifi

on the phone, termux session
python multi_lang_kbd.py

Choose kbd layout on the PC
Choose the same layout on the android
Todo - indicate the layout on the termux program

On esp8266 + micropro3, use the AT standard commands on the esp8266, and the micropro3_wifi_mlkbd.ino on the micropro3

Development environment setup - Yun
===================================

Connect arduino Yun to the laptop (power + hid emulation + wifi server)

Connect the phone to the laptop (adb connection)
Connect the mobile phone to the Yun wifi

Start sshd in termux on the phone

adb connection to the phone from the laptop
In a cygwin session, 
cd /cygdrive/c/Floppies/PortableApps/Android/platform-tools/
 ./adb forward tcp:8022 tcp:8022
 ssh localhost -p 8022 -i /cygdrive/c/~rene/doc/id_rsa

Start ser2net on the Yun - From the adb session on the phone
ssh root@192.168.240.1
cd /home/rene
./ser2net.sh
Exit the ssh session

on the phone, termux session
python multi_lang_kbd.py

Edit the file in the local PC and send to the phone for testing
Test on the phone with the various keyboard layouts

On Yun, use the yun_tty2kbdandmouse.ino

On esp8266 + micropro3, use the AT standard commands on the esp8266, and the micropro3_wifi_mlkbd.ino on the micropro3




'''





import struct
import time
import sys
import telnetlib
import string
import curses


#tn = telnetlib.Telnet("192.168.240.1", 5055)
#tn = telnetlib.Telnet("10.0.0.10", 5055)
#print("After initiatin telnet")
#print tn.read_all()

press = "0 97 1\n"
release = "0 97 0\n"

language = 0

#while True:
	#tn.write(press)
	#tn.write(release)
	#time.sleep(5)


def updateTitle(msg):
	boxTitle.box()
	boxTitle.erase()
	boxTitle.addstr(0,0,msg[0:40])
	boxTitle.refresh()

	
	boxFirst.box()
	if (language == 0):
		boxFirst.addstr(1,1, " en-us  ", curses.color_pair(1))
		boxFirst.addstr(2,1, " Qwerty ", curses.color_pair(1))
	else:
		boxFirst.addstr(1,1, " en-us  ")
		boxFirst.addstr(2,1, " Qwerty ")
	boxFirst.refresh()


	boxSecond.box()
	if (language == 1):
		boxSecond.addstr(1,1, " fr-fr  ", curses.color_pair(1))
		boxSecond.addstr(2,1, " Azerty ", curses.color_pair(1))
	else:
		boxSecond.addstr(1,1, " fr-fr  ")
		boxSecond.addstr(2,1, " Azerty ")
	boxSecond.refresh()

	boxThird.box()
	if (language == 2):
		boxThird.addstr(1,1, "  Bepo  ", curses.color_pair(1))
		boxThird.addstr(2,1, "        ", curses.color_pair(1))
	else:
		boxThird.addstr(1,1, "  Bepo  ")
	boxThird.refresh()

	boxFourth.box()
	if (language == 3):
		boxFourth.addstr(1,1, " fr-ch  ", curses.color_pair(1))
		boxFourth.addstr(2,1, " Qwertz ", curses.color_pair(1))
	else:
		boxFourth.addstr(1,1, " fr-ch  ")
		boxFourth.addstr(2,1, " Qwertz ")
	boxFourth.refresh()

	boxFifth.box()
	if (language == 4):
		boxFifth.addstr(1,1, " Esper  ", curses.color_pair(1))
		boxFifth.addstr(2,1, " anto   ", curses.color_pair(1))
	else:
		boxFifth.addstr(1,1, " Esper  ")
		boxFifth.addstr(2,1, " anto   ")
	boxFifth.refresh()

	boxSixth.box()
	if (language == 5):
		boxSixth.addstr(1,1, " Hebrew ", curses.color_pair(1))
	else:
		boxSixth.addstr(1,1, " Hebrew ")
	boxSixth.refresh()

	boxSeventh.box()
	boxSeventh.refresh()

	boxEigth.box()
	boxEigth.refresh()



if __name__ == "__main__":

	screen = curses.initscr()
	#curses.curs_set(0) 
	screen.keypad(1)
	curses.mousemask(1)
	curses.noecho() 
	curses.cbreak() 

	curses.start_color()
	curses.init_pair(1,curses.COLOR_WHITE, curses.COLOR_BLUE)
	highlightText = curses.color_pair( 1 )

	boxTitle = curses.newwin(3, 45, 0, 0)
	boxTitle.box()
	boxTitle.refresh()


	boxFirst = curses.newwin(4, 10, 7, 0)
	boxFirst.box()
	#boxFirst.addstr(1,1, " en-us  ", curses.color_pair(1))
	#boxFirst.addstr(2,1, " Qwerty ", curses.color_pair(1))
	#boxFirst.refresh()

	boxSecond = curses.newwin(4, 10, 7, 11)
	boxSecond.box()
	#boxSecond.addstr(1,1, " fr-fr  ")
	#boxSecond.addstr(2,1, " Azerty ")
	#boxSecond.refresh()

	boxThird = curses.newwin(4, 10, 7, 22)
	boxThird.box()
	#boxThird.addstr(1,1, "  Bepo  ")
	#boxThird.addstr(2,1, "        ")
	#boxThird.refresh()

	boxFourth = curses.newwin(4, 10, 7, 33)
	boxFourth.box()
	#boxFourth.addstr(1,1, " fr-ch  ")
	#boxFourth.addstr(2,1, " Qwertz ")
	#boxFourth.refresh()

	boxFifth = curses.newwin(4, 10, 12, 0)
	boxFifth.box()
	#boxFifth.addstr(1,1, " Esper  ")
	#boxFifth.addstr(2,1, " anto   ")
	#boxFifth.refresh()

	boxSixth = curses.newwin(4, 10, 12, 11)
	boxSixth.box()
	#boxSixth.addstr(1,1, " Hebrew ")
	#boxFifth.refresh()
	#boxSixth.refresh()

	boxSeventh = curses.newwin(4, 10, 12, 22)
	boxSeventh.box()
	boxSeventh.refresh()

	boxEigth = curses.newwin(4, 10, 12, 33)
	boxEigth.box()
	boxEigth.refresh()

	updateTitle("Starting")
	time.sleep(2)

	azerty_lookup = []
	bepo_lookup = []
	qwertz_lookup = []
	esperanto_lookup = []
	hebrew_lookup = []

	for i in range(255):
		azerty_lookup.append(i)
		bepo_lookup.append(i)
		qwertz_lookup.append(i)
		esperanto_lookup.append(i)
		hebrew_lookup.append(i)

	#azerty[0xa7] = 0x65	#kuf to e

	hebrew_lookup[0xa7] = 0x65	#kuf to e
	hebrew_lookup[0xa8] = 0x72	#resh to r
	hebrew_lookup[0x90] = 0x74	#alef to t
	hebrew_lookup[0x98] = 0x79	#tet to y
	hebrew_lookup[0x95] = 0x75	#vav to u
	hebrew_lookup[0x9f] = 0x69	#nun final to i
	hebrew_lookup[0x9d] = 0x6f	#mem final to o
	hebrew_lookup[0xa4] = 0x70	#pe to p

	hebrew_lookup[0xa9] = 0x61	#shin to a
	hebrew_lookup[0x93] = 0x73	#daled to s
	hebrew_lookup[0x92] = 0x64	#gimel to d
	hebrew_lookup[0x9b] = 0x66	#caf to f
	hebrew_lookup[0xa2] = 0x67	#Ayin to g
	hebrew_lookup[0x99] = 0x68	#iud to h
	hebrew_lookup[0x97] = 0x6a	#het to j
	hebrew_lookup[0x9c] = 0x6b	#lamed to k
	hebrew_lookup[0x9a] = 0x6c	#caf final to l
	hebrew_lookup[0xa3] = 0x3b	#pei final to colon

		
	hebrew_lookup[0x96] = 0x7a	#zayin to z
	hebrew_lookup[0xa1] = 0x78	#samekh to x
	hebrew_lookup[0x91] = 0x63	#bet to c
	hebrew_lookup[0x94] = 0x76	#hei to v
	hebrew_lookup[0xa0] = 0x62	#nun to b
	hebrew_lookup[0x9e] = 0x6e	#mem to n
	hebrew_lookup[0xa6] = 0x6d	#zadi to m
	hebrew_lookup[0xaa] = 0x2c	#taf to comma
	hebrew_lookup[0xa5] = 0x2e	#zadi final to dot

	updateTitle("Before Telnet connexion")
	#time.sleep(2)
	#tn = telnetlib.Telnet("10.0.0.8", g055g
	#tn = telnetlib.Telnet("192.168.240.1", 5055)

	tn = telnetlib.Telnet("192.168.4.1", 8888)
	updateTitle("After Telnet connexion - please wait")

	time.sleep(2)
	updateTitle("Ready")
	screen.refresh()


	updateTitle("Presss q to Terminate " ) 

	while True:
		event = screen.getch() 

		if event == ord("q"): 
			break 
		if event == curses.KEY_MOUSE:
			_, mx, my, _, _ = curses.getmouse()
			#y, x = screen.getyx()

			updateTitle("Mouse key press at " + str(mx) + " - " + str(my))


#        boxFirst = curses.newwin(4, 10, 7, 0)
#        boxSecond = curses.newwin(4, 10, 7, 11)
#        boxThird = curses.newwin(4, 10, 7, 22)
#        boxFourth = curses.newwin(4, 10, 7, 33)
#        boxFifth = curses.newwin(4, 10, 12, 0)
#        boxSixth = curses.newwin(4, 10, 12, 11)
#        boxSeventh = curses.newwin(4, 10, 12, 22)
#        boxEigth = curses.newwin(4, 10, 12, 33)

			if (my >= 7) and (my <= 10): 
				if ((mx > 0) and (mx < 10)):
					language = 0
					updateTitle("Clicked First")
				if ((mx > 11) and (mx < 21)):
					language = 1
					updateTitle("Clicked Second")
				if ((mx > 22) and (mx < 32)):
					language = 2
					updateTitle("Clicked Third")
				if ((mx > 33) and (mx < 43)):
					language = 3
					updateTitle("Clicked Fourth")

			if (my >= 12) and (my <= 16): 
				if ((mx > 0) and (mx < 10)):
					language = 4
					updateTitle("Clicked Fifth")
				if ((mx > 11) and (mx < 21)):
					language = 5
					updateTitle("Clicked Sixth")
				if ((mx > 22) and (mx < 32)):
					language = 6
					updateTitle("Clicked Seventh")
				if ((mx > 33) and (mx < 43)):
					language = 7
					updateTitle("Clicked Eighth")



		if (event == 0x7f):			# 0x7f Backspacej
			press = str("0 " + str(0xb2) +  " 1\n")
			release = str("0 " + str(0xb2) +  " 0\n")

		if (event == 0xd7):			# hebrew keyboard
			language = 5
			#screen.erase()
			#updateTitle("hebrew keyboard")
			event = screen.getch() 
			#updateTitle(hex(event))
			#press = "0 97 1\n"
			#release = "0 97 0\n"
			press = str("0 " + str(hebrew_lookup[event]) +  " 1\n")
			release = str("0 " + str(hebrew_lookup[event]) +  " 0\n")
		else:
			#screen.erase()
			if (language == 0):	#Qwerty
				updateTitle(hex(event))
				press = str("0 " + str(event) +  " 1\n")
				release = str("0 " + str(event) +  " 0\n")
			elif (language == 1):
				#press = str("0 " + str(azerty_lookup[event]) +  " 1\n")
				#release = str("0 " + str(azerty_lookup[event]) +  " 0\n")
				pass
			elif (language == 2):
				#press = str("0 " + str(bepo_lookup[event]) +  " 1\n")
				#release = str("0 " + str(bepo_lookup[event]) +  " 0\n")
				pass
			elif (language == 3):
				#press = str("0 " + str(qwertz_lookup[event]) +  " 1\n")
				#release = str("0 " + str(qwertz_lookup[event]) +  " 0\n")
				pass
			elif (language == 4):
				#press = str("0 " + str(esperanto_lookup[event]) +  " 1\n")
				#release = str("0 " + str(esperanto_lookup[event]) +  " 0\n")
				pass

		tn.write(press.encode('ascii'))
		#tn.write(release.encode('ascii'))
		updateTitle("After writing " + press)

		if (event == 263):
				#screen.erase()
				pass


	curses.endwin()
