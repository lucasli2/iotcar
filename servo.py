import lgpio
import time

SERVO_PIN = 19
SERVO_FREQ = 50

servo = lgpio.gpiochip_open(0) #Neutral Position at 50

targetPos = 50

while 1:
	lgpio.tx_pwm(servo, SERVO_PIN, SERVO_FREQ, targetPos)
	print(f"Set Servo to position {targetPos}")
	time.sleep(5/SERVO_FREQ)

	targetPos = int(input("TARGET SERVO POSITION (0-100): "))
	if targetPos >100: targetPos = 100
	if targetPos <0: targetPos = 0
	if targetPos == 666:
		print("End Loop")
		break

lgpio.gpiochip_close(servo)



