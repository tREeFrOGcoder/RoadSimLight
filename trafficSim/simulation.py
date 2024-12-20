from .road import Road
from copy import deepcopy
from .vehicle_generator import VehicleGenerator
from .traffic_signal import TrafficSignal
import csv

class Simulation:
    vehiclesPassed = 0;
    vehiclesPresent = 0;
    vehicleRate = 0;
    isPaused = False;

    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0            # Time keeping
        self.frame_count = 0    # Frame count keeping
        self.dt = 1/60          # Simulation time step
        # self.dt = 1/10          # Simulation time step
        self.roads = []         # Array to store roads
        self.generators = []
        self.traffic_signals = []
        self.iteration = 0      # n-th iteration (of sampling, if enabled)

    def create_road(self, start, end):
        road = Road(start, end)
        self.roads.append(road)
        return road

    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_gen(self, config={}):
        gen = VehicleGenerator(self, config)
        self.generators.append(gen)
        Simulation.vehicleRate = gen.vehicle_rate
        return gen

    def create_signal(self, roads, config={}):
        roads = [[self.roads[i] for i in road_group] for road_group in roads]
        sig = TrafficSignal(roads, config)
        self.traffic_signals.append(sig)
        return sig

    def update(self):
        # Update every road
        for road in self.roads:
            road.update(self.dt)

        # Add vehicles
        for gen in self.generators:
            gen.update()

        for signal in self.traffic_signals:
            signal.update(self)

        # Check roads for out of bounds vehicle
        for road in self.roads:
            # If road has no vehicles, continue
            if len(road.vehicles) == 0: continue
            # If not
            vehicle = road.vehicles[0]
            # If first vehicle is out of road bounds
            if vehicle.x >= road.length:
                # If vehicle has a next road
                if vehicle.current_road_index + 1 < len(vehicle.path):
                    # Update current road to next road
                    vehicle.current_road_index += 1
                    # Create a copy and reset some vehicle properties
                    new_vehicle = deepcopy(vehicle)
                    new_vehicle.x = 0
                    # Add it to the next road
                    next_road_index = vehicle.path[vehicle.current_road_index]
                    # print("next_road_index: " + str(next_road_index))
                    self.roads[next_road_index].vehicles.append(new_vehicle)
                else:
                    Simulation.vehiclesPassed += 1
                # In all cases, remove it from its road
                road.vehicles.popleft() 

                # if vehicle reached the end of the path
                # if vehicle.current_road_index + 1 == len(vehicle.path):
                #     Simulation.vehiclesPassed += 1
                    # print("Vehicle passed: " + str(Simulation.vehiclesPassed))

        # Check for the number of vehicles present
        Simulation.vehiclesPresent = 0
        for road in self.roads:
            Simulation.vehiclesPresent += len(road.vehicles)

        # Increment time
        self.t += self.dt
        self.frame_count += 1

        # Stop at certain time in seconds (for sampling purposes. Comment out if not needed)
        self.time_limit = 1200
        if self.t >= self.time_limit:
            vehicles_passed = Simulation.vehiclesPassed
            vehicles_present = Simulation.vehiclesPresent
            vehicle_rate = Simulation.vehicleRate
            

            # Derived indicators
            traffic_density = Simulation.vehiclesPresent / (4 * 100)
            throughput_rate = vehicles_passed / self.t                      # Vehicles per second
            vehicle_turnover_rate = throughput_rate*3600 / (60*vehicle_rate)


            # average_density_per_road = traffic_density / len(self.roads) if len(self.roads) > 0 else 0
            # congestion_efficiency = vehicle_rate / traffic_density if traffic_density > 0 else 0

            # Print results
            print("---------------------------------")
            print("---------------------------------")
            print("Iteration: " + str(self.iteration))
            # print(f"Time: {round(self.t, 2)} s")
            print(f"Traffic Lights Duration: {self.traffic_signals[0].cycle_length}s")
            # print(f"Vehicle Speed: {5} m/s")
            # print(f"Acceleration: {3} m/s^2")
            print(f"Vehicle Rate: {60*vehicle_rate} cars/hr")
            print("*************")
            # print(f"Vehicles Passed: {Simulation.vehiclesPassed}")
            # print(f"Vehicles Present: {Simulation.vehiclesPresent}")
            # print(f"Traffic Density: {round(traffic_density*1000, 2)} cars/km")
            # print(f"Vehicle Turnover Rate: {round(vehicle_turnover_rate * 100, 2)}%")
            # print(f"Throughput Rate: {round(throughput_rate*3600, 2)} cars/hour")
            print(f"{round(traffic_density*1000, 2)} {round(vehicle_turnover_rate * 100, 2)}% {round(throughput_rate*3600, 2)}")
            # print("Average Density per Road:", round(average_density_per_road, 2))
            # print("Congestion Efficiency:", round(congestion_efficiency, 2))



            # print("Traffic Signal Cycle Length: " + str(self.traffic_signals[0].cycle_length))
            # print("Time: " + str(self.t))
            # print("Vehicles Passed: " + str(Simulation.vehiclesPassed))
            # print("Vehicles Present: " + str(Simulation.vehiclesPresent))
            # print("Vehicle Rate: " + str(Simulation.vehicleRate))
            # print("Traffic Density: " + str(Simulation.vehiclesPresent / (len(self.roads) * self.roads[0].length)))
            # print()
            # print("Iteration: " + str(self.iteration))




            # # Add to CSV the time and vehicles passed
            # with open('data.csv', mode='a') as data_file:
            #     data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #     data_writer.writerow([self.traffic_signals[0].cycle_length, Simulation.vehiclesPassed])

            # Reset time and vehicles passed
            self.t = 0.001
            gen.delete_all_vehicles()
            Simulation.vehiclesPassed = 0
            Simulation.vehiclesPresent = 0
            self.iteration += 1
            if self.iteration % 5 == 0:
                # Set all traffic signals to +1
                for signal in self.traffic_signals:
                    signal.cycle_length += 1


    def run(self, steps):
        for _ in range(steps):
            self.update()

    def pause(self):
        self.isPaused = True

    def resume(self):
        self.isPaused = False