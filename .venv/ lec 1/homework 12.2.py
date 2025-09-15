def second_index(text,some_srt):
    first = text.find(some_srt)
    if first ==-1:
        return None
    second=text.find(some_srt,first + 1)
    if second ==-1:
        return None
    return second

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print("ОК")
