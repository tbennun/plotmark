# -*- coding: utf-8 -*-

from typing import List, Tuple
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

def _angle(pt1: Tuple[float, float], pt2: Tuple[float, float]) -> float:
    """ Compute the slope and return angle between two points. """
    angle_rad = math.atan2(pt2[1] - pt1[1], pt2[0] - pt1[0])
    return (360 * (angle_rad / (2*math.pi)))

def plotmark(line: mpl.lines.Line2D, ticks: List[float], **marker_kwargs):
    """ Add marker ticks to plot, oriented to the given line.
        @param line The line to plot markers onto.
        @param ticks A list of points to add markers to.
        @param marker_kwargs Dictionary of plotting overrides for markers.
        @return An array of the plotted tick markers.
    """
    # Sort points for ease of access
    spt = sorted(line.get_path().vertices, key=lambda pt: pt[0])
    sticks = sorted(ticks)
    cur_pt = 0
    
    tickargs = dict(markersize=10, linestyle=None, color='black')
    tickargs.update(marker_kwargs)
    
    result = [None] * len(sticks)

    for i, tick in enumerate(sticks):
        # Compute angle for each tick
        angle = 0.0
        
        # Find tick location
        while True:
            if ((cur_pt == 0 and spt[cur_pt][0] > tick) or 
                    (cur_pt == len(spt) - 1)):
                cur_pt = -1
                break
            if spt[cur_pt][0] <= tick and spt[cur_pt + 1][0] > tick:
                break
            cur_pt += 1
        if cur_pt == -1:
            print('WARNING: Tick %f out of bounds, ignoring.' % tick)
            cur_pt = 0
            continue
        
        # Our point is within the plot points, use average angle from prev and
        # next points
        if tick == spt[cur_pt][0]:
            n = 0
            if cur_pt > 0:
                angle += _angle(spt[cur_pt - 1], spt[cur_pt])
                n += 1
            if cur_pt < len(spt) - 1:
                angle += _angle(spt[cur_pt], spt[cur_pt + 1])
                n += 1
            if n > 0:
                angle /= n
        else:
            # Point is between cur_pt and cur_pt + 1
            angle = _angle(spt[cur_pt], spt[cur_pt + 1])
            
        # Interpolate y point
        xa, ya = spt[cur_pt]
        xb, yb = spt[cur_pt + 1]
        ypt = ya + (yb - ya) * ((tick - xa) / (xb - xa))
        
        # Plot rotated tick
        result[i] = plt.plot(tick, ypt, marker=(2, 0, angle), **tickargs)
        
    return result
