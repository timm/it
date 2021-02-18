#i!/usr/bin/env python3
# vim: ts=2 sw=2 sts=2 et tw=81:
"""
Very succinct object system that bundles nested functions and some get set
methods into a container.

- License: (c) 2021 Tim Menzies <timm@ieee.org>, MIT License  
- Doco: http://menzies.us/it   
- Code: http://github.com/timm/it
- Example: see the [demoIt](#it.demoIt) function.

"""
from types import FunctionType as Fun

class it:
  "Simple container of names fields, with methods."
  def __init__(i, **d): i.__dict__.update(d)
  def __repr__(i):
    "Pretty print, sorted keys, ignore private keys (those  with `_`)."
    return "{"+ ', '.join( 
      [f":{k} {v}" for k, v in sorted(i.__dict__.items())
       if  type(v) != Fun and k[0] != "_"])+"}"
  def __add__(i, maybe):
    "For all functions, add them as methods to `i`."
    def method(i,f): 
      return lambda *lst, **kw: f(i, *lst, **kw)
    for k,v in maybe.items():
      if type(v) == Fun and k[0] != "_": 
        i.__dict__[k] = method(i,v)
    return i

def itDemo()
  from datetime import datetime as date
  def Person(name=name,yob=1809):
    def age(i): return date.now().year - i.yob
    def birthday(i): i.weight *=1.05
    return o(name=name, yob=yob,weight=100) + locals()
  p = Person(name"Abraham")
  for _ in range(56): p.birthday()
  print(p,p.age())

__name__ == "__main__" and itDemo()
