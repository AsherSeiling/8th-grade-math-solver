def g(l):
    cmd = input("cmd:// ")
    if cmd in l:
        return cmd
    elif cmd == 'help':
        print("Use the number keys and prompts to progress")
        return g(l)

    else:
        print("invalid command - please type help")
        return g(l)

class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


