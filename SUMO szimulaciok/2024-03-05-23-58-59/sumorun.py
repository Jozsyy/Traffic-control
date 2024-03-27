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

while traci.simulation.getMinExpectedNumber()>0:
        print(f"Step {step}:")
       
        traci.simulationStep()

        vehicles=traci.vehicle.getIDList()
        trafficlights=traci.trafficlight.getIDList()
            
        ##----------MACHINE LEARNING CODES/FUNCTIONS HERE----------##

        #Fuzzy logic
        Fuzzy_System = fz.Fuz_Sys()
        fz.Fuzzy_Init(Fuzzy_System)
        traffic_light = "cluster_1936414352_1936414379_26003429_7516041220_#2more"
        tl2 = "joinedS_cluster_1048507714_1528675438_248743350_248743351_#2more_cluster_248743346_3620518112_513613012_cluster_26003932_3620518113_3620518114"
        tl3 = "GS_cluster_1016184195_8729367879_9418026652_9418026684_#1more"
        #controlled lanes:('-948993200#1_0', '-948993200#1_0', '-948993200#1_0', '-948993200#1_0', '198516616#5_0', '198516616#5_0', '198516616#5_1', '198516616#5_1', '198516616#5_1', '-198516616#9_0', '-198516616#9_0', '-198516616#9_1', '-198516616#9_1', '-198516616#9_1')
        
        detector1="laneAreaDetector1"
        detector2="laneAreaDetector2"
        detector3="laneAreaDetector3"
        detector4="laneAreaDetector4"
        detector5="laneAreaDetector5"

        print("Cars waiting in lane 1:"+str(traci.lanearea.getLastStepVehicleNumber(detector1)))
        print("Cars waiting in lane 2:"+str(traci.lanearea.getLastStepVehicleNumber(detector2)))
        print("Cars waiting in lane 3:"+str(traci.lanearea.getLastStepVehicleNumber(detector3)))
        print("Cars waiting in lane 4:"+str(traci.lanearea.getLastStepVehicleNumber(detector4)))
        print("Cars waiting in lane 5:"+str(traci.lanearea.getLastStepVehicleNumber(detector5)))


        if step<10 or step>40:
                traci.trafficlight.setPhaseDuration(traffic_light, 5)
                traci.trafficlight.setRedYellowGreenState(traffic_light, "GGGGrrrrrrrGGGGg")
        else:
                traci.trafficlight.setPhaseDuration(traffic_light, 5)
                traci.trafficlight.setRedYellowGreenState(traffic_light, "yyyyGGGGGGGGrrrr")

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
