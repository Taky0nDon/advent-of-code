def fizzbuzz_generator(n: int) -> str:
    res = ""
    if not n % 3:
        res += "fizz"
    if not n % 5:
        res += "buzz"
    if res == "":
        res = str(n)
    yield res

if __name__ == "__main__":
    for num in range(1, 31):
        fbg = fizzbuzz_generator(num)
        while fbg:
            try:
                print(next(fbg))
            except StopIteration:
                break
