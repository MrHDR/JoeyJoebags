EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Gameboy:CartBus U0
U 1 1 5E0FEE35
P 6000 4550
F 0 "U0" H 6950 4177 50  0000 C CNN
F 1 "CartBus" H 6950 4086 50  0000 C CNN
F 2 "Custom:DSL_Cartridge_Reader_Micro" H 6000 4550 50  0001 C CNN
F 3 "" H 6000 4550 50  0001 C CNN
	1    6000 4550
	1    0    0    1   
$EndComp
$Comp
L MCU_Module:Maple_Mini A1
U 1 1 5E2FBB54
P 7700 2800
F 0 "A1" H 7725 2175 50  0000 C CNN
F 1 "Maple_Mini" H 7700 2100 50  0000 C CNN
F 2 "Module:Maple_Mini" H 7750 1750 50  0001 L CNN
F 3 "http://docs.leaflabs.com/static.leaflabs.com/pub/leaflabs/maple-docs/0.0.12/hardware/maple-mini.html" H 7750 800 50  0001 L CNN
	1    7700 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	8500 4650 8500 4700
Wire Wire Line
	8400 4650 8400 4700
Wire Wire Line
	8300 4650 8300 4700
Wire Wire Line
	8200 4650 8200 4700
Wire Wire Line
	8100 4650 8100 4700
Wire Wire Line
	8000 4650 8000 4700
Wire Wire Line
	7900 4650 7900 4700
Wire Wire Line
	7800 4650 7800 4700
Wire Wire Line
	7700 4650 7700 4700
Wire Wire Line
	7600 4650 7600 4700
Wire Wire Line
	7500 4650 7500 4700
Wire Wire Line
	7400 4650 7400 4700
Wire Wire Line
	7300 4650 7300 4700
Wire Wire Line
	7200 4650 7200 4700
Wire Wire Line
	7100 4650 7100 4700
Wire Wire Line
	7000 4650 7000 4700
Wire Wire Line
	6900 4650 6900 4700
Wire Wire Line
	6800 4650 6800 4700
Wire Wire Line
	6700 4650 6700 4700
Wire Wire Line
	6600 4650 6600 4700
Wire Wire Line
	6500 4650 6500 4700
Wire Wire Line
	6400 4650 6400 4700
Wire Wire Line
	6300 4650 6300 4700
Wire Wire Line
	6200 4650 6200 4700
Wire Wire Line
	6100 4650 6100 4700
Wire Wire Line
	6000 4650 6000 4700
Wire Wire Line
	5900 4650 5900 4700
Wire Wire Line
	5800 4650 5800 4700
Wire Wire Line
	5700 4650 5700 4700
Wire Wire Line
	5600 4650 5600 4700
Wire Wire Line
	5400 4650 5400 4700
$Comp
L power:GND #PWR0101
U 1 1 5E301A55
P 8500 4700
F 0 "#PWR0101" H 8500 4450 50  0001 C CNN
F 1 "GND" V 8500 4500 50  0000 C CNN
F 2 "" H 8500 4700 50  0001 C CNN
F 3 "" H 8500 4700 50  0001 C CNN
	1    8500 4700
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5500 4650 5500 4700
Text GLabel 5400 4700 3    50   Input ~ 0
VIN
Text GLabel 7700 1650 1    50   Input ~ 0
5V
Text GLabel 5500 4700 3    50   Input ~ 0
D2-boot1
Text GLabel 6850 2100 0    50   Input ~ 0
D2-boot1
Wire Wire Line
	6850 2100 6900 2100
Text GLabel 5600 4700 3    50   Input ~ 0
M13
Text GLabel 6850 3200 0    50   Input ~ 0
M13
Wire Wire Line
	6900 3200 6850 3200
Text GLabel 5700 4700 3    50   Input ~ 0
M14
Text GLabel 6850 3300 0    50   Input ~ 0
M14
Wire Wire Line
	6850 3300 6900 3300
Text GLabel 5800 4700 3    50   Input ~ 0
M12
Text GLabel 6850 3100 0    50   Input ~ 0
M12
Wire Wire Line
	6850 3100 6900 3100
Text GLabel 5900 4700 3    50   Input ~ 0
M11
Text GLabel 6850 3000 0    50   Input ~ 0
M11
Wire Wire Line
	6850 3000 6900 3000
Text GLabel 6850 2900 0    50   Input ~ 0
M10
Wire Wire Line
	6850 2900 6900 2900
Text GLabel 6100 4700 3    50   Input ~ 0
M9
Text GLabel 6850 2800 0    50   Input ~ 0
M9
Wire Wire Line
	6900 2800 6850 2800
Text GLabel 6200 4700 3    50   Input ~ 0
M8
Text GLabel 6850 2700 0    50   Input ~ 0
M8
Wire Wire Line
	6850 2700 6900 2700
Text GLabel 6300 4700 3    50   Input ~ 0
M7
Text GLabel 6850 2600 0    50   Input ~ 0
M7
Wire Wire Line
	6850 2600 6900 2600
Text GLabel 6400 4700 3    50   Input ~ 0
M6
Text GLabel 6850 2500 0    50   Input ~ 0
M6
Wire Wire Line
	6850 2500 6900 2500
Text GLabel 6500 4700 3    50   Input ~ 0
M5
Text GLabel 6600 4700 3    50   Input ~ 0
M4
Text GLabel 6850 2400 0    50   Input ~ 0
M5
Text GLabel 6850 2300 0    50   Input ~ 0
M4
Wire Wire Line
	6850 2300 6900 2300
Wire Wire Line
	6850 2400 6900 2400
Text GLabel 6700 4700 3    50   Input ~ 0
M18
Text GLabel 8550 2200 2    50   Input ~ 0
M18
Wire Wire Line
	8500 2200 8550 2200
Text GLabel 6800 4700 3    50   Input ~ 0
M17
Text GLabel 8550 2100 2    50   Input ~ 0
M17
Wire Wire Line
	8500 2100 8550 2100
Text GLabel 6900 4700 3    50   Input ~ 0
M16
Text GLabel 8550 2000 2    50   Input ~ 0
M16
Wire Wire Line
	8500 2000 8550 2000
$Comp
L power:GND #PWR0102
U 1 1 5E32F4FC
P 7700 3950
F 0 "#PWR0102" H 7700 3700 50  0001 C CNN
F 1 "GND" V 7700 3750 50  0000 C CNN
F 2 "" H 7700 3950 50  0001 C CNN
F 3 "" H 7700 3950 50  0001 C CNN
	1    7700 3950
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7700 3900 7700 3950
Text GLabel 6000 4700 3    50   Input ~ 0
M10
Text GLabel 8400 4700 3    50   Input ~ 0
M1
Text GLabel 6850 2000 0    50   Input ~ 0
M1
Wire Wire Line
	6900 2000 6850 2000
Text GLabel 8300 4700 3    50   Input ~ 0
M0
Text GLabel 6850 1900 0    50   Input ~ 0
M0
Wire Wire Line
	6850 1900 6900 1900
$Comp
L Device:R R2
U 1 1 5E33B8C6
P 5925 3350
F 0 "R2" H 5995 3396 50  0000 L CNN
F 1 "R" H 5995 3305 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 5855 3350 50  0001 C CNN
F 3 "~" H 5925 3350 50  0001 C CNN
	1    5925 3350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E33BAAF
P 5600 3350
F 0 "R1" H 5670 3396 50  0000 L CNN
F 1 "R" H 5670 3305 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 5530 3350 50  0001 C CNN
F 3 "~" H 5600 3350 50  0001 C CNN
	1    5600 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 3200 5600 3150
Wire Wire Line
	5925 3200 5925 3150
$Comp
L Device:LED LED1
U 1 1 5E33F111
P 5600 3000
F 0 "LED1" V 5547 3079 50  0000 L CNN
F 1 "LED" V 5638 3079 50  0000 L CNN
F 2 "LED_THT:LED_D3.0mm" H 5600 3000 50  0001 C CNN
F 3 "~" H 5600 3000 50  0001 C CNN
	1    5600 3000
	0    1    1    0   
$EndComp
Wire Wire Line
	5600 3500 5600 3550
Text GLabel 5600 3550 3    50   Input ~ 0
VIN
Text GLabel 5925 3550 3    50   Input ~ 0
VIN
Wire Wire Line
	5925 3550 5925 3500
$Comp
L Device:LED LED2
U 1 1 5E347640
P 5925 3000
F 0 "LED2" V 5872 3079 50  0000 L CNN
F 1 "LED" V 5963 3079 50  0000 L CNN
F 2 "LED_THT:LED_D3.0mm" H 5925 3000 50  0001 C CNN
F 3 "~" H 5925 3000 50  0001 C CNN
	1    5925 3000
	0    1    1    0   
$EndComp
Wire Wire Line
	5925 2850 5925 2800
Wire Wire Line
	5600 2850 5600 2800
Text GLabel 5925 2800 1    50   Input ~ 0
M14
Text GLabel 5600 2800 1    50   Input ~ 0
M13
Text GLabel 8200 4700 3    50   Input ~ 0
M20
Text GLabel 8550 2400 2    50   Input ~ 0
M20
Wire Wire Line
	8500 2400 8550 2400
Text GLabel 8100 4700 3    50   Input ~ 0
M21
Text GLabel 8000 4700 3    50   Input ~ 0
M22
Text GLabel 8550 2500 2    50   Input ~ 0
M21
Wire Wire Line
	8500 2500 8550 2500
Wire Wire Line
	8500 2600 8550 2600
Text GLabel 8550 2600 2    50   Input ~ 0
M22
Text GLabel 7900 4700 3    50   Input ~ 0
D32-boot0
Text GLabel 8550 3600 2    50   Input ~ 0
D32-boot0
Wire Wire Line
	8500 3600 8550 3600
Text GLabel 7800 4700 3    50   Input ~ 0
M19
Text GLabel 8550 2300 2    50   Input ~ 0
M19
Wire Wire Line
	8500 2300 8550 2300
Text GLabel 7700 4700 3    50   Input ~ 0
M25
Text GLabel 8550 2900 2    50   Input ~ 0
M25
Wire Wire Line
	8500 2900 8550 2900
Text GLabel 7600 4700 3    50   Input ~ 0
M26
Text GLabel 8550 3000 2    50   Input ~ 0
M26
Wire Wire Line
	8500 3000 8550 3000
Text GLabel 7500 4700 3    50   Input ~ 0
M27
Text GLabel 8550 3100 2    50   Input ~ 0
M27
Wire Wire Line
	8500 3100 8550 3100
Text GLabel 7400 4700 3    50   Input ~ 0
M28
Text GLabel 7300 4700 3    50   Input ~ 0
M29
Text GLabel 7200 4700 3    50   Input ~ 0
M30
Text GLabel 7100 4700 3    50   Input ~ 0
M31
Text GLabel 7000 4700 3    50   Input ~ 0
M15
Text GLabel 8550 3200 2    50   Input ~ 0
M28
Wire Wire Line
	8500 3200 8550 3200
Text GLabel 8550 3300 2    50   Input ~ 0
M29
Wire Wire Line
	8500 3300 8550 3300
Text GLabel 8550 3400 2    50   Input ~ 0
M30
Wire Wire Line
	8500 3400 8550 3400
Text GLabel 8550 3500 2    50   Input ~ 0
M31
Wire Wire Line
	8500 3500 8550 3500
Text GLabel 8550 1900 2    50   Input ~ 0
M15
Wire Wire Line
	8500 1900 8550 1900
NoConn ~ 7800 1700
NoConn ~ 6900 2200
NoConn ~ 8500 2800
NoConn ~ 6900 3500
NoConn ~ 6900 3600
NoConn ~ 6900 3700
Text GLabel 7600 1650 1    50   Input ~ 0
3.3V
$Comp
L custom:NLAS4157 U1
U 1 1 5E9C9E84
P 10175 2500
F 0 "U1" H 10175 2625 50  0000 C CNN
F 1 "NLAS4157" H 10175 2534 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-363_SC-70-6" H 10175 2500 50  0001 C CNN
F 3 "" H 10175 2500 50  0001 C CNN
	1    10175 2500
	1    0    0    -1  
$EndComp
Text GLabel 9775 2600 0    50   Input ~ 0
5V
Text GLabel 9775 2800 0    50   Input ~ 0
3.3V
Wire Wire Line
	7700 1650 7700 1700
Wire Wire Line
	7600 1650 7600 1700
Wire Wire Line
	9825 2600 9775 2600
Wire Wire Line
	9825 2700 9775 2700
Wire Wire Line
	9825 2800 9775 2800
Wire Wire Line
	10575 2600 10525 2600
Wire Wire Line
	10575 2700 10525 2700
Wire Wire Line
	10575 2800 10525 2800
Text GLabel 10575 2800 2    50   Input ~ 0
VIN
Text GLabel 10575 2700 2    50   Input ~ 0
5V
Wire Wire Line
	10575 2600 10575 2375
$Comp
L Device:R R0
U 1 1 5E9DE12C
P 10725 2375
F 0 "R0" V 10625 2375 50  0000 C CNN
F 1 "10k" V 10725 2375 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 10655 2375 50  0001 C CNN
F 3 "~" H 10725 2375 50  0001 C CNN
	1    10725 2375
	0    1    1    0   
$EndComp
Wire Wire Line
	10875 2375 10925 2375
Wire Wire Line
	10925 2375 10925 2450
$Comp
L power:GND #PWR0103
U 1 1 5E9E0E36
P 10925 2450
F 0 "#PWR0103" H 10925 2200 50  0001 C CNN
F 1 "GND" H 10930 2277 50  0000 C CNN
F 2 "" H 10925 2450 50  0001 C CNN
F 3 "" H 10925 2450 50  0001 C CNN
	1    10925 2450
	1    0    0    -1  
$EndComp
Text GLabel 10575 2325 1    50   Input ~ 0
VSwitch
Wire Wire Line
	10575 2325 10575 2375
Connection ~ 10575 2375
$Comp
L power:GND #PWR0104
U 1 1 5E9E830E
P 9775 2700
F 0 "#PWR0104" H 9775 2450 50  0001 C CNN
F 1 "GND" V 9775 2500 50  0000 C CNN
F 2 "" H 9775 2700 50  0001 C CNN
F 3 "" H 9775 2700 50  0001 C CNN
	1    9775 2700
	0    1    1    0   
$EndComp
Wire Wire Line
	8500 2700 8550 2700
Text GLabel 8550 2700 2    50   Input ~ 0
VSwitch
$EndSCHEMATC
