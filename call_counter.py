def counting(func, state={}, mykey="something_or_other"):
  def do_call(*args, _howmany=False, _reset=False, **kwargs):
    if func not in state or _reset is mykey:
      state[func] = 0
      if _reset is mykey:
        return
    if _howmany is mykey:
      return state[func]
    state[func] += 1
    func(*args, **kwargs)

  def get_count():
    return do_call(_howmany=mykey)

  def reset_count():
    return do_call(_reset=mykey)

  do_call.get_count = get_count
  do_call.reset_count = reset_count
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
  hello.reset_count()
  print(f"zero'd count: {hello.get_count()}")
