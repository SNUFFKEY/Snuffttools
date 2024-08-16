# This is a section of my tool that automatically creates a reverse shell in your specified languages. Please note that these
# not my reverse shells and that I found them off of the web


import sys

helpOutput = """

-f [fileExt] : Specify the file extension for your shell
-sT or --shellType : Specify whether you want a bind shell (bind) , reverse shell (revshell), or web shell (webshell)

"""


formatOutput = """

PHP | Bash | Golang | Vlang | Awk | Dart | Crystal | Javascript | telnet | PowerShell | C# | curl | nc | Perl | Lua



"""


def autoShell(fileExt=none,shellType=none,formats=none):
    if formats == "formats" and fileExt == none and shellType == none:
        print(formatOutput)
        

