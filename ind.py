#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    A = {"c", "g", "h", "k", "y"}
    B = {"a", "b", "k", "n", "u"}
    C = {"i", "j", "o", "y", "z"}
    D = {"a", "b", "f", "g", "y", "z"}

    x = (A.union(B)).intersection(D)
    print(f"x = {x}")

    An = u.difference(A)
    Cn = u.difference(C)
    Bn = u.difference(B)

    y = (An.intersection(D)).union(Cn.difference(Bn))
    print(f"y = {y}")
