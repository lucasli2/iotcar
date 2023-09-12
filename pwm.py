import lgpio
import time

ESC_PIN = 18
RC_FREQ = 50 #Might vary, 100hz also viable

esc = lgpio.gpiochip_open(0)
print("Initialized ESC")

targetFreq = 0
while (1):
	print(f"Setting Target Power to {targetFreq};")
	lgpio.tx_pwm(esc, ESC_PIN,RC_FREQ,targetFreq)
	time.sleep(5/RC_FREQ)

	targetFreq = int(input("ESC POWER 0-100: "))
	if targetFreq == 666:
		print("Stopping")
		break
	elif targetFreq>100: targetFreq = 100
	elif targetFreq<0: targetFreq = 0


lgpio.gpiochip_close(esc)
