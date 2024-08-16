import sys
from src.autoshell import autoShell



for args in sys.argv:
    if sys.argv[arg] == "autoshell" and sys.argv[arg + 1] != "--formats" or sys.argv[arg + 1] != "-f" :
        autoShell()
    elif sys.argv[arg] == "autoshell" and sys.argv[arg + 1] == "--formats":
        autoShell("formats")
    
        
