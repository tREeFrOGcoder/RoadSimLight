# Traffic-Simulation
 
Incorporated from https://github.com/BilHim/trafficSimulator and https://github.com/gigahidjrikaaa/Traffic-Simulation.

A traffic flow simulation using a microscopic model called Intelligent-Driver Model, implemented using Python with the Pygame module. 
The related original authors' fantastic articles can be found: https://towardsdatascience.com/simulating-traffic-flow-in-python-ee1eab4dd20f and https://muddy-vulture-d01.notion.site/The-Modelling-of-Simpang-Empat-Pingit-Crossroad-a7f1a8adf0d44317aebff998149494b9?pvs=25.

# How To Run?
- Using conda for env separation: `conda create -name roadsim python=3.10`
- `conda activate roadsim`
- Then run these to download dependencies:
    ```
    pip install numpy
    pip install pygame
    pip install scipy
    ```
- Final step, `python simp_main.py` will run the 2-lane version; `python main.py` will run the three-lane version.

# Parameter tuning: 
(will use `simp_main.py` as an example, `main.py` is the same)
- Adjust vehicle generation rate by setting `VEHICLE_RATE` in `simp_main.py`
- Adjust simulation speed-up by setting `STEPS_PER_UPDATE` in `simp_main.py`
- Adjust traffic signal cycle (s) by setting `self.cycle_length` in `traffic_signal.py`
- Adjust vehicle average speed, starting acceleration and braking acceleration by setting `self.v_max`, `self.a_max` and `self.b_max` respectively in `vehicle.py`