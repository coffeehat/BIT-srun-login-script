import hmac
import hashlib
def get_md5(password,token):
	return hmac.new(token.encode(), password.encode(), hashlib.md5).hexdigest()
if __name__ == '__main__':
	password="15879684798qq"
	token="711ab370231392679fe06523b119a8fe096f5ed9bd206b4de8d7b5b994bbc3e5"
	print(get_md5(password,token))