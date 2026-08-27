from collections.abc import Callable
from copy import copy

class PQueue():
    elems = []
    comp: Callable
    def __init__(self, elems: list = None, comp: Callable = lambda x : x) -> None:
        self.comp = comp
        if not elems is None:
            for e in elems:
                self.add_elem(e)

    def add_elem(self, v):
        self.elems.append(v)
        i = len(self.elems)-1
        while i > 0 and (self.comp(self.elems[i]) < self.comp(self.elems[(i-1)//2])):
            self.swap(i, (i-1)//2)
            i = (i-1)//2

    def peek(self):
        return copy(self.elems[0])
    
    def __shift_down(self, idx: int):
        i = idx
        l = len(self.elems)
        while i < l:
            if i*2+1 >= l: break
            q = i*2+1
            if i*2+2 < l and self.comp(self.elems[q]) > self.comp(self.elems[q+1]):
                q += 1
            if self.comp(self.elems[q]) < self.comp(self.elems[i]):
                self.swap(i, q)
                i = q
            else:
                break
    
    def reheap(self):
        k = self.elems.copy()
        self.elems = []
        for v in k:
            self.add_elem(v)

    def pop(self):
        l = len(self.elems)
        if l == 0:
            raise IndexError("Priority Queue is empty!")
        self.swap(0, l-1)
        v = self.elems.pop()
        self.__shift_down(0)
        
        return v

    def swap(self, i, j) -> None:
        self.elems[i], self.elems[j] = self.elems[j], self.elems[i]

    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return "PQueue([" + ",".join([str(e) for e in self.elems]) + "])"

__all__ = ["PQueue"]

if __name__ == "__main__":
    q = PQueue([7,3,5,6,4])
    print(q)
    print("Top Peek:", q.peek())
    print(q)
    print("Pop:",q.pop())
    print(q)
    q.elems[3] = 1
    print(q)
    q.reheap()
    print(q)
