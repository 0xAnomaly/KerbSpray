# KerbSpray

KerbSpray is an improvement to Kerbrute/kerbspray.py that supports pass-the-hash for a single user by taking a list from a hash file. The only similar tool i managed to found could spray single hash for a list of users, but that scenario would be quite rare. Possible scenario (for which I made this) would be finding old backup of ntds.dit or just testing reused passwords. 

```Usage: python3 kerbspray.py <domain> <username> <dc_ip> <hash_list>```

Modified Repo: https://github.com/cube0x0/HashSpray.py <br />
Refereces: https://github.com/ropnop/kerbrute
