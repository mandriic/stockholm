from logging import root
from time import sleep
import climage
import os
from playsound import playsound


def show(root):
    os.chdir(root)
    pid = os.fork()
    if pid > 0:
        playsound(".src/1.wav")
        os._exit(os.EX_OK)
    else:
        two = climage.convert('.src/2.jpg', is_256color=True, is_unicode=True)
        three = climage.convert('.src/3.jpg', is_256color=True, is_unicode=True)
        four = climage.convert('.src/4.jpg', is_256color=True, is_unicode=True)
        five = climage.convert('.src/5.jpg', is_256color=True, is_unicode=True)
        six = climage.convert('.src/6.jpg', is_256color=True, is_unicode=True)
        seven = climage.convert('.src/7.jpg', is_256color=True, is_unicode=True)
        eight = climage.convert('.src/8.jpg', is_256color=True, is_unicode=True)
        nine = climage.convert('.src/9.jpg', is_256color=True, is_unicode=True)
        ten = climage.convert('.src/10.jpg', is_256color=True, is_unicode=True)
        once = climage.convert('.src/11.jpg', is_256color=True, is_unicode=True)

        output = climage.convert('.src/pirate2.jpg', is_256color=True, is_unicode=True)
        output2 = climage.convert('.src/pirate4.jpg',is_unicode=True, palette="gruvboxdark")
        output3 = climage.convert('.src/pirate5.jpg',is_unicode=True, palette="gruvboxdark")
        output4 = climage.convert('.src/pirate6.jpg',is_unicode=True, palette="gruvboxdark")
        output5 = climage.convert('.src/pirate7.jpg',is_unicode=True, palette="gruvboxdark")
        output9 = climage.convert('.src/pirate9.jpg',is_unicode=True, palette="gruvboxdark")



        print(output)
        sleep(2)
        os.system('clear')
        print(output2)
        sleep(1)
        os.system('clear')
        print(once)
        sleep(0.2)
        os.system('clear')
        print(output5)
        sleep(0.3)
        os.system('clear')
        print(output3)
        sleep(0.5)
        os.system('clear')
        print(once)
        sleep(0.1)
        os.system('clear')
        print(output4)
        sleep(1)
        os.system('clear')
        print(output4)
        sleep(1)
        os.system('clear')
        print (output)
        sleep(1)
        print (output5)
        os.system('clear')
        sleep(0.5)
        os.system('clear')
        print(output9)
        os.system('clear')
        print(output3)
        sleep(0.3)
        os.system('clear')
        print (output)
        sleep(1)
        os.system('clear')
        print(once)
        sleep(0.1)
        os.system('clear')
        print (output5)
        sleep(1)
        os.system('clear')
        print(once)
        sleep(0.1)
        os.system('clear')
        print(output9)
        sleep(0.3)
        os.system('clear')
        print(once)
        sleep(0.1)
        os.system('clear')
        print(once)
        sleep(0.1)
        os.system('clear')
        print(output3)
        os.system('clear')
        print (output)
        sleep(1)
        os.system('clear')
        print (output)
        sleep(1)
        os.system('clear')
        print(output9)
        sleep(0.3)
        os.system('clear')
        print (output)
        os.system('clear')
        sleep(1)
        sleep(1)
        os.system('clear')
        print(two)
        sleep(0.5)
        os.system('clear')
        print(three)
        sleep(1)
        os.system('clear')
        print(four)
        sleep(0.3)
        os.system('clear')
        print(five)
        sleep(1)
        os.system('clear')
        print(six)
        sleep(0.7)
        os.system('clear')
        print(seven)
        sleep(0.5)
        os.system('clear')
        print(eight)
        sleep(0.3)
        os.system('clear')
        print(nine)
        os.system('clear')
        sleep(0.5)
        os.system('clear')
        print(ten)
        sleep(2)
        os.system('clear')
        print(once)
        sleep(1)
        i = 0
        while(i < 10):
            print("Your system was infected with stockholm. Give me your money, or you files will die")
            sleep(1)
            i += 1
        os.system('clear')
        print(output)
        os._exit(os.EX_OK)
