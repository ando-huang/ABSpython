import webbrowser, sys, pyperclip

sys.argv

address = ''
#there are args
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
  
webbrowser.open("httpsL//www.google.com/maps/place/" + address)
    
