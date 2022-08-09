<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">stockhom</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 🧐 About <a name = "Stockholm"></a>

This program imitate wannacry virus. Program is based in client(victim) - server(hacker) logic. 
./gen_keypair.sh - will create pair of RSA private and public keys, you need to runit in server machine. (pass for key was hardcoded '1234').
 Script will compile one binary file stockholm of stockholm.py Public key will be copied in folder stockholm_src with stockholm app + list of extencions (private key will be send to victim in case of decription)
 Afterall will be run tar command to create an archived named stockholm.tar.gz
 In site of victim run ./stockholm. It will create URL-safe base64-encoded 32-byte key and all files wich are in list of extencions and in ~/infection/ will be encoded with it.
 After that key will be encoded with public.pem of server and saved in directory. Original key will be lost. Usage ./stockholm [-hvrs] -h --help, -v --version, -s --silence, -r --reverse
 For restoring files you need copy private.pem from server into stockholm directory of victim. It can decode encoded key and after that decode all files. Usage flag -r for that.
