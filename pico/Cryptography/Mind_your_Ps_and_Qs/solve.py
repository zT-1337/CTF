from multiprocessing import Pool
import math
from Crypto.Util.number import long_to_bytes, inverse

def main():
  c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
  n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
  e = 65537
  #p = calculate_p(n) 
  #q = n / p
  p = 2434792384523484381583634042478415057961
  q = 650809615742055581459820253356987396346063
  phi = (p-1) * (q-1)
  d = inverse(e, phi)
  m = pow(c, d, n)
  print(long_to_bytes(m))


def calculate_p(n):
  n_sqrt = math.floor(math.sqrt(n))

  start1 = 2
  end1 = math.floor(n_sqrt / 2) 

  start2 = end1 + 1
  end2 = n_sqrt

  results = None
  with Pool(processes=3) as pool:
    results = pool.map(find_factorial, [{"start": start1, "end": end1, "n": n}, {"start": start2, "end": end2, "n": n}])
    for r in results:
      if r is not None:
        return r

def find_factorial(data):
  i = data["start"]
  end = data["end"]
  n = data["n"]

  while i <= end:
    if is_prime(i) and n % i == 0:
      return i
    i = i + 1

  return None

def is_prime(i):
  if i < 3 and i > -1:
    return True

  j = 2
  i_sqrt = math.sqrt(i)

  while j <= i_sqrt:
    if i % j == 0:
      return False 
    j = j + 1

  return True

if __name__ == "__main__":
  main()