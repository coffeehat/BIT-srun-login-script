_PADCHAR = "="
_ALPHA = "LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA"
def _getbyte(s, i):
    x = ord(s[i])
    if (x > 255):
        print("INVALID_CHARACTER_ERR: DOM Exception 5")
        exit(0)
    return x
def get_base64(s):
    i=0
    b10=0
    x = []
    imax = len(s) - len(s) % 3
    if len(s) == 0:
        return s
    for i in range(0,imax,3):
        b10 = (_getbyte(s, i) << 16) | (_getbyte(s, i + 1) << 8) | _getbyte(s, i + 2)
        x.append(_ALPHA[(b10 >> 18)])
        x.append(_ALPHA[((b10 >> 12) & 63)])
        x.append(_ALPHA[((b10 >> 6) & 63)])
        x.append(_ALPHA[(b10 & 63)])
    i=imax
    if len(s) - imax == 1:
        b10 = _getbyte(s, i) << 16
        x.append(_ALPHA[(b10 >> 18)] + _ALPHA[((b10 >> 12) & 63)] + _PADCHAR + _PADCHAR)
    elif len(s) - imax == 2:
        b10 = (_getbyte(s, i) << 16) | (_getbyte(s, i + 1) << 8)
        x.append(_ALPHA[(b10 >> 18)] + _ALPHA[((b10 >> 12) & 63)] + _ALPHA[((b10 >> 6) & 63)] + _PADCHAR)
    else:
        # do nothing
        pass
    return "".join(x)
if __name__ == '__main__':
    r=get_base64("132456")
    print(r)