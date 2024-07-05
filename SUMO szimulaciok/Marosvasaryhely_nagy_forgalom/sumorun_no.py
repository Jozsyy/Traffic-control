import traci
import numpy as np

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

### Reformatus kollegium utcai keresztezodes
sequence=1
sequence_time1=45
sequence_time2=45
sequence_time3=45
next_sequence=0
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
next_sequence_f=0
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
next_sequence_k=0
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


while traci.simulation.getMinExpectedNumber()>0:
        print(f"Step {step}:")
       
        traci.simulationStep()
        
        #Reformatus kollegium        
        if step==next_sequence and sequence==1:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "gggrrrrrrrgggrrrrrr")
                next_sequence+=sequence_time1
                sequence=2

        elif step==next_sequence and sequence==2:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "grrgggggggrrrggrrrr")
                next_sequence+=sequence_time2
                sequence=3

        elif step==next_sequence and sequence==3:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "grrrrrrrrrrrrrrgggg")
                next_sequence+=sequence_time3
                sequence=1

        ###Fortuna
        if step==next_sequence_f and sequence_f==1:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "rrrrgggrrrrgggr") #foutrol elore
                next_sequence_f+=sequence_time1_f
                sequence_f=2

        elif step==next_sequence_f and sequence_f==2:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "grrrrrrggrrrrrg") #foutrol balra
                next_sequence_f+=sequence_time2_f
                sequence_f=3

        elif step==next_sequence_f and sequence_f==3:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "gggrrrrrggrrrrr") #mellekutrol elore
                next_sequence_f+=sequence_time3_f
                sequence_f=4
                
        elif step==next_sequence_f and sequence_f==4:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "rrrggrrrrrggrrr") #mellekutrol balra
                next_sequence_f+=sequence_time4_f
                sequence_f=1
        
        ### Kozpont
        if step==next_sequence_k and sequence_k==1:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rggrrrrrrrgggrrrrrrgrrgggg") #Dozsa Gyorgy elore
                next_sequence_k+=sequence_time1_k
                sequence_k=2

        elif step==next_sequence_k and sequence_k==2:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rrrgggrrrrrrrgggrrrrgggggr") #Dozsa Gorgy balra
                next_sequence_k+=sequence_time2_k
                sequence_k=3
                
        elif step==next_sequence_k and sequence_k==3:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rrrrrgggrrrrrrrggrrrgggggg")  #Hosszzu utca elore, jobbra
                next_sequence_k+=sequence_time3_k
                sequence_k=4                

        elif step==next_sequence_k and sequence_k==4:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "grrrrrrrgggrrrrrrggggggggg")   ##Hosszu utca balra
                next_sequence_k+=sequence_time4_k
                sequence_k=1
        

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

        #print("Fortuna: "+str(fortuna))
        #print("Refo: "+str(refo))
        print("Kozpont: "+ str(kozpont))

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

                np.savetxt('Meresek/fortuna.txt', fortuna_v, fmt="%d", delimiter=" ")
                np.savetxt('Meresek/refo.txt', refo_v, fmt="%d", delimiter=" ")
                np.savetxt('Meresek/kozpont.txt', kozpont_v, fmt="%d", delimiter=" ")

                fortuna_prev2=fortuna_prev
                fortuna_prev=fortuna
                refo_prev2=refo_prev
                refo_prev=refo
                kozpont_prev2=kozpont_prev
                kozpont_prev=kozpont
traci.close()
