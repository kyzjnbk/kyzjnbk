#!/usr/bin/env python3
from functools import singledispatch
from collections import Iterable
import numpy as np


@singledispatch
def func(*arg, **kwarg):
    raise NotImplementedError


@func.register
def _(val: str):
    print('This is a string')


@func.register
def _(val: int):
    print('This is an int')


func(1)
func('1')
try:
    func(1.0)
except NotImplementedError:
    print("NotImplemented")


@singledispatch
def flatten(atom):
    yield atom


@flatten.register
def _(val: Iterable):
    for i in val:
        for j in flatten(i):
            yield j


@flatten.register
def _(val: str):
    for i in val:
        yield i


x = tuple(
    flatten([1, 2, [3], [[4], 5]])
)
print(x)

x = tuple(
    flatten((1, 2, 3))
)
print(x)

x = tuple(
    flatten(np.arange(0, 10, dtype=float))
)
print(x)

x = tuple(
    flatten('abcd')
)
print(x)
