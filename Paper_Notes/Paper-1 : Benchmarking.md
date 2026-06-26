# Platform-Independent Benchmarking for Task and Motion Planning (TAMP)

This paper proposes a platform-independent benchmarking framework for evaluating Task and Motion Planning (TAMP) systems.

---

**Author:** Fabien Lagriffoul

**Source:** IEEE

---

## Research Problem

TAMP systems currently use different evaluation metrics, making comparison across methods difficult.

The paper proposes five benchmark metrics to standardize evaluation.

---

## Proposed Benchmark Metrics

- **Infeasible Task Action:** Checks whether a task is feasible.
- **Large Task Space:** Measures search complexity.
- **Motion/Task Tradeoff:** Evaluates how motion planning affects task feasibility.
- **Non-Monotonicity:** Measures whether objects must be moved multiple times.
- **Non-Geometric Actions:** Captures actions that change symbolic state without changing geometry.

> **Note**
>
> These metrics are platform-independent because they characterize the planning problem itself rather than the robot or planner implementation.

---

## Strengths

- Standardizes TAMP evaluation.
- Enables comparison across different planning systems.
- Categorizes problems according to planning complexity.

---

## Weaknesses

- Does not explicitly model object dependencies.
- Assumes several infeasible manipulation scenarios remain unsolved.

---

## Recommendations

- Introduce an **Object Dependency** benchmark.
- Extend the framework to better represent rearrangement-heavy tasks.

---

## Key Insights

Benchmark categories could help assign the most appropriate planner to different task types.

These categories may also serve as labels when evaluating or training VLM-based planners.

---

## Connection to My Research

This benchmarking framework could be extended with an **Object Dependency** metric.

Such a benchmark may help evaluate confidence-aware VLM planners and determine when adaptive TAMP triggering becomes necessary.

---

## Open Questions

- Can dependency graphs be extracted automatically from a VLM?
- Are these metrics sufficient for open-world planning?
- How should dynamic environments be benchmarked?
- Can benchmark metrics predict VLM planning failures?
           
