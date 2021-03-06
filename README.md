# funccy-state
Amazing.

## Why?
It was fun to write.

## ...Why?
An error I see often with new Pythonistas is using mutable objects as parameter defaults. It usually leads to unintended behavior that's tricky to debug if you don't know to look for it. The problem comes from modifying it inside the function, the next call you're going to start off with an already modified object, not the original one you may be expecting. In essense, the function has retained state.

So I thought to myself 'Can I treat this as a *feature*, and not a bug?' I mean, I'd probably *never* do this, but... can I?

## Ok but how does ___ in call_counter.py work?
I'm going to gloss over some stuff like 'how decorators work' (for now), because they're more normal use-case Python stuff. Lots of people have explained them, I probably won't do much better than they will.

* `state[func]` --> Functions are hashable, so we can conveniently use them as dict keys.
* Adding params to do_call --> Perfectly fine! When you're calling a decorated function like normal, they have default values. If you happen to decorate a function with the same param name, it will pass through just fine from `do_call` to `func`.
* Passing and identical string to `mykey` --> Also perfectly fine! Since we're comparing with `is`, even is the string is equal it will be a different object, and the check will be false. **NOTE: Python has some optimizations on common objects, like int `1`. You can 'make' `1` 100 times, it's all the same object. Just something to be aware of.**
* `do_call.get_count = get_count` --> We can get access to our decorators local functions by... adding attributes that point to them to `do_call`! It's Python, everything is an object, fun! It's not the only way to get access to them (or `state` in `counting`), but it's the way I wanted to access them.
* Is `mykey` secret/hidden? --> Nope! And you can actually break the code a bit by retrieving and using it. You can pass your decorated function `_howmany=counting.__defaults__[1]` to trigger returning the number of counts... but why would you! (Ignore the question of 'why would you do any of this??')


## call_counter.py Output:
```
Hello
Hello
Hey!
Hello
Hello
Hey!
Hello
hello count: 5
hey count: 2
zero'd count: 0
```
