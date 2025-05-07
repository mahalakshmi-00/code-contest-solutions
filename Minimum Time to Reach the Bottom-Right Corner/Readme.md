# Min Time to Reach Target Room

This Python project contains a solution to find the minimum time required to travel from the top-left corner to the bottom-right corner of a grid, where each room in the grid has a specific time to move into. The problem is solved using **Dijkstra's Algorithm**, which is ideal for finding the shortest path in a weighted graph.

## Problem Description

In a grid `moveTime`, each element represents the time to enter that room. The goal is to calculate the minimum time to travel from the top-left corner `(0, 0)` to the bottom-right corner `(n-1, m-1)` while adhering to the following rules:

- You can move **up**, **down**, **left**, or **right**.
- The time to enter a new room is the maximum of the current room's time and the new room's time.
- The task is to find the path that minimizes the total time.

## Solution Approach

The problem is solved using **Dijkstra's Algorithm**, a popular algorithm for finding the shortest path in a graph with weighted edges.

### Key Steps:
1. Initialize a distance array `dist` to store the minimum time to reach each room, initially set to infinity.
2. Use a **min-heap priority queue** to explore rooms starting from `(0, 0)` and process the rooms with the least accumulated time.
3. For each room, evaluate its neighboring rooms and update the time if a better path is found.

### Algorithm:
- We use the **min-heap** to ensure the cell with the smallest time is processed first.
- We update the neighboring cells' time only if we find a faster way to reach them.
- The algorithm continues until the bottom-right corner is reached, or all reachable rooms are processed.
