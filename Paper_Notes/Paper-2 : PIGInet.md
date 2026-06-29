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

## Metrics : 

**Efficiency** : Does PIGInet improve speed without success rate loss ?

**Generalization** : can a trained model make acurate predictions in problems with unseen objects ?

**Ablation** : if parts if the input are missing can PIGInet still make accurate predictions ?

> All 3 metrics have been improved

---

## Strengths :

- Reduces compute time and improves optimality by making better planning predictions.
- Has been finetuned with a relatively small dataset , which has improved the accuracy irrespective of it's size.
- Due to the encoding in the transformer there is better semantic reasoning internally.

---

## Limitations

- No real life environments or situations have a perfect multi camera setup with perfect
  3D map , making this idea simulation only.
- Doesn't consider the properties of the objects and there relations with other objects or surfaces.
- Cannot plan in a unseen envirnment.
- Cannot have more than 10 interactive objects in the environment.
- Doesn't check for further paths when the object is obstructed or occluded

---

## Key insights :

- By using the Embedding of the image and text with other inputs into a single encoder improves accuracy with some to no more increase in compute.
- PIGInet is a key reference point in the develop of the future projects which involve VLM and LLM based architecture with the same encoding solution.

---

## Research questions : 
- How do we implement the Encoding in a way that promotes the VLM and LLM based architecture?
- Can it be used to tranfer embedding from VLM to LLM without large amounts of transition overhead?
- How does such a small finetuning data set help improve the results?
- Can this be applied in real world by making changes in how the model works and interprets the environment?
