from functools import wraps

def checkvars(varlist, errorinfo):
	"""
	Decorator, check if some vars are defined before running a function
	"""
	if type(varlist) is str:
		varlist = [varlist]
	def decorator(func):
		@wraps(func)
		def wrapper(self,*args,**kwargs):
			exist_status = [self._is_defined(var) for var in varlist]
			assert not (False in exist_status), errorinfo
			return func(self, *args, **kwargs)
		return wrapper
	return decorator

def infomanage(callinfo=None, successinfo=None, errorinfo=None):
	"""
	Decorator, print some info when begin, success, fail to execute a function
	Doesn't block any exceptions
	"""
	def decorator(func):
		nonlocal callinfo, successinfo, errorinfo
		if callinfo == None: callinfo = "Calling function " + func.__name__
		if successinfo == None: successinfo = "Successfully call function " + func.__name__
		if errorinfo == None: errorinfo = "Failed to call function " + func.__name__
		@wraps(func)
		def wrapper(self, *args, **kwargs):
			print(callinfo)
			try:
				outputs = func(self, *args, **kwargs)
				print(successinfo)
				return outputs
			except Exception:
				print(errorinfo)
				# doesn't handle exception
				raise
		return wrapper
	return decorator

checkip = checkvars(
	varlist = "ip",
	errorinfo = "Lack of local IP. Need to run '_resolve_ip_from_login_page' in advance to get it"
)

checktoken = checkvars(
	varlist = "token",
	errorinfo = "Lack of token. Need to run '_resolve_token_from_challenge_response' in advance"
)

checkinfo = checkvars(
	varlist = "info",
	errorinfo = "Lack of info. Need to run '_generate_info' in advance"
)

checkencryptedinfo = checkvars(
	varlist = "encrypted_info",
	errorinfo = "Lack of encrypted_info. Need to run '_encrypt_info' in advance"
)

checkmd5 = checkvars(
	varlist = "md5",
	errorinfo = "Lack of md5. Need to run '_generate_md5' in advance"
)

checkencryptedmd5 = checkvars(
	varlist = "encrypted_md5",
	errorinfo = "Lack of encrypted_md5. Need to run '_encrypt_md5' in advance"
)

checkchkstr = checkvars(
	varlist = "chkstr",
	errorinfo = "Lack of chkstr. Need to run '_generate_chksum' in advance"
)

checkencryptedchkstr = checkvars(
	varlist = "encrypted_chkstr",
	errorinfo = "Lack of encrypted_chkstr. Need to run '_encrypt_chksum' in advance"
)