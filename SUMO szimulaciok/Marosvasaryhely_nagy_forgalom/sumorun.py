import traci
import fuzzy as fz

sumoCmd = ["sumo-gui", "-c", "osm.sumocfg"]
traci.start(sumoCmd)

step=0

### Reformatus kollegium utcai keresztezodes
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

        
        print("Cars waiting in lane 1_0:"+str(lane1_0))
        print("Cars waiting in lane 1_1:"+str(lane1_1))
        print("Cars waiting in lane 1_2:"+str(lane1_2))
        print("Cars waiting in lane 2_0:"+str(lane2_0))
        print("Cars waiting in lane 3_0:"+str(lane3_0))
        print("Cars waiting in lane 3_1:"+str(lane3_1))
        print("Cars waiting in lane 3_2:"+str(lane3_2))
        print("Cars waiting in lane 4_0:"+str(lane4_0))
        print("Cars waiting in lane 4_1:"+str(lane4_1))
         

        waiting_cars=lane1_0+lane1_1+lane1_2+lane2_0+lane3_0+lane3_1+lane3_2+lane4_0+lane4_1
        print("All waiting cars:"+str(waiting_cars))
        
        sequence1_cars=lane1_0+lane1_1+lane3_0+lane3_1
        sequence2_cars=lane1_2+lane2_0+lane3_2
        sequence3_cars=lane4_0+lane4_1

        sequence1_change=sequence1_cars-sequence1_cars_prev
        sequence2_change=sequence2_cars-sequence2_cars_prev
        sequence3_change=sequence3_cars-sequence3_cars_prev

        
        print(f"Sequence 1 change:{sequence1_change}")
        print(f"Sequence 2 change:{sequence2_change}")
        print(f"Sequence 3 change:{sequence3_change}")
        

        #Fuzzy control
        if step!=0:
                fuzzy_system = fz.FuzzySystem()
                if sequence==1:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence1_cars, sequence1_change)
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

        print(f"Fuzzy output Ref: {fuzzy_output}")
        return round(fuzzy_output,0)

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

        '''
        print("Cars waiting in lane 1_0:"+str(lane1_0_f))
        print("Cars waiting in lane 1_1:"+str(lane1_1_f))
        print("Cars waiting in lane 1_2:"+str(lane1_2_f))
        print("Cars waiting in lane 2_0:"+str(lane2_0_f))
        print("Cars waiting in lane 2_1:"+str(lane2_1_f))
        print("Cars waiting in lane 3_0:"+str(lane3_0_f))
        print("Cars waiting in lane 3_1:"+str(lane3_1_f))
        print("Cars waiting in lane 3_2:"+str(lane3_2_f))
        print("Cars waiting in lane 4_0:"+str(lane4_0_f))
        print("Cars waiting in lane 4_1:"+str(lane4_1_f))
        print("Cars waiting in lane 4_2:"+str(lane4_2_f))
        print("Cars waiting in lane 4_3:"+str(lane4_3_f))
        '''

        sequence1_cars_f=lane2_0_f+lane2_1_f+lane4_0_f+lane4_1_f+lane4_2_f
        sequence2_cars_f=lane2_1_f+lane4_3_f
        sequence3_cars_f=lane1_0_f+lane1_1_f+lane3_0_f+lane3_1_f
        sequence4_cars_f=lane1_2_f+lane3_2_f

        sequence1_change_f=sequence1_cars_f-sequence1_cars_prev_f
        sequence2_change_f=sequence2_cars_f-sequence2_cars_prev_f
        sequence3_change_f=sequence3_cars_f-sequence3_cars_prev_f
        sequence4_change_f=sequence4_cars_f-sequence4_cars_prev_f
        '''
        print(f"Sequence 1 change:{sequence1_change_f}")
        print(f"Sequence 2 change:{sequence2_change_f}")
        print(f"Sequence 3 change:{sequence3_change_f}")
        print(f"Sequence 4 change:{sequence4_change_f}")
        '''

        #Fuzzy control
        if step!=0:
                fuzzy_system = fz.FuzzySystem()
                if sequence_f==1:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence1_cars_f, sequence1_change_f)
                elif sequence_f==2:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence2_cars_f, sequence2_change_f)
                elif sequence_f==3:
                        fuzzy_output=fuzzy_system.fuzzy_control(sequence3_cars_f, sequence3_change_f)
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
        return round(fuzzy_output,0)

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

        '''
        print("Cars waiting in lane 4_2_k:"+str(lane4_2_k))
        print("Cars waiting in lane 1_0_k:"+str(lane1_0_k))
        print("Cars waiting in lane 1_1_k:"+str(lane1_1_k))
        print("Cars waiting in lane 1_2_k:"+str(lane1_2_k))
        print("Cars waiting in lane 2_0_k:"+str(lane2_0_k))
        print("Cars waiting in lane 2_1_k:"+str(lane2_1_k))
        print("Cars waiting in lane 3_0_k:"+str(lane3_0_k))
        print("Cars waiting in lane 3_1_k:"+str(lane3_1_k))
        print("Cars waiting in lane 4_0_k:"+str(lane4_0_k))
        print("Cars waiting in lane 4_1_k:"+str(lane4_1_k))
        '''


        sequence1_cars_k=lane1_0_k+lane1_1_k+lane1_2_k+lane3_0_k+lane3_1_k
        sequence2_cars_k=lane1_2_k+lane3_0_k
        sequence3_cars_k=lane2_0_k+lane2_1_k+lane4_0_k
        sequence4_cars_k=lane2_1_k+lane4_1_k+lane4_2_k

        sequence1_change_k=sequence1_cars_k-sequence1_cars_prev_k
        sequence2_change_k=sequence2_cars_k-sequence2_cars_prev_k
        sequence3_change_k=sequence3_cars_k-sequence3_cars_prev_k
        sequence4_change_k=sequence4_cars_k-sequence4_cars_prev_k

        '''
        print(f"Sequence 1 change:{sequence1_change_k}")
        print(f"Sequence 2 change:{sequence2_change_k}")
        print(f"Sequence 3 change:{sequence3_change_k}")
        print(f"Sequence 4 change:{sequence4_change_k}")
        '''


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

        #vehicles=traci.vehicle.getIDList()
        #trafficlights=traci.trafficlight.getIDList()
        if step>20:
                traci.vehicle.setSpeed("veh123",12.5)

        #Reformatus kollegium        
        if step==next_sequence and sequence==1:
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "gggrrrrrrrgggrrrrrr")
                
                delta_t1=sequence_control_ref(sequence)
                print(delta_t1)

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
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "rrrgggggggrrrggrrrr")
                delta_t2=sequence_control_ref(sequence)
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
                traci.trafficlight.setRedYellowGreenState(traffic_light_ref, "grrrrrrrrrrrrrrgggg")
                delta_t3=sequence_control_ref(sequence)
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

        ### Fortuna
        if step==next_sequence_f and sequence_f==1:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "rrrrgggrrrrgggr") #foutrol elore
                delta_t1_f=sequence_control_fortuna(sequence_f)
                #print("DELTA1:"+str(delta_t1_f))
                       
                sequence_time1_f+=delta_t1_f  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t1_f!=0 and delta_t1_f%3==0:
                        sequence_time2_f-=delta_t1_f/3
                        sequence_time3_f-=delta_t1_f/3
                        sequence_time4_f-=delta_t1_f/3
                elif delta_t1_f!=0 and delta_t1_f%3!=0:
                        sequence_time2_f-=round(delta_t1_f/3,0)
                        delta_t1_f-=round(delta_t1_f/3,0)
                        sequence_time3_f-=round(delta_t1_f/2,0)
                        delta_t1_f-=round(delta_t1_f/2,0)
                        sequence_time4_f-=delta_t1_f

                next_sequence_f+=sequence_time1_f
                sequence_f+=1
                '''
                print("Time Fortuna:")
                print(sequence_time1_f+sequence_time2_f+sequence_time3_f+sequence_time4_f)
                print(sequence_time1_f)
                print(sequence_time2_f)
                print(sequence_time3_f)
                print(sequence_time4_f)
                '''

        elif step==next_sequence_f and sequence_f==2:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "grrrrrrggrrrrrg") #foutrol balra
                delta_t2_f=sequence_control_fortuna(sequence_f)
                #print(delta_t2_f)
                sequence_time2_f+=delta_t2_f  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t2_f!=0 and delta_t2_f%3==0:
                        sequence_time1_f-=delta_t2_f/3
                        sequence_time3_f-=delta_t2_f/3
                        sequence_time4_f-=delta_t2_f/3
                elif delta_t2_f!=0 and delta_t2_f%3!=0:
                        sequence_time1_f-=round(delta_t2_f/3,0)
                        delta_t2_f-=round(delta_t2_f/3,0)
                        sequence_time3_f-=round(delta_t2_f/2,0)
                        delta_t2_f-=round(delta_t2_f/2,0)
                        sequence_time4_f-=delta_t2_f
                
                next_sequence_f+=sequence_time2_f
                sequence_f+=1
                '''
                print("Time Fortuna:")
                print(sequence_time1_f+sequence_time2_f+sequence_time3_f+sequence_time4_f)
                print(sequence_time1_f)
                print(sequence_time2_f)
                print(sequence_time3_f)
                print(sequence_time4_f)
                '''

        elif step==next_sequence_f and sequence_f==3:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "gggrrrrrggrrrrr") #mellekutrol elore
                delta_t3_f=sequence_control_fortuna(sequence_f)
                #print(delta_t3_f)
                sequence_time3_f+=delta_t3_f  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t3_f!=0 and delta_t3_f%3==0:
                        sequence_time1_f-=delta_t3_f/3
                        sequence_time2_f-=delta_t3_f/3
                        sequence_time4_f-=delta_t3_f/3
                elif delta_t3_f!=0 and delta_t3_f%3!=0:
                        sequence_time1_f-=round(delta_t3_f/3,0)
                        delta_t3_f-=round(delta_t3_f/3,0)
                        sequence_time2_f-=round(delta_t3_f/2,0)
                        delta_t3_f-=round(delta_t3_f/2,0)
                        sequence_time4_f-=delta_t3_f

                next_sequence_f+=sequence_time3_f
                sequence_f+=1
                '''
                print("Time Fortuna:")
                print(sequence_time1_f+sequence_time2_f+sequence_time3_f+sequence_time4_f)
                print(sequence_time1_f)
                print(sequence_time2_f)
                print(sequence_time3_f)
                print(sequence_time4_f)
                '''
                
        elif step==next_sequence_f and sequence_f==4:
                traci.trafficlight.setRedYellowGreenState(traffic_light_Fortuna, "rrrggrrrrrggrrr") #mellekutrol balra
                delta_t4_f=sequence_control_fortuna(sequence_f)
                #print(delta_t4_f)
                sequence_time4_f+=delta_t4_f  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t4_f!=0 and delta_t4_f%3==0:
                        sequence_time1_f-=delta_t4_f/3
                        sequence_time2_f-=delta_t4_f/3
                        sequence_time3_f-=delta_t4_f/3
                elif delta_t4_f!=0 and delta_t4_f%3!=0:
                        sequence_time1_f-=round(delta_t4_f/3,0)
                        delta_t4_f-=round(delta_t4_f/3,0)
                        sequence_time2_f-=round(delta_t4_f/2,0)
                        delta_t4_f-=round(delta_t4_f/2,0)
                        sequence_time3_f-=delta_t4_f

                next_sequence_f+=sequence_time4_f
                sequence_f=1
                '''
                print("Time Fortuna:")
                print(sequence_time1_f+sequence_time2_f+sequence_time3_f+sequence_time4_f)
                print(sequence_time1_f)
                print(sequence_time2_f)
                print(sequence_time3_f)
                print(sequence_time4_f)
                '''

        ### Kozpont
        if step==next_sequence_k and sequence_k==1:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rggrrrrrrrgggrrrrrrgrrgggg") #Dozsa Gyorgy elore
                delta_t1_k=sequence_control_kozpont(sequence_k)
                #print("DELTA1:"+str(delta_t1_k))

                sequence_time1_k+=delta_t1_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t1_k!=0 and delta_t1_k%3==0:
                        sequence_time2_k-=delta_t1_k/3
                        sequence_time3_k-=delta_t1_k/3
                        sequence_time4_k-=delta_t1_k/3
                elif delta_t1_k!=0 and delta_t1_k%3!=0:
                        sequence_time2_k-=round(delta_t1_k/3,0)
                        delta_t1_k-=round(delta_t1_k/3,0)
                        sequence_time3_k-=round(delta_t1_k/2,0)
                        delta_t1_k-=round(delta_t1_k/2,0)
                        sequence_time4_k-=delta_t1_k

                next_sequence_k+=sequence_time1_k
                sequence_k+=1
                '''
                print("Time kozpont:")
                print(sequence_time1_k+sequence_time2_k+sequence_time3_k+sequence_time4_k)
                print(sequence_time1_k)
                print(sequence_time2_k)
                print(sequence_time3_k)
                print(sequence_time4_k)
                '''

        elif step==next_sequence_k and sequence_k==2:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rrrgggrrrrrrrgggrrrrgggggr") #Dozsa Gorgy balra
                delta_t2_k=sequence_control_kozpont(sequence_k)
                #print(delta_t2_k)
                sequence_time2_k+=delta_t2_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t2_k!=0 and delta_t2_k%3==0:
                        sequence_time1_k-=delta_t2_k/3
                        sequence_time3_k-=delta_t2_k/3
                        sequence_time4_k-=delta_t2_k/3
                elif delta_t2_k!=0 and delta_t2_k%3!=0:
                        sequence_time1_k-=round(delta_t2_k/3,0)
                        delta_t2_k-=round(delta_t2_k/3,0)
                        sequence_time3_k-=round(delta_t2_k/2,0)
                        delta_t2_k-=round(delta_t2_k/2,0)
                        sequence_time4_k-=delta_t2_k
                
                next_sequence_k+=sequence_time2_k
                sequence_k+=1
                '''
                print("Time kozpont:")
                print(sequence_time1_k+sequence_time2_k+sequence_time3_k+sequence_time4_k)
                print(sequence_time1_k)
                print(sequence_time2_k)
                print(sequence_time3_k)
                print(sequence_time4_k)
                '''

        elif step==next_sequence_k and sequence_k==3:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "rrrrrgggrrrrrrrggrrrgggggg")  #Hosszzu utca elore, jobbra
                delta_t3_k=sequence_control_kozpont(sequence_k)
                #print(delta_t3_k)
                sequence_time3_k+=delta_t3_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t3_k!=0 and delta_t3_k%3==0:
                        sequence_time1_k-=delta_t3_k/3
                        sequence_time2_k-=delta_t3_k/3
                        sequence_time4_k-=delta_t3_k/3
                elif delta_t3_k!=0 and delta_t3_k%3!=0:
                        sequence_time1_k-=round(delta_t3_k/3,0)
                        delta_t3_k-=round(delta_t3_k/3,0)
                        sequence_time2_k-=round(delta_t3_k/2,0)
                        delta_t3_k-=round(delta_t3_k/2,0)
                        sequence_time4_k-=delta_t3_k

                next_sequence_k+=sequence_time3_k
                sequence_k+=1
                '''
                print("Time kozpont:")
                print(sequence_time1_k+sequence_time2_k+sequence_time3_k+sequence_time4_k)
                print(sequence_time1_k)
                print(sequence_time2_k)
                print(sequence_time3_k)
                print(sequence_time4_k)
                '''

        elif step==next_sequence_k and sequence_k==4:
                traci.trafficlight.setRedYellowGreenState(traffic_ligt_kozpont, "grrrrrrrgggrrrrrrggggggggg")   ##Hosszu utca balra
                #delta_t4_k=sequence_control_kozpont(sequence_k)
                print(delta_t4_k)
                sequence_time4_k+=delta_t4_k  #meddig tartson a zold jelzes

                #fuzzy altal meghatarozott +- ido levonasa/hozzaadasa a tobbi zold jelzeshez
                if delta_t4_k!=0 and delta_t4_k%3==0:
                        sequence_time1_k-=delta_t4_k/3
                        sequence_time2_k-=delta_t4_k/3
                        sequence_time3_k-=delta_t4_k/3
                elif delta_t4_k!=0 and delta_t4_k%3!=0:
                        sequence_time1_k-=round(delta_t4_k/3,0)
                        delta_t4_k-=round(delta_t4_k/3,0)
                        sequence_time2_k-=round(delta_t4_k/2,0)
                        delta_t4_k-=round(delta_t4_k/2,0)
                        sequence_time3_k-=delta_t4_k

                next_sequence_k+=sequence_time4_k
                sequence_k=1
                '''
                print("Time kozpont:")
                print(sequence_time1_k+sequence_time2_k+sequence_time3_k+sequence_time4_k)
                print(sequence_time1_k)
                print(sequence_time2_k)
                print(sequence_time3_k)
                print(sequence_time4_k)
                '''

        step += 1
traci.close()
