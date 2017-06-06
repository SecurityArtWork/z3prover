#!/usr/bin/env python
from z3 import *

def get_models(F):
    result = []
    s = Solver()
    s.add(F)
    while True:
        if s.check() == sat:
            m = s.model()
            result.append(m)
            block = []
            for d in m:
                if d.arity() > 0:
                    raise Z3Exception("uninterpreted functions are not supported")
                c = d()
                if is_array(c) or c.sort().kind() == Z3_UNINTERPRETED_SORT:
                    raise Z3Exception("arrays and uninterpreted sorts are not supported")
                block.append(c != m[d])
            s.add(Or(block))
        else:
            return result

def verify(rcx):
    rax = 0x0A5E3C04BB1623035
    rdx = 0x0E4957041B271F986
    rsi = rcx
    rax = (rax + rcx * 2)
    rax = rax & 0x0FFFFFFFFFFFFFFFE
    rdx = (rdx + rax)
    rax = 0x0DE9BC364362C55EF
    rsi = (rsi - rdx)
    rdi = (rax + rsi * 2)
    rax = 0x2BB33127ADA5CBCA
    rax = (rax - rcx)
    rax = (rax + rdx)
    rdi = rdi & 0x0FFFFFFFFFFFFFFFE
    rdx = 0x54780300041002
    rsi = (rsi - rdi)
    rcx = (rax + rdi)
    rax = 0x0A84525ADA4B05868
    rax = (rax + rsi * 2)
    rax = rax & rdx
    rdx = 0x23F3F28C54D59B2E
    rax = (rax + rcx)
    rcx = rax
    rax = (~rax)
    rcx = rcx ^ rdx
    rax = rax & rdx
    rcx = rcx | rdx
    return (rcx == rax)

if __name__ == "__main__":
    rcx = BitVec("rcx", 64)

    F = [
        verify(rcx)
    ]

    for x in get_models(F):
        print(x)