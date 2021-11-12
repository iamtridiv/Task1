def check_teen(val):
  if val >12 and val <20 and not val ==15 and not val ==16:
    return 0
  else:
    return val
def sum(a, b, c):
  return check_teen(a) + check_teen(b)+check_teen(c)