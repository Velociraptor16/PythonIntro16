# 2 ^ 5 = 2 * 2 * 2 * 2 * 2
# 2 ^ 5 = 2 * 2 ^ 4 => 2 * 2 ^ 3 => 2 * 2 ^ 2 => 2 * 2 ^ 1 => 2 * 2 ^ 0
#   32  = 2 *   16  <= 2 *   8   <= 2 *   4   <= 2 *   2   <= 2 *   1


def i_pow(num, exp):
    res = 1
    while exp > 0:
        res *= num
        exp -= 1

    return res


print(i_pow(2, 5))


def r_pow(num, exp):
    if exp == 0:
        return 1

    return num * r_pow(num, exp-1)


print(r_pow(2, 5))

# 5! = 1 * 2 * 3 * 4 * 5
# 5! = 5 * 4! => 4 * 3! => 3 * 2! => 2 * 1! => 1


def i_fact(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


print(i_fact(5))


def r_fact(num):
    if num == 1:
        return 1

    return num * r_fact(num-1)


print(r_fact(5))


def discovery_fs(root_dir, indent_level=1):
    import os

    for name in os.listdir(root_dir):
        if not name.startswith('.'):
            try:
                path = os.path.join(root_dir, name)
                prefix = indent_level * (' '*4)
                if os.path.isfile(path):
                    print('{prefix} ({size} bytes)'.format(prefix=prefix + '|__ ' + name,
                                                           size=os.path.getsize(path)))
                else:
                    print(prefix + name + ':')
                    discovery_fs(path, indent_level+1)
            except Exception as ex:
                print(ex)


discovery_fs('<some path>')
