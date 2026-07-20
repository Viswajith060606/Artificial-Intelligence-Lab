# Analytical Problem Solving - AI Search Algorithms

## Metadata

* **Title:** Analytical Problem Solving
* **Objective:** To formulate AI search problems and evaluate problem-solving agents.
* **Software Used:** Python 3.13
* **Tools:** VS Code
* **Algorithms Implemented:** Breadth-First Search (BFS), Uniform Cost Search (UCS), Backtracking Search
* **Result:** Successfully implemented BFS for the Water Jug problem, Backtracking for the 8-Queens problem, and Uniform Cost Search for delivery path optimization.

\---

## Overview

This repository contains comprehensive analytical problem-solving implementations for key foundational concepts in **Artificial Intelligence (Course Code: CSA17)**. The implementations address classic search problems, intelligent agent configurations (PEAS), pathfinding heuristics, and logic simulation frameworks.

\---

## Structure \& Modules Included

### 1\. The Water Jug Problem

* **Formulation:** Solves the classic 4-gallon and 3-gallon water jug challenge to isolate exactly 2 gallons of water in the 4-gallon container.
* **Search Strategy:** Explores the state-space tree using a **Breadth-First Search (BFS)** tracking algorithm to guarantee the shortest operational path sequence.

### 2\. Mars Rover PEAS Analysis

* **Framework:** Formal characterization of a robotic planetary exploration environment.
* **Components covered:**

  * **Percepts:** Visual feeds, LiDAR distance parameters, spectrometer telemetry, and sensor feedback.
  * **Environment:** Characterized as partially observable, stochastic, sequential, dynamic, continuous, and single-agent.
  * **Actions:** Steering control, sample collection via drilling, chemical analysis sequencing, and satellite telemetry transmission.
  * **Performance Measures:** High-yield unique scientific data generation, extreme situational preservation/safety, and minimal resource exhaustion.
* **Architecture:** Justifies a **Utility-Based Hybrid Agent Structure** capable of optimizing multi-objective scientific gains against battery/thermal realities under severe command signal delay.

### 3\. The 8-Queens Challenge

* **Formulation:** Places 8 individual queens onto a standard $8 \\times 8$ chessboard layout without any mutual overlapping attack vectors (rows, columns, or diagonal paths).
* **Search Strategy:** Implements an **Incremental Backtracking Search** architecture that prunes illegal layout paths early to effectively search through potential board states.

### 4\. OLA Cab Problem-Solving Agent

* **Formulation:** Models an on-demand transit request optimization framework mapping out a journey from an initial pick-up point to a destination.
* **Agent Type:** A **Goal-Based Problem-Solving Agent** executing pathfinding optimization over a live weighted traffic map.
* **Simulation Flow:** Automatically screens available fleet arrays matching specific user preferences (Mini, Micro, Sedan, Prime), minimizes pick-up ETA, and generates an optimized transit action sequence.

### 5\. Delivery Network Path Optimization (Uniform Cost Search)

* **Formulation:** Solves the least-cost routing problem for a logistics transportation matrix spanning multiple warehouses.
* **Search Strategy:** Executes a complete **Uniform Cost Search (UCS)** using an active Min-Priority Queue structure. The algorithm safely determines that the global optimal minimum path from origin node `S` to goal node `G` runs via vertices `A` and `C` (`S -> A -> C -> G`) with a guaranteed minimal cumulative operational cost of **4 units**, avoiding local sub-optimal routes.

\---

## Getting Started

### Prerequisites

Ensure that Python 3.13+ is installed on your local environment.

### Execution

Run the consolidated interactive suite tool from your terminal console to evaluate individual module workflows:

```bash
Python\_code.py
```

Select a number between `1` and `5` in the prompt terminal layout to trigger the standalone path calculation traces and step tables directly inside your workspace shell environment.

