class OddNumInfinite:
  """ infinite iterator to return all odd numbers """

  def __iter__(self):
    self.n = 1
    return self

  def __next__(self):
    n = self.n
    self.n += 2
    return n

oddNum = iter(OddNumInfinite())

for _ in range(5):
  print(next(oddNum))