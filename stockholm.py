import os
import sys
import client
import server



def revers_infection(rev_arg):
    try:
        print("Infecting reverse", sys.argv[rev_arg + 1])
    except Exception as e:
        client.logging(e)
        print("flag -r need key")
        

def parsing_args(args):
    need_print = 1
    if ("-s" in args or "-silent" in args):
        need_print = 0
    if ("-h" in args or "-help" in args) and need_print == 1:
        print ("Usage: \n./stockholm [-hvrs] -h --help, -v --version, -s --silence, -r --reverse")
        os._exit(os.EX_OK)
    if ("-v" in args or "-version" in args):
        print("ver 1.0")
        os._exit(os.EX_OK)
    if ("-r" in args or "-reverse" in sys.argv):
        rev_arg = sys.argv.index("-r")
        server.ft_server_part(need_print)
    else:
        client.ft_client_part(need_print)

parsing_args(sys.argv)









