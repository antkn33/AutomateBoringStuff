# 
import webbrowser, sys, pyperclip
# webbrowser.open('https://automatetheboringstuff.com')

sys.argv # ['mapit.py', '101', 'Main', 'st.']

# check if there are comand line arguements
if len(sys.argv) > 1:
    # join the cmd line arguements after program name
    address = ' '.join(sys.argv[1:]) # join starting at position 1, until the end. '101 Main St.'
else:
    address = pyperclip.paste()

# https://google.com/maps/search

webbrowser.open('https://google.com/maps/search/' + address)


