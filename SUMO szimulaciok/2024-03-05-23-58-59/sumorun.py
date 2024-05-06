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
sequence_time1=50
sequence_time2=50
sequence_time3=50
delta_t1=0
delta_t2=0
delta_t3=0
next_sequence=0
sequence1_cars_prev=0
sequence2_cars_prev=0
sequence3_cars_prev=0

def sequence_control(sequence):
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

        print(f"Sequence 1 change:{sequence1_change}")
        print(f"Sequence 2 change:{sequence2_change}")
        print(f"Sequence 3 change:{sequence3_change}")


        #Fuzzy control
        Fuzzy_System = fz.Fuz_Sys()
        fz.Fuzzy_Init(Fuzzy_System)
        if sequence==1:
                fuzzy_output=fz.Fuzzy_Control(sequence1_cars, sequence1_change, Fuzzy_System)
        elif sequence==2:
                fuzzy_output=fz.Fuzzy_Control(sequence2_cars, sequence2_change, Fuzzy_System)
        else:
                fuzzy_output=fz.Fuzzy_Control(sequence3_cars, sequence3_change, Fuzzy_System)

        #Update previous waiting cars by sequence
        sequence1_cars_prev=sequence1_cars
        sequence2_cars_prev=sequence2_cars
        sequence3_cars_prev=sequence3_cars

        print(f"Fuzzy output: {fuzzy_output}")
        return round(fuzzy_output,0)

while traci.simulation.getMinExpectedNumber()>0:
        print(f"Step {step}:")
       
        traci.simulationStep()

        vehicles=traci.vehicle.getIDList()
        trafficlights=traci.trafficlight.getIDList()
            
        ##----------MACHINE LEARNING CODES/FUNCTIONS HERE----------##


        ##---------------------------------------------------------------##
        


        ##----------CONTROL Vehicles and Traffic Lights----------##


        
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
                        delta_t1=sequence_control(sequence)
                        print(delta_t1)
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

                sequence_time1+=delta_t1  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t1!=0 and delta_t1%2==0:
                        sequence_time2-=delta_t1/2
                        sequence_time3-=delta_t1/2
                elif delta_t1!=0 and delta_t1%2!=0:
                        sequence_time2-=round(delta_t1/2,0)
                        delta_t1-=round(delta_t1/2,0)
                        sequence_time3-=delta_t1

                next_sequence+=sequence_time1
                sequence+=1
                print("Time:")
                print(sequence_time1+sequence_time2+sequence_time3)
                print(sequence_time1)
                print(sequence_time2)
                print(sequence_time3)

        elif step==next_sequence and sequence==2:
                #traci.trafficlight.setPhaseDuration(traffic_light_ref, sequence_time)
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "rrrgggggggrrrggrrrr")
                delta_t2=sequence_control(sequence)
                print(delta_t2)
                sequence_time2+=delta_t2  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t2!=0 and delta_t2%2==0:
                        sequence_time3-=delta_t2/2
                        sequence_time1-=delta_t2/2
                elif delta_t2!=0 and delta_t2%2!=0:
                        sequence_time3-=round(delta_t2/2,0)
                        delta_t2-=round(delta_t2/2,0)
                        sequence_time1-=delta_t2
                
                next_sequence+=sequence_time2
                sequence+=1
                print("Time:")
                print(sequence_time1+sequence_time2+sequence_time3)
                print(sequence_time1)
                print(sequence_time2)
                print(sequence_time3)

        elif step==next_sequence and sequence==3:
                #traci.trafficlight.setPhaseDuration(traffic_light_ref, sequence_time-5)
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "Grrrrrrrrrrrrrrgggg")
                delta_t3=sequence_control(sequence)
                print(delta_t3)
                sequence_time3+=delta_t3  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t3!=0 and delta_t3%2==0:
                        sequence_time1-=delta_t3/2
                        sequence_time2-=delta_t3/2
                elif delta_t3!=0 and delta_t3%2!=0:
                        sequence_time1-=round(delta_t3/2,0)
                        delta_t3-=round(delta_t3/2,0)
                        sequence_time2-=delta_t3

                next_sequence+=sequence_time3
                sequence=1
                print("Time:")
                print(sequence_time1+sequence_time2+sequence_time3)
                print(sequence_time1)
                print(sequence_time2)
                print(sequence_time3)
        
        #Szekvenciak
        #traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "GGGrrrrrrrGGGrrrrrr")
        #traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "Grrrrrrrrrrrrrrgggg")
        #traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "rrrgggggggrrrggrrrr")


        ##------------------------------------------------------##

        vehicles=traci.vehicle.getIDList()
        trafficlights=traci.trafficlight.getIDList()

        '''
        if step % 5 == 0:
                lane1_0=traci.lanearea.getLastStepVehicleNumber(detector1_0)
                lane1_1=traci.lanearea.getLastStepVehicleNumber(detector1_1)
                lane1_2=traci.lanearea.getLastStepVehicleNumber(detector1_2)
                lane2_0=traci.lanearea.getLastStepVehicleNumber(detector2_0)
                lane3_0=traci.lanearea.getLastStepVehicleNumber(detector3_0)
                lane3_1=traci.lanearea.getLastStepVehicleNumber(detector3_1)
                lane3_2=traci.lanearea.getLastStepVehicleNumber(detector3_2)
                lane4_0=traci.lanearea.getLastStepVehicleNumber(detector4_0)
                lane4_1=traci.lanearea.getLastStepVehicleNumber(detector4_1)

                sequence1_cars_prev=lane1_0+lane1_1+lane3_0+lane3_1
                sequence2_cars_prev=lane1_2+lane2_0+lane3_2
                sequence3_cars_prev=lane4_0+lane4_1
        '''

        step += 1
traci.close()
