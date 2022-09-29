import random
import time, sys

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)




import os
try:
    import colorama
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()






colorama.init(autoreset=True)
try:
    import os
    os.system("title " + "Amazon Giftcard Generator,   Made By Bingleton#2539")
except:
    pass

while True:
  sys.stdout.write(colorama.Fore.CYAN + "> ")
  print01("Wanna Auto Save (y/n): ")
  save = input("")
  if save == "y" or save == "n":
    break
  else:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print015("Enter A Valid Choice")

while True:
  try:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Amount Of Codes: ")
    amount = int(input(""))
    break
  except Exception:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print015("Enter A Valid Choice")

while True:
  try:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Delay Per Code: ")
    delay = float(input(""))
    break
  except Exception:
    sys.stdout.write(colorama.Fore.RED + "> ")
    print015("Enter A Valid Choice")

donegen = 0
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(int(amount)):
  r1 = random.choices(choices, k=14)
  code = "".join(r1)
  if save == "y":
    file = open("unchecked_amazon_codes.txt", "a")
    file.write(code + "\n")
    file.close()
  donegen = int(donegen) + 1
  i = int(i) + 1
  print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(i)}, Unchecked{colorama.Fore.CYAN}]{colorama.Fore.RESET} Code: {str(code)}")
  time.sleep(float(delay))
sys.stdout.write(colorama.Fore.CYAN + "> ")
print01("Done Generating Codes")
input("")
exit()
