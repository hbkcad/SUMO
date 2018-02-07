import traci
import subprocess
import random
import optparse
import os, sys
import time
import traci.vehicle
import traci.simulation
import datetime
import math

if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
     print("success")
     #print(time.clock())
    # print(time.asctime())
else:   
     sys.exit("please declare environment variable 'SUMO_HOME'")
	 
PORT=8873
def generate_routefile(directoryPath, newRouteFilename):

    print "Generating random route file at - {0}".format(os.path.join(directoryPath,newRouteFilename))

    # All random stop duration will be between 0 to 99.
    
    # Generate random stop timings for vehicle - GC1.
    # For vehicle - GC1 there 11 bus stops. Hence we generate 11 stop duration 
    GC1_s11 = random.randint(200,500)
    GC1_s12 = random.randint(200,400)
    GC1_s13 = random.randint(300,500)
    GC1_s14 = random.randint(400,500)
    GC1_s15 = random.randint(200,500)
    GC1_s16 = random.randint(500,700)
    GC1_s17 = random.randint(460,500)
    GC1_s18 = random.randint(300,500)
    GC1_s19 = random.randint(200,500)
    GC1_s110 = random.randint(100,400)
    GC1_s111 = random.randint(600,700)

    # Generate random stop timings for vehicle - GC2.
    # For vehicle - GC2 there 9 bus stops. Hence we generate 9 stop duration
    GC2_s21 = random.randint(200,500)
    GC2_s22 = random.randint(300,600)
    GC2_s23 = random.randint(400,600)
    GC2_s24 = random.randint(300,500)
    GC2_s25 = random.randint(200,400)
    GC2_s26 = random.randint(0,0)
    GC2_s27 = random.randint(350,500)
    GC2_s28 = random.randint(100,300)
    GC2_s29 = random.randint(200,400)

    # Generate random stop timings for vehicle - GC3.
    # For vehicle - GC3 there 10 bus stops. Hence we generate 10 stop duration
    GC3_s31 = random.randint(200,400)
    GC3_s32 = random.randint(200,500)
    GC3_s33 = random.randint(500,600)
    GC3_s34 = random.randint(200,500)
    GC3_s35 = random.randint(20,500)
    GC3_s36 = random.randint(800,1000)
    GC3_s37 = random.randint(700,1000)
    GC3_s38 = random.randint(20,300)
    GC3_s39 = random.randint(200,400)
    GC3_s310 = random.randint(200,300)

    # Input additional file first half.
    inputAdditionFileContents = """
<additional xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.sf.net/xsd/additional_file.xsd">
        <!--
		Pick up points for Vehicle 1.
	-->
	<busStop id="s11" lane="D12_0" startPos="20" endPos="20" lines="Stop1" friendlyPos="true"/>
	<busStop id="s12" lane="D87_0" startPos="10" endPos="15" lines="Stop2" friendlyPos="true"/>
	<busStop id="s13" lane="D715_0" startPos="10" endPos="15" lines="Stop3" friendlyPos="true"/>	
	<busStop id="s14" lane="D1514_0" startPos="10" endPos="5" lines="Stop4" friendlyPos="true"/>
	<busStop id="s15" lane="D146_0" startPos="35" endPos="40" lines="Stop5" friendlyPos="true"/>
	<busStop id="s16" lane="D513_0" startPos="35" endPos="40" lines="Stop6" friendlyPos="true"/>
	<busStop id="s17" lane="D1319_0" startPos="55" endPos="65" lines="Stop7" friendlyPos="true"/>
	
	<busStop id="s19" lane="D1920_0" startPos="35" endPos="40" lines="Stop9" friendlyPos="true"/>
	<busStop id="s110" lane="D2026_0" startPos="85" endPos="90" lines="Stop10" friendlyPos="true"/>
	<busStop id="s111" lane="D168_0" startPos="35" endPos="40" lines="Stop11" friendlyPos="true"/>
	
	<!--
		Pick up points for Vehicle 2.
	-->
	<busStop id="s21" lane="D312_0" startPos="20" endPos="20" lines="Stop1" friendlyPos="true"/>
	<busStop id="s22" lane="D1218_0" startPos="10" endPos="10" lines="Stop2" friendlyPos="true"/>
	<busStop id="s23" lane="D1817_0" startPos="10" endPos="15" lines="Stop3" friendlyPos="true"/>	
	<busStop id="s24" lane="D1711_0" startPos="10" endPos="5" lines="Stop4" friendlyPos="true"/>
	<busStop id="s25" lane="D910_0" startPos="35" endPos="40" lines="Stop5" friendlyPos="true"/>
	<busStop id="s26" lane="D1021_0" startPos="35" endPos="40" lines="Stop6" friendlyPos="true"/>
	<busStop id="s27" lane="D2821_0" startPos="55" endPos="65" lines="Stop7" friendlyPos="true"/>
	<busStop id="s28" lane="D2122_0" startPos="10" endPos="10" lines="Stop8" friendlyPos="true"/>
	<busStop id="s29" lane="D2423_0" startPos="35" endPos="40" lines="Stop9" friendlyPos="true"/>
	
	<!--
		Pick up points for Vehicle 3.
	-->
	<busStop id="s31" lane="D32_0" startPos="120" endPos="120" lines="Stop1" friendlyPos="true"/>
	<busStop id="s32" lane="D927_0" startPos="10" endPos="10" lines="Stop2" friendlyPos="true"/>
	<busStop id="s33" lane="D927_0" startPos="35" endPos="35" lines="Stop3" friendlyPos="true"/>	
	<busStop id="s34" lane="D927_0" startPos="55" endPos="55" lines="Stop4" friendlyPos="true"/>
	<busStop id="s35" lane="D2625_0" startPos="25" endPos="25" lines="Stop5" friendlyPos="true"/>
	<busStop id="s36" lane="D2526_0" startPos="45" endPos="45" lines="Stop6" friendlyPos="true"/>
	<busStop id="s37" lane="D2627_0" startPos="85" endPos="85" lines="Stop7" friendlyPos="true"/>
	<busStop id="s38" lane="D2829_0" startPos="150" endPos="150" lines="Stop8" friendlyPos="true"/>
	<busStop id="s39" lane="D2928_0" startPos="180" endPos="180" lines="Stop9" friendlyPos="true"/>
		
	<vType id="truck/trailer" accel="2.6" decel="4.5" sigma="0" length="7" minGap="3" maxSpeed="70" imgFile="t.png"/>

        {}
        {}
        {}
        <inductionLoop id="dt" lane="D2821_0" pos="2" freq="100" file="detect.xml"/>
        <inductionLoop id="dt1" lane="D2625_0" pos="2" freq="100" file="detect.xml"/>
        <inductionLoop id="dt2" lane="D2627_0" pos="2" freq="100" file="detect.xml"/>
        <inductionLoop id="dt3" lane="D2829_0" pos="2" freq="100" file="detect.xml"/>
        <inductionLoop id="dt4" lane="D2928_0" pos="2" freq="100" file="detect.xml"/>
        <inductionLoop id="dt5" lane="D927_0" pos="2" freq="100" file="detect.xml"/>
        <inductionLoop id="dt6" lane="D32_0" pos="2" freq="100" file="detect.xml"/>
</additional>
	"""

    # Vehicle 1 definition
    vehicle1Definition = """
    <vehicle id="GC1" type="truck/trailer" depart="0">
        <route edges="D12 D29 D98 D87 D715 D1514 D146 D65 D513 D1319 D1920 D2026 D2620 D2016 D168 D89 D92 D21"/>
        <param key="has.btsender.device" value="true"/>
        <stop busStop="s11" duration="{}"/>
        <stop busStop="s12" duration="{}"/>
        <stop busStop="s13" duration="{}"/>
        <stop busStop="s14" duration="{}"/>
        <stop busStop="s15" duration="{}"/>
        <stop busStop="s16" duration="{}"/>
        <stop busStop="s17" duration="{}"/>
        
        <stop busStop="s19" duration="{}"/>
        <stop busStop="s110" duration="{}"/>
        <stop busStop="s111" duration="{}"/>
    </vehicle>
    """.format(GC1_s11, GC1_s12,GC1_s13,GC1_s14,GC1_s15,GC1_s16,GC1_s17,GC1_s18,GC1_s19,GC1_s110,GC1_s111)
    print ("Vehicle 1complete")
    # Vehicle 2 definition
    vehicle2Definition = """
    <vehicle id="GC2" type="truck/trailer" depart="0">
	<route edges="D43 D312 D1218 D1817 D1711 D1110 D109 D910 D1021 D2128 D2821 D2122 D2223 D2324 D2423 D2318 D1812 D123 D34" />
	<param key="has.btreiver.device" value="true"/>
	<stop busStop="s21" duration="{}"/>
	<stop busStop="s22" duration="{}"/>
	<stop busStop="s23" duration="{}"/>
	<stop busStop="s24" duration="{}"/>
	<stop busStop="s25" duration="{}"/>
	<stop busStop="s26" duration="{}"/>
	<stop busStop="s27" duration="{}"/>
	<stop busStop="s28" duration="{}"/>
	<stop busStop="s29" duration="{}"/>	
    </vehicle>
	""".format(GC2_s21,GC2_s22,GC2_s23,GC2_s24,GC2_s25,GC2_s26,GC2_s27,GC2_s28,GC2_s29)
    print("vehicle2 complete")

    # Vehiclee 3 definition
    vehicle3Definition = """
    <vehicle id="GC3" type="truck/trailer" depart="0">
	<route edges="D43 D32 D29 D927 D2726 D2625 D2526 D2627 D2728 D2829 D2928 D2827 D279 D92 D23 D34" />
	<param key="has.btsender.device" value="true"/>
	<stop busStop="s31" duration="{}"/>
	<stop busStop="s32" duration="{}"/>
	<stop busStop="s33" duration="{}"/>
	<stop busStop="s34" duration="{}"/>
	<stop busStop="s35" duration="{}"/>
	<stop busStop="s36" duration="{}"/>
        <stop busStop="s37" duration="{}"/>
	<stop busStop="s38" duration="{}"/>
	<stop busStop="s39" duration="{}"/>
	
    </vehicle>
    """.format(GC3_s31,GC3_s32,GC3_s33,GC3_s34,GC3_s35,GC3_s36,GC3_s37,GC3_s38,GC3_s39)
    
    # Now combine all file contents together and write to the given file.    
    with open(os.path.join(directoryPath,newRouteFilename), "w") as routes:
        routes.write(inputAdditionFileContents.format(vehicle1Definition, vehicle2Definition, vehicle3Definition))

    print "Generating random route file COMPLETE"

def inc_realtime(now):
    new_now = now + datetime.timedelta(minutes=1)
    #print 'Now:', new_now.hour, new_now.minute, new_now.second
    return new_now
flag_check=[0]*31  

def run():
     
    """execute the TraCI control loop"""
    traci.init(PORT)
    print ("success")
    fd=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", 'w')
    fd.close()
    fd=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", 'w')
    fd.close()
    fd=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", 'w')
    fd.close()
    fd=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", 'w')
    fd.close()
    print"enter the simulation time"
    x=input()
   # print(x, type(x))
    t1=datetime.datetime.now()
    print(t1)
    t2=t1.minute+x
    print("the simulation will run for :")
    print(x)
    print("minutes")
    i=0
    step = 0
    si1=0
    si2=0
    si3=0
    v1_countstop1=0
    v2_countstop2=0
    v3_countstop3=0
    v1position='\0'
    count1=0
    v1stop='\0'
    v2stop='\0'
    v3stop='\0'
    count2=0
    v2_count=0
    count3=0
    v3_count=0
    begin='\0'
    end='\0'
    begin2='\0'
    end2='\0'
    begin3='\0'
    end2='\0'
   
    position_list2=['(206.65, 40.249)','p12','(206.65, 59.749)','p13','(189.751, 74.65)','p14','(183.35, 63.251)','p15','(150.999, 43.35)','p16','(166.65, 80.999)','p17','(163.35, 99.751)','p18','(179.749, 93.35000000000001)','p19','(209.751, 96.65)','p20']
    position_list3=['(124.751, 21.650000000000002)','p21','(121.65, 59.749)','p22','(121.65, 84.749)','p23','(121.65, 104.749)','p24','(45.251000000000005, 121.65)','p25','(70.249, 118.35000000000001)','p26','(115.249, 118.35000000000001)','p27','(223.249, 118.35000000000001)','p28','(175.501, 121.65)','p29','(200.249,18.35)','p30']
    position_list1=['(44.998999999999995, 18.35)','p1','(55.251, 46.65)','p2','(51.65, 64.749)','p3','(40.251, 71.65)','p4','(23.35, 49.751)','p5','(1.6500000000000001, 65.249)','p6','(1.6500000000000001, 91.749)','p7','(43.249, 93.35000000000001)','p9','(76.65, 115.249)','p10','(73.35000000000001, 49.751)','p11']

    now=datetime.datetime.now()
    
    while traci.simulation.getMinExpectedNumber() and int(t1.minute)!=t2:
         traci.simulationStep()
         now-inc_realtime(now)
         if not v1_countstop1>=10:
              if traci.vehicle.isAtBusStop("GC1"):
                   if count1==0:
                        v1position=traci.vehicle.getPosition("GC1")
                        v1position=str(v1position)
                        for i in range(0,len(position_list1),2):
                             if position_list1[i] == v1position:
                                  v1stop=position_list1[i+1]
                                  si1=int(v1stop[1:])
                                  #print si1
                                  break
                        begin_time=datetime.datetime.now()
                        count1+=1
                        v1_countstop1+=1

              else:
                   if count1==1:
                        end_time=datetime.datetime.now()
                        duration1=end_time.minute-begin_time.minute
                        f=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", "a")
                        print>>f,"v1",v1stop,
                        print>>f," ",time.strftime("%d-%m-%Y"),
                        print>>f," ",begin_time.hour,":",begin_time.minute,
                        print>>f," ",end_time.hour,":",end_time.minute,
                        #print>>f," ",duration
                        f.close()
                        f=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>f,"v1",v1stop,
                        print>>f," ",time.strftime("%d-%m-%Y"),
                        print>>f," ",begin_time.hour,":",begin_time.minute,
                        print>>f," ",end_time.hour,":",end_time.minute,
                        f.close()
                        
                        print "v1",v1stop,
                        print " ",time.strftime("%d-%m-%Y"),
                        print " ",begin_time.hour,":",begin_time.minute,
                        print " ",end_time.hour,":",end_time.minute,
                        #duration1=math.floor(duration1/6)
                        if duration1<2:
                             fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", "a")
                             print>>fx," Not Serviced"
                             fx.close()
                             fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                             print>>fx," Not Serviced"
                             fx.close()
                             flag_check[si1]=-1
                             print " Not Serviced"
                        else:
                             fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", "a")
                             print>>fx," ",duration1,"minutes"
                             fx.close()
                             fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                             print>>fx," ",duration1,"minutes"
                             fx.close()
                             flag_check[si1]=1
                             print flag_check[si1]
                             print " ",duration1,"minutes"
                        #print(datetime.strptime(end,FMT) - datetime.strptime(begin,FMT))
                        count1=0
          

         if v1_countstop1==10:
              if not traci.vehicle.isAtBusStop("GC1"):
                   end_time=datetime.datetime.now()
                   duration1=end_time.minute-begin_time.minute
                   f=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", "a")
                   print>>f,"v1",v1stop,
                   print>>f," ",time.strftime("%d-%m-%Y"),
                   print>>f," ",begin_time.hour,":",begin_time.minute,
                   print>>f," ",end_time.hour,":",end_time.minute,
                   #print>>f," ",duration
                   f.close()
                   f=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                   print>>f,"v1",v1stop,
                   print>>f," ",time.strftime("%d-%m-%Y"),
                   print>>f," ",begin_time.hour,":",begin_time.minute,
                   print>>f," ",end_time.hour,":",end_time.minute,
                   #print>>f," ",duration
                   f.close()
                   print "v1",v1stop,
                   print " ",time.strftime("%d-%m-%Y"),
                   print " ",begin_time.hour,":",begin_time.minute,
                   print " ",end_time.hour,":",end_time.minute,
                   #duration1=math.floor(duration1/6)
                   if duration1<2:
                        fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", "a")
                        print>>fx," Not Serviced"
                        fx.close()
                        fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fx," Not Serviced"
                        fx.close()
                        flag_check[si1]=-1
                        print " Not Serviced"
                   else:
                        fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", "a")
                        print>>fx," ",duration1,"minutes"
                        fx.close()
                        fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fx," ",duration1,"minutes"
                        fx.close()
                        flag_check[si1]=1
                        print " ",duration1,"minutes"
                        #print(datetime.strptime(end,FMT) - datetime.strptime(begin,FMT))
                        count1=0
                   v1_countstop1+=1
               

         if not v2_countstop2>=9:
              if traci.vehicle.isAtBusStop("GC2"):
                   if count2==0:
                        v2position=traci.vehicle.getPosition("GC2")
                        v2position=str(v2position)
                        for i in range(0,len(position_list2),2):
                             if position_list2[i] == v2position:
                                  v2stop=position_list2[i+1]
                                  si2=int(v2stop[1:])
                                  #print si2
                                  break
                        start_time2=datetime.datetime.now()
                        count2+=1
                        v2_countstop2+=1
              else:
                   if count2==1:
                        end_time2=datetime.datetime.now()
                        duration2=end_time2.minute-start_time2.minute
                        fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", "a")
                        print>>fx,"v2",v2stop,
                        print>>fx," ",time.strftime("%d-%m-%Y"),
                        print>>fx," ",start_time2.hour,":",start_time2.minute,
                        print>>fx," ",end_time2.hour,":",end_time2.minute,
                        #print>>fx," ",duration2
                        fx.close()
                        fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fx,"v2",v2stop,
                        print>>fx," ",time.strftime("%d-%m-%Y"),
                        print>>fx," ",start_time2.hour,":",start_time2.minute,
                        print>>fx," ",end_time2.hour,":",end_time2.minute,
                        #print>>fx," ",duration2
                        fx.close()
                        print "v2",v2stop,
                        print " ",time.strftime("%d-%m-%Y"),
                        print " ",start_time2.hour,":",start_time2.minute,
                        print " ",end_time2.hour,":",end_time2.minute,
                        if duration2<2:
                             fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", "a")
                             print>>fx," Not Serviced"
                             fx.close()
                             fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                             print>>fx," Not Serviced"
                             fx.close()
                         
                             flag_check[si2]=-1
                             print "Not Serviced"
                        else:
                             fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", "a")
                             print>>fx," ",duration2,"minutes"
                             fx.close()
                             fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                             print>>fx," ",duration2,"minutes"
                             fx.close()
                             flag_check[si2]=1
                             print " ",duration2,"minutes"
                        count2=0

         if v2_countstop2==9:
              if not traci.vehicle.isAtBusStop("GC2"):
                   end_time=datetime.datetime.now()
                   duration2=end_time.minute-begin_time.minute
                   f=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", "a")
                   print>>f,"v2",v2stop,
                   print>>f," ",time.strftime("%d-%m-%Y"),
                   print>>f," ",begin_time.hour,":",begin_time.minute,
                   print>>f," ",end_time.hour,":",end_time.minute,
                   #print>>f," ",duration
                   f.close()
                   f=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                   print>>f,"v2",v2stop,
                   print>>f," ",time.strftime("%d-%m-%Y"),
                   print>>f," ",begin_time.hour,":",begin_time.minute,
                   print>>f," ",end_time.hour,":",end_time.minute,
                   #print>>f," ",duration
                   f.close()
                   print "v2",v2stop,
                   print " ",time.strftime("%d-%m-%Y"),
                   print " ",begin_time.hour,":",begin_time.minute,
                   print " ",end_time.hour,":",end_time.minute,
                   #duration1=math.floor(duration1/6)
                   if duration2<2:
                        fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", "a")
                        print>>fx," Not Serviced"
                        fx.close()
                        fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fx," Not Serviced"
                        fx.close()
                        flag_check[si2]=-1
                        print " Not Serviced"
                   else:
                        fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", "a")
                        print>>fx," ",duration2,"minutes"
                        fx.close()
                        fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fx," ",duration2,"minutes"
                        fx.close()
                        flag_check[si2]=1
                        print " ",duration1,"minutes"
                        #print(datetime.strptime(end,FMT) - datetime.strptime(begin,FMT))
                        count1=0
                   v2_countstop2+=1
                       
         if not v3_countstop3>=9:
              if traci.vehicle.isAtBusStop("GC3"):
                   if count3==0:
                        v3position=traci.vehicle.getPosition("GC3")
                        v3position = str(v3position)
                        for i in range(0,len(position_list3),2):
                             if position_list3[i] == v3position:
                                  v3stop = position_list3[i+1]
                                  si3=int(v3stop[1:])
                                  #print si3
                                  break
                        count3+=1
                        begin3=datetime.datetime.now()
                        v3_countstop3+=1
                     
               
              else:
                   if count3==1:
                        end3=datetime.datetime.now()
                        duration=end3.minute-begin3.minute
                        fo=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", "a")
                        print>>fo,"v3",v3stop,
                        print>>fo," ",time.strftime("%d-%m-%Y"),
                        print>>fo," ",begin3.hour,":",begin3.minute,
                        print>>fo," ",end3.hour,":",end3.minute,
                        #print>>fo," ",duration
                        fo.close()
                        fo=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fo,"v3",v3stop,
                        print>>fo," ",time.strftime("%d-%m-%Y"),
                        print>>fo," ",begin3.hour,":",begin3.minute,
                        print>>fo," ",end3.hour,":",end3.minute,
                        #print>>fo," ",duration
                        fo.close()
                        print "v3",v3stop,
                        print " ",time.strftime("%d-%m-%Y"),
                        print " ",begin3.hour,":",begin3.minute,
                        print " ",end3.hour,":",end3.minute,
                        if duration<2:
                             fo=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", "a")
                             print>>fo," Not Serviced"
                             fo.close()
                             fo=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                             print>>fo," Not Serviced"
                             fo.close()
                             print "not serviced"
                             flag_check[si3]=-1
                             
                        else:
                             fo=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", "a")
                             print>>fo," ",duration,"minutes"
                             fo.close()
                             fo=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                             print>>fo," ",duration,"minutes"
                             fo.close()
                             flag_check[si3]=1
                             print " ",duration,"minutes"
                        count3=0

         if v3_countstop3==9:
              if not traci.vehicle.isAtBusStop("GC3"):
                   end3=datetime.datetime.now()
                   duration=end3.minute-begin3.minute
                   f=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", "a")
                   print>>f,"v3",v3stop,
                   print>>f," ",time.strftime("%d-%m-%Y"),
                   print>>f," ",begin3.hour,":",begin3.minute,
                   print>>f," ",end3.hour,":",end3.minute,
                   #print>>f," ",duration
                   f.close()
                   f=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                   print>>f,"v3",v3stop,
                   print>>f," ",time.strftime("%d-%m-%Y"),
                   print>>f," ",begin3.hour,":",begin3.minute,
                   print>>f," ",end3.hour,":",end3.minute,
                   #print>>f," ",duration
                   f.close()
                   print "v3",v3stop,
                   print " ",time.strftime("%d-%m-%Y"),
                   print " ",begin3.hour,":",begin3.minute,
                   print " ",end3.hour,":",end3.minute,
                   #duration1=math.floor(duration1/6)
                   if duration<2:
                        fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", "a")
                        print>>fx," Not Serviced"
                        fx.close()
                        fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fx," Not Serviced"
                        fx.close()
                        flag_check[si3]=-1
                        print " Not Serviced"
                   else:
                        fx=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", "a")
                        print>>fx," ",duration,"minutes"
                        fx.close()
                        fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
                        print>>fx," ",duration,"minutes"
                        fx.close()
                        flag_check[si3]=1
                        print " ",duration,"minutes"
                        #print(datetime.strptime(end,FMT) - datetime.strptime(begin,FMT))
                        #count=0
                   v3_countstop3+=1
       
         step += 1
         t1=datetime.datetime.now()

    fo=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo1.txt", "a")
    fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
    print flag_check
    for j in range(1,12,1):
         if flag_check[j]== -1 and j<12:
              print>>fo," ","stop", j,"not serviced by vehicle1"
              print>>fx," ","stop", j,"not serviced by vehicle1"
         if flag_check[j]== 0 and j<12:
              print>>fo," ","stop", j,"not visited by vehicle1"
              print>>fx," ","stop", j,"not visited by vehicle1"
    fo.close()
    fx.close()

    fo=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo2.txt", "a")
    fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
    print flag_check
    for j in range(12,21,1):
         if flag_check[j]== -1 and j<21:
              print>>fo," ","stop",j,"not serviced by vehicle2"
              print>>fx," ","stop",j,"not serviced by vehicle2"
         if flag_check[j]== 0 and j<21:
              print>>fo," ","stop", j,"not visited by vehicle2"
              print>>fx," ","stop", j,"not visited by vehicle2"
    fo.close()
    fx.close()

    fo=open(r"C:\Users\Harsharadhya\Desktop\vehicleinfo3.txt", "a")
    fx=open(r"C:\Users\Harsharadhya\Desktop\allvehicleinfo.txt", "a")
    print flag_check
    for j in range(21,31,1):
         if flag_check[j]== -1 and j<30:
              print>>fo," ","stop",j,"not serviced by vehicle3"
              print>>fx," ","stop",j,"not serviced by vehicle3"
         if flag_check[j]== 0 and j<31:
              print>>fo," ","stop", j,"not visited by vehicle3"
              print>>fx," ","stop", j,"not visited by vehicle3"
    fo.close()
    fx.close()
    traci.close()
    
def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options
	
# this is the main entry point of this script
if __name__ == "__main__":
	# first, generate the route file for this simulation
    generate_routefile("D:\Sumo\garbage3", "input_additional.add.xml")


    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    """if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
	"""
    # first, generate the route file for this simulation
    #generate_routefile()

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    sumoBinary = r"C:\Program Files (x86)\DLR\Sumo\bin\sumo-gui.exe"
    sumoProcess = subprocess.Popen([sumoBinary, "-c", r"D:\Sumo\garbage3\ait.sumocfg", "--tripinfo-output","--begin 0",
                                    "--remote-port", str(PORT)], stdout=sys.stdout, stderr=sys.stderr)
    run()
    sumoProcess.wait()
