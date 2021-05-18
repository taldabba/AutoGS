from pyautogui import press, typewrite, hotkey, position, moveTo,click

import time

def spamPicture():
	# pyperclip.copy(link)
	hotkey('ctrl','v')
	press('enter')

for x in range(5):
	print(f'SPAMMING IN: {x} SECONDS')
	time.sleep(1)

for x in range(100):
	# print(position())
	moveTo(630,700)

	spamPicture()
	click()
	time.sleep(0.1)



# for x in range(3):
# 	spamPicture()
# 	time.sleep(0.2)


	# if x == 1:

#630 700