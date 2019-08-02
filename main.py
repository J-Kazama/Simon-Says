# This program runs on a Raspberry Pi with proper hardware to
# play Simon Says. The main implementation of the game starts at
# line 49 in the loop() method which generates rounds in coherence with
# UI (LEDs, buttons, and a buzzer) and waits for user inputs to see that
# he or she enters the correct sequence per round.

import RPi.GPIO as GPIO
import random
import time

# Setting up hardware

LedRed = 40      # Red LED
LedGreen = 38    # Green LED
LedYellow = 36   # Yellow LED
LedBlue = 32     # Blue LED

BtnRed = 37
BtnGreen = 35
BtnYellow = 33
BtnBlue = 31
BZRPin = 11

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(BZRPin, GPIO.LOW)

p = GPIO.PWM(BZRPin, 100) # initial frequency: 50HZ
p.start(50)               # Duty cycle: 50%


#Setting up the GPIOs
def setup():
            GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
            GPIO.setup(LedRed, GPIO.OUT)   # Set LedPin's mode is output
            GPIO.setup(LedGreen, GPIO.OUT)
            GPIO.setup(LedYellow, GPIO.OUT)
            GPIO.setup(LedBlue, GPIO.OUT)

            GPIO.setup(BtnRed, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set BtnPin's mode is input, and pull up to high level(3.3V)
            GPIO.setup(BtnGreen, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(BtnYellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(BtnBlue, GPIO.IN, pull_up_down=GPIO.PUD_UP)

            GPIO.output(LedRed, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off
            GPIO.output(LedGreen, GPIO.HIGH)
            GPIO.output(LedYellow, GPIO.HIGH)
            GPIO.output(LedBlue, GPIO.HIGH)

# Algorithm of Simon Says
def loop():
        while True:
                if GPIO.input(BtnRed) == GPIO.LOW:
                        GPIO.output(LedRed, GPIO.LOW)
                        p.ChangeFrequency(200)
                        time.sleep(0.5)
                        p.ChangeFrequency(0)
                if GPIO.input(BtnGreen) == GPIO.LOW:
                        GPIO.output(LedGreen, GPIO.LOW) # led on
                        p.ChangeFrequency(400)
                        time.sleep(0.5)
                        p.ChangeFrequency(0)
                if GPIO.input(BtnYellow) == GPIO.LOW:
                        GPIO.output(LedYellow, GPIO.LOW) # led on
                        p.ChangeFrequency(600)
                        time.sleep(0.5)
                        p.changeFreqeuncy(0)
                if GPIO.input(BtnBlue)  == GPIO.LOW:
                        GPIO.output(LedBlue, GPIO.LOW) # led on
                        p.ChangeFreqeuncy(800)
                        time.sleep(0.5)
                        p.ChangeFrequency(0)
                else:
                        GPIO.output(LedRed, GPIO.HIGH) # led off
                        GPIO.output(LedGreen, GPIO.HIGH) # led off
                        GPIO.output(LedYellow, GPIO.HIGH) # led off
                        GPIO.output(LedBlue, GPIO.HIGH) # led off

                generatemove = [0,0,0,0,0,0,0,0,0,0] # Array to save value of leds lit, and to compare buttons clicked
                usermove = [0,0,0,0,0,0,0,0,0,0]     # This array corresponds to the buttons clicked by the player
                print('Remember the sequenc!')
                time.sleep(0.5)

                j = 0
                i = 1
                led = 0
                k = 0

                # The integer in the while loop's condition determines the number of rounds (Simon Says has 10 rounds)
                while (i<11):
                    while (j<i):
	                    # If statement to check if last move reached (iteration wise), only then generate a random move
                        if (j == i-1):
                            led = random.randint(1,5)
                            if led == 1:
                                GPIO.output(LedRed, GPIO.LOW)
                                generatemove[j] = led
                                p.ChangeFrequency(200)
                                time.sleep(0.5)
                                p.ChangeFrequency(1)
                                GPIO.output(LedRed, GPIO.HIGH)
                                time.sleep(0.5)
                                j = j+1
                            if led == 2:
                                GPIO.output(LedGreen, GPIO.LOW)
                                generatemove[j] = led
                                p.ChangeFrequency(400)
                                time.sleep(0.5)
                                p.ChangeFrequency(1)
                                GPIO.output(LedGreen, GPIO.HIGH)
                                time.sleep(0.5)
                                j= j+1
                            if led == 3:
                                GPIO.output(LedYellow, GPIO.LOW)
                                generatemove[j] = led
                                p.ChangeFrequency(600)
                                time.sleep(0.5)
                                p.ChangeFrequency(1)
                                GPIO.output(LedYellow, GPIO.HIGH)
                                time.sleep(0.5)
                                j = j+1
                            if led == 4:
                                GPIO.output(LedBlue, GPIO.LOW)
                                generatemove[j] = led
                                p.ChangeFrequency(800)
                                time.sleep(0.5)
                                p.ChangeFrequency(1)
                                GPIO.output(LedBlue, GPIO.HIGH)
                                time.sleep(0.5)
                                j=j+1
                        # If not last move, then lit leds which were already saved
                        else:
                            led = generatemove[j]
                            if led == 1:
                                GPIO.output(LedRed, GPIO.LOW)
                                p.ChangeFrequency(201)
                                time.sleep(0.5)
                                p.ChangeFrequency(100)
                                GPIO.output(LedRed, GPIO.HIGH)
                                time.sleep(0.5)
                                j = j+1
                            if led == 2:
                                GPIO.output(LedGreen, GPIO.LOW)
                                p.ChangeFrequency(401)
                                time.sleep(0.5)
                                p.ChangeFrequency(100)
                                GPIO.output(LedGreen, GPIO.HIGH)
                                time.sleep(0.5)
                                j = j+1
                            if led == 3:
                                GPIO.output(LedYellow, GPIO.LOW)
                                p.ChangeFrequency(601)
                                time.sleep(0.5)
                                p.ChangeFrequency(100)
                                GPIO.output(LedYellow, GPIO.HIGH)
                                time.sleep(0.5)
                                j= j+1
                            if led == 4:
                                GPIO.output(LedBlue, GPIO.LOW)
                                p.ChangeFrequency(801)
                                time.sleep(0.5)
                                p.ChangeFrequency(100)
                                GPIO.output(LedBlue, GPIO.HIGH)
                                time.sleep(0.5)
                                j=j+1

                    button = 0
                    k = 0
                    x = 1

                    # Here we wait for the user input, each time we click number of buttons corresponding to
                    # the stage of the game, again while using the same array from before to check correct buttons are
                    # clicked. If the wrong button is clicked – user fails and it indicates on terminal while
                    # program finishes.
                    while (k<i and k!=-1):
                        h = 0
                        while (h<i):
                            x =1
                            if ((x==1) and (GPIO.input(BtnRed) == GPIO.LOW or GPIO.input(BtnGreen) == GPIO.LOW or GPIO.input(BtnYellow) == GPIO.LOW or GPIO.input(BtnBlue) == GPIO.LOW)):
                                print('button clicked')
                                x=0
                                if  GPIO.input(BtnRed) == GPIO.LOW:
                                    GPIO.output(LedRed, GPIO.LOW)
                                    button = 1
                                    k=k+1
                                    p.ChangeFrequency(202)

                                    print ('You Selected Red')
                                    x = 0
                                    time.sleep(0.2)
                                elif GPIO.input(BtnGreen) == GPIO.LOW:
                                    GPIO.output(LedGreen, GPIO.LOW)
                                    button = 2
                                    k=k+1
                                    x = 0
                                    p.ChangeFrequency(402)
                                    print ('You Selected Green')
                                    time.sleep(0.2)
                                elif GPIO.input(BtnYellow) == GPIO.LOW:
                                    GPIO.output(LedYellow, GPIO.LOW)
                                    button = 3
                                    k=k+1
                                    x = 0
                                    p.ChangeFrequency(602)
                                    print('You selected Yeloow')
                                    time.sleep(0.2)
                                elif GPIO.input(BtnBlue) == GPIO.LOW:
                                    GPIO.output(LedBlue, GPIO.LOW)
                                    button = 4
                                    k=k+1
                                    x=0
                                    p.ChangeFrequency(802)
                                    print('You selected  Blue')
                                    time.sleep(0.2)
                                usermove[h] = button
                                time.sleep(0.5)
                                if (button == generatemove[h]) and (h == i-1):
                                    print('Correct\n')
                                    print('Red=1,Green=2,Yeloow=3,Blue=4')
                                    print(generatemove)
                                if button != generatemove[h]:
                                    i = 0
                                    j = 0
                                    led = 0
                                    k = 0
                                    # When the user clicks the wrong buttons
                                    print('GAME OVER!, Try Again!')
                                    print('Red=1,Green=2,Yeloow=3,Blue=4')
                                    print(usermove)
                                h = h+1
                                GPIO.output(LedRed, GPIO.HIGH)    # led off
                                GPIO.output(LedGreen, GPIO.HIGH)  # led off
                                GPIO.output(LedYellow, GPIO.HIGH) # led off
                                GPIO.output(LedBlue, GPIO.HIGH)   # led off
                                p.ChangeFrequency(100)

                    # Next round
                    i=i+1
                    j=0

def destroy():
        GPIO.output(LedRed, GPIO.HIGH)        # led off
        GPIO.output(LedGreen, GPIO.HIGH)
        GPIO.output(LedYellow, GPIO.HIGH)     # led off
        GPIO.output(LedBlue, GPIO.HIGH)
        GPIO.cleanup()                        # Release resource

if __name__ == '__main__':     # Program starts here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed (termination).
                destroy()
