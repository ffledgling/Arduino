#!/usr/bin/env python

import wall

from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path

def svgresizer(h, w, d):
    # Map a canvas of height h and width w to an arc of d degress by d degrees

    # These are the scaling factors
    yf = h/d
    xf = w/d

    # Translation factors
    xs = h/2
    ys = w/2
    def f(x, y):
        return (int((x-xs)/xf), int((y-ys)/yf))

    return f

def svg():
    resize = svgresizer(250,250,60)
    p = parse_path("m21,65h208l-104,180zm0,120h208l-104-180z")
    for l in p:
        wall.line(resize(l.start.real, l.start.imag), resize(l.end.real, l.end.imag))

