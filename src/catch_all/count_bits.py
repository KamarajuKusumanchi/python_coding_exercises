def count_bits(n):
    num_bits = 0
    while n:
        num_bits += n & 1
        n >>= 1
    return num_bits

if __name__ == "__main__":
    a = [4, 5, 7, 12]
    for i in a:
        print(f"number of bits in {i} = {count_bits(i)}")
