def gen_recur(chr_lst, length, n , s, ls):
    
    if (n == 0):
        ls.append(s)
        return

    for j in range(0, length):
        str_app = s + chr_lst[j]
        gen_recur(chr_lst, length, n-1, str_app, ls)
    return

def generate_passwords(chr_str, length, ls):
    chr_lst = [char for char in chr_str]
    s = ""
    for n in range(1, length + 1):
        gen_recur(chr_lst, length, n, s, ls)

if __name__ == "__main__":
    chr_str = 'abc'
    length = 2
    ls = []
    generate_passwords(chr_str, length, ls)
    print(ls)