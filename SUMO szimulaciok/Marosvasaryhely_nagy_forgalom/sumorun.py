import traci
import fuzzy as fz
import numpy as np
import fuzzy_sync as fzs

sumoCmd = ["sumo-gui", "-c", "osm.sumocfg"]
traci.start(sumoCmd)

step=0

fortuna_v=[]
refo_v=[]
kozpont_v=[]

kozpont=0
refo=0
fortuna=0

fortuna_prev=0
refo_prev=0
kozpont_prev=0
fortuna_prev2=0
refo_prev2=0
kozpont_prev2=0

sequence_time_max=80

### Reformatus kollegium utcai keresztezodes
sequence=1
sequence_time1=45
sequence_time2=45
sequence_time3=45
delta_t1=0
delta_t2=0
delta_t3=0
next_sequence=0
sequence1_cars_prev=0
sequence2_cars_prev=0
sequence3_cars_prev=0
traffic_light_ref="cluster_1987096989_257998255_26003945_7717709774_#1more"
detector1_0="laneAreaDetector-43791591#1_0"
detector1_1="laneAreaDetector-43791591#1_1"
detector1_2="laneAreaDetector-43791591#1_2"
detector2_0="laneAreaDetector-954637017#1_0"
detector3_0="laneAreaDetector826606609#0_0"
detector3_1="laneAreaDetector826606609#0_1"
detector3_2="laneAreaDetector826606609#0_2"
detector4_0="laneAreaDetector23349324#4_0"
detector4_1="laneAreaDetector23349324#4_1"
lane1_0_prev=0
lane1_1_prev=0
lane1_2_prev=0
lane2_0_prev=0
lane3_0_prev=0
lane3_1_prev=0
lane3_2_prev=0
lane4_0_prev=0
lane4_1_prev=0

### Fortuna keresztezodes
sequence_f=4
sequence_time1_f=40
sequence_time2_f=40
sequence_time3_f=40
sequence_time4_f=40
delta_t1_f=0
delta_t2_f=0
delta_t3_f=0
delta_t4_f=0
next_sequence_f=0
sequence1_cars_prev_f=0
sequence2_cars_prev_f=0
sequence3_cars_prev_f=0
sequence4_cars_prev_f=0
traffic_light_Fortuna="cluster_249821091_249821092_249821094_26003449_#13more"
detector1_0_f="laneAreaDetector188302703#1_0"
detector1_1_f="laneAreaDetector188302703#1_1"
detector1_2_f="laneAreaDetector188302703#1_2"
detector2_0_f="laneAreaDetector-869087990_0"
detector2_1_f="laneAreaDetector-869087990_1"
detector3_0_f="laneAreaDetector695614758_0"
detector3_1_f="laneAreaDetector695614758_1"
detector3_2_f="laneAreaDetector695614758_2"
detector4_0_f="laneAreaDetector862984187_0"
detector4_1_f="laneAreaDetector862984187_1"
detector4_2_f="laneAreaDetector862984187_2"
detector4_3_f="laneAreaDetector862984187_3"
lane1_0_f_prev=0
lane1_1_f_prev=0
lane1_2_f_prev=0
lane2_0_f_prev=0
lane2_1_f_prev=0
lane3_0_f_prev=0
lane3_1_f_prev=0
lane3_2_f_prev=0
lane4_0_f_prev=0
lane4_1_f_prev=0
lane4_2_f_prev=0
lane4_3_f_prev=0

### Kozpont keresztezodes
sequence_k=2
sequence_time1_k=40
sequence_time2_k=40
sequence_time3_k=40
sequence_time4_k=40
delta_t1_k=0
delta_t2_k=0
delta_t3_k=0
delta_t4_k=0
next_sequence_k=0
sequence1_cars_prev_k=0
sequence2_cars_prev_k=0
sequence3_cars_prev_k=0
sequence4_cars_prev_k=0
traffic_ligt_kozpont="joinedS_cluster_1048507714_1528675438_248743350_248743351_#2more_cluster_248743346_3620518112_513613012_cluster_26003932_3620518113_3620518114"
detector4_2_k="laneAreaDetector23060091#1"
detector1_0_k="laneAreaDetector42956742#0_0"
detector1_1_k="laneAreaDetector23051421#0_0"
detector1_2_k="laneAreaDetector23051421#0_1"
detector2_0_k="laneAreaDetector-8516747#0_0"
detector2_1_k="laneAreaDetector-8516747#0_1"
detector3_0_k="laneAreaDetector23021229#0_0"
detector3_1_k="laneAreaDetector23021229#0_1"
detector4_0_k="laneAreaDetector42956741#1_0"
detector4_1_k="laneAreaDetector42956741#1_1"
lane1_0_k_prev=0
lane1_1_k_prev=0
lane1_2_k_prev=0
lane2_0_k_prev=0
lane2_1_k_prev=0
lane3_0_k_prev=0
lane3_1_k_prev=0
lane4_0_k_prev=0
lane4_1_k_prev=0
lane4_2_k_prev=0

def waiting_cars_fortuna():
        #Waiting cars by lane
        lane1_0_f=traci.lanearea.getLastStepVehicleNumber(detector1_0_f)
        lane1_1_f=traci.lanearea.getLastStepVehicleNumber(detector1_1_f)
        lane1_2_f=traci.lanearea.getLastStepVehicleNumber(detector1_2_f)
        lane2_0_f=traci.lanearea.getLastStepVehicleNumber(detector2_0_f)
        lane2_1_f=traci.lanearea.getLastStepVehicleNumber(detector2_1_f)
        lane3_0_f=traci.lanearea.getLastStepVehicleNumber(detector3_0_f)
        lane3_1_f=traci.lanearea.getLastStepVehicleNumber(detector3_1_f)
        lane3_2_f=traci.lanearea.getLastStepVehicleNumber(detector3_2_f)
        lane4_0_f=traci.lanearea.getLastStepVehicleNumber(detector4_0_f)
        lane4_1_f=traci.lanearea.getLastStepVehicleNumber(detector4_1_f)
        lane4_2_f=traci.lanearea.getLastStepVehicleNumber(detector4_2_f)
        lane4_3_f=traci.lanearea.getLastStepVehicleNumber(detector4_3_f)

        return lane1_0_f+lane1_1_f+lane1_2_f+lane2_0_f+lane2_1_f+lane3_0_f+lane3_1_f+lane3_2_f+lane4_0_f+lane4_1_f+lane4_2_f+lane4_3_f

def waiting_cars_ref():
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

        return lane1_0+lane1_1+lane1_2+lane2_0+lane3_0+lane3_1+lane3_2+lane4_0+lane4_1

def waiting_cars_kozpont():
        #Waiting cars by lane
        lane1_0_k=traci.lanearea.getLastStepVehicleNumber(detector1_0_k)
        lane1_1_k=traci.lanearea.getLastStepVehicleNumber(detector1_1_k)
        lane1_2_k=traci.lanearea.getLastStepVehicleNumber(detector1_2_k)
        lane2_0_k=traci.lanearea.getLastStepVehicleNumber(detector2_0_k)
        lane2_1_k=traci.lanearea.getLastStepVehicleNumber(detector2_1_k)
        lane3_0_k=traci.lanearea.getLastStepVehicleNumber(detector3_0_k)
        lane3_1_k=traci.lanearea.getLastStepVehicleNumber(detector3_1_k)
        lane4_0_k=traci.lanearea.getLastStepVehicleNumber(detector4_0_k)
        lane4_1_k=traci.lanearea.getLastStepVehicleNumber(detector4_1_k)
        lane4_2_k=traci.lanearea.getLastStepVehicleNumber(detector4_2_k)

        return lane1_0_k+lane1_1_k+lane1_2_k+lane2_0_k+lane2_1_k+lane3_0_k+lane3_1_k+lane4_0_k+lane4_1_k+lane4_2_k


def sequence_control_ref(sequence):
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

        sequence1_cars=lane1_0+lane1_1+lane3_0+lane3_1
        sequence2_cars=lane1_2+lane2_0+lane3_2
        sequence3_cars=lane4_0+lane4_1

        sequence1_change=sequence1_cars-sequence1_cars_prev
        sequence2_change=sequence2_cars-sequence2_cars_prev
        sequence3_change=sequence3_cars-sequence3_cars_prev

        fuzzy_sync_output=0
        #Fuzzy control
        if step!=0:
                fuzzy_system = fz.FuzzySystem()
                fuzzy_system2 = fzs.FuzzySystem()
                if sequence==1:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence1_cars, sequence1_change)
                        fuzzy_sync_output=fuzzy_system2.fuzzy_control(7/30*(sequence3_cars-sequence1_cars)+0.5, 7/60*waiting_cars_kozpont()+0.5)
                elif sequence==2:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence2_cars, sequence2_change)
                else:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence3_cars, sequence3_change)
        else:
                fuzzy_output=0

        #Update previous waiting cars by sequence
        sequence1_cars_prev=sequence1_cars
        sequence2_cars_prev=sequence2_cars
        sequence3_cars_prev=sequence3_cars

        #print(f"Fuzzy output Ref: {fuzzy_output}")
        return round(fuzzy_output+fuzzy_sync_output/5,0)

def sequence_control_fortuna(sequence_f):
        global sequence1_cars_prev_f
        global sequence2_cars_prev_f
        global sequence3_cars_prev_f
        global sequence4_cars_prev_f

        #Waiting cars by lane
        lane1_0_f=traci.lanearea.getLastStepVehicleNumber(detector1_0_f)
        lane1_1_f=traci.lanearea.getLastStepVehicleNumber(detector1_1_f)
        lane1_2_f=traci.lanearea.getLastStepVehicleNumber(detector1_2_f)
        lane2_0_f=traci.lanearea.getLastStepVehicleNumber(detector2_0_f)
        lane2_1_f=traci.lanearea.getLastStepVehicleNumber(detector2_1_f)
        lane3_0_f=traci.lanearea.getLastStepVehicleNumber(detector3_0_f)
        lane3_1_f=traci.lanearea.getLastStepVehicleNumber(detector3_1_f)
        lane3_2_f=traci.lanearea.getLastStepVehicleNumber(detector3_2_f)
        lane4_0_f=traci.lanearea.getLastStepVehicleNumber(detector4_0_f)
        lane4_1_f=traci.lanearea.getLastStepVehicleNumber(detector4_1_f)
        lane4_2_f=traci.lanearea.getLastStepVehicleNumber(detector4_2_f)
        lane4_3_f=traci.lanearea.getLastStepVehicleNumber(detector4_3_f)

        sequence1_cars_f=lane2_0_f+lane2_1_f+lane4_0_f+lane4_1_f+lane4_2_f
        sequence2_cars_f=lane2_1_f+lane4_3_f
        sequence3_cars_f=lane1_0_f+lane1_1_f+lane3_0_f+lane3_1_f
        sequence4_cars_f=lane1_2_f+lane3_2_f

        sequence1_change_f=sequence1_cars_f-sequence1_cars_prev_f
        sequence2_change_f=sequence2_cars_f-sequence2_cars_prev_f
        sequence3_change_f=sequence3_cars_f-sequence3_cars_prev_f
        sequence4_change_f=sequence4_cars_f-sequence4_cars_prev_f

        fuzzy_sync_output=0
        #Fuzzy control
        if step!=0:
                fuzzy_system = fz.FuzzySystem()
                fuzzy_system2 = fzs.FuzzySystem()
                if sequence_f==1:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence1_cars_f, sequence1_change_f)
                elif sequence_f==2:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence2_cars_f, sequence2_change_f)
                elif sequence_f==3:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence3_cars_f, sequence3_change_f)
                        fuzzy_sync_output=fuzzy_system2.fuzzy_control(7/30*(sequence1_cars_f-sequence4_cars_f)+0.5, 7/60*waiting_cars_ref()+0.5)
                else:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence4_cars_f, sequence4_change_f)
        else:
                fuzzy_output=0

        #Update previous waiting cars by sequence
        sequence1_cars_prev_f=sequence1_cars_f
        sequence2_cars_prev_f=sequence2_cars_f
        sequence3_cars_prev_f=sequence3_cars_f
        sequence4_cars_prev_f=sequence3_cars_f

        #print(f"Fuzzy output Fortuna: {fuzzy_output}")
        return round(fuzzy_output+fuzzy_sync_output/5,0)

def sequence_control_kozpont(sequence_k):
        global sequence1_cars_prev_k
        global sequence2_cars_prev_k
        global sequence3_cars_prev_k
        global sequence4_cars_prev_k

        #Waiting cars by lane
        lane1_0_k=traci.lanearea.getLastStepVehicleNumber(detector1_0_k)
        lane1_1_k=traci.lanearea.getLastStepVehicleNumber(detector1_1_k)
        lane1_2_k=traci.lanearea.getLastStepVehicleNumber(detector1_2_k)
        lane2_0_k=traci.lanearea.getLastStepVehicleNumber(detector2_0_k)
        lane2_1_k=traci.lanearea.getLastStepVehicleNumber(detector2_1_k)
        lane3_0_k=traci.lanearea.getLastStepVehicleNumber(detector3_0_k)
        lane3_1_k=traci.lanearea.getLastStepVehicleNumber(detector3_1_k)
        lane4_0_k=traci.lanearea.getLastStepVehicleNumber(detector4_0_k)
        lane4_1_k=traci.lanearea.getLastStepVehicleNumber(detector4_1_k)
        lane4_2_k=traci.lanearea.getLastStepVehicleNumber(detector4_2_k)

        sequence1_cars_k=lane1_0_k+lane1_1_k+lane1_2_k+lane3_0_k+lane3_1_k
        sequence2_cars_k=lane1_2_k+lane3_0_k
        sequence3_cars_k=lane2_0_k+lane2_1_k+lane4_0_k
        sequence4_cars_k=lane2_1_k+lane4_1_k+lane4_2_k

        sequence1_change_k=sequence1_cars_k-sequence1_cars_prev_k
        sequence2_change_k=sequence2_cars_k-sequence2_cars_prev_k
        sequence3_change_k=sequence3_cars_k-sequence3_cars_prev_k
        sequence4_change_k=sequence4_cars_k-sequence4_cars_prev_k

        #Fuzzy control
        if step!=0:
                fuzzy_system = fz.FuzzySystem()
                if sequence_f==1:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence1_cars_k, sequence1_change_k)
                elif sequence_f==2:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence2_cars_k, sequence2_change_k)
                elif sequence_f==3:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence3_cars_k, sequence3_change_k)
                else:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence4_cars_k, sequence4_change_k)
        else: 
                fuzzy_output=0

        #Update previous waiting cars by sequence
        sequence1_cars_prev_k=sequence1_cars_k
        sequence2_cars_prev_k=sequence2_cars_k
        sequence3_cars_prev_k=sequence3_cars_k
        sequence4_cars_prev_k=sequence3_cars_k

        #print(f"Fuzzy output kozpont: {fuzzy_output}")
        return round(fuzzy_output,0)

while traci.simulation.getMinExpectedNumber()>0:
        print(f"Step {step}:")
       
        traci.simulationStep()

        #Stefan cel Mare utca-hosszu utcai keresztezodes (Reformatus kollegium utca)    
        if step==next_sequence and sequence==1:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "gggrrrrrrrgggrrrrrr")
                delta_t1=sequence_control_ref(sequence)

                if sequence_time1+delta_t1<=0:
                        delta_t1=-sequence_time1+1      #legalabb 1 mp-t minimum tart
                elif delta_t1>0 and sequence_time1+delta_t1>=sequence_time_max:
                        delta_t1=0
                sequence_time1+=delta_t1  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t1!=0 and delta_t1%2==0:
                        if sequence_time2 >= delta_t1/2:
                                sequence_time2-=delta_t1/2
                        else:
                                sequence_time1-=delta_t1/2
                        if sequence_time3 >= delta_t1/2:
                                sequence_time3-=delta_t1/2
                        else:
                                sequence_time1-=delta_t1/2
                elif delta_t1!=0 and delta_t1%2!=0:
                        if sequence_time2 >= round(delta_t1/2,0):
                                sequence_time2-=round(delta_t1/2,0)
                        else:
                                sequence_time1-=round(delta_t1/2,0)
                        delta_t1-=round(delta_t1/2,0)
                        if sequence_time3 >= delta_t1:
                                sequence_time3-=delta_t1
                        else:
                                sequence_time1-=round(delta_t1/2,0)

                next_sequence+=sequence_time1
                sequence=2

        elif step==next_sequence and sequence==2:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "grrgggggggrrrggrrrr")
                delta_t2=sequence_control_ref(sequence)

                if sequence_time2+delta_t2<=0:
                        delta_t2=-sequence_time2+1
                elif delta_t2>0 and sequence_time2+delta_t2>=sequence_time_max:
                        delta_t2=0
                sequence_time2+=delta_t2  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t2!=0 and delta_t2%2==0:
                        if sequence_time3 >= delta_t2/2:
                                sequence_time3-=delta_t2/2
                        else:
                                sequence_time2-=delta_t2/2
                        if sequence_time1 >= delta_t2/2:
                                sequence_time1-=delta_t2/2
                        else:
                                sequence_time2-=delta_t2/2
                elif delta_t2!=0 and delta_t2%2!=0:
                        if sequence_time3 >= round(delta_t2/2,0):
                                sequence_time3-=round(delta_t2/2,0)
                        else:
                                sequence_time2-=round(delta_t2/2,0)
                        delta_t2-=round(delta_t2/2,0)
                        if sequence_time1 >= delta_t2:
                                sequence_time1-=delta_t2
                        else:
                                sequence_time2-=delta_t2
                
                next_sequence+=sequence_time2
                sequence=3

        elif step==next_sequence and sequence==3:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "grrrrrrrrrrrrrrgggg")
                delta_t3=sequence_control_ref(sequence)

                if sequence_time3+delta_t3<=0:
                        delta_t3=-sequence_time3+1
                elif delta_t3>0 and sequence_time3+delta_t3>=sequence_time_max:
                        delta_t3=0
                sequence_time3+=delta_t3  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t3!=0 and delta_t3%2==0:
                        if sequence_time1 >= delta_t3/2:
                                sequence_time1-=delta_t3/2
                        else:
                                sequence_time3-=delta_t3/2
                        if sequence_time2 >= delta_t3/2:
                                sequence_time2-=delta_t3/2
                        else:
                                sequence_time3-=delta_t3/2
                elif delta_t3!=0 and delta_t3%2!=0:
                        if sequence_time1 >= round(delta_t3/2,0):
                                sequence_time1-=round(delta_t3/2,0)
                        else:
                                sequence_time3-=round(delta_t3/2,0)
                        delta_t3-=round(delta_t3/2,0)
                        if sequence_time2 >= delta_t3:
                                sequence_time2-=delta_t3
                        else:
                                sequence_time3-=delta_t3

                next_sequence+=sequence_time3
                sequence=1

        ### Fortuna
        if step==next_sequence_f and sequence_f==1:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "rrrrgggrrrrgggr") #foutrol elore
                delta_t1_f=sequence_control_fortuna(sequence_f)
                #print(f"Szekvencia 1 zold ido modositasa: {delta_t1_f}")
                       
                if sequence_time1_f+delta_t1_f<=0:
                        delta_t1_f=-sequence_time1_f+1
                elif delta_t1_f>0 and sequence_time1_f+delta_t1_f>=sequence_time_max:
                        delta_t1_f=0
                sequence_time1_f+=delta_t1_f  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t1_f!=0 and delta_t1_f%3==0:
                        if sequence_time2_f >= delta_t1_f/3:
                                sequence_time2_f-=delta_t1_f/3
                        else:
                                sequence_time1_f-=delta_t1_f/3
                        if sequence_time3_f >= delta_t1_f/3:
                                sequence_time3_f-=delta_t1_f/3
                        else:
                                sequence_time1_f-=delta_t1_f/3
                        if sequence_time4_f >= delta_t1_f/3:
                                sequence_time4_f-=delta_t1_f/3
                        else:
                                sequence_time1_f-=delta_t1_f/3
                elif delta_t1_f!=0 and delta_t1_f%3!=0:
                        if sequence_time2_f >= round(delta_t1_f/3,0):
                                sequence_time2_f-=round(delta_t1_f/3,0)
                        else:
                                sequence_time1_f-=round(delta_t1_f/3,0)
                        delta_t1_f-=round(delta_t1_f/3,0)
                        if sequence_time3_f >= round(delta_t1_f/2,0):
                                sequence_time3_f-=round(delta_t1_f/2,0)
                        else:
                                sequence_time1_f-=round(delta_t1_f/2,0)
                        delta_t1_f-=round(delta_t1_f/2,0)
                        if sequence_time4_f >= delta_t1_f:
                                sequence_time4_f-=delta_t1_f
                        else:
                                sequence_time1_f-=delta_t1_f
                next_sequence_f+=sequence_time1_f
                sequence_f=2

                print(f"Szekvencia 1 idotartam: {sequence_time1_f}")
                print(f"Szekvencia 2 idotartam: {sequence_time2_f}")
                print(f"Szekvencia 3 idotartam: {sequence_time3_f}")
                print(f"Szekvencia 4 idotartam: {sequence_time4_f}")

        elif step==next_sequence_f and sequence_f==2:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "grrrrrrggrrrrrg") #foutrol balra
                delta_t2_f=sequence_control_fortuna(sequence_f)
                print(f"Szekvencia 2 zold ido modositasa: {delta_t2_f}")

                if sequence_time2_f+delta_t2_f<=0:
                        delta_t2_f=-sequence_time2_f+1
                elif delta_t2_f>0 and sequence_time2_f+delta_t2_f>=sequence_time_max:
                        delta_t2_f=0
                sequence_time2_f+=delta_t2_f  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t2_f!=0 and delta_t2_f%3==0:
                        if sequence_time1_f >= delta_t2_f/3:
                                sequence_time1_f-=delta_t2_f/3
                        else:
                                sequence_time2_f-=delta_t2_f/3
                        if sequence_time3_f >= delta_t2_f/3:
                                sequence_time3_f-=delta_t2_f/3
                        else:
                                sequence_time2_f-=delta_t2_f/3
                        if sequence_time4_f >= delta_t2_f/3:
                                sequence_time4_f-=delta_t2_f/3
                        else:
                                sequence_time2_f-=delta_t2_f/3
                elif delta_t2_f!=0 and delta_t2_f%3!=0:
                        if sequence_time1_f >= round(delta_t2_f/3,0):
                                sequence_time1_f-=round(delta_t2_f/3,0)
                        else:
                                sequence_time2_f-=round(delta_t2_f/3,0)
                        delta_t2_f-=round(delta_t2_f/3,0)
                        if sequence_time3_f >= round(delta_t2_f/2,0):
                                sequence_time3_f-=round(delta_t2_f/2,0)
                        else:
                                sequence_time2_f-=round(delta_t2_f/2,0)
                        delta_t2_f-=round(delta_t2_f/2,0)
                        if sequence_time4_f >= delta_t2_f:
                                sequence_time4_f-=delta_t2_f
                        else:
                                sequence_time2_f-=delta_t2_f
                
                next_sequence_f+=sequence_time2_f
                sequence_f=3

                print(f"Szekvencia 1 idotartam: {sequence_time1_f}")
                print(f"Szekvencia 2 idotartam: {sequence_time2_f}")
                print(f"Szekvencia 3 idotartam: {sequence_time3_f}")
                print(f"Szekvencia 4 idotartam: {sequence_time4_f}")

        elif step==next_sequence_f and sequence_f==3:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "gggrrrrrggrrrrr") #mellekutrol elore
                delta_t3_f=sequence_control_fortuna(sequence_f)
                print(f"Szekvencia 3 zold ido modositasa: {delta_t3_f}")

                if sequence_time3_f+delta_t3_f<=0:
                        delta_t3_f=-sequence_time3_f+1
                elif delta_t3_f>0 and sequence_time3_f+delta_t3_f>=sequence_time_max:
                        delta_t3_f=0
                sequence_time3_f+=delta_t3_f  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t3_f!=0 and delta_t3_f%3==0:
                        if sequence_time1_f >= delta_t3_f/3:
                                sequence_time1_f-=delta_t3_f/3
                        else:
                                sequence_time3_f-=delta_t3_f/3
                        if sequence_time2_f >= delta_t3_f/3:
                                sequence_time2_f-=delta_t3_f/3
                        else:
                                sequence_time3_f-=delta_t3_f/3        
                        if sequence_time4_f >= delta_t3_f/3:
                                sequence_time4_f-=delta_t3_f/3
                        else:
                                sequence_time3_f-=delta_t3_f/3
                elif delta_t3_f!=0 and delta_t3_f%3!=0:
                        if sequence_time1_f >= round(delta_t3_f/3,0):
                                sequence_time1_f-=round(delta_t3_f/3,0)
                        else:
                                sequence_time3_f-=round(delta_t3_f/3,0)
                        delta_t3_f-=round(delta_t3_f/3,0)
                        if sequence_time2_f >= round(delta_t3_f/2,0):
                                sequence_time2_f-=round(delta_t3_f/2,0)
                        else:
                                sequence_time3_f-=round(delta_t3_f/2,0)
                        delta_t3_f-=round(delta_t3_f/2,0)
                        if sequence_time4_f >= delta_t3_f:
                                sequence_time4_f-=delta_t3_f
                        else:
                                sequence_time3_f-=delta_t3_f

                next_sequence_f+=sequence_time3_f
                sequence_f=4

                print(f"Szekvencia 1 idotartam: {sequence_time1_f}")
                print(f"Szekvencia 2 idotartam: {sequence_time2_f}")
                print(f"Szekvencia 3 idotartam: {sequence_time3_f}")
                print(f"Szekvencia 4 idotartam: {sequence_time4_f}")
                
        elif step==next_sequence_f and sequence_f==4:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "rrrggrrrrrggrrr") #mellekutrol balra
                delta_t4_f=sequence_control_fortuna(sequence_f)
                print(f"Szekvencia 4 zold ido modositasa: {delta_t4_f}")

                if sequence_time4_f+delta_t4_f<=0:
                        delta_t4_f=-sequence_time4_f+1
                elif delta_t4_f>0 and sequence_time4_f+delta_t4_f>=sequence_time_max:
                        delta_t4_f=0
                sequence_time4_f+=delta_t4_f  #meddig tartson a zold jelzes


                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t4_f!=0 and delta_t4_f%3==0:
                        if sequence_time1_f >= delta_t4_f/3:
                                sequence_time1_f-=delta_t4_f/3
                        else:
                                sequence_time4_f-=delta_t4_f/3
                        if sequence_time2_f >= delta_t4_f/3:
                                sequence_time2_f-=delta_t4_f/3
                        else:
                                sequence_time4_f-=delta_t4_f/3
                        if sequence_time3_f >= delta_t4_f/3:
                                sequence_time3_f-=delta_t4_f/3
                        else:
                                sequence_time4_f-=delta_t4_f/3
                elif delta_t4_f!=0 and delta_t4_f%3!=0:
                        if sequence_time1_f >= round(delta_t4_f/3,0):
                                sequence_time1_f-=round(delta_t4_f/3,0)
                        else:
                                sequence_time4_f-=round(delta_t4_f/3,0)
                        delta_t4_f-=round(delta_t4_f/3,0)
                        if sequence_time2_f >= round(delta_t4_f/2,0):
                                sequence_time2_f-=round(delta_t4_f/2,0)
                        else:
                                sequence_time4_f-=round(delta_t4_f/2,0)
                        delta_t4_f-=round(delta_t4_f/2,0)
                        if sequence_time3_f >= delta_t4_f:
                                sequence_time3_f-=delta_t4_f
                        else:
                                sequence_time4_f-=delta_t4_f

                next_sequence_f+=sequence_time4_f
                sequence_f=1
                print(f"Szekvencia 1 idotartam: {sequence_time1_f}")
                print(f"Szekvencia 2 idotartam: {sequence_time2_f}")
                print(f"Szekvencia 3 idotartam: {sequence_time3_f}")
                print(f"Szekvencia 4 idotartam: {sequence_time4_f}")


        ### Kozpont
        if step==next_sequence_k and sequence_k==1:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rggrrrrrrrgggrrrrrrgrrgggg") #Dozsa Gyorgy elore
                delta_t1_k=sequence_control_kozpont(sequence_k)

                if sequence_time1_k+delta_t1_k<=0:
                        delta_t1_k=-sequence_time1_k+1
                elif delta_t1_k>0 and sequence_time1_k+delta_t1_k>=sequence_time_max:
                        delta_t1_k=0
                sequence_time1_k+=delta_t1_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t1_k!=0 and delta_t1_k%3==0:
                        if sequence_time2_k >= delta_t1_k/3:
                                sequence_time2_k-=delta_t1_k/3
                        else:
                                sequence_time1_k-=delta_t1_k/3
                        if sequence_time3_k >= delta_t1_k/3:
                                sequence_time3_k-=delta_t1_k/3
                        else:
                                sequence_time1_k-=delta_t1_k/3
                        if sequence_time4_k >= delta_t1_k/3:
                                sequence_time4_k-=delta_t1_k/3
                        else:
                                sequence_time1_k-=delta_t1_k/3
                elif delta_t1_k!=0 and delta_t1_k%3!=0:
                        if sequence_time2_k >= round(delta_t1_k/3,0):
                                sequence_time2_k-=round(delta_t1_k/3,0)
                        else:
                                sequence_time1_k-=round(delta_t1_k/3,0)
                        delta_t1_k-=round(delta_t1_k/3,0)
                        if sequence_time3_k >= round(delta_t1_k/2,0):
                                sequence_time3_k-=round(delta_t1_k/2,0)
                        else:
                                sequence_time1_k-=round(delta_t1_k/2,0)
                        delta_t1_k-=round(delta_t1_k/2,0)
                        if sequence_time4_k >= delta_t1_k:
                                sequence_time4_k-=delta_t1_k
                        else:
                                sequence_time1_k-=delta_t1_k

                next_sequence_k+=sequence_time1_k
                sequence_k=2 

        elif step==next_sequence_k and sequence_k==2:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rrrgggrrrrrrrgggrrrrgggggr") #Dozsa Gorgy balra
                delta_t2_k=sequence_control_kozpont(sequence_k)

                if sequence_time2_k+delta_t2_k<=0:
                        delta_t2_k=-sequence_time2_k+1
                elif delta_t2_k>0 and sequence_time2_k+delta_t2_k>=sequence_time_max:
                        delta_t2_k=0
                sequence_time2_k+=delta_t2_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t2_k!=0 and delta_t2_k%3==0:
                        if sequence_time1_k >= delta_t2_k/3:
                                sequence_time1_k-=delta_t2_k/3
                        else:
                                sequence_time2_k-=delta_t2_k/3
                        if sequence_time3_k >= delta_t2_k/3:
                                sequence_time3_k-=delta_t2_k/3
                        else:
                                sequence_time2_k-=delta_t2_k/3
                        if sequence_time4_k >= delta_t2_k/3:
                                sequence_time4_k-=delta_t2_k/3
                        else:
                                sequence_time2_k-=delta_t2_k/3
                elif delta_t2_k!=0 and delta_t2_k%3!=0:
                        if sequence_time1_k >= round(delta_t2_k/3,0):
                                sequence_time1_k-=round(delta_t2_k/3,0)
                        else:
                                sequence_time2_k-=round(delta_t2_k/3,0)
                        delta_t2_k-=round(delta_t2_k/3,0)
                        if sequence_time3_k >= round(delta_t2_k/2,0):
                                sequence_time3_k-=round(delta_t2_k/2,0)
                        else:
                                sequence_time2_k-=round(delta_t2_k/2,0)
                        delta_t2_k-=round(delta_t2_k/2,0)
                        if sequence_time4_k >= delta_t2_k:
                                sequence_time4_k-=delta_t2_k
                        else:
                                sequence_time2_k-=delta_t2_k
                
                next_sequence_k+=sequence_time2_k
                sequence_k=3            

        elif step==next_sequence_k and sequence_k==3:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rrrrrgggrrrrrrrggrrrgggggg")  #Hosszzu utca elore, jobbra
                delta_t3_k=sequence_control_kozpont(sequence_k)

                if sequence_time3_k+delta_t3_k<=0:
                        delta_t3_k=-sequence_time3_k+1
                elif delta_t3_k>0 and sequence_time3_k+delta_t3_k>=sequence_time_max:
                        delta_t3_k=0
                sequence_time3_k+=delta_t3_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t3_k!=0 and delta_t3_k%3==0:
                        if sequence_time1_k >= delta_t3_k/3:
                                sequence_time1_k-=delta_t3_k/3
                        else:
                                sequence_time3_k-=delta_t3_k/3
                        if sequence_time2_k >= delta_t3_k/3:
                                sequence_time2_k-=delta_t3_k/3
                        else:
                                sequence_time3_k-=delta_t3_k/3
                        if sequence_time4_k >= delta_t3_k/3:
                                sequence_time4_k-=delta_t3_k/3
                        else:
                                sequence_time3_k-=delta_t3_k/3
                elif delta_t3_k!=0 and delta_t3_k%3!=0:
                        if sequence_time1_k >= round(delta_t3_k/3,0):
                                sequence_time1_k-=round(delta_t3_k/3,0)
                        else:
                                sequence_time3_k-=round(delta_t3_k/3,0)
                        delta_t3_k-=round(delta_t3_k/3,0)
                        if sequence_time2_k >= round(delta_t3_k/2,0):
                                sequence_time2_k-=round(delta_t3_k/2,0)
                        else:
                                sequence_time3_k-=round(delta_t3_k/2,0)
                        delta_t3_k-=round(delta_t3_k/2,0)
                        if sequence_time4_k >= delta_t3_k:
                                sequence_time4_k-=delta_t3_k
                        else:
                                sequence_time3_k-=delta_t3_k


                next_sequence_k+=sequence_time3_k
                sequence_k=4         

        elif step==next_sequence_k and sequence_k==4:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "grrrrrrrgggrrrrrrggggggggg")   ##Hosszu utca balra
                delta_t4_k=sequence_control_kozpont(sequence_k)

                if sequence_time4_k+delta_t4_k<=0:
                        delta_t4_k=-sequence_time4_k+1
                elif delta_t4_k>0 and sequence_time4_k+delta_t4_k>=sequence_time_max:
                        delta_t4_k=0
                sequence_time4_k+=delta_t4_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t4_k!=0 and delta_t4_k%3==0:
                        if sequence_time1_k >= delta_t4_k/3:
                                sequence_time1_k-=delta_t4_k/3
                        else:
                                sequence_time4_k-=delta_t4_k/3
                        if sequence_time2_k >= delta_t4_k/3:
                                sequence_time2_k-=delta_t4_k/3
                        else:
                                sequence_time4_k-=delta_t4_k/3
                        if sequence_time3_k >= delta_t4_k/3:
                                sequence_time3_k-=delta_t4_k/3
                        else:
                                sequence_time4_k-=delta_t4_k/3
                elif delta_t4_k!=0 and delta_t4_k%3!=0:
                        if sequence_time1_k >= round(delta_t4_k/3,0):
                                sequence_time1_k-=round(delta_t4_k/3,0)
                        else:
                                sequence_time4_k-=round(delta_t4_k/3,0)
                        delta_t4_k-=round(delta_t4_k/3,0)
                        if sequence_time2_k >= round(delta_t4_k/2,0):
                                sequence_time2_k-=round(delta_t4_k/2,0)
                        else:
                                sequence_time4_k-=round(delta_t4_k/2,0)
                        delta_t4_k-=round(delta_t4_k/2,0)
                        if sequence_time3_k >= delta_t4_k:
                                sequence_time3_k-=delta_t4_k
                        else:
                                sequence_time4_k-=delta_t4_k


                next_sequence_k+=sequence_time4_k
                sequence_k=1

        ###Keresztezodesen athaladt autok szamolasa      
        #Fortuna
        lane1_0_f=traci.lanearea.getLastStepVehicleNumber(detector1_0_f)
        lane1_1_f=traci.lanearea.getLastStepVehicleNumber(detector1_1_f)
        lane1_2_f=traci.lanearea.getLastStepVehicleNumber(detector1_2_f)
        lane2_0_f=traci.lanearea.getLastStepVehicleNumber(detector2_0_f)
        lane2_1_f=traci.lanearea.getLastStepVehicleNumber(detector2_1_f)
        lane3_0_f=traci.lanearea.getLastStepVehicleNumber(detector3_0_f)
        lane3_1_f=traci.lanearea.getLastStepVehicleNumber(detector3_1_f)
        lane3_2_f=traci.lanearea.getLastStepVehicleNumber(detector3_2_f)
        lane4_0_f=traci.lanearea.getLastStepVehicleNumber(detector4_0_f)
        lane4_1_f=traci.lanearea.getLastStepVehicleNumber(detector4_1_f)
        lane4_2_f=traci.lanearea.getLastStepVehicleNumber(detector4_2_f)
        lane4_3_f=traci.lanearea.getLastStepVehicleNumber(detector4_3_f)

        if lane1_0_f < lane1_0_f_prev:
                fortuna+=lane1_0_f_prev-lane1_0_f

        if lane1_1_f < lane1_1_f_prev:
                fortuna+=lane1_1_f_prev-lane1_1_f

        if lane1_2_f < lane1_2_f_prev:
                fortuna+=lane1_2_f_prev-lane1_2_f

        if lane2_0_f < lane2_0_f_prev:
                fortuna+=lane2_0_f_prev-lane2_0_f

        if lane2_1_f < lane2_1_f_prev:
                fortuna+=lane2_1_f_prev-lane2_1_f

        if lane3_0_f < lane3_0_f_prev:
                fortuna+=lane3_0_f_prev-lane3_0_f
        
        if lane3_1_f < lane3_1_f_prev:
                fortuna+=lane3_1_f_prev-lane3_1_f

        if lane3_2_f < lane3_2_f_prev:
                fortuna+=lane3_2_f_prev-lane3_2_f

        if lane4_0_f < lane4_0_f_prev:
                fortuna+=lane4_0_f_prev-lane4_0_f

        if lane4_1_f < lane4_1_f_prev:
                fortuna+=lane4_1_f_prev-lane4_1_f

        if lane4_2_f < lane4_2_f_prev:
                fortuna+=lane4_2_f_prev-lane4_2_f

        if lane4_3_f < lane4_3_f_prev:
                fortuna+=lane4_3_f_prev-lane4_3_f


        lane1_0_f_prev=lane1_0_f
        lane1_1_f_prev=lane1_1_f
        lane1_2_f_prev=lane1_2_f
        lane2_0_f_prev=lane2_0_f
        lane2_1_f_prev=lane2_1_f
        lane3_0_f_prev=lane3_0_f
        lane3_1_f_prev=lane3_1_f
        lane3_2_f_prev=lane3_2_f
        lane4_0_f_prev=lane4_0_f
        lane4_1_f_prev=lane4_1_f
        lane4_2_f_prev=lane4_2_f
        lane4_3_f_prev=lane4_3_f

         #Ref
        lane1_0=traci.lanearea.getLastStepVehicleNumber(detector1_0)
        lane1_1=traci.lanearea.getLastStepVehicleNumber(detector1_1)
        lane1_2=traci.lanearea.getLastStepVehicleNumber(detector1_2)
        lane2_0=traci.lanearea.getLastStepVehicleNumber(detector2_0)
        lane3_0=traci.lanearea.getLastStepVehicleNumber(detector3_0)
        lane3_1=traci.lanearea.getLastStepVehicleNumber(detector3_1)
        lane3_2=traci.lanearea.getLastStepVehicleNumber(detector3_2)
        lane4_0=traci.lanearea.getLastStepVehicleNumber(detector4_0)
        lane4_1=traci.lanearea.getLastStepVehicleNumber(detector4_1)

        if lane1_0<lane1_0_prev:
                refo+=lane1_0_prev-lane1_0
            
        if lane1_1<lane1_1_prev:
                refo+=lane1_1_prev-lane1_1

        if lane1_2<lane1_2_prev:
                refo+=lane1_2_prev-lane1_2

        if lane2_0<lane2_0_prev:
                refo+=lane2_0_prev-lane2_0

        if lane3_0<lane3_0_prev:
                refo+=lane3_0_prev-lane3_0

        if lane3_1<lane3_1_prev:
                refo+=lane3_1_prev-lane3_1

        if lane3_2<lane3_2_prev:
                refo+=lane3_2_prev-lane3_2
        
        if lane4_0<lane4_0_prev:
                refo+=lane4_0_prev-lane4_0

        if lane4_1<lane4_1_prev:
                refo+=lane4_1_prev-lane4_1   

        lane1_0_prev=lane1_0
        lane1_1_prev=lane1_1
        lane1_2_prev=lane1_2
        lane2_0_prev=lane2_0
        lane3_0_prev=lane3_0
        lane3_1_prev=lane3_1
        lane3_2_prev=lane3_2
        lane4_0_prev=lane4_0
        lane4_1_prev=lane4_1

        #Kozpont
        lane1_0_k=traci.lanearea.getLastStepVehicleNumber(detector1_0_k)
        lane1_1_k=traci.lanearea.getLastStepVehicleNumber(detector1_1_k)
        lane1_2_k=traci.lanearea.getLastStepVehicleNumber(detector1_2_k)
        lane2_0_k=traci.lanearea.getLastStepVehicleNumber(detector2_0_k)
        lane2_1_k=traci.lanearea.getLastStepVehicleNumber(detector2_1_k)
        lane3_0_k=traci.lanearea.getLastStepVehicleNumber(detector3_0_k)
        lane3_1_k=traci.lanearea.getLastStepVehicleNumber(detector3_1_k)
        lane4_0_k=traci.lanearea.getLastStepVehicleNumber(detector4_0_k)
        lane4_1_k=traci.lanearea.getLastStepVehicleNumber(detector4_1_k)
        lane4_2_k=traci.lanearea.getLastStepVehicleNumber(detector4_2_k)

        if lane1_0_k<lane1_0_k_prev:
                kozpont+=lane1_0_k_prev-lane1_0_k

        if lane1_1_k<lane1_1_k_prev:
                kozpont+=lane1_1_k_prev-lane1_1_k
        
        if lane1_2_k<lane1_2_k_prev:
                kozpont+=lane1_2_k_prev-lane1_2_k

        if lane2_0_k<lane2_0_k_prev:
                kozpont+=lane2_0_k_prev-lane2_0_k

        if lane2_1_k<lane2_1_k_prev:
                kozpont+=lane2_1_k_prev-lane2_1_k

        if lane3_0_k<lane3_0_k_prev:
                kozpont+=lane3_0_k_prev-lane3_0_k

        if lane3_1_k<lane3_1_k_prev:
                kozpont+=lane3_1_k_prev-lane3_1_k

        if lane4_0_k<lane4_0_k_prev:
                kozpont+=lane4_0_k_prev-lane4_0_k
        
        if lane4_1_k<lane4_1_k_prev:
                kozpont+=lane4_1_k_prev-lane4_1_k

        if lane4_2_k<lane4_2_k_prev:
                kozpont+=lane4_2_k_prev-lane4_2_k

        lane1_0_k_prev=lane1_0_k
        lane1_1_k_prev=lane1_1_k
        lane1_2_k_prev=lane1_2_k
        lane2_0_k_prev=lane2_0_k
        lane2_1_k_prev=lane2_1_k
        lane3_0_k_prev=lane3_0_k
        lane3_1_k_prev=lane3_1_k
        lane4_0_k_prev=lane4_0_k
        lane4_1_k_prev=lane4_1_k
        lane4_2_k_prev=lane4_2_k

        step += 1

        '''
        fortuna_v.append(waiting_cars_fortuna())
        refo_v.append(waiting_cars_ref())
        kozpont_v.append(waiting_cars_kozpont())
        '''

        if step%150==0:

                fortuna_v.append(fortuna-fortuna_prev2)
                refo_v.append(refo-refo_prev2)
                kozpont_v.append(kozpont-kozpont_prev2)

                np.savetxt('Meresek/fortuna_fuzzy.txt', fortuna_v, fmt="%d", delimiter=" ")
                np.savetxt('Meresek/refo_fuzzy.txt', refo_v, fmt="%d", delimiter=" ")
                np.savetxt('Meresek/kozpont_fuzzy.txt', kozpont_v, fmt="%d", delimiter=" ")

                fortuna_prev2=fortuna_prev
                fortuna_prev=fortuna
                refo_prev2=refo_prev
                refo_prev=refo
                kozpont_prev2=kozpont_prev
                kozpont_prev=kozpont
traci.close()
