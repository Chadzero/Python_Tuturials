# ####################################################################
# #
# # NAME: si_postscript.py
# # Desc: 13G DTK
# # Author: Jake Rennemeyer - 09/23/2014
# #
# ####################################################################

# ####################################################################
# # Import Standard Code Libraries
# ####################################################################
import cfi_tools
import os
import re
import string
import time

# ####################################################################
# # Standard Variables
# ####################################################################
PN = cfi_tools.cfi_getenv('PN')
NAME = "[13G DTK] - "
SCRIPTVER = '1.0'
OWNER = 'CFI'

# ####################################################################
# # Set the System Variables
# ####################################################################
CP = cfi_tools.cfi_getenv("CUSTOMERPARTITION")  # Get Customer Partition
OS = cfi_tools.cfi_getenv("OS")  # Get OS 
OSL = cfi_tools.cfi_getenv("OSL")  # Get OS Language
MODEL = cfi_tools.cfi_getenv("model")  # Get System Model
SNUM = cfi_tools.cfi_getenv("snum")  # Get Service Tag
ASSETTAG = cfi_tools.cfi_getenv("ASSETTAG")  # Get the Asset Tag
SI = cfi_tools.cfi_getenv("SI")  # Get the SI
TEMP_PATH = cfi_tools.cfi_get_temp_directory()  # Get the Temp Directory
PROCESS_PATH = cfi_tools.cfi_get_process_directory()  # Pull the process directory (usually X:\USR\BIN)
FI_ASD = cfi_tools.cfi_getenv("FI_ASD")  # Get current ASD mode 

# ####################################################################
# ####################################################################
# # MAIN PROGRAM BODY
# ####################################################################
# ####################################################################
cfi_tools.cfi_log(NAME + "Made it to DTK", "LOG")

# #########################################
# # Check for ASD
# #########################################
if FI_ASD == "YES":
  cfi_tools.cfi_log(NAME + "Detected ASD Mode", "LOG")
else:
  cfi_tools.cfi_log(NAME + "Did not detect ASD Mode", "LOG")

# #########################################
# # Begin actual DTK work
# #########################################
  if not cfi_tools.get_cfi_process_files(os.path.join("BIOS_TOOLS", "dtksetup")):
    cfi_tools.cfi_fail(NAME + "Failed to import DTK Setup! Cannot continue with DTK settings")
  else:
    import dtksetup
    SLEEP_DELAY = 15

    # Delay to allow the DRAC to "settle" before we start making changes
    time.sleep(SLEEP_DELAY)

    # NIC Enabled
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.Enable 1")
    cfi_tools.cfi_log( NAME + "Set iDRAC NIC to Enabled" , "LOG" )
    time.sleep(SLEEP_DELAY)

    # NIC Selection Dedicated
    # 1 = Dedicated, 2 = LOM1, 3 = LOM2, 4 = LOM3, 5 = LOM4
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.Selection 1")
    cfi_tools.cfi_log( NAME + "Set iDRAC NIC selection to Dedicated" , "LOG" )
    time.sleep(SLEEP_DELAY)
	
    # Autonegotiate ON
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.Autoneg 1")
    cfi_tools.cfi_log( NAME + "Set Autonegotiate to Enabled" , "LOG" )
    time.sleep(SLEEP_DELAY)

    # Set Duplex to FULL
	# dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.Duplex 1")
    # cfi_tools.cfi_log( NAME + "Set Duplex to Full" , "LOG" )
    # time.sleep(SLEEP_DELAY)

	  # Set MTU to 1500
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.MTU 1500")
    cfi_tools.cfi_log( NAME + "Set MTU to 1500" , "LOG" )
    time.sleep(SLEEP_DELAY)
	
	  # Register DRAC on DNS - Enable
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.DNSRegister 1")
    cfi_tools.cfi_log( NAME + "Set iDRAC Register DRAC on DNS to Enable" , "LOG" )
    time.sleep(SLEEP_DELAY)
	
	  # IPv4 - Enable
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.IPv4.Enable 1")
    cfi_tools.cfi_log( NAME + "Set IPv4 to Enable" , "LOG" )
    time.sleep(SLEEP_DELAY)	
	
	  # IPv4 Address Source to DHCP
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.IPv4.DHCPEnable 1")
    cfi_tools.cfi_log( NAME + "Set IPv4 Address Source to DHCP" , "LOG" )
    time.sleep(SLEEP_DELAY)
	
	  # Autoconfig Domain Name - Enable
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.DNSDomainNameFromDHCP 1")
    cfi_tools.cfi_log( NAME + "Set Autoconfigure Domain Name to Enable" , "LOG" )
    time.sleep(SLEEP_DELAY)	
	
    # DNS Servers from DHCP
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.IPv4.DNSFromDHCP 1")
    cfi_tools.cfi_log( NAME + "Set IPv4 DNS Servers from DHCP to Enabled" , "LOG" )
    time.sleep(SLEEP_DELAY)

    # Set DNS RAC Name to idrac-<servicetag> %%%%% added 3/20/2015 per PM request %%%%%
    RACNAME = str.lower("idrac-%s" % SNUM)
    dtksetup.tool_set_dtk_option("racadm8","set iDRAC.NIC.DNSRacName %s" % RACNAME)
    cfi_tools.cfi_log( NAME + " iDRAC set DNS RAC Name " , "LOG" )
    time.sleep(SLEEP_DELAY)

    cfi_tools.cfi_log( NAME + "All 13G iDRAC settings made successfully!" , "LOG" )