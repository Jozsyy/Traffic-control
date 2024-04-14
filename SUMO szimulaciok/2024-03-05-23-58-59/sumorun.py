import traci
import time
import traci.constants as tc
import pytz
import datetime
from random import randrange
import pandas as pd
import fuzzy as fz

sumoCmd = ["sumo-gui", "-c", "osm.sumocfg"]
traci.start(sumoCmd)

packVehicleData = []
packTLSData = []
packBigData = []
step=0

lane1_cars_prev=0
lane2_cars_prev=0
lane3_cars_prev=0
lane4_cars_prev=0
lane5_cars_prev=0

traffic_light_ref="cluster_1987096989_257998255_26003945_7717709774_#1more"
sequence=1
sequence_time=50
delta_t=0
delta_t1=0
delta_t2=0
delta_t3=0
next_sequence=0
sequence1_cars_prev=0
sequence2_cars_prev=0
sequence3_cars_prev=0

def sequence_control():
        global sequence1_cars_prev
        global sequence2_cars_prev
        global sequence3_cars_prev

        #Waiting cars by lane
        lane1_0=traci.lanearea.getLastStepVehicleNumber(detector1_0)
        lane1_1=traci.lanearea.getLastStepVehicleNumber(detector1_1)
        lane1_2=traci.lanearea.getLastStepVehicleNumber(detector1_2)
        lane2_0=traci.lanearea.getLastStepVehicleNumber(detector2_0)
        lane3_0=traci.lanearea.getLastStepVehicleNumber(detector3_0)
        lane3_1=traci.lanearea.getLastStepVehicleNumber(detector3_1)
        lane3_2=traci.lanearea.getLastStepVehicleNumber(detector3_2)
        lane4_0=traci.lanearea.getLastStepVehicleNumber(detector4_0)
        lane4_1=traci.lanearea.getLastStepVehicleNumber(detector4_1)

        print("Cars waiting in lane 1_0:"+str(lane1_0))
        print("Cars waiting in lane 1_1:"+str(lane1_1))
        print("Cars waiting in lane 1_2:"+str(lane1_2))
        print("Cars waiting in lane 2_0:"+str(lane2_0))
        print("Cars waiting in lane 3_0:"+str(lane3_0))
        print("Cars waiting in lane 1_1:"+str(lane3_1))
        print("Cars waiting in lane 1_2:"+str(lane3_2))
        print("Cars waiting in lane 1_0:"+str(lane4_0))
        print("Cars waiting in lane 1_1:"+str(lane4_1))

        waiting_cars=lane1_0+lane1_1+lane1_2+lane2_0+lane3_0+lane3_1+lane3_2+lane4_0+lane4_1
        print("All waiting cars:"+str(waiting_cars))

        sequence1_cars=lane1_0+lane1_1+lane3_0+lane3_1
        sequence2_cars=lane1_2+lane2_0+lane3_2
        sequence3_cars=lane4_0+lane4_1

        sequence1_change=sequence1_cars_prev-sequence1_cars
        sequence2_change=sequence2_cars_prev-sequence2_cars
        sequence3_change=sequence3_cars_prev-sequence3_cars


        #Fuzzy control
        Fuzzy_System = fz.Fuz_Sys()
        fz.Fuzzy_Init(Fuzzy_System)
        fuzzy_output=fz.Fuzzy_Control(sequence1_cars, sequence1_change, sequence2_cars, sequence2_change, sequence3_cars, sequence3_change, Fuzzy_System)

        #Update previous waiting cars by sequence
        sequence1_cars_prev=sequence1_cars
        sequence2_cars_prev=sequence2_cars
        sequence3_cars_prev=sequence3_cars

        print(f"Fuzzy output: {fuzzy_output}")
        return fuzzy_output

while traci.simulation.getMinExpectedNumber()>0:
        print(f"Step {step}:")
       
        traci.simulationStep()

        vehicles=traci.vehicle.getIDList()
        trafficlights=traci.trafficlight.getIDList()
            
        ##----------MACHINE LEARNING CODES/FUNCTIONS HERE----------##

        '''
        traffic_light = "cluster_1936414352_1936414379_26003429_7516041220_#2more"

        detector1="laneAreaDetector1"
        detector2="laneAreaDetector2"
        detector3="laneAreaDetector3"
        detector4="laneAreaDetector4"
        detector5="laneAreaDetector5"

        
        if step<10 or step>40:
                #traci.trafficlight.setPhaseDuration(traffic_light, 5)
                traci.trafficlight.setRedYellowGreenState(traffic_light, "rrrrrrGGGrrGGG")
        else:
                #traci.trafficlight.setPhaseDuration(traffic_light, 5)
                traci.trafficlight.setRedYellowGreenState(traffic_light, "yyyyrrrGGyyyGG")

        tls="258668307"
        traci.trafficlight.setRedYellowGreenState(tls, "rr")
        '''
        ### Dozsa Gyorgy utca
        '''
        if step%5==0:

                lane1_cars=traci.lanearea.getLastStepVehicleNumber(detector1)
                lane2_cars=traci.lanearea.getLastStepVehicleNumber(detector2)
                lane3_cars=traci.lanearea.getLastStepVehicleNumber(detector3)
                lane4_cars=traci.lanearea.getLastStepVehicleNumber(detector4)
                lane5_cars=traci.lanearea.getLastStepVehicleNumber(detector5)

                print("Cars waiting in lane 1:"+str(lane1_cars))
                print("Cars waiting in lane 2:"+str(lane2_cars))
                print("Cars waiting in lane 3:"+str(lane3_cars))
                print("Cars waiting in lane 4:"+str(lane4_cars))
                print("Cars waiting in lane 5:"+str(lane5_cars))

                lane1_change=lane1_cars-lane1_cars_prev
                lane2_change=lane2_cars-lane2_cars_prev
                lane3_change=lane3_cars-lane3_cars_prev
                lane4_change=lane4_cars-lane4_cars_prev
                lane5_change=lane5_cars=lane5_cars_prev

                print("Cars waiting in lane 1 - prev:"+str(lane1_change))
                print("Cars waiting in lane 2 - prev:"+str(lane2_change))
                print("Cars waiting in lane 3 - prev:"+str(lane3_change))
                print("Cars waiting in lane 4 - prev:"+str(lane4_change))
                print("Cars waiting in lane 5 - prev:"+str(lane5_change))

                #Fuzzy logic
                Fuzzy_System = fz.Fuz_Sys()
                fz.Fuzzy_Init(Fuzzy_System)

                #input1=[lane1_cars/12, lane1_change/12]
                #input2=[(lane2_cars+lane3_cars)/12, (lane2_change+lane3_change)/12]
                #input3=[(lane4_cars+lane5_cars)/12, (lane4_change+lane5_change)/12]

                #print(input1, input2)

                output_fuzzy=fz.Fuzzy_Control(lane1_cars, lane2_cars, Fuzzy_System)
                print("Fuzzy control:", output_fuzzy)

                if output_fuzzy<0.5:
                        traci.trafficlight.setRedYellowGreenState(traffic_light, "rrrrGGGGGGGGGG")
                else:
                        traci.trafficlight.setRedYellowGreenState(traffic_light, "GGGGrrrrrrrrrr")

                lane1_cars_prev=lane1_cars
                lane2_cars_prev=lane2_cars
                lane3_cars_prev=lane3_cars
                lane4_cars_prev=lane4_cars
                lane5_cars_prev=lane5_cars
        '''
        
        ### Reformatus kollegium utca
        detector1_0="laneAreaDetector-43791591#1_0"
        detector1_1="laneAreaDetector-43791591#1_1"
        detector1_2="laneAreaDetector-43791591#1_2"
        detector2_0="laneAreaDetector-954637017#1_0"
        detector3_0="laneAreaDetector826606609#0_0"
        detector3_1="laneAreaDetector826606609#0_1"
        detector3_2="laneAreaDetector826606609#0_2"
        detector4_0="laneAreaDetector23349324#4_0"
        detector4_1="laneAreaDetector23349324#4_1"
        
        if step==next_sequence and sequence==1:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "GGGrrrrrrrGGGrrrrrr")
                if step>0:
                        delta_t1=sequence_control()
                else: 
                        lane1_0=traci.lanearea.getLastStepVehicleNumber(detector1_0)
                        lane1_1=traci.lanearea.getLastStepVehicleNumber(detector1_1)
                        lane1_2=traci.lanearea.getLastStepVehicleNumber(detector1_2)
                        lane2_0=traci.lanearea.getLastStepVehicleNumber(detector2_0)
                        lane3_0=traci.lanearea.getLastStepVehicleNumber(detector3_0)
                        lane3_1=traci.lanearea.getLastStepVehicleNumber(detector3_1)
                        lane3_2=traci.lanearea.getLastStepVehicleNumber(detector3_2)
                        lane4_0=traci.lanearea.getLastStepVehicleNumber(detector4_0)
                        lane4_1=traci.lanearea.getLastStepVehicleNumber(detector4_1)

                        print("Cars waiting in lane 1_0:"+str(lane1_0))
                        print("Cars waiting in lane 1_1:"+str(lane1_1))
                        print("Cars waiting in lane 1_2:"+str(lane1_2))
                        print("Cars waiting in lane 2_0:"+str(lane2_0))
                        print("Cars waiting in lane 3_0:"+str(lane3_0))
                        print("Cars waiting in lane 1_1:"+str(lane3_1))
                        print("Cars waiting in lane 1_2:"+str(lane3_2))
                        print("Cars waiting in lane 1_0:"+str(lane4_0))
                        print("Cars waiting in lane 1_1:"+str(lane4_1))

                        waiting_cars=lane1_0+lane1_1+lane1_2+lane2_0+lane3_0+lane3_1+lane3_2+lane4_0+lane4_1
                        print("All waiting cars:"+str(waiting_cars))

                        sequence1_cars=lane1_0+lane1_1+lane3_0+lane3_1
                        sequence2_cars=lane1_2+lane2_0+lane3_2
                        sequence3_cars=lane4_0+lane4_1

                        #Update previous waiting cars by sequence
                        sequence1_cars_prev=sequence1_cars
                        sequence2_cars_prev=sequence2_cars
                        sequence3_cars_prev=sequence3_cars
                        delta_t1=0
                next_sequence+=sequence_time+delta_t1
                sequence+=1

        elif step==next_sequence and sequence==2:
                #traci.trafficlight.setPhaseDuration(traffic_light_ref, sequence_time)
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "rrrgggggggrrrggrrrr")
                delta_t2=delta_t1=sequence_control()
                next_sequence+=sequence_time+delta_t2
                sequence+=1

        elif step==next_sequence and sequence==3:
                #traci.trafficlight.setPhaseDuration(traffic_light_ref, sequence_time-5)
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "Grrrrrrrrrrrrrrgggg")
                delta_t3=delta_t1=sequence_control()
                next_sequence+=sequence_time+delta_t3
                sequence=1
        
        #Szekvenciak
        #traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "GGGrrrrrrrGGGrrrrrr")
        #traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "Grrrrrrrrrrrrrrgggg")
        #traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "rrrgggggggrrrggrrrr")


        ##---------------------------------------------------------------##
        


        ##----------CONTROL Vehicles and Traffic Lights----------##


        #***SET FUNCTION FOR TRAFFIC LIGHTS***
        #REF: https://sumo.dlr.de/docs/TraCI/Change_Traffic_Lights_State.html
        trafficlightduration = [5,37,5,35,6,3]
        trafficsignal = ["rrrrrrGGGGgGGGrr", "yyyyyyyyrrrrrrrr", "rrrrrGGGGGGrrrrr", "rrrrryyyyyyrrrrr", "GrrrrrrrrrrGGGGg", "yrrrrrrrrrryyyyy"]
        tfl = "1529566418"
        #traci.trafficlight.setPhaseDuration(tfl, trafficlightduration[randrange(6)])
        #traci.trafficlight.setRedYellowGreenState(tfl, trafficsignal[randrange(6)])
        traci.trafficlight.setPhaseDuration(tfl, 30)
        traci.trafficlight.setRedYellowGreenState(tfl, "GGGGGGGGGGGGGGGGGGGGyyyyyRRRR")

        ##------------------------------------------------------##

        vehicles=traci.vehicle.getIDList()
        trafficlights=traci.trafficlight.getIDList()

        step += 1
traci.close()
