def makescale(lo, hi, targetlo, targethi, output=float):
    """Makes a function for converting numbers from one scale to
    another.  The canonical example, I guess, would be converting
    degree Farenheit to degrees Celsius, which is done like so:

        >>> f = makescale(32, 212, 0, 100)
        >>> f(32)
        0.0
        >>> f(212)
        100.0
        >>> f(98.6)
        36.999999999999993

    The type of the return value can be changed by passing in a
    different return type as the output parameter.  E.g.:

        >>> f = makescale(32, 212, 0, 100, output=int)
        >>> f(32)
        0
        >>> f(212)
        100
        >>> f(98.6)
        36

    Dr. Math taught me how to do this:
    http://mathforum.org/library/drmath/view/54556.html"""
    offset = 0 - targetlo
    targetlo += offset
    targethi += offset
    a, b = (hi - lo) / float(targethi), lo
    return lambda x: output((x - b) / a - offset)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
