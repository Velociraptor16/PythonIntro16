def func(a, b, c, d=9, e=8, f=7):
    print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}')


func(1, 2, 3)
func(c=4, a=6, b=2)
func(1, 2, 3, 4, 5, 6)
func(c=4, a=6, b=2, f=1, d=0, e=5)

func(1, 2, 3, 4, 5, 6)
func(1, 2, 3, 4, 5)
func(1, 2, 3, 4)
func(1, 2, 3)

func(c=4, a=6, b=2, f=1, e=5)
func(c=4, a=6, b=2, d=0)


print()
print(1)
print(2, 4, 6, 2)


def func_args(*args):
    print(type(args), args)


func_args()
func_args(3, 4, 'test', 5.4, True)


def func_kwargs(**kwargs):
    print(type(kwargs), kwargs)


func_kwargs()
func_kwargs(w=3, x=4, s='test', pi=5.4, log=True)


def func1(*args, **kwargs):
    print(args, kwargs)


func1(5, 6, 3, e=0, s=9)
