"""
This file is from the lecture of Tree classs.
"""
from typing import List

class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    def __init__(self, value: object = None,
                 children: List['Tree'] = None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        self.children = children.copy() if children is not None else []

    def __repr__(self) ->str:
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.
        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('{}({}, {})'.format(self.__class__.__name__,
                                    repr(self.value),
                                    repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other: 'Tree') ->bool:
        """
        Return whether this Tree is equivalent to other.
        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent: int = 0) -> str:
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual in indent: amount to indent
        each level of tree
        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
           23
        19
           17
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
              23
           19
              17
        29
           31
        """
        root_str = indent * " " + str(self.value)
        mid = len(self.non_none_kids()) // 2
        left_str = [c.__str__(indent + 3)
                    for c in self.non_none_kids()][: mid]
        right_str = [c.__str__(indent + 3)
                     for c in self.non_none_kids()][mid:]
        return '\n'.join(right_str + [root_str] + left_str)

    def non_none_kids(self):
        """ Return a list of Tree self's non-None children.

        @param Tree self:
        @rtype: list[Tree]
        """
        return [c
                for c in self.children
                if c is not None]

if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
