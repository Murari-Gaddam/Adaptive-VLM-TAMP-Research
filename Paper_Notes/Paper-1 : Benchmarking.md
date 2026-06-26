# **Platform independent benchmarking for task and motion planning (TAMP)**

This papers main perpose is to create universal benchmarking metrics for task and planning which is platform independent.

## **Author** : Fabien Lagriffoul
## **Source** : IEEE Paper

---

## **Problem** : 
TAMP models from different sources use varies benchmarking metrics.
This paper proposes 5 standard benchmarking metrics to forster easy communication.

---

## **Idea** : 
There are 5 benchmarking metrics proposed :

- **Infeasible task action** : Checking if the task is feasible or not . 

- **Large task space** : larger the task space more is the search effort .

- **Motion/task tradeoff** : can the task be done is the motion planning is done carefully .

- **Non-Monotonicity** : Do objects need to be moves more than once .

- **Non-Geometric action** : does the problem involve actions which chnage the task planning but not the configuration space.

**Note :**
- This paper is called platform independent benchmarking as the metrics check the actual problem rather than the robot or the tamp model.
- Tamp model is tested on its success rate, CPU or GPU usage, time taken, plan optimality.

---

## **Strengths** : 
- Creates a standard benchmarking metric . 
- Adds a way to catagories problems based on these metrics.

---

## **Weaknesses** : 
- Doesn't factor additional criteria such as object relations.
- Doesn't consider object rearrangement and motion planninf infeasibility problems as solvable.

---

## **Recommendations** :
- Add a benchmmark called **Object Dependencies** into the metrics.
- By creating catagories of problems it would be easier to understand which metric is true for which.

---

## **Key Insights** : 
By using a benchmarking system like this we can catagories problems and assign the required solver . 
this metric also helps us finetune a VLM based on the different Catagories of problems

---

## **Connections with research** : 

This paper provides a benchmarking framework that could be extended with an additional Object Dependency metric.

Such a benchmark could later be used to evaluate confidence-aware VLM planners and determine when adaptive TAMP triggering becomes necessary.

---

## **Open Questions** :
- Can dependency graphs be automatically extracted from a VLM?

- Are these metrics sufficient for open-world planning?

- How would dynamic environments affect these benchmarks?
  
- Could these metrics predict VLM failure?
           
