
<h3 align="center">stockhom</h3>

---


## 🧐 About <a name = "Stockholm"></a>
<p>This program imitate wannacry virus. Program is based in client(victim) - server(hacker) logic. </p>
<p>./gen_keypair.sh - will create pair of RSA private and public keys, you need to runit in server machine. (pass for key was hardcoded '1234').</p>
 <p>Script will compile one binary file stockholm of stockholm.py Public key will be copied in folder stockholm_src with stockholm app + list of extencions (private key will be send to victim in case of decription)</p>
 <p>Afterall will be run tar command to create an archived named stockholm.tar.gz</p>
 <p>In site of victim run ./stockholm. It will create URL-safe base64-encoded 32-byte key and all files wich are in list of extencions and in ~/infection/ will be encoded with it.</p>
 <p>After that key will be encoded with public.pem of server and saved in directory. Original key will be lost. Usage ./stockholm [-hvrs] -h --help, -v --version, -s --silence, -r --reverse</p>
 <p>For restoring files you need copy private.pem from server into stockholm directory of victim. It can decode encoded key and after that decode all files. Usage flag -r for that.</p>
