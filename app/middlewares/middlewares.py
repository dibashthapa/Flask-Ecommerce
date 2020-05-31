from functools import wraps
from flask import abort
import jwt

def login_required(f):
	@wraps(f)
	def authorize(*args, **kwargs):
		