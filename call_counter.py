def counting(func, state={}):
  mykey = "THEKEYISSECRET"

  def do_call(*args, _howmany=False, **kwargs):
    if func not in state:
      state[func] = 0
    if _howmany is mykey:
      return state[func]
    state[func] += 1
    func()

  def get_count():
    return do_call(_howmany=mykey)

  do_call.get_count = get_count
  return do_call

@counting
def hello():
  print("Hello")

@counting
def hey():
  print("Hey!")


if __name__ == "__main__":
  for i in range(5):
    hello()
    if i % 2:
      hey()

  print(f"hello count: {hello.get_count()}")
  print(f"hey count: {hey.get_count()}")
