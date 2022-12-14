
import logging
from datetime import datetime
from turtle import st
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os

home = os.getenv("HOME")
root = os.getcwd()

def logging (exception, need_print):
    f = open(root + '/log.txt', 'a')
    date = datetime.now()
    date = str(date)
    if need_print == 1:
        print("Log file writing")
    f.write('%s: ' % date)
    f.write(' Error -> %s \n' % exception)
    f.close()

def ft_server_part(need_print):
    try:
        os.chdir(home + "/infection")
        f = open(".ciperKey3", "rb")
    except Exception as e:
        logging(e, need_print)
        os._exit(os.EX_OK)
    ciphertext = f.read()
    try:
        with open(root + "/.private.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=b"1234",
            )

        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except Exception as e:
        logging(e, need_print)
        os._exit(os.EX_OK)
    # print(plaintext)
    key = Fernet(plaintext)
    try:
        not_enc_file = open(home + "/infection/.not_encoded.ft", "rb")
        not_enc_text = key.decrypt(not_enc_file.read())
        not_enc_file.close()
        os.remove(home + "/infection/.not_encoded.ft")
        not_enc_text = not_enc_text.decode("utf-8")
    except Exception as e:
        logging(e, need_print)
        os._exit(os.EX_OK)
    # print(not_enc_text)
    will_rev_infect = list (filter(os.path.isfile, os.listdir(".")))
    for file in will_rev_infect:
        name = file.split(".")
        # print (name)
        str_name = ""
        if name[-1] == "ft" and file not in not_enc_text:
            name.pop(-1)
            for part in name:
                if str_name == "":
                    str_name = part
                else: 
                    str_name = str_name + "." + part
            # print(str_name)
            os.rename(file, str_name)
            encr_file = open(str_name, "rb")
            encr_inf = encr_file.read()
            encr_file.close()

            # print(key.decrypt(encr_inf))
            try:
                encr_file = open (str_name, "wb")
                encr_file.write(key.decrypt(encr_inf))
                encr_file.close()
            except Exception as e:
                logging(e, need_print)
    os.remove(home + "/infection/.ciperKey3")

# print (list (filter(os.path.isdir, os.listdir("."))))
# print (os.listdir("."))
# will_rev_infect_renamed = list (filter(os.path.isfile, os.listdir(".")))
# print(will_rev_infect_renamed)






# encr_file = open("encripted_file", "rb")
# encr_inf = encr_file.read()
# print(encr_inf)
# # decr_file = bytearray(encr_inf)
# key = Fernet(plaintext)
# print (key)
# # print (decr_file)
# print (encr_inf)
# # test = Fernet.generate_key()
# # testkey = Fernet(test)
# # print (testkey)
# print(key.decrypt(encr_inf))
