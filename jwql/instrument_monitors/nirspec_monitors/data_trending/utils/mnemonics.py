"""Module lists all neccessary mnemonics for NIRSpec data trending

The module includes several lists to import to NIRSpec data trending monitor program.
The lists are used for data aquisation and to set up the initial database.

Authors
-------
    - Daniel Kühbacher

Use
---
    import mnemoncis as mn

References
----------
    JWQL_NIRSpec_INputs_V4[2414].xlsx

Notes
-----

"""

# mnemonics underlaying certain conditions 15min
# INRSD_EXP_STAT != STARTED
mnemonic_cond_1 = [
    "SE_ZINRSFPEA",
    "SE_ZINRSFPEB"]

# mnemonics underlaying condition 15min
# INRSH_LAMP_SEL = NO_LAMP
mnemonic_cond_2 = [
    "SE_ZINRSICEA",
    "SE_ZINRSICEB"]

mnemonic_cond_3 = [
    "SE_ZINRSMCEA",
    "SE_ZINRSMCEB"]

# menmonics applicable when CAA is powered
# INRSH_CAA_PWRF_ST = ON
mnemonic_caa = [
    "IGDP_NRSI_C_CAAL1_TEMP",
    "IGDP_NRSI_C_CAAL2_TEMP",
    "IGDP_NRSI_C_CAAL3_TEMP",
    "IGDP_NRSI_C_CAAL4_TEMP"]

# only applicable when Filter table 10 is set
mnemonic_ft10 = [
    "INRSH_OA_VREFOFF",
    "INRSH_OA_VREF",

    "INRSH_CAA_VREFOFF",
    "INRSH_CAA_VREF",

    "INRSH_FWA_ADCMGAIN",
    "INRSH_FWA_ADCMOFFSET",
    "INRSH_FWA_MOTOR_VREF",

    "INRSH_GWA_ADCMGAIN",
    "INRSH_GWA_ADCMOFFSET",
    "INRSH_GWA_MOTOR_VREF",

    "INRSH_RMA_ADCMGAIN",
    "INRSH_RMA_ADCMOFFSET"]

# all mnemonics used for conditions
mnemonic_for_conditions = [
    "INRSM_MOVE_STAT",
    "INRSH_WHEEL_MOT_SVREF",
    "INRSI_CAA_ON_FLAG",
    "INRSH_LAMP_SEL",
    "INRSD_EXP_STAT",

    "INRSH_CAA_PWRF_ST",

    "INRSI_FWA_MOVE_ST",
    "INRSI_FWA_MECH_POS",
    "INRSI_GWA_MOVE_ST",
    "INRSI_GWA_MECH_POS",

    "INRSI_C_FWA_POSITION",
    "INRSI_C_GWA_X_POSITION",
    "INRSI_C_GWA_Y_POSITION",

    "ICTM_RT_FILTER"]

# these mnemonic are used by the day routine
mnemSet_day = [
    "INRSM_MSA_Q1_365VDD",
    "INRSM_MSA_Q1_365VPP",
    "INRSM_MSA_Q1_171VPP",
    "IGDPM_MSA_Q1_365IDD",
    "IGDPM_MSA_Q1_365IPP",
    "IGDPM_MSA_Q1_171RTN",

    "INRSM_MSA_Q2_365VDD",
    "INRSM_MSA_Q2_365VPP",
    "INRSM_MSA_Q2_171VPP",
    "IGDPM_MSA_Q2_365IDD",
    "IGDPM_MSA_Q2_365IPP",
    "IGDPM_MSA_Q2_171RTN",

    "INRSM_MSA_Q3_365VDD",
    "INRSM_MSA_Q3_365VPP",
    "INRSM_MSA_Q3_171VPP",
    "IGDPM_MSA_Q3_365IDD",
    "IGDPM_MSA_Q3_365IPP",
    "IGDPM_MSA_Q3_171RTN",

    "INRSM_MSA_Q4_365VDD",
    "INRSM_MSA_Q4_365VPP",
    "INRSM_MSA_Q4_171VPP",
    "IGDPM_MSA_Q4_365IDD",
    "IGDPM_MSA_Q4_365IPP",
    "IGDPM_MSA_Q4_171RTN",

    "IGDP_NRSD_ALG_FPA_TEMP",
    "IGDP_NRSD_ALG_A1_TEMP",
    "IGDP_NRSD_ALG_A2_TEMP",
    "IGDP_NRSI_C_FWA_TEMP",
    "IGDP_NRSI_C_GWA_TEMP",

    "SI_GZCTS74A",
    "SI_GZCTS74B",
    "SI_GZCTS67A",
    "SI_GZCTS67B"]

# these mnemonic are used by the 15min routine
mnemSet_15min = [
    "IGDP_NRSD_ALG_TEMP",

    "INRSD_ALG_ACC_P12C",
    "INRSD_ALG_ACC_N12C",
    "INRSD_ALG_ACC_3D3_1D5_C",
    "INRSD_ALG_CHASSIS",

    "IGDP_NRSD_ALG_A1_VDD_C",
    "IGDP_NRSD_ALG_A1_VDDA",
    "IGDP_NRSD_ALG_A1VDAP12C",
    "IGDP_NRSD_ALG_A1VDAN12C",
    "IGDP_NRSD_ALG_A1GND4VDA",
    "IGDP_NRSD_ALG_A1GND5VRF",
    "INRSD_ALG_A1_VDD3P3",
    "INRSD_ALG_A1_VDD",
    "INRSD_ALG_A1_REF",
    "INRSD_A1_DSUB_V",
    "INRSD_A1_VRESET_V",
    "INRSD_A1_CELLDRN_V",
    "INRSD_A1_DRAIN_V",
    "INRSD_A1_VBIASGATE_V",
    "INRSD_A1_VBIASPWR_V",
    "INRSD_A1_VDDA_I",

    "IGDP_NRSD_ALG_A2_VDD_C",
    "IGDP_NRSD_ALG_A2_VDDA",
    "IGDP_NRSD_ALG_A2VDAP12C",
    "IGDP_NRSD_ALG_A2VDAN12C",
    "IGDP_NRSD_ALG_A2GND4VDA",
    "IGDP_NRSD_ALG_A2GND5VRF",
    "INRSD_ALG_A2_VDD3P3",
    "INRSD_ALG_A2_VDD",
    "INRSD_ALG_A2_REF",
    "INRSD_A2_DSUB_V",
    "INRSD_A2_VRESET_V",
    "INRSD_A2_CELLDRN_V",
    "INRSD_A2_DRAIN_V",
    "INRSD_A2_VBIASGATE_V",
    "INRSD_A2_VBIASPWR_V",
    "INRSD_A2_VDDA_I",

    "INRSH_HK_TEMP1",
    "INRSH_HK_TEMP2",

    "INRSH_HK_P15V",
    "INRSH_HK_N15V",
    "INRSH_HK_VMOTOR",
    "INRSH_HK_P5V",
    "INRSH_HK_2P5V",
    "INRSH_HK_ADCTGAIN",
    "INRSH_HK_ADCTOFFSET",

    "IGDP_NRSI_C_CAM_TEMP",
    "IGDP_NRSI_C_COL_TEMP",
    "IGDP_NRSI_C_COM1_TEMP",
    "IGDP_NRSI_C_FOR_TEMP",
    "IGDP_NRSI_C_IFU_TEMP",
    "IGDP_NRSI_C_BP1_TEMP",
    "IGDP_NRSI_C_BP2_TEMP",
    "IGDP_NRSI_C_BP3_TEMP",
    "IGDP_NRSI_C_BP4_TEMP",
    "IGDP_NRSI_C_RMA_TEMP",

    "SI_GZCTS75A",
    "SI_GZCTS68A",
    "SI_GZCTS81A",
    "SI_GZCTS80A",
    "SI_GZCTS70A",
    "SI_GZCTS76A",
    "SI_GZCTS79A",
    "SI_GZCTS77A",
    "SI_GZCTS78A",
    "SI_GZCTS69A",

    "INRSM_MCE_AIC_1R5_V",
    "INRSM_MCE_AIC_3R3_V",
    "INRSM_MCE_AIC_5_V",
    "INRSM_MCE_AIC_P12_V",
    "INRSM_MCE_AIC_N12_V",
    "INRSM_MCE_AIC_3R3_I",
    "INRSM_MCE_AIC_5_I",
    "INRSM_MCE_AIC_P12_I",
    "INRSM_MCE_AIC_N12_I",

    "INRSM_MCE_MDAC_1R5_V",
    "INRSM_MCE_MDAC_3R3_V",
    "INRSM_MCE_MDAC_5_V",
    "INRSM_MCE_MDAC_P12_V",
    "INRSM_MCE_MDAC_N12_V",
    "INRSM_MCE_MDAC_3R3_I",
    "INRSM_MCE_MDAC_5_I",
    "INRSM_MCE_MDAC_P12_I",
    "INRSM_MCE_MDAC_N12_I",

    "INRSM_MCE_PCA_TMP1",
    "INRSM_MCE_PCA_TMP2",
    "INRSM_MCE_AIC_TMP_FPGA",
    "INRSM_MCE_AIC_TMP_ADC",
    "INRSM_MCE_AIC_TMP_VREG",
    "INRSM_MCE_MDAC_TMP_FPGA",
    "INRSM_MCE_MDAC_TMP_OSC",
    "INRSM_MCE_MDAC_TMP_BRD",
    "INRSM_MCE_MDAC_TMP_PHA",
    "INRSM_MCE_MDAC_TMP_PHB",

    "INRSM_Q1_TMP_A",
    "INRSM_Q2_TMP_A",
    "INRSM_Q3_TMP_A",
    "INRSM_Q4_TMP_A",
    "INRSM_MECH_MTR_TMP_A",
    "INRSM_LL_MTR_TMP_A",
    "INRSM_MSA_TMP_A"]

# mnemonic set for setting up database
mnemonic_set_database = [
    "GP_ZPSVOLT",
    "SE_ZINRSFPEA",
    "SE_ZINRSFPEB",

    "IGDP_NRSD_ALG_TEMP",

    "IGDP_NRSD_ALG_FPA_TEMP",
    "IGDP_NRSD_ALG_A1_TEMP",
    "IGDP_NRSD_ALG_A2_TEMP",
    "SI_GZCTS74A",
    "SI_GZCTS74B",
    "SI_GZCTS67A",
    "SI_GZCTS67B",

    "INRSD_ALG_ACC_P12C",
    "INRSD_ALG_ACC_N12C",
    "INRSD_ALG_ACC_3D3_1D5_C",
    "INRSD_ALG_CHASSIS",

    "IGDP_NRSD_ALG_A1_VDD_C",
    "IGDP_NRSD_ALG_A1_VDDA",
    "IGDP_NRSD_ALG_A1VDAP12C",
    "IGDP_NRSD_ALG_A1VDAN12C",
    "IGDP_NRSD_ALG_A1GND4VDA",
    "IGDP_NRSD_ALG_A1GND5VRF",
    "INRSD_ALG_A1_VDD3P3",
    "INRSD_ALG_A1_VDD",
    "INRSD_ALG_A1_REF",
    "INRSD_A1_DSUB_V",
    "INRSD_A1_VRESET_V",
    "INRSD_A1_CELLDRN_V",
    "INRSD_A1_DRAIN_V",
    "INRSD_A1_VBIASGATE_V",
    "INRSD_A1_VBIASPWR_V",
    "INRSD_A1_VDDA_I",

    "IGDP_NRSD_ALG_A2_VDD_C",
    "IGDP_NRSD_ALG_A2_VDDA",
    "IGDP_NRSD_ALG_A2VDAP12C",
    "IGDP_NRSD_ALG_A2VDAN12C",
    "IGDP_NRSD_ALG_A2GND4VDA",
    "IGDP_NRSD_ALG_A2GND5VRF",
    "INRSD_ALG_A2_VDD3P3",
    "INRSD_ALG_A2_VDD",
    "INRSD_ALG_A2_REF",
    "INRSD_A2_DSUB_V",
    "INRSD_A2_VRESET_V",
    "INRSD_A2_CELLDRN_V",
    "INRSD_A2_DRAIN_V",
    "INRSD_A2_VBIASGATE_V",
    "INRSD_A2_VBIASPWR_V",
    "INRSD_A2_VDDA_I",

    "SE_ZINRSICEA",
    "SE_ZINRSICEB",

    "INRSH_HK_TEMP1",
    "INRSH_HK_TEMP2",

    "INRSH_HK_P15V",
    "INRSH_HK_N15V",
    "INRSH_HK_VMOTOR",
    "INRSH_HK_P5V",
    "INRSH_HK_2P5V",
    "INRSH_HK_ADCTGAIN",
    "INRSH_HK_ADCTOFFSET",

    "INRSH_OA_VREFOFF",
    "INRSH_OA_VREF",

    "IGDP_NRSI_C_CAM_TEMP",
    "IGDP_NRSI_C_COL_TEMP",
    "IGDP_NRSI_C_COM1_TEMP",
    "IGDP_NRSI_C_FOR_TEMP",
    "IGDP_NRSI_C_IFU_TEMP",
    "IGDP_NRSI_C_BP1_TEMP",
    "IGDP_NRSI_C_BP2_TEMP",
    "IGDP_NRSI_C_BP3_TEMP",
    "IGDP_NRSI_C_BP4_TEMP",
    "IGDP_NRSI_C_RMA_TEMP",

    "INRSH_CAA_VREFOFF",
    "INRSH_CAA_VREF",

    "INRSH_LAMP_SEL",
    "INRSI_C_CAA_CURRENT",
    "INRSI_C_CAA_VOLTAGE",

    "IGDP_NRSI_C_CAAL1_TEMP",
    "IGDP_NRSI_C_CAAL2_TEMP",
    "IGDP_NRSI_C_CAAL3_TEMP",
    "IGDP_NRSI_C_CAAL4_TEMP",

    "INRSH_FWA_ADCMGAIN",
    "INRSH_FWA_ADCMOFFSET",
    "INRSH_FWA_MOTOR_VREF",

    "IGDP_NRSI_C_FWA_TEMP",

    "INRSH_GWA_ADCMGAIN",
    "INRSH_GWA_ADCMOFFSET",
    "INRSH_GWA_MOTOR_VREF",

    "IGDP_NRSI_C_GWA_TEMP",

    "INRSH_RMA_ADCMGAIN",
    "INRSH_RMA_ADCMOFFSET",

    "SI_GZCTS75A",
    "SI_GZCTS68A",
    "SI_GZCTS81A",
    "SI_GZCTS80A",
    "SI_GZCTS70A",
    "SI_GZCTS76A",
    "SI_GZCTS79A",
    "SI_GZCTS77A",
    "SI_GZCTS78A",
    "SI_GZCTS69A",
    "SI_GZCTS75B",
    "SI_GZCTS68B",
    "SI_GZCTS81B",
    "SI_GZCTS80B",
    "SI_GZCTS70B",
    "SI_GZCTS76B",
    "SI_GZCTS79B",
    "SI_GZCTS77B",
    "SI_GZCTS78B",
    "SI_GZCTS69B",

    "SE_ZINRSMCEA",
    "SE_ZINRSMCEB",

    "INRSM_MCE_AIC_1R5_V",
    "INRSM_MCE_AIC_3R3_V",
    "INRSM_MCE_AIC_5_V",
    "INRSM_MCE_AIC_P12_V",
    "INRSM_MCE_AIC_N12_V",
    "INRSM_MCE_AIC_3R3_I",
    "INRSM_MCE_AIC_5_I",
    "INRSM_MCE_AIC_P12_I",
    "INRSM_MCE_AIC_N12_I",

    "INRSM_MCE_MDAC_1R5_V",
    "INRSM_MCE_MDAC_3R3_V",
    "INRSM_MCE_MDAC_5_V",
    "INRSM_MCE_MDAC_P12_V",
    "INRSM_MCE_MDAC_N12_V",
    "INRSM_MCE_MDAC_3R3_I",
    "INRSM_MCE_MDAC_5_I",
    "INRSM_MCE_MDAC_P12_I",
    "INRSM_MCE_MDAC_N12_I",

    "INRSM_MCE_PCA_TMP1",
    "INRSM_MCE_PCA_TMP2",
    "INRSM_MCE_AIC_TMP_FPGA",
    "INRSM_MCE_AIC_TMP_ADC",
    "INRSM_MCE_AIC_TMP_VREG",
    "INRSM_MCE_MDAC_TMP_FPGA",
    "INRSM_MCE_MDAC_TMP_OSC",
    "INRSM_MCE_MDAC_TMP_BRD",
    "INRSM_MCE_MDAC_TMP_PHA",
    "INRSM_MCE_MDAC_TMP_PHB",

    "INRSM_Q1_TMP_A",
    "INRSM_Q2_TMP_A",
    "INRSM_Q3_TMP_A",
    "INRSM_Q4_TMP_A",
    "INRSM_MECH_MTR_TMP_A",
    "INRSM_LL_MTR_TMP_A",
    "INRSM_MSA_TMP_A",

    "INRSM_Q1_TMP_B",
    "INRSM_Q2_TMP_B",
    "INRSM_Q3_TMP_B",
    "INRSM_Q4_TMP_B",
    "INRSM_MECH_MTR_TMP_B",
    "INRSM_LL_MTR_TMP_B",
    "INRSM_MSA_TMP_B",

    "INRSM_MSA_Q1_365VDD",
    "INRSM_MSA_Q1_365VPP",
    "INRSM_MSA_Q1_171VPP",
    "IGDPM_MSA_Q1_365IDD",
    "IGDPM_MSA_Q1_365IPP",
    "IGDPM_MSA_Q1_171RTN",

    "INRSM_MSA_Q2_365VDD",
    "INRSM_MSA_Q2_365VPP",
    "INRSM_MSA_Q2_171VPP",
    "IGDPM_MSA_Q2_365IDD",
    "IGDPM_MSA_Q2_365IPP",
    "IGDPM_MSA_Q2_171RTN",

    "INRSM_MSA_Q3_365VDD",
    "INRSM_MSA_Q3_365VPP",
    "INRSM_MSA_Q3_171VPP",
    "IGDPM_MSA_Q3_365IDD",
    "IGDPM_MSA_Q3_365IPP",
    "IGDPM_MSA_Q3_171RTN",

    "INRSM_MSA_Q4_365VDD",
    "INRSM_MSA_Q4_365VPP",
    "INRSM_MSA_Q4_171VPP",
    "IGDPM_MSA_Q4_365IDD",
    "IGDPM_MSA_Q4_365IPP",
    "IGDPM_MSA_Q4_171RTN",

    "LAMP_FLAT1_CURR",
    "LAMP_FLAT2_CURR",
    "LAMP_FLAT3_CURR",
    "LAMP_FLAT4_CURR",
    "LAMP_FLAT5_CURR",
    "LAMP_LINE1_CURR",
    "LAMP_LINE2_CURR",
    "LAMP_LINE3_CURR",
    "LAMP_LINE4_CURR",
    "LAMP_REF_CURR",
    "LAMP_TEST_CURR",

    "LAMP_FLAT1_VOLT",
    "LAMP_FLAT2_VOLT",
    "LAMP_FLAT3_VOLT",
    "LAMP_FLAT4_VOLT",
    "LAMP_FLAT5_VOLT",
    "LAMP_LINE1_VOLT",
    "LAMP_LINE2_VOLT",
    "LAMP_LINE3_VOLT",
    "LAMP_LINE4_VOLT",
    "LAMP_REF_VOLT",
    "LAMP_TEST_VOLT"]

mnemonic_wheelpositions = [
    "INRSI_C_FWA_POSITION_F110W",
    "INRSI_C_FWA_POSITION_F100LP",
    "INRSI_C_FWA_POSITION_F140X",
    "INRSI_C_FWA_POSITION_OPAQUE",
    "INRSI_C_FWA_POSITION_F290LP",
    "INRSI_C_FWA_POSITION_F170LP",
    "INRSI_C_FWA_POSITION_CLEAR",
    "INRSI_C_FWA_POSITION_F070LP",

    "INRSI_C_GWA_X_POSITION_PRISM",
    "INRSI_C_GWA_Y_POSITION_PRISM",

    "INRSI_C_GWA_X_POSITION_MIRROR",
    "INRSI_C_GWA_Y_POSITION_MIRROR",

    "INRSI_C_GWA_X_POSITION_G140H",
    "INRSI_C_GWA_Y_POSITION_G140H",

    "INRSI_C_GWA_X_POSITION_G235H",
    "INRSI_C_GWA_Y_POSITION_G235H",

    "INRSI_C_GWA_X_POSITION_G395H",
    "INRSI_C_GWA_Y_POSITION_G395H",

    "INRSI_C_GWA_X_POSITION_G140M",
    "INRSI_C_GWA_Y_POSITION_G140M",

    "INRSI_C_GWA_X_POSITION_G235M",
    "INRSI_C_GWA_Y_POSITION_G235M",

    "INRSI_C_GWA_X_POSITION_G395M",
    "INRSI_C_GWA_Y_POSITION_G395M"]

fw_nominals = {
    'F110W': -123.99,
    'F100LP': -10.32,
    'CLEAR': -56.44,
    'F070LP': 43.45,
    'F140X': -78.37,
    'OPAQUE': 21.58,
    'F290LP': -95.78,
    'F170LP': 8.95}

gwx_nominals = {
    'PRISM': 169.01,
    'MIRROR': 171.11,
    'G140H': 180.25,
    'G235H': 176.66,
    'G395H': 159.96,
    'G140M': 164.31,
    'G235M': 159.24,
    'G395M': 141.69}

gwy_nominals = {
    'PRISM': 17.08,
    'MIRROR': 98.72,
    'G140H': 67.47,
    'G235H': 70.00,
    'G395H': 73.29,
    'G140M': 63.18,
    'G235M': 69.81,
    'G395M': 89.57}

# use this list for query
mnemonic_set_query = mnemonic_set_database + mnemonic_for_conditions
