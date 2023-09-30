# KerbSpray

KerbSpray is kerberos NTLM brute-force script that supports pass-the-hash for a single user by taking a wordlist from a hash file. The only similar tool i managed to find could spray single hash for a list of users, but that scenario would be quite rare. Possible scenario (for which I made this) would be finding old backup of ntds.dit or just testing for reused passwords. 

```Usage: python3 kerbspray.py <domain> <username> <dc_ip> <hash_list>```
![image](https://user-images.githubusercontent.com/89078611/236806411-540bb4e9-20ba-41df-ba8a-4e97d8ea1bb9.png)


Modified Repo: https://github.com/cube0x0/HashSpray.py <br />
Refereces: https://github.com/ropnop/kerbrute
