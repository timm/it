from types import FunctionType as Fun

class it:
  "Simple container of names fields, with methods."
  def __init__(i, **d): i.__dict__.update(d)
  def __repr__(i):
    "Pretty print, sorted keys, ignore private keys (those  with `_`)."
    return "{"+ ', '.join( [f":{k} {v}" for k, v in sorted(i.__dict__.items())
                            if  type(v) != Fun and k[0] != "_"])+"}"
  def __add__(i, maybe):
    "For all functions, add them as methods to `i`."
    def method(i,f): return lambda *lst, **kw: f(i, *lst, **kw)
    for k,v in maybe.items():
      if type(v) == Fun and k[0] != "_": i.__dict__[k] = method(i,v)
    return i

