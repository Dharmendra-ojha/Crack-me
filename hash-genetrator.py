import hashlib
from pyfiglet import Figlet as fg
from colorama import *
def render(text):
    design = fg(font="slant")
    return print(Fore.YELLOW,design.renderText(text))

render("C R A C K - M E")
print("[*] Hash Generator [*]")

prompt = input("[?]Enter the String to Hash: ")
hash_type = input("[?]Enter type of Hash: ")
if hash_type == "md5" :
    enc_word = prompt.encode("utf-8")
  
    # to Hash the word into md5 hash  
    digest = hashlib.md5(enc_word.strip()).hexdigest()
    print("[*]Generated Hash -> ",digest)	
    
elif hash_type == "sha1" :
    enc_word = prompt.encode("utf-8")

    # to Hash the word into sha1 hash
    digest = hashlib.sha1(enc_word.strip()).hexdigest()
    print("[*]Genersted Hash -> ",digest)
    
else:
  print("[ERR]Invalid type[ERR]")
  print("[info]This hash generator Supports only md5 and sha1 hashes[info]")
