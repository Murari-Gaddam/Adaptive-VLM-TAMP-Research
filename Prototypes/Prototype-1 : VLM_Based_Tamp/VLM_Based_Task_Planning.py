import PIL.Image
from google import genai
import time

client = genai.Client(api_key="")

image = PIL.Image.open("Path Planing/images/RL_Bookself1.jpeg")
goal_object = input("Enter goal object: ")


vlm_start = time.perf_counter()

response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[image, f"""You are an advanced AI Robot Task Planner operating in a 3D tabletop environment. 
Your goal is to analyze the provided image and generate a collision-free, logically sound sequential task plan to retrieve the target object.

### Target Object
Target: {goal_object}

### Robot Kinematic Capabilities (Action Space)
Only use the following parameterized actions. Do not invent new actions.
- pick(object): Grasp an object from the side (top-down grasps are physically blocked).
- place(object, location): Place a held object onto a stable surface location.
- move(object, direction): Shift an object linearly.
- slide(object, direction): Slide an object along a surface without lifting.
- push(object, direction) / pull(object, direction): Apply lateral force.
- open(object) / close(object): Operate articulated joints (drawers, lids, doors).

*Note: For 'direction', use relative egocentric terms: [left, right, forward, backward, up, down].*

### Environmental & Physics Constraints
1. **Grasp Obstruction:** If an object is inside a container, drawer, or under a lid, the container must be `open(object)` before a `pick` is attempted.
2. **Clearance Rule:** If an object is stacked beneath or directly blocked by another object, the obstructing object(s) must be cleared first.
3. **Stability Guard:** Do not generate any action that violates gravity or causes ungrasped objects to fall, tip over, or become unstable.
4. **Efficiency:** Minimize the total number of actions. Do not move objects that do not directly or indirectly block the target object.

Output Format:

1. Scene Description: List objects and their spatial relations (e.g., "A is inside B").
2. Constraints: Identify blocking objects and why the target isn't immediately accessible.
3. Action Plan:
   1. [Action] -> [Expected world state change]
   2. [Action] -> [Expected world state change]
"""])

vlm_end = time.perf_counter()
vlm_duration = vlm_end - vlm_start

print(f"System 1 (VLM ) Latency: {vlm_duration:.4f} seconds")

print(response.text)
