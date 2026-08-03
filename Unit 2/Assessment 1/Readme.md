# Artificial Intelligence - Multi-Scenario Assignment Suite 🚀

This repository contains a unified Python implementation covering **5 key Artificial Intelligence scenarios** spanning Pathfinding, Local Search, Online Search, Constraint Satisfaction Problems (CSP), and Adversarial Game Search.

The application includes an **interactive terminal menu**, allowing users to execute and evaluate each algorithm simulation individually or run all scenarios sequentially.

---

## 📌 Features & Implemented AI Concepts

### 1. 🛸 Problem 1: Emergency Medical Drones in Dynamic Flood Zones
* **Concepts:** Pathfinding under dynamic environmental uncertainty.
* **Algorithms Implemented:**
  * **Greedy Best-First Search (GBFS):** Evaluates path selection strictly using $f(n) = h(n)$ (Euclidean Straight-Line Distance).
  * **A\* Search:** Balances cumulative movement/risk cost $g(n)$ with heuristic guidance $h(n)$ via $f(n) = g(n) + h(n)$.
  * **D\* Lite Strategy Simulation:** Analysis of incremental re-planning performance when obstacles dynamically block corridors.

### 2. 🚦 Problem 2: Smart City Traffic Signal Optimization
* **Concepts:** High-dimensional local search & metaheuristics.
* **Algorithms Implemented:**
  * **Simple Hill Climbing:** Demonstrates local search mechanics and highlights failures when trapped in local minima/plateaus.
  * **Simulated Annealing (SA):** Escapes local optima using the probabilistic Metropolis acceptance criterion $P(\text{accept}) = \exp(-\Delta E / T)$.
  * **Genetic Algorithm (GA) Strategy:** Highlights multi-objective optimization across interconnected traffic corridors.

### 3. 🔴 Problem 3: Autonomous Mars Rover Navigation
* **Concepts:** Online search agents in partially observable, dynamic environments.
* **Algorithms Implemented:**
  * **Learning Real-Time A\* (LRTA\*):** Demonstrates interleaving real-time planning and execution, updating local heuristic estimates $H(s)$ dynamically as hazards are detected.

### 4. 📅 Problem 4: Automated University Exam Timetabling (CSP)
* **Concepts:** Constraint Satisfaction Problems.
* **Algorithms Implemented:**
  * **Backtracking CSP Search:** Systematically builds consistent timetable assignments.
  * **Minimum Remaining Values (MRV) Heuristic:** Prioritizes most-constrained variables first to shrink the search tree.

### 5. ⚔️ Problem 5: Strategic Real-Time Game AI
* **Concepts:** Adversarial search & decision trees.
* **Algorithms Implemented:**
  * **Minimax Framework:** Evaluates optimal decision-making for zero-sum games.
  * **Alpha-Beta Pruning:** Simulates branch cutoffs ($\alpha$ and $\beta$ thresholds) to reduce search complexity from $O(b^d)$ toward $O(b^{d/2})$.

---

## 🛠️ Requirements & Setup

### Prerequisites
* **Python 3.7+** (No external third-party libraries required; uses built-in modules `math`, `random`, `time`).

### Installation
1. Clone or download this repository:
   ```bash
   git clone [https://github.com/your-username/ai-scenario-suite.git](https://github.com/your-username/ai-scenario-suite.git)
   cd ai-scenario-suite