#Import required module
import colorama
from colorama import Fore, Back, Style

#Initialize colorama
colorama.init(autoreset=True)

# Colours list and how to -->
# Argument Name	Description
# Autoreset --> It is used to reset the color and style after each line when the value of this argument is set to True.
# Strip	--> It is used to remove the ANSI code from the output when the value of this argument is set to True.
# Convert --> It is used to convert the ANSI code of the output when the value of this argument is set to True.
# Wrap --> It is used to disable the overriding task when the value of this argument is set to False.

# Terminal Colors
# The following colors can be used by the Colorama as the background and font color of the terminal.
# 1. RED
# 2. GREEN
# 3. BLUE
# 4. WHITE
# 5. YELLOW
# 6. MAGENTA
# 7. CYAN
# 8. WHITE

#Print text using font color
print(Fore.CYAN + 'Welcome to this new app ')
#Print text using background color and DIM style
print(Back.YELLOW + Style.DIM + 'Learn Python', end='')
#Reset all style
print(Style.RESET_ALL)
#Print text using font color and BRIGHT style
print(Fore.RED + Style.BRIGHT + 'Bright Text', end='')
#Print reset all style again
print(Style.RESET_ALL)
#Print text without any color and normal style
print(Style.NORMAL + 'Normal Text')
#Print text using background and font colors
print(Back.RED + Fore.BLUE + "Hi there!")
#Add newline
print()
#Print text using background color
print(Back.GREEN + "I like programming")