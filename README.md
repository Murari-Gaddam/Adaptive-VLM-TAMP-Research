# Adaptive-VLM-TAMP-Research

## Overview

This repository documents my research into adaptive Vision-Language Model (VLM) based Task and Motion Planning (TAMP).

The primary objective is to investigate when lightweight VLM reasoning is sufficient and when a robot should invoke a full TAMP pipeline.

---

## Motivation

Current robotic planning systems generally follow one of two approaches:

- Symbolic TAMP
- Vision-Language based planning

Both have advantages and limitations.

This project investigates whether uncertainty estimation can be used to combine both approaches.

---

## Current Research Questions

- How can VLM planning confidence be estimated?
- How do object dependencies affect planning reliability?
- Can uncertainty trigger adaptive planner selection?
- What limitations exist in current VLM-TAMP systems?
- How do we apply this in openworld without complete world Knowledge

---

## Repository Contents

adaptive-vlm-tamp-research/
│
├── README.md
│
├── 01_paper_notes/
│   ├── piginet.md
│   ├── vlm_tamp.md
│   ├── vizcoast.md
│   └── integrated_tamp.md
│
├── 02_ideas/
│   ├── confidence_triggering.md
│   ├── observer_vlm.md
│   └── adaptive_vlm_tamp.md
│
├── 03_prototypes/
│   └── prototype_v1/
│
├── 04_experiments/
│   └── experiment_log.md
│
├── 05_research_questions/
│   ├── confidence_metrics.md
│   ├── dependency_reasoning.md
│   └── open_world_planning.md
│
└── 06_timeline/
    ├── research_journey.md
    └── milestones.md
    
---


## Research Roadmap

- [x] Read foundational VLM-TAMP literature
- [x] Build initial task-planning prototype
- [ ] Investigate confidence estimation
- [ ] Develop confidence-aware planning prototype
- [ ] Evaluate against existing TAMP approaches
- [ ] Explore adaptive VLM-TAMP architecture

---

## Disclaimer

This repository serves as an open research journal documenting my ideas, prototypes, literature review, and experimental progress.

Many ideas presented here are exploratory and may evolve, be refined, or be discarded as the research progresses.
