# Sequence based plan feasibility prediction for efficient task and motion planning

**Author** : Zhutian Yang
**Source** : arXiv

---

## Overview

- PIGInet is a transformer based feasibility predictor which cuts down time taken aswell as works on generalising for unseen objects.
- It prones large number of task plans created by a task planner into a 3-5 most feasible task plans which are then sent to motion planning.
- It breakes down the image and unput prompt ito smaller embedding tokens and then passes them through a CLIP pretrained model

---

## Idea

- The PIGInet works by using a pre-trianed CLIP transformers.
- Then the image and prompt is sent to a encoder to get semantic reasoning and combines all the features into a single position encoding which after runs through the VLM.
- The output is passed through a sigmoid and linear function.
- The output of this architecture is a probability matri which provides the top 3-5 Task plans.
- The finetuning, validation and testing is done ona kitchen setup with multiple interactive objects and cabinets.
- There are 6 cameras in the simulation to get the comlpete world view.
- 7 Key tasks were taken and 200 - 500 samples per problem were taken in the dataset.

---



