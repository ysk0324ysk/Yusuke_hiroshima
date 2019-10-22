import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup( 23 , GPIO.OUT )

sleep_time = 0.03

def startbit():
    st_bit = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
    for s in range(len(st_bit)):
        if st_bit[s] is 0:
            GPIO.output( 23 , 0 )
        else:
            GPIO.output( 23 , 1 )
        time.sleep(sleep_time)
    
    
input_word = input("送りたい文字を入力してください：")
print("「" + input_word + "」を光で送ります。")

word_length = len(input_word)
print("送る文字は" + str(word_length) + "文字です。")

word_list = list(input_word)
all_word_binary = []

try:
    while True:
        for i in word_list:
            binary_8bit = format(ord(i),"b").zfill(8)
            binary_list = list(binary_8bit)
            all_word_binary.append(binary_list)

        startbit()

        for x in range(word_length):
            for y in range(8):
                if all_word_binary[x][y] is "1":
                    GPIO.output( 23 , 1 )
                    time.sleep(sleep_time)
            
                else:
                    GPIO.output( 23 , 0 )
                    time.sleep(sleep_time)
                    
except(KeyboardInterrupt):
    print("end\n")
    GPIO.cleanup()