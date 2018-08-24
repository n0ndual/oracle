def modulus_from_pubkey(pem_pubkey):
    b64_str = ''
    lines = pem_pubkey.split('\n')
    #omit header and footer lines
    for i in range(1,len(lines)-1):
        b64_str += lines[i]
    der = b64decode(b64_str)
    #last 5 bytes are 2 DER bytes and 3 bytes exponent, our pubkey is the preceding 512 bytes
    pubkey = der[len(der)-517:len(der)-5]
    return pubkey


def checkGetConsoleOutput():
  try:
    b64data = '''
PageSigner public key for verification
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA19DLDrATFTAJ2dknmx7B
TmfE/7SrqjagbDXK/4WgwZl8A9YP61/JjcSOuwBPx3Ihyx8HYhHvnagNL6/gER7P
0fk6tju/YFKdonPB6rgn3sldHUy5aSqUkfuCAjBdyF0DBgoWdh0/NyDskjIBwZZq
XJO5SR20D4MMw2aJLFwN+MrlVY4Gt7hGnScj6JulKwoXSUOhB+PlKv8tu59oFwHu
tjGMfQdiaNSw56mSy2VkxN9jDct0VdfYBhCKIGFT1kBAzbVH74cd6CUMpH0RcLTX
+tnfZk8qDvPE5690NGsenM7x8aY9aR9PTR7Aya+IwXGAsk7SeeKuDZttbsIB9YrH
436hsNBHoi7WLGY5gFSAyA5+lddNFUkkXxWijhxOdm1Mg8u3NEFWedBaBOf5/yYE
pBCzmOjXVooXlkpttryttHzm0SgMvvz/VO0MRsmidU4Um8NHtsE+f4g8EDe7kPMk
Kbds2fOICJ6Y5c0FpxFGluZA9UDG130g4IEXJKrBKIdFx44qYc3hvJq7f38q5Lr7
lmgLxSMZc+R/iMGF9i8+E8ii4VK7nB7E5VZMy1bOSsC8HpGlWH/N4mCrVeWBQdYQ
k+cV773s/LoO9lfHjhUjN62Bdg4L+9/JiMPi9CNEDCpYNhqkAg/RfeQCerI6NHQi
Mq9hjzDFFqMsJ0b17LF/7CsCAwEAAQ==
-----END PUBLIC KEY-----
'''
    logstr = b64decode(b64data)
    sigmark = 'PageSigner public key for verification'
    pkstartmark = '-----BEGIN PUBLIC KEY-----'
    pkendmark = '-----END PUBLIC KEY-----'

    mark_start = logstr.index(sigmark)
    assert mark_start != -1
    pubkhey_start = mark_start + logstr[mark_start:].index(pkstartmark)
    pubkey_end = pubkey_start+ logstr[pubkey_start:].index(pkendmark) + len(pkendmark)
    pk = logstr[pubkey_start:pubkey_end]
    assert len(pk) > 0
    return pk
  except:
    return False

if __name__  == "__main__":
    pk = checkGetConsoleOutput();
    modulus = modulus_from_pubkey(pk);
    print(modulus);
