import write
import Vd_value




f = open("aermod.inp", "w")

# 寫入資料
f.write("CO STARTING\n")
f.write("   TITLEONE AERMOD Model\n")
f.write("   MODELOPT DFAULT CONC\n")
f.write("   AVERTIME 1 PERIOD\n")
f.write("   URBANOPT 2000000 TC\n")
f.write("   POLLUTID CO\n")
f.write("   RUNORNOT RUN\n")
f.write("   ERRORFIL ERROR.OUT\n")
f.write("CO FINISHED\n")
f.write("\n")
f.write("SO STARTING\n")
f.write("** Point Source         UTM_E  UTM_N  ZS\n")
f.write("   LOCATION PM1001 VOLUME 216930 2673130 9.0\n")
f.write("   LOCATION PM1002 VOLUME 216930 2673120 9.0\n")
f.write("   LOCATION PM1003 VOLUME 216760 2673650 9.0\n")
f.write("   LOCATION PM1004 VOLUME 216760 2673640 9.0\n")
f.write("   LOCATION PM1005 VOLUME 216600 2674380 9.0\n")
f.write("   LOCATION PM1006 VOLUME 216600 2674370 9.0\n")
f.write("   LOCATION PM1007 VOLUME 216170 2675000 9.0\n")
f.write("   LOCATION PM1008 VOLUME 216170 2675010 9.0\n")
f.write("   LOCATION PM1009 VOLUME 215430 2676440 9.0\n")
f.write("   LOCATION PM1010 VOLUME 213300 2673750 9.0\n")
f.write("   LOCATION PM1011 VOLUME 213300 2673740 9.0\n")
f.write("   LOCATION PM1012 VOLUME 214760 2672800 9.0\n")
f.write("   LOCATION PM1013 VOLUME 214075 2673250 9.0\n")
f.write("   LOCATION PM1014 VOLUME 213550 2673700 9.0\n")
f.write("   LOCATION PM1015 VOLUME 213550 2673710 9.0\n")
f.write("   LOCATION PM1016 VOLUME 214080 2673200 9.0\n")
f.write("   LOCATION PM1017 VOLUME 213530 2673700 9.0\n")
f.write("   LOCATION PM1018 VOLUME 214075 2673260 9.0\n")
f.write("   LOCATION PM1019 VOLUME 214050 2673265 9.0\n")
f.write("   LOCATION PM1020 VOLUME 213530 2673700 9.0\n")
f.write("   LOCATION PM1021 VOLUME 213530 2673710 9.0\n")
f.write("   LOCATION PM1022 VOLUME 213300 2673750 9.0\n")
f.write("   LOCATION PM1023 VOLUME 213120 2674000 9.0\n")
f.write("   LOCATION PM1024 VOLUME 213120 2674010 9.0\n")
f.write("   LOCATION PM1025 VOLUME 213450 2670680 9.0\n")
f.write("   LOCATION PM1026 VOLUME 212262 2671445 9.0\n")
f.write("   LOCATION PM1027 VOLUME 212011 2671527 9.0\n")
f.write("   LOCATION PM1028 VOLUME 211760 2671622 9.0\n")
f.write("   LOCATION PM1029 VOLUME 216560 2677368 9.0\n")
f.write("** Volume Source    QS hgt \n")
f.write("** Parameters:     ---- ---- ----  ---- \n")
f.write("** SRCPARAM PM25 0.0572 0.0 500 3.0\n")
f.write(f"   SRCPARAM PM1001 {((0.0793*Vd_value.a/200))} 0.0 500 0.3\n") #使用teds11.0作為排放係數來源
f.write(f"   SRCPARAM PM1002 {((0.0793*Vd_value.b/200))} 0.0 500 0.3\n") #V.K.T單位為(KM/年)
f.write(f"   SRCPARAM PM1003 {((0.0793*Vd_value.c)/200)} 0.0 500 0.3\n") #所以排放係數(g/vkt*輛)
f.write(f"   SRCPARAM PM1004 {((0.0793*Vd_value.d)/200)} 0.0 500 0.3\n") #排放量=排放係數(g/vkt*輛)*V.K.T(KM/年)*車流量(輛/5min)
f.write(f"   SRCPARAM PM1005 {((0.0793*Vd_value.e)/200)} 0.0 500 0.3\n") #加上單位換算，要每公里故*10/2000=/200(網格為200公尺)，車流量換算成每10分鐘故/2
f.write(f"   SRCPARAM PM1006 {((0.0793*Vd_value.f)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1007 {((0.0793*Vd_value.g)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1008 {((0.0793*Vd_value.h)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1009 {((0.0793*Vd_value.i)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1010 {((0.0793*Vd_value.k)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1011 {((0.0793*Vd_value.l)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1012 {((0.0793*Vd_value.m)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1013 {((0.0793*Vd_value.n)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1014 {((0.0793*Vd_value.o)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1015 {((0.0793*Vd_value.p)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1016 {((0.0793*Vd_value.q)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1017 {((0.0793*Vd_value.r)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1018 {((0.0793*Vd_value.s)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1019 {((0.0793*Vd_value.u)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1020 {((0.0793*Vd_value.v)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1021 {((0.0793*Vd_value.w)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1022 {((0.0793*Vd_value.x)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1023 {((0.0793*Vd_value.y)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1024 {((0.0793*Vd_value.z)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1025 {((0.0793*Vd_value.aa)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1026 {((0.0793*Vd_value.bb)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1027 {((0.0793*Vd_value.cc)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1028 {((0.0793*Vd_value.dd)/200)} 0.0 500 0.3\n")
f.write(f"   SRCPARAM PM1029 {((0.0793*Vd_value.ee)/200)} 0.0 500 0.3\n")
f.write("   URBANSRC PM1001-PM1029\n")
f.write("   SRCGROUP ALL\n")
f.write("SO FINISHED\n")
f.write(" \n")
f.write("RE STARTING\n")
f.write("   GRIDCART PM STA\n")
f.write("            XYINC 206734 118 200 2666635 65 200\n")
f.write("            PM END\n")
f.write("RE FINISHED\n")
f.write(" \n")
f.write("ME STARTING\n")
f.write("   SURFFILE Output.sfc\n")
f.write("   PROFFILE Output.pfl\n")
f.write("   SURFDATA 467490 2021 Taichung\n")
f.write("   UAIRDATA 466920 2021 Taipei\n")
f.write("   PROFBASE 84.0\n")
f.write("ME FINISHED\n")
f.write(" \n")
f.write("OU STARTING\n")
f.write("   RECTABLE ALLAVE FIRST\n")
f.write("   DAYTABLE ALLAVE\n")
f.write("   MAXTABLE ALLAVE 50\n")
f.write("   POSTFILE 1 all plot pm25.csv\n")
f.write("OU FINISHED\n")
'''

input_aermod()