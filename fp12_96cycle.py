# test artefact for the case that pyschedule is
# read from folder
import sys
import networkx as nx
sys.path.append('../src')
import getopt
import matplotlib.pyplot as plt
import random
import numpy as np

opts, _ = getopt.getopt(sys.argv[1:], 't:', ['test'])


horizon=30000

from pyschedule import Scenario, solvers, plotters

S = Scenario('20*fp12',horizon=horizon)

# define two employees
ADD = S.Resources('ADD',num=6)   #加法
MUL = S.Resources('MUL',num=6)  #乘法

mud = S.Tasks('mud',num=108,length=2,delay_cost=1)
mod = S.Tasks('mod',num=108,length=2,delay_cost=1)
mdd = S.Tasks('mdd',num=108,length=2,delay_cost=1)
mld = S.Tasks('mld',num=108,length=2,delay_cost=1)
mrd = S.Tasks('mrd',num=108,length=2,delay_cost=1)

add = S.Tasks('add',num=134,delay_cost=1)
sub = S.Tasks('sub',num=134,delay_cost=1)

for i in range(0,108):
	mud[i] += MUL[0]|MUL[1]|MUL[2]|MUL[3]|MUL[4]|MUL[5]
for i in range(0,108):
	mod[i] += MUL[0]|MUL[1]|MUL[2]|MUL[3]|MUL[4]|MUL[5]
for i in range(0,108):
	mld[i] += MUL[0]|MUL[1]|MUL[2]|MUL[3]|MUL[4]|MUL[5]
for i in range(0,108):
	mrd[i] += MUL[0]|MUL[1]|MUL[2]|MUL[3]|MUL[4]|MUL[5]	
for i in range(0,108):
	mdd[i] += MUL[0]|MUL[1]|MUL[2]|MUL[3]|MUL[4]|MUL[5]
for i in range(0,134):
	add[i] += ADD[0]|ADD[1]|ADD[2]|ADD[3]|ADD[4]|ADD[5]
for i in range(0,134):
	sub[i] += ADD[0]|ADD[1]|ADD[2]|ADD[3]|ADD[4]|ADD[5]

S += mld[0] < mod[0]
S += mld[0] < mud[0]
S += mod[0] < mud[0]
S += mod[0] < mdd[0]
S += mod[0] < mdd[1]
S += mud[0] < mdd[0]
S += mrd[0] < mdd[0]
S += mdd[0] < mld[1]
S += mdd[0] < mrd[1]
S += mld[1] < mod[1]
S += mld[1] < mud[1]
S += mod[1] < mud[1]
S += mud[1] < mdd[1]
S += mrd[1] < mdd[1]
S += mdd[1] < sub[0]
S += mdd[1] <= add[2]
S += mld[2] < mod[2]
S += mld[2] < mud[2]
S += mod[2] < mud[2]
S += mod[2] < mdd[2]
S += mod[2] < mdd[3]
S += mud[2] < mdd[2]
S += mrd[2] < mdd[2]
S += mdd[2] < mld[3]
S += mdd[2] < mrd[3]
S += mld[3] < mod[3]
S += mld[3] < mud[3]
S += mod[3] < mud[3]
S += mud[3] < mdd[3]
S += mrd[3] < mdd[3]
S += mdd[3] < sub[0]
S += mdd[3] <= add[2]
S += mdd[3] < sub[1]
S += mld[4] < mod[4]
S += mld[4] < mud[4]
S += mod[4] < mud[4]
S += mod[4] < mdd[4]
S += mod[4] < mdd[5]
S += mud[4] < mdd[4]
S += mrd[4] < mdd[4]
S += mdd[4] < mld[5]
S += mdd[4] < mrd[5]
S += mld[5] < mod[5]
S += mld[5] < mud[5]
S += mod[5] < mud[5]
S += mud[5] < mdd[5]
S += mrd[5] < mdd[5]
S += mdd[5] < sub[2]
S += sub[0] < sub[1]
S += add[2] < sub[2]
S += sub[1] < sub[13]
S += sub[1] < add[13]
S += sub[2] < sub[14]
S += sub[2] < add[14]
S += mld[6] < mod[6]
S += mld[6] < mud[6]
S += mod[6] < mud[6]
S += mod[6] < mdd[6]
S += mod[6] < mdd[7]
S += mud[6] < mdd[6]
S += mrd[6] < mdd[6]
S += mdd[6] < mld[7]
S += mdd[6] < mrd[7]
S += mld[7] < mod[7]
S += mld[7] < mud[7]
S += mod[7] < mud[7]
S += mud[7] < mdd[7]
S += mrd[7] < mdd[7]
S += mdd[7] < sub[3]
S += mdd[7] <= add[5]
S += mld[8] < mod[8]
S += mld[8] < mud[8]
S += mod[8] < mud[8]
S += mod[8] < mdd[8]
S += mod[8] < mdd[9]
S += mud[8] < mdd[8]
S += mrd[8] < mdd[8]
S += mdd[8] < mld[9]
S += mdd[8] < mrd[9]
S += mld[9] < mod[9]
S += mld[9] < mud[9]
S += mod[9] < mud[9]
S += mud[9] < mdd[9]
S += mrd[9] < mdd[9]
S += mdd[9] < sub[3]
S += mdd[9] <= add[5]
S += mdd[9] < sub[4]
S += mld[10] < mod[10]
S += mld[10] < mud[10]
S += mod[10] < mud[10]
S += mod[10] < mdd[10]
S += mod[10] < mdd[11]
S += mud[10] < mdd[10]
S += mrd[10] < mdd[10]
S += mdd[10] < mld[11]
S += mdd[10] < mrd[11]
S += mld[11] < mod[11]
S += mld[11] < mud[11]
S += mod[11] < mud[11]
S += mud[11] < mdd[11]
S += mrd[11] < mdd[11]
S += mdd[11] < sub[5]
S += sub[3] < sub[4]
S += add[5] < sub[5]
S += sub[4] < sub[7]
S += sub[4] < sub[15]
S += sub[5] < sub[6]
S += sub[5] < sub[8]
S += sub[5] < sub[16]
S += add[6] < add[10]
S += add[7] < add[10]
S += add[8] < add[11]
S += add[9] < add[11]
S += sub[6] < sub[8]
S += sub[7] < sub[9]
S += sub[8] < add[13]
S += sub[9] < add[14]
S += mld[12] < mod[12]
S += mld[12] < mud[12]
S += mod[12] < mud[12]
S += mod[12] < mdd[12]
S += mod[12] < mdd[13]
S += mud[12] < mdd[12]
S += mrd[12] < mdd[12]
S += mdd[12] < mld[13]
S += mdd[12] < mrd[13]
S += mld[13] < mod[13]
S += mld[13] < mud[13]
S += mod[13] < mud[13]
S += mud[13] < mdd[13]
S += mrd[13] < mdd[13]
S += mdd[13] < sub[10]
S += mdd[13] <= add[12]
S += mld[14] < mod[14]
S += mld[14] < mud[14]
S += mod[14] < mud[14]
S += mod[14] < mdd[14]
S += mod[14] < mdd[15]
S += mud[14] < mdd[14]
S += mrd[14] < mdd[14]
S += mdd[14] < mld[15]
S += mdd[14] < mrd[15]
S += mld[15] < mod[15]
S += mld[15] < mud[15]
S += mod[15] < mud[15]
S += mud[15] < mdd[15]
S += mrd[15] < mdd[15]
S += mdd[15] < sub[10]
S += mdd[15] <= add[12]
S += mdd[15] < sub[11]
S += mld[16] < mod[16]
S += mld[16] < mud[16]
S += mod[16] < mud[16]
S += mod[16] < mdd[16]
S += mod[16] < mdd[17]
S += mud[16] < mdd[16]
S += mrd[16] < mdd[16]
S += mdd[16] < mld[17]
S += mdd[16] < mrd[17]
S += mld[17] < mod[17]
S += mld[17] < mud[17]
S += mod[17] < mud[17]
S += mud[17] < mdd[17]
S += mrd[17] < mdd[17]
S += mdd[17] < sub[12]
S += sub[10] < sub[11]
S += add[12] < sub[12]
S += sub[11] < sub[13]
S += sub[12] < sub[14]
S += sub[13] < sub[15]
S += sub[14] < sub[16]
S += sub[15] < sub[70]
S += sub[15] < sub[98]
S += sub[15] < sub[128]
S += sub[16] < sub[71]
S += sub[16] < add[107]
S += sub[16] < sub[129]
S += add[13] < sub[68]
S += add[13] < sub[99]
S += add[13] < sub[126]
S += add[14] < sub[69]
S += add[14] < sub[100]
S += add[14] < sub[127]
S += add[15] < add[46]
S += add[15] < add[52]
S += add[16] < add[46]
S += add[16] < add[53]
S += add[17] < add[49]
S += add[17] < add[52]
S += add[18] < add[49]
S += add[18] < add[53]
S += add[19] < add[47]
S += add[19] < add[54]
S += add[20] < add[47]
S += add[20] < add[55]
S += add[21] < add[50]
S += add[21] < add[54]
S += add[22] < add[50]
S += add[22] < add[55]
S += mld[18] < mod[18]
S += mld[18] < mud[18]
S += mod[18] < mud[18]
S += mod[18] < mdd[18]
S += mod[18] < mdd[19]
S += mud[18] < mdd[18]
S += mrd[18] < mdd[18]
S += mdd[18] < mld[19]
S += mdd[18] < mrd[19]
S += mld[19] < mod[19]
S += mld[19] < mud[19]
S += mod[19] < mud[19]
S += mud[19] < mdd[19]
S += mrd[19] < mdd[19]
S += mdd[19] < sub[17]
S += mdd[19] <= add[25]
S += mld[20] < mod[20]
S += mld[20] < mud[20]
S += mod[20] < mud[20]
S += mod[20] < mdd[20]
S += mod[20] < mdd[21]
S += mud[20] < mdd[20]
S += mrd[20] < mdd[20]
S += mdd[20] < mld[21]
S += mdd[20] < mrd[21]
S += mld[21] < mod[21]
S += mld[21] < mud[21]
S += mod[21] < mud[21]
S += mud[21] < mdd[21]
S += mrd[21] < mdd[21]
S += mdd[21] < sub[17]
S += mdd[21] <= add[25]
S += mdd[21] < sub[18]
S += mld[22] < mod[22]
S += mld[22] < mud[22]
S += mod[22] < mud[22]
S += mod[22] < mdd[22]
S += mod[22] < mdd[23]
S += mud[22] < mdd[22]
S += mrd[22] < mdd[22]
S += mdd[22] < mld[23]
S += mdd[22] < mrd[23]
S += mld[23] < mod[23]
S += mld[23] < mud[23]
S += mod[23] < mud[23]
S += mud[23] < mdd[23]
S += mrd[23] < mdd[23]
S += mdd[23] < sub[19]
S += sub[17] < sub[18]
S += add[25] < sub[19]
S += sub[18] < sub[30]
S += sub[18] < add[36]
S += sub[19] < sub[31]
S += sub[19] < add[37]
S += mld[24] < mod[24]
S += mld[24] < mud[24]
S += mod[24] < mud[24]
S += mod[24] < mdd[24]
S += mod[24] < mdd[25]
S += mud[24] < mdd[24]
S += mrd[24] < mdd[24]
S += mdd[24] < mld[25]
S += mdd[24] < mrd[25]
S += mld[25] < mod[25]
S += mld[25] < mud[25]
S += mod[25] < mud[25]
S += mud[25] < mdd[25]
S += mrd[25] < mdd[25]
S += mdd[25] < sub[20]
S += mdd[25] <= add[28]
S += mld[26] < mod[26]
S += mld[26] < mud[26]
S += mod[26] < mud[26]
S += mod[26] < mdd[26]
S += mod[26] < mdd[27]
S += mud[26] < mdd[26]
S += mrd[26] < mdd[26]
S += mdd[26] < mld[27]
S += mdd[26] < mrd[27]
S += mld[27] < mod[27]
S += mld[27] < mud[27]
S += mod[27] < mud[27]
S += mud[27] < mdd[27]
S += mrd[27] < mdd[27]
S += mdd[27] < sub[20]
S += mdd[27] <= add[28]
S += mdd[27] < sub[21]
S += mld[28] < mod[28]
S += mld[28] < mud[28]
S += mod[28] < mud[28]
S += mod[28] < mdd[28]
S += mod[28] < mdd[29]
S += mud[28] < mdd[28]
S += mrd[28] < mdd[28]
S += mdd[28] < mld[29]
S += mdd[28] < mrd[29]
S += mld[29] < mod[29]
S += mld[29] < mud[29]
S += mod[29] < mud[29]
S += mud[29] < mdd[29]
S += mrd[29] < mdd[29]
S += mdd[29] < sub[22]
S += sub[20] < sub[21]
S += add[28] < sub[22]
S += sub[21] < sub[24]
S += sub[21] < sub[32]
S += sub[22] < sub[23]
S += sub[22] < sub[25]
S += sub[22] < sub[33]
S += add[29] < add[33]
S += add[30] < add[33]
S += add[31] < add[34]
S += add[32] < add[34]
S += sub[23] < sub[25]
S += sub[24] < sub[26]
S += sub[25] < add[36]
S += sub[26] < add[37]
S += mld[30] < mod[30]
S += mld[30] < mud[30]
S += mod[30] < mud[30]
S += mod[30] < mdd[30]
S += mod[30] < mdd[31]
S += mud[30] < mdd[30]
S += mrd[30] < mdd[30]
S += mdd[30] < mld[31]
S += mdd[30] < mrd[31]
S += mld[31] < mod[31]
S += mld[31] < mud[31]
S += mod[31] < mud[31]
S += mud[31] < mdd[31]
S += mrd[31] < mdd[31]
S += mdd[31] < sub[27]
S += mdd[31] <= add[35]
S += mld[32] < mod[32]
S += mld[32] < mud[32]
S += mod[32] < mud[32]
S += mod[32] < mdd[32]
S += mod[32] < mdd[33]
S += mud[32] < mdd[32]
S += mrd[32] < mdd[32]
S += mdd[32] < mld[33]
S += mdd[32] < mrd[33]
S += mld[33] < mod[33]
S += mld[33] < mud[33]
S += mod[33] < mud[33]
S += mud[33] < mdd[33]
S += mrd[33] < mdd[33]
S += mdd[33] < sub[27]
S += mdd[33] <= add[35]
S += mdd[33] < sub[28]
S += mld[34] < mod[34]
S += mld[34] < mud[34]
S += mod[34] < mud[34]
S += mod[34] < mdd[34]
S += mod[34] < mdd[35]
S += mud[34] < mdd[34]
S += mrd[34] < mdd[34]
S += mdd[34] < mld[35]
S += mdd[34] < mrd[35]
S += mld[35] < mod[35]
S += mld[35] < mud[35]
S += mod[35] < mud[35]
S += mud[35] < mdd[35]
S += mrd[35] < mdd[35]
S += mdd[35] < sub[29]
S += sub[27] < sub[28]
S += add[35] < sub[29]
S += sub[28] < sub[30]
S += sub[29] < sub[31]
S += sub[30] < sub[32]
S += sub[31] < sub[33]
S += sub[32] < sub[74]
S += sub[32] < sub[103]
S += sub[32] < add[132]
S += sub[33] < sub[75]
S += sub[33] < sub[104]
S += sub[33] < add[133]
S += add[36] < sub[72]
S += add[36] < sub[101]
S += add[36] < add[130]
S += add[37] < sub[73]
S += add[37] < sub[102]
S += add[37] < add[131]
S += add[38] < add[111]
S += add[38] < add[117]
S += add[39] < add[111]
S += add[39] < add[118]
S += add[40] < add[114]
S += add[40] < add[117]
S += add[41] < add[114]
S += add[41] < add[118]
S += add[42] < add[112]
S += add[42] < add[119]
S += add[43] < add[112]
S += add[43] < add[120]
S += add[44] < add[115]
S += add[44] < add[119]
S += add[45] < add[115]
S += add[45] < add[120]
S += mld[36] < mod[36]
S += mld[36] < mud[36]
S += mod[36] < mud[36]
S += mod[36] < mdd[36]
S += mod[36] < mdd[37]
S += mud[36] < mdd[36]
S += mrd[36] < mdd[36]
S += mdd[36] < mld[37]
S += mdd[36] < mrd[37]
S += mld[37] < mod[37]
S += mld[37] < mud[37]
S += mod[37] < mud[37]
S += mud[37] < mdd[37]
S += mrd[37] < mdd[37]
S += mdd[37] < sub[34]
S += mdd[37] <= add[48]
S += mld[38] < mod[38]
S += mld[38] < mud[38]
S += mod[38] < mud[38]
S += mod[38] < mdd[38]
S += mod[38] < mdd[39]
S += mud[38] < mdd[38]
S += mrd[38] < mdd[38]
S += mdd[38] < mld[39]
S += mdd[38] < mrd[39]
S += mld[39] < mod[39]
S += mld[39] < mud[39]
S += mod[39] < mud[39]
S += mud[39] < mdd[39]
S += mrd[39] < mdd[39]
S += mdd[39] < sub[34]
S += mdd[39] <= add[48]
S += mdd[39] < sub[35]
S += mld[40] < mod[40]
S += mld[40] < mud[40]
S += mod[40] < mud[40]
S += mod[40] < mdd[40]
S += mod[40] < mdd[41]
S += mud[40] < mdd[40]
S += mrd[40] < mdd[40]
S += mdd[40] < mld[41]
S += mdd[40] < mrd[41]
S += mld[41] < mod[41]
S += mld[41] < mud[41]
S += mod[41] < mud[41]
S += mud[41] < mdd[41]
S += mrd[41] < mdd[41]
S += mdd[41] < sub[36]
S += sub[34] < sub[35]
S += add[48] < sub[36]
S += sub[35] < sub[47]
S += sub[35] < add[59]
S += sub[36] < sub[48]
S += sub[36] < add[60]
S += mld[42] < mod[42]
S += mld[42] < mud[42]
S += mod[42] < mud[42]
S += mod[42] < mdd[42]
S += mod[42] < mdd[43]
S += mud[42] < mdd[42]
S += mrd[42] < mdd[42]
S += mdd[42] < mld[43]
S += mdd[42] < mrd[43]
S += mld[43] < mod[43]
S += mld[43] < mud[43]
S += mod[43] < mud[43]
S += mud[43] < mdd[43]
S += mrd[43] < mdd[43]
S += mdd[43] < sub[37]
S += mdd[43] <= add[51]
S += mld[44] < mod[44]
S += mld[44] < mud[44]
S += mod[44] < mud[44]
S += mod[44] < mdd[44]
S += mod[44] < mdd[45]
S += mud[44] < mdd[44]
S += mrd[44] < mdd[44]
S += mdd[44] < mld[45]
S += mdd[44] < mrd[45]
S += mld[45] < mod[45]
S += mld[45] < mud[45]
S += mod[45] < mud[45]
S += mud[45] < mdd[45]
S += mrd[45] < mdd[45]
S += mdd[45] < sub[37]
S += mdd[45] <= add[51]
S += mdd[45] < sub[38]
S += mld[46] < mod[46]
S += mld[46] < mud[46]
S += mod[46] < mud[46]
S += mod[46] < mdd[46]
S += mod[46] < mdd[47]
S += mud[46] < mdd[46]
S += mrd[46] < mdd[46]
S += mdd[46] < mld[47]
S += mdd[46] < mrd[47]
S += mld[47] < mod[47]
S += mld[47] < mud[47]
S += mod[47] < mud[47]
S += mud[47] < mdd[47]
S += mrd[47] < mdd[47]
S += mdd[47] < sub[39]
S += sub[37] < sub[38]
S += add[51] < sub[39]
S += sub[38] < sub[41]
S += sub[38] < sub[49]
S += sub[39] < sub[40]
S += sub[39] < sub[42]
S += sub[39] < sub[50]
S += add[52] < add[56]
S += add[53] < add[56]
S += add[54] < add[57]
S += add[55] < add[57]
S += sub[40] < sub[42]
S += sub[41] < sub[43]
S += sub[42] < add[59]
S += sub[43] < add[60]
S += mld[48] < mod[48]
S += mld[48] < mud[48]
S += mod[48] < mud[48]
S += mod[48] < mdd[48]
S += mod[48] < mdd[49]
S += mud[48] < mdd[48]
S += mrd[48] < mdd[48]
S += mdd[48] < mld[49]
S += mdd[48] < mrd[49]
S += mld[49] < mod[49]
S += mld[49] < mud[49]
S += mod[49] < mud[49]
S += mud[49] < mdd[49]
S += mrd[49] < mdd[49]
S += mdd[49] < sub[44]
S += mdd[49] <= add[58]
S += mld[50] < mod[50]
S += mld[50] < mud[50]
S += mod[50] < mud[50]
S += mod[50] < mdd[50]
S += mod[50] < mdd[51]
S += mud[50] < mdd[50]
S += mrd[50] < mdd[50]
S += mdd[50] < mld[51]
S += mdd[50] < mrd[51]
S += mld[51] < mod[51]
S += mld[51] < mud[51]
S += mod[51] < mud[51]
S += mud[51] < mdd[51]
S += mrd[51] < mdd[51]
S += mdd[51] < sub[44]
S += mdd[51] <= add[58]
S += mdd[51] < sub[45]
S += mld[52] < mod[52]
S += mld[52] < mud[52]
S += mod[52] < mud[52]
S += mod[52] < mdd[52]
S += mod[52] < mdd[53]
S += mud[52] < mdd[52]
S += mrd[52] < mdd[52]
S += mdd[52] < mld[53]
S += mdd[52] < mrd[53]
S += mld[53] < mod[53]
S += mld[53] < mud[53]
S += mod[53] < mud[53]
S += mud[53] < mdd[53]
S += mrd[53] < mdd[53]
S += mdd[53] < sub[46]
S += sub[44] < sub[45]
S += add[58] < sub[46]
S += sub[45] < sub[47]
S += sub[46] < sub[48]
S += sub[47] < sub[49]
S += sub[48] < sub[50]
S += sub[49] < sub[70]
S += sub[50] < sub[71]
S += add[59] < sub[68]
S += add[60] < sub[69]
S += add[61] < add[88]
S += add[61] < add[94]
S += add[62] < add[88]
S += add[62] < add[95]
S += add[63] < add[91]
S += add[63] < add[94]
S += add[64] < add[91]
S += add[64] < add[95]
S += add[65] < add[89]
S += add[65] < add[96]
S += add[66] < add[89]
S += add[66] < add[97]
S += add[67] < add[92]
S += add[67] < add[96]
S += add[68] < add[92]
S += add[68] < add[97]
S += mld[54] < mod[54]
S += mld[54] < mud[54]
S += mod[54] < mud[54]
S += mod[54] < mdd[54]
S += mod[54] < mdd[55]
S += mud[54] < mdd[54]
S += mrd[54] < mdd[54]
S += mdd[54] < mld[55]
S += mdd[54] < mrd[55]
S += mld[55] < mod[55]
S += mld[55] < mud[55]
S += mod[55] < mud[55]
S += mud[55] < mdd[55]
S += mrd[55] < mdd[55]
S += mdd[55] < sub[51]
S += mdd[55] <= add[71]
S += mld[56] < mod[56]
S += mld[56] < mud[56]
S += mod[56] < mud[56]
S += mod[56] < mdd[56]
S += mod[56] < mdd[57]
S += mud[56] < mdd[56]
S += mrd[56] < mdd[56]
S += mdd[56] < mld[57]
S += mdd[56] < mrd[57]
S += mld[57] < mod[57]
S += mld[57] < mud[57]
S += mod[57] < mud[57]
S += mud[57] < mdd[57]
S += mrd[57] < mdd[57]
S += mdd[57] < sub[51]
S += mdd[57] <= add[71]
S += mdd[57] < sub[52]
S += mld[58] < mod[58]
S += mld[58] < mud[58]
S += mod[58] < mud[58]
S += mod[58] < mdd[58]
S += mod[58] < mdd[59]
S += mud[58] < mdd[58]
S += mrd[58] < mdd[58]
S += mdd[58] < mld[59]
S += mdd[58] < mrd[59]
S += mld[59] < mod[59]
S += mld[59] < mud[59]
S += mod[59] < mud[59]
S += mud[59] < mdd[59]
S += mrd[59] < mdd[59]
S += mdd[59] < sub[53]
S += sub[51] < sub[52]
S += add[71] < sub[53]
S += sub[52] < sub[64]
S += sub[52] < add[82]
S += sub[53] < sub[65]
S += sub[53] < add[83]
S += mld[60] < mod[60]
S += mld[60] < mud[60]
S += mod[60] < mud[60]
S += mod[60] < mdd[60]
S += mod[60] < mdd[61]
S += mud[60] < mdd[60]
S += mrd[60] < mdd[60]
S += mdd[60] < mld[61]
S += mdd[60] < mrd[61]
S += mld[61] < mod[61]
S += mld[61] < mud[61]
S += mod[61] < mud[61]
S += mud[61] < mdd[61]
S += mrd[61] < mdd[61]
S += mdd[61] < sub[54]
S += mdd[61] <= add[74]
S += mld[62] < mod[62]
S += mld[62] < mud[62]
S += mod[62] < mud[62]
S += mod[62] < mdd[62]
S += mod[62] < mdd[63]
S += mud[62] < mdd[62]
S += mrd[62] < mdd[62]
S += mdd[62] < mld[63]
S += mdd[62] < mrd[63]
S += mld[63] < mod[63]
S += mld[63] < mud[63]
S += mod[63] < mud[63]
S += mud[63] < mdd[63]
S += mrd[63] < mdd[63]
S += mdd[63] < sub[54]
S += mdd[63] <= add[74]
S += mdd[63] < sub[55]
S += mld[64] < mod[64]
S += mld[64] < mud[64]
S += mod[64] < mud[64]
S += mod[64] < mdd[64]
S += mod[64] < mdd[65]
S += mud[64] < mdd[64]
S += mrd[64] < mdd[64]
S += mdd[64] < mld[65]
S += mdd[64] < mrd[65]
S += mld[65] < mod[65]
S += mld[65] < mud[65]
S += mod[65] < mud[65]
S += mud[65] < mdd[65]
S += mrd[65] < mdd[65]
S += mdd[65] < sub[56]
S += sub[54] < sub[55]
S += add[74] < sub[56]
S += sub[55] < sub[58]
S += sub[55] < sub[66]
S += sub[56] < sub[57]
S += sub[56] < sub[59]
S += sub[56] < sub[67]
S += add[75] < add[79]
S += add[76] < add[79]
S += add[77] < add[80]
S += add[78] < add[80]
S += sub[57] < sub[59]
S += sub[58] < sub[60]
S += sub[59] < add[82]
S += sub[60] < add[83]
S += mld[66] < mod[66]
S += mld[66] < mud[66]
S += mod[66] < mud[66]
S += mod[66] < mdd[66]
S += mod[66] < mdd[67]
S += mud[66] < mdd[66]
S += mrd[66] < mdd[66]
S += mdd[66] < mld[67]
S += mdd[66] < mrd[67]
S += mld[67] < mod[67]
S += mld[67] < mud[67]
S += mod[67] < mud[67]
S += mud[67] < mdd[67]
S += mrd[67] < mdd[67]
S += mdd[67] < sub[61]
S += mdd[67] <= add[81]
S += mld[68] < mod[68]
S += mld[68] < mud[68]
S += mod[68] < mud[68]
S += mod[68] < mdd[68]
S += mod[68] < mdd[69]
S += mud[68] < mdd[68]
S += mrd[68] < mdd[68]
S += mdd[68] < mld[69]
S += mdd[68] < mrd[69]
S += mld[69] < mod[69]
S += mld[69] < mud[69]
S += mod[69] < mud[69]
S += mud[69] < mdd[69]
S += mrd[69] < mdd[69]
S += mdd[69] < sub[61]
S += mdd[69] <= add[81]
S += mdd[69] < sub[62]
S += mld[70] < mod[70]
S += mld[70] < mud[70]
S += mod[70] < mud[70]
S += mod[70] < mdd[70]
S += mod[70] < mdd[71]
S += mud[70] < mdd[70]
S += mrd[70] < mdd[70]
S += mdd[70] < mld[71]
S += mdd[70] < mrd[71]
S += mld[71] < mod[71]
S += mld[71] < mud[71]
S += mod[71] < mud[71]
S += mud[71] < mdd[71]
S += mrd[71] < mdd[71]
S += mdd[71] < sub[63]
S += sub[61] < sub[62]
S += add[81] < sub[63]
S += sub[62] < sub[64]
S += sub[63] < sub[65]
S += sub[64] < sub[66]
S += sub[65] < sub[67]
S += sub[66] < add[105]
S += sub[66] < sub[107]
S += sub[66] < sub[132]
S += sub[67] < add[106]
S += sub[67] < sub[108]
S += sub[67] < sub[133]
S += add[82] < add[103]
S += add[82] < sub[105]
S += add[82] < sub[130]
S += add[83] < add[104]
S += add[83] < sub[106]
S += add[83] < sub[131]
S += sub[68] < sub[72]
S += sub[69] < sub[73]
S += sub[70] < sub[74]
S += sub[71] < sub[75]
S += sub[72] < sub[78]
S += sub[73] < sub[79]
S += sub[74] < sub[77]
S += sub[75] < add[84]
S += add[84] < sub[76]
S += add[85] < sub[77]
S += add[86] < sub[78]
S += add[87] < sub[79]
S += sub[76] < add[103]
S += sub[77] < add[104]
S += sub[78] < add[105]
S += sub[79] < add[106]
S += mld[72] < mod[72]
S += mld[72] < mud[72]
S += mod[72] < mud[72]
S += mod[72] < mdd[72]
S += mod[72] < mdd[73]
S += mud[72] < mdd[72]
S += mrd[72] < mdd[72]
S += mdd[72] < mld[73]
S += mdd[72] < mrd[73]
S += mld[73] < mod[73]
S += mld[73] < mud[73]
S += mod[73] < mud[73]
S += mud[73] < mdd[73]
S += mrd[73] < mdd[73]
S += mdd[73] < sub[80]
S += mdd[73] <= add[90]
S += mld[74] < mod[74]
S += mld[74] < mud[74]
S += mod[74] < mud[74]
S += mod[74] < mdd[74]
S += mod[74] < mdd[75]
S += mud[74] < mdd[74]
S += mrd[74] < mdd[74]
S += mdd[74] < mld[75]
S += mdd[74] < mrd[75]
S += mld[75] < mod[75]
S += mld[75] < mud[75]
S += mod[75] < mud[75]
S += mud[75] < mdd[75]
S += mrd[75] < mdd[75]
S += mdd[75] < sub[80]
S += mdd[75] <= add[90]
S += mdd[75] < sub[81]
S += mld[76] < mod[76]
S += mld[76] < mud[76]
S += mod[76] < mud[76]
S += mod[76] < mdd[76]
S += mod[76] < mdd[77]
S += mud[76] < mdd[76]
S += mrd[76] < mdd[76]
S += mdd[76] < mld[77]
S += mdd[76] < mrd[77]
S += mld[77] < mod[77]
S += mld[77] < mud[77]
S += mod[77] < mud[77]
S += mud[77] < mdd[77]
S += mrd[77] < mdd[77]
S += mdd[77] < sub[82]
S += sub[80] < sub[81]
S += add[90] < sub[82]
S += sub[81] < sub[93]
S += sub[81] < add[101]
S += sub[82] < sub[94]
S += sub[82] < add[102]
S += mld[78] < mod[78]
S += mld[78] < mud[78]
S += mod[78] < mud[78]
S += mod[78] < mdd[78]
S += mod[78] < mdd[79]
S += mud[78] < mdd[78]
S += mrd[78] < mdd[78]
S += mdd[78] < mld[79]
S += mdd[78] < mrd[79]
S += mld[79] < mod[79]
S += mld[79] < mud[79]
S += mod[79] < mud[79]
S += mud[79] < mdd[79]
S += mrd[79] < mdd[79]
S += mdd[79] < sub[83]
S += mdd[79] <= add[93]
S += mld[80] < mod[80]
S += mld[80] < mud[80]
S += mod[80] < mud[80]
S += mod[80] < mdd[80]
S += mod[80] < mdd[81]
S += mud[80] < mdd[80]
S += mrd[80] < mdd[80]
S += mdd[80] < mld[81]
S += mdd[80] < mrd[81]
S += mld[81] < mod[81]
S += mld[81] < mud[81]
S += mod[81] < mud[81]
S += mud[81] < mdd[81]
S += mrd[81] < mdd[81]
S += mdd[81] < sub[83]
S += mdd[81] <= add[93]
S += mdd[81] < sub[84]
S += mld[82] < mod[82]
S += mld[82] < mud[82]
S += mod[82] < mud[82]
S += mod[82] < mdd[82]
S += mod[82] < mdd[83]
S += mud[82] < mdd[82]
S += mrd[82] < mdd[82]
S += mdd[82] < mld[83]
S += mdd[82] < mrd[83]
S += mld[83] < mod[83]
S += mld[83] < mud[83]
S += mod[83] < mud[83]
S += mud[83] < mdd[83]
S += mrd[83] < mdd[83]
S += mdd[83] < sub[85]
S += sub[83] < sub[84]
S += add[93] < sub[85]
S += sub[84] < sub[87]
S += sub[84] < sub[95]
S += sub[85] < sub[86]
S += sub[85] < sub[88]
S += sub[85] < sub[96]
S += add[94] < add[98]
S += add[95] < add[98]
S += add[96] < add[99]
S += add[97] < add[99]
S += sub[86] < sub[88]
S += sub[87] < sub[89]
S += sub[88] < add[101]
S += sub[89] < add[102]
S += mld[84] < mod[84]
S += mld[84] < mud[84]
S += mod[84] < mud[84]
S += mod[84] < mdd[84]
S += mod[84] < mdd[85]
S += mud[84] < mdd[84]
S += mrd[84] < mdd[84]
S += mdd[84] < mld[85]
S += mdd[84] < mrd[85]
S += mld[85] < mod[85]
S += mld[85] < mud[85]
S += mod[85] < mud[85]
S += mud[85] < mdd[85]
S += mrd[85] < mdd[85]
S += mdd[85] < sub[90]
S += mdd[85] <= add[100]
S += mld[86] < mod[86]
S += mld[86] < mud[86]
S += mod[86] < mud[86]
S += mod[86] < mdd[86]
S += mod[86] < mdd[87]
S += mud[86] < mdd[86]
S += mrd[86] < mdd[86]
S += mdd[86] < mld[87]
S += mdd[86] < mrd[87]
S += mld[87] < mod[87]
S += mld[87] < mud[87]
S += mod[87] < mud[87]
S += mud[87] < mdd[87]
S += mrd[87] < mdd[87]
S += mdd[87] < sub[90]
S += mdd[87] <= add[100]
S += mdd[87] < sub[91]
S += mld[88] < mod[88]
S += mld[88] < mud[88]
S += mod[88] < mud[88]
S += mod[88] < mdd[88]
S += mod[88] < mdd[89]
S += mud[88] < mdd[88]
S += mrd[88] < mdd[88]
S += mdd[88] < mld[89]
S += mdd[88] < mrd[89]
S += mld[89] < mod[89]
S += mld[89] < mud[89]
S += mod[89] < mud[89]
S += mud[89] < mdd[89]
S += mrd[89] < mdd[89]
S += mdd[89] < sub[92]
S += sub[90] < sub[91]
S += add[100] < sub[92]
S += sub[91] < sub[93]
S += sub[92] < sub[94]
S += sub[93] < sub[95]
S += sub[94] < sub[96]
S += sub[95] < sub[103]
S += sub[96] < sub[104]
S += add[101] < sub[101]
S += add[102] < sub[102]
S += add[107] < sub[97]
S += add[108] < sub[98]
S += add[109] < sub[99]
S += add[110] < sub[100]
S += sub[97] < add[126]
S += sub[98] < add[127]
S += sub[99] < add[128]
S += sub[100] < add[129]
S += sub[101] < sub[105]
S += sub[102] < sub[106]
S += sub[103] < sub[107]
S += sub[104] < sub[108]
S += sub[105] < add[126]
S += sub[106] < add[127]
S += sub[107] < add[128]
S += sub[108] < add[129]
S += mld[90] < mod[90]
S += mld[90] < mud[90]
S += mod[90] < mud[90]
S += mod[90] < mdd[90]
S += mod[90] < mdd[91]
S += mud[90] < mdd[90]
S += mrd[90] < mdd[90]
S += mdd[90] < mld[91]
S += mdd[90] < mrd[91]
S += mld[91] < mod[91]
S += mld[91] < mud[91]
S += mod[91] < mud[91]
S += mud[91] < mdd[91]
S += mrd[91] < mdd[91]
S += mdd[91] < sub[109]
S += mdd[91] <= add[113]
S += mld[92] < mod[92]
S += mld[92] < mud[92]
S += mod[92] < mud[92]
S += mod[92] < mdd[92]
S += mod[92] < mdd[93]
S += mud[92] < mdd[92]
S += mrd[92] < mdd[92]
S += mdd[92] < mld[93]
S += mdd[92] < mrd[93]
S += mld[93] < mod[93]
S += mld[93] < mud[93]
S += mod[93] < mud[93]
S += mud[93] < mdd[93]
S += mrd[93] < mdd[93]
S += mdd[93] < sub[109]
S += mdd[93] <= add[113]
S += mdd[93] < sub[110]
S += mld[94] < mod[94]
S += mld[94] < mud[94]
S += mod[94] < mud[94]
S += mod[94] < mdd[94]
S += mod[94] < mdd[95]
S += mud[94] < mdd[94]
S += mrd[94] < mdd[94]
S += mdd[94] < mld[95]
S += mdd[94] < mrd[95]
S += mld[95] < mod[95]
S += mld[95] < mud[95]
S += mod[95] < mud[95]
S += mud[95] < mdd[95]
S += mrd[95] < mdd[95]
S += mdd[95] < sub[111]
S += sub[109] < sub[110]
S += add[113] < sub[111]
S += sub[110] < sub[122]
S += sub[110] < add[124]
S += sub[111] < sub[123]
S += sub[111] < add[125]
S += mld[96] < mod[96]
S += mld[96] < mud[96]
S += mod[96] < mud[96]
S += mod[96] < mdd[96]
S += mod[96] < mdd[97]
S += mud[96] < mdd[96]
S += mrd[96] < mdd[96]
S += mdd[96] < mld[97]
S += mdd[96] < mrd[97]
S += mld[97] < mod[97]
S += mld[97] < mud[97]
S += mod[97] < mud[97]
S += mud[97] < mdd[97]
S += mrd[97] < mdd[97]
S += mdd[97] < sub[112]
S += mdd[97] <= add[116]
S += mld[98] < mod[98]
S += mld[98] < mud[98]
S += mod[98] < mud[98]
S += mod[98] < mdd[98]
S += mod[98] < mdd[99]
S += mud[98] < mdd[98]
S += mrd[98] < mdd[98]
S += mdd[98] < mld[99]
S += mdd[98] < mrd[99]
S += mld[99] < mod[99]
S += mld[99] < mud[99]
S += mod[99] < mud[99]
S += mud[99] < mdd[99]
S += mrd[99] < mdd[99]
S += mdd[99] < sub[112]
S += mdd[99] <= add[116]
S += mdd[99] < sub[113]
S += mld[100] < mod[100]
S += mld[100] < mud[100]
S += mod[100] < mud[100]
S += mod[100] < mdd[100]
S += mod[100] < mdd[101]
S += mud[100] < mdd[100]
S += mrd[100] < mdd[100]
S += mdd[100] < mld[101]
S += mdd[100] < mrd[101]
S += mld[101] < mod[101]
S += mld[101] < mud[101]
S += mod[101] < mud[101]
S += mud[101] < mdd[101]
S += mrd[101] < mdd[101]
S += mdd[101] < sub[114]
S += sub[112] < sub[113]
S += add[116] < sub[114]
S += sub[113] < sub[116]
S += sub[113] < sub[124]
S += sub[114] < sub[115]
S += sub[114] < sub[117]
S += sub[114] < sub[125]
S += add[117] < add[121]
S += add[118] < add[121]
S += add[119] < add[122]
S += add[120] < add[122]
S += sub[115] < sub[117]
S += sub[116] < sub[118]
S += sub[117] < add[124]
S += sub[118] < add[125]
S += mld[102] < mod[102]
S += mld[102] < mud[102]
S += mod[102] < mud[102]
S += mod[102] < mdd[102]
S += mod[102] < mdd[103]
S += mud[102] < mdd[102]
S += mrd[102] < mdd[102]
S += mdd[102] < mld[103]
S += mdd[102] < mrd[103]
S += mld[103] < mod[103]
S += mld[103] < mud[103]
S += mod[103] < mud[103]
S += mud[103] < mdd[103]
S += mrd[103] < mdd[103]
S += mdd[103] < sub[119]
S += mdd[103] <= add[123]
S += mld[104] < mod[104]
S += mld[104] < mud[104]
S += mod[104] < mud[104]
S += mod[104] < mdd[104]
S += mod[104] < mdd[105]
S += mud[104] < mdd[104]
S += mrd[104] < mdd[104]
S += mdd[104] < mld[105]
S += mdd[104] < mrd[105]
S += mld[105] < mod[105]
S += mld[105] < mud[105]
S += mod[105] < mud[105]
S += mud[105] < mdd[105]
S += mrd[105] < mdd[105]
S += mdd[105] < sub[119]
S += mdd[105] <= add[123]
S += mdd[105] < sub[120]
S += mld[106] < mod[106]
S += mld[106] < mud[106]
S += mod[106] < mud[106]
S += mod[106] < mdd[106]
S += mod[106] < mdd[107]
S += mud[106] < mdd[106]
S += mrd[106] < mdd[106]
S += mdd[106] < mld[107]
S += mdd[106] < mrd[107]
S += mld[107] < mod[107]
S += mld[107] < mud[107]
S += mod[107] < mud[107]
S += mud[107] < mdd[107]
S += mrd[107] < mdd[107]
S += mdd[107] < sub[121]
S += sub[119] < sub[120]
S += add[123] < sub[121]
S += sub[120] < sub[122]
S += sub[121] < sub[123]
S += sub[122] < sub[124]
S += sub[123] < sub[125]
S += sub[124] < sub[128]
S += sub[125] < sub[129]
S += add[124] < sub[126]
S += add[125] < sub[127]
S += sub[126] < sub[130]
S += sub[127] < sub[131]
S += sub[128] < sub[132]
S += sub[129] < sub[133]
S += sub[130] < add[130]
S += sub[131] < add[131]
S += sub[132] < add[132]
S += sub[133] < add[133]


'''
with open('2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        exec(line.strip())
'''
#solvers.mip.solve(S,msg=True)
#result = solvers.mip.solve(S,msg=1)
result = solvers.cpoptimizer.solve(S,msg=1)

list1 = S.solution()

schedule = {op: (start_time, end_time) for op, _, start_time, end_time in list1}

'''
for key, value in schedule.items():
    print(f"'{key}',")
'''
#打印指令调度
print (list1)


adjusted_schedule = {str(op): list(times) for op, times in schedule.items()}

dependencies = [
('mld0','mod0'),
('mld0','mud0'),
('mod0','mud0'),
('mod0','mdd0'),
('mod0','mdd1'),
('mud0','mdd0'),
('mrd0','mdd0'),
('mdd0','mld1'),
('mdd0','mrd1'),
('mld1','mod1'),
('mld1','mud1'),
('mod1','mud1'),
('mud1','mdd1'),
('mrd1','mdd1'),
('mdd1','sub0'),
('mdd1','add2'),
('mld2','mod2'),
('mld2','mud2'),
('mod2','mud2'),
('mod2','mdd2'),
('mod2','mdd3'),
('mud2','mdd2'),
('mrd2','mdd2'),
('mdd2','mld3'),
('mdd2','mrd3'),
('mld3','mod3'),
('mld3','mud3'),
('mod3','mud3'),
('mud3','mdd3'),
('mrd3','mdd3'),
('mdd3','sub0'),
('mdd3','add2'),
('mdd3','sub1'),
('mld4','mod4'),
('mld4','mud4'),
('mod4','mud4'),
('mod4','mdd4'),
('mod4','mdd5'),
('mud4','mdd4'),
('mrd4','mdd4'),
('mdd4','mld5'),
('mdd4','mrd5'),
('mld5','mod5'),
('mld5','mud5'),
('mod5','mud5'),
('mud5','mdd5'),
('mrd5','mdd5'),
('mdd5','sub2'),
('sub0','sub1'),
('add2','sub2'),
('sub1','sub13'),
('sub1','add13'),
('sub2','sub14'),
('sub2','add14'),
('mld6','mod6'),
('mld6','mud6'),
('mod6','mud6'),
('mod6','mdd6'),
('mod6','mdd7'),
('mud6','mdd6'),
('mrd6','mdd6'),
('mdd6','mld7'),
('mdd6','mrd7'),
('mld7','mod7'),
('mld7','mud7'),
('mod7','mud7'),
('mud7','mdd7'),
('mrd7','mdd7'),
('mdd7','sub3'),
('mdd7','add5'),
('mld8','mod8'),
('mld8','mud8'),
('mod8','mud8'),
('mod8','mdd8'),
('mod8','mdd9'),
('mud8','mdd8'),
('mrd8','mdd8'),
('mdd8','mld9'),
('mdd8','mrd9'),
('mld9','mod9'),
('mld9','mud9'),
('mod9','mud9'),
('mud9','mdd9'),
('mrd9','mdd9'),
('mdd9','sub3'),
('mdd9','add5'),
('mdd9','sub4'),
('mld10','mod10'),
('mld10','mud10'),
('mod10','mud10'),
('mod10','mdd10'),
('mod10','mdd11'),
('mud10','mdd10'),
('mrd10','mdd10'),
('mdd10','mld11'),
('mdd10','mrd11'),
('mld11','mod11'),
('mld11','mud11'),
('mod11','mud11'),
('mud11','mdd11'),
('mrd11','mdd11'),
('mdd11','sub5'),
('sub3','sub4'),
('add5','sub5'),
('sub4','sub7'),
('sub4','sub15'),
('sub5','sub6'),
('sub5','sub8'),
('sub5','sub16'),
('add6','add10'),
('add7','add10'),
('add8','add11'),
('add9','add11'),
('sub6','sub8'),
('sub7','sub9'),
('sub8','add13'),
('sub9','add14'),
('mld12','mod12'),
('mld12','mud12'),
('mod12','mud12'),
('mod12','mdd12'),
('mod12','mdd13'),
('mud12','mdd12'),
('mrd12','mdd12'),
('mdd12','mld13'),
('mdd12','mrd13'),
('mld13','mod13'),
('mld13','mud13'),
('mod13','mud13'),
('mud13','mdd13'),
('mrd13','mdd13'),
('mdd13','sub10'),
('mdd13','add12'),
('mld14','mod14'),
('mld14','mud14'),
('mod14','mud14'),
('mod14','mdd14'),
('mod14','mdd15'),
('mud14','mdd14'),
('mrd14','mdd14'),
('mdd14','mld15'),
('mdd14','mrd15'),
('mld15','mod15'),
('mld15','mud15'),
('mod15','mud15'),
('mud15','mdd15'),
('mrd15','mdd15'),
('mdd15','sub10'),
('mdd15','add12'),
('mdd15','sub11'),
('mld16','mod16'),
('mld16','mud16'),
('mod16','mud16'),
('mod16','mdd16'),
('mod16','mdd17'),
('mud16','mdd16'),
('mrd16','mdd16'),
('mdd16','mld17'),
('mdd16','mrd17'),
('mld17','mod17'),
('mld17','mud17'),
('mod17','mud17'),
('mud17','mdd17'),
('mrd17','mdd17'),
('mdd17','sub12'),
('sub10','sub11'),
('add12','sub12'),
('sub11','sub13'),
('sub12','sub14'),
('sub13','sub15'),
('sub14','sub16'),
('sub15','sub70'),
('sub15','sub98'),
('sub15','sub128'),
('sub16','sub71'),
('sub16','add107'),
('sub16','sub129'),
('add13','sub68'),
('add13','sub99'),
('add13','sub126'),
('add14','sub69'),
('add14','sub100'),
('add14','sub127'),
('add15','add46'),
('add15','add52'),
('add16','add46'),
('add16','add53'),
('add17','add49'),
('add17','add52'),
('add18','add49'),
('add18','add53'),
('add19','add47'),
('add19','add54'),
('add20','add47'),
('add20','add55'),
('add21','add50'),
('add21','add54'),
('add22','add50'),
('add22','add55'),
('mld18','mod18'),
('mld18','mud18'),
('mod18','mud18'),
('mod18','mdd18'),
('mod18','mdd19'),
('mud18','mdd18'),
('mrd18','mdd18'),
('mdd18','mld19'),
('mdd18','mrd19'),
('mld19','mod19'),
('mld19','mud19'),
('mod19','mud19'),
('mud19','mdd19'),
('mrd19','mdd19'),
('mdd19','sub17'),
('mdd19','add25'),
('mld20','mod20'),
('mld20','mud20'),
('mod20','mud20'),
('mod20','mdd20'),
('mod20','mdd21'),
('mud20','mdd20'),
('mrd20','mdd20'),
('mdd20','mld21'),
('mdd20','mrd21'),
('mld21','mod21'),
('mld21','mud21'),
('mod21','mud21'),
('mud21','mdd21'),
('mrd21','mdd21'),
('mdd21','sub17'),
('mdd21','add25'),
('mdd21','sub18'),
('mld22','mod22'),
('mld22','mud22'),
('mod22','mud22'),
('mod22','mdd22'),
('mod22','mdd23'),
('mud22','mdd22'),
('mrd22','mdd22'),
('mdd22','mld23'),
('mdd22','mrd23'),
('mld23','mod23'),
('mld23','mud23'),
('mod23','mud23'),
('mud23','mdd23'),
('mrd23','mdd23'),
('mdd23','sub19'),
('sub17','sub18'),
('add25','sub19'),
('sub18','sub30'),
('sub18','add36'),
('sub19','sub31'),
('sub19','add37'),
('mld24','mod24'),
('mld24','mud24'),
('mod24','mud24'),
('mod24','mdd24'),
('mod24','mdd25'),
('mud24','mdd24'),
('mrd24','mdd24'),
('mdd24','mld25'),
('mdd24','mrd25'),
('mld25','mod25'),
('mld25','mud25'),
('mod25','mud25'),
('mud25','mdd25'),
('mrd25','mdd25'),
('mdd25','sub20'),
('mdd25','add28'),
('mld26','mod26'),
('mld26','mud26'),
('mod26','mud26'),
('mod26','mdd26'),
('mod26','mdd27'),
('mud26','mdd26'),
('mrd26','mdd26'),
('mdd26','mld27'),
('mdd26','mrd27'),
('mld27','mod27'),
('mld27','mud27'),
('mod27','mud27'),
('mud27','mdd27'),
('mrd27','mdd27'),
('mdd27','sub20'),
('mdd27','add28'),
('mdd27','sub21'),
('mld28','mod28'),
('mld28','mud28'),
('mod28','mud28'),
('mod28','mdd28'),
('mod28','mdd29'),
('mud28','mdd28'),
('mrd28','mdd28'),
('mdd28','mld29'),
('mdd28','mrd29'),
('mld29','mod29'),
('mld29','mud29'),
('mod29','mud29'),
('mud29','mdd29'),
('mrd29','mdd29'),
('mdd29','sub22'),
('sub20','sub21'),
('add28','sub22'),
('sub21','sub24'),
('sub21','sub32'),
('sub22','sub23'),
('sub22','sub25'),
('sub22','sub33'),
('add29','add33'),
('add30','add33'),
('add31','add34'),
('add32','add34'),
('sub23','sub25'),
('sub24','sub26'),
('sub25','add36'),
('sub26','add37'),
('mld30','mod30'),
('mld30','mud30'),
('mod30','mud30'),
('mod30','mdd30'),
('mod30','mdd31'),
('mud30','mdd30'),
('mrd30','mdd30'),
('mdd30','mld31'),
('mdd30','mrd31'),
('mld31','mod31'),
('mld31','mud31'),
('mod31','mud31'),
('mud31','mdd31'),
('mrd31','mdd31'),
('mdd31','sub27'),
('mdd31','add35'),
('mld32','mod32'),
('mld32','mud32'),
('mod32','mud32'),
('mod32','mdd32'),
('mod32','mdd33'),
('mud32','mdd32'),
('mrd32','mdd32'),
('mdd32','mld33'),
('mdd32','mrd33'),
('mld33','mod33'),
('mld33','mud33'),
('mod33','mud33'),
('mud33','mdd33'),
('mrd33','mdd33'),
('mdd33','sub27'),
('mdd33','add35'),
('mdd33','sub28'),
('mld34','mod34'),
('mld34','mud34'),
('mod34','mud34'),
('mod34','mdd34'),
('mod34','mdd35'),
('mud34','mdd34'),
('mrd34','mdd34'),
('mdd34','mld35'),
('mdd34','mrd35'),
('mld35','mod35'),
('mld35','mud35'),
('mod35','mud35'),
('mud35','mdd35'),
('mrd35','mdd35'),
('mdd35','sub29'),
('sub27','sub28'),
('add35','sub29'),
('sub28','sub30'),
('sub29','sub31'),
('sub30','sub32'),
('sub31','sub33'),
('sub32','sub74'),
('sub32','sub103'),
('sub32','add132'),
('sub33','sub75'),
('sub33','sub104'),
('sub33','add133'),
('add36','sub72'),
('add36','sub101'),
('add36','add130'),
('add37','sub73'),
('add37','sub102'),
('add37','add131'),
('add38','add111'),
('add38','add117'),
('add39','add111'),
('add39','add118'),
('add40','add114'),
('add40','add117'),
('add41','add114'),
('add41','add118'),
('add42','add112'),
('add42','add119'),
('add43','add112'),
('add43','add120'),
('add44','add115'),
('add44','add119'),
('add45','add115'),
('add45','add120'),
('mld36','mod36'),
('mld36','mud36'),
('mod36','mud36'),
('mod36','mdd36'),
('mod36','mdd37'),
('mud36','mdd36'),
('mrd36','mdd36'),
('mdd36','mld37'),
('mdd36','mrd37'),
('mld37','mod37'),
('mld37','mud37'),
('mod37','mud37'),
('mud37','mdd37'),
('mrd37','mdd37'),
('mdd37','sub34'),
('mdd37','add48'),
('mld38','mod38'),
('mld38','mud38'),
('mod38','mud38'),
('mod38','mdd38'),
('mod38','mdd39'),
('mud38','mdd38'),
('mrd38','mdd38'),
('mdd38','mld39'),
('mdd38','mrd39'),
('mld39','mod39'),
('mld39','mud39'),
('mod39','mud39'),
('mud39','mdd39'),
('mrd39','mdd39'),
('mdd39','sub34'),
('mdd39','add48'),
('mdd39','sub35'),
('mld40','mod40'),
('mld40','mud40'),
('mod40','mud40'),
('mod40','mdd40'),
('mod40','mdd41'),
('mud40','mdd40'),
('mrd40','mdd40'),
('mdd40','mld41'),
('mdd40','mrd41'),
('mld41','mod41'),
('mld41','mud41'),
('mod41','mud41'),
('mud41','mdd41'),
('mrd41','mdd41'),
('mdd41','sub36'),
('sub34','sub35'),
('add48','sub36'),
('sub35','sub47'),
('sub35','add59'),
('sub36','sub48'),
('sub36','add60'),
('mld42','mod42'),
('mld42','mud42'),
('mod42','mud42'),
('mod42','mdd42'),
('mod42','mdd43'),
('mud42','mdd42'),
('mrd42','mdd42'),
('mdd42','mld43'),
('mdd42','mrd43'),
('mld43','mod43'),
('mld43','mud43'),
('mod43','mud43'),
('mud43','mdd43'),
('mrd43','mdd43'),
('mdd43','sub37'),
('mdd43','add51'),
('mld44','mod44'),
('mld44','mud44'),
('mod44','mud44'),
('mod44','mdd44'),
('mod44','mdd45'),
('mud44','mdd44'),
('mrd44','mdd44'),
('mdd44','mld45'),
('mdd44','mrd45'),
('mld45','mod45'),
('mld45','mud45'),
('mod45','mud45'),
('mud45','mdd45'),
('mrd45','mdd45'),
('mdd45','sub37'),
('mdd45','add51'),
('mdd45','sub38'),
('mld46','mod46'),
('mld46','mud46'),
('mod46','mud46'),
('mod46','mdd46'),
('mod46','mdd47'),
('mud46','mdd46'),
('mrd46','mdd46'),
('mdd46','mld47'),
('mdd46','mrd47'),
('mld47','mod47'),
('mld47','mud47'),
('mod47','mud47'),
('mud47','mdd47'),
('mrd47','mdd47'),
('mdd47','sub39'),
('sub37','sub38'),
('add51','sub39'),
('sub38','sub41'),
('sub38','sub49'),
('sub39','sub40'),
('sub39','sub42'),
('sub39','sub50'),
('add52','add56'),
('add53','add56'),
('add54','add57'),
('add55','add57'),
('sub40','sub42'),
('sub41','sub43'),
('sub42','add59'),
('sub43','add60'),
('mld48','mod48'),
('mld48','mud48'),
('mod48','mud48'),
('mod48','mdd48'),
('mod48','mdd49'),
('mud48','mdd48'),
('mrd48','mdd48'),
('mdd48','mld49'),
('mdd48','mrd49'),
('mld49','mod49'),
('mld49','mud49'),
('mod49','mud49'),
('mud49','mdd49'),
('mrd49','mdd49'),
('mdd49','sub44'),
('mdd49','add58'),
('mld50','mod50'),
('mld50','mud50'),
('mod50','mud50'),
('mod50','mdd50'),
('mod50','mdd51'),
('mud50','mdd50'),
('mrd50','mdd50'),
('mdd50','mld51'),
('mdd50','mrd51'),
('mld51','mod51'),
('mld51','mud51'),
('mod51','mud51'),
('mud51','mdd51'),
('mrd51','mdd51'),
('mdd51','sub44'),
('mdd51','add58'),
('mdd51','sub45'),
('mld52','mod52'),
('mld52','mud52'),
('mod52','mud52'),
('mod52','mdd52'),
('mod52','mdd53'),
('mud52','mdd52'),
('mrd52','mdd52'),
('mdd52','mld53'),
('mdd52','mrd53'),
('mld53','mod53'),
('mld53','mud53'),
('mod53','mud53'),
('mud53','mdd53'),
('mrd53','mdd53'),
('mdd53','sub46'),
('sub44','sub45'),
('add58','sub46'),
('sub45','sub47'),
('sub46','sub48'),
('sub47','sub49'),
('sub48','sub50'),
('sub49','sub70'),
('sub50','sub71'),
('add59','sub68'),
('add60','sub69'),
('add61','add88'),
('add61','add94'),
('add62','add88'),
('add62','add95'),
('add63','add91'),
('add63','add94'),
('add64','add91'),
('add64','add95'),
('add65','add89'),
('add65','add96'),
('add66','add89'),
('add66','add97'),
('add67','add92'),
('add67','add96'),
('add68','add92'),
('add68','add97'),
('mld54','mod54'),
('mld54','mud54'),
('mod54','mud54'),
('mod54','mdd54'),
('mod54','mdd55'),
('mud54','mdd54'),
('mrd54','mdd54'),
('mdd54','mld55'),
('mdd54','mrd55'),
('mld55','mod55'),
('mld55','mud55'),
('mod55','mud55'),
('mud55','mdd55'),
('mrd55','mdd55'),
('mdd55','sub51'),
('mdd55','add71'),
('mld56','mod56'),
('mld56','mud56'),
('mod56','mud56'),
('mod56','mdd56'),
('mod56','mdd57'),
('mud56','mdd56'),
('mrd56','mdd56'),
('mdd56','mld57'),
('mdd56','mrd57'),
('mld57','mod57'),
('mld57','mud57'),
('mod57','mud57'),
('mud57','mdd57'),
('mrd57','mdd57'),
('mdd57','sub51'),
('mdd57','add71'),
('mdd57','sub52'),
('mld58','mod58'),
('mld58','mud58'),
('mod58','mud58'),
('mod58','mdd58'),
('mod58','mdd59'),
('mud58','mdd58'),
('mrd58','mdd58'),
('mdd58','mld59'),
('mdd58','mrd59'),
('mld59','mod59'),
('mld59','mud59'),
('mod59','mud59'),
('mud59','mdd59'),
('mrd59','mdd59'),
('mdd59','sub53'),
('sub51','sub52'),
('add71','sub53'),
('sub52','sub64'),
('sub52','add82'),
('sub53','sub65'),
('sub53','add83'),
('mld60','mod60'),
('mld60','mud60'),
('mod60','mud60'),
('mod60','mdd60'),
('mod60','mdd61'),
('mud60','mdd60'),
('mrd60','mdd60'),
('mdd60','mld61'),
('mdd60','mrd61'),
('mld61','mod61'),
('mld61','mud61'),
('mod61','mud61'),
('mud61','mdd61'),
('mrd61','mdd61'),
('mdd61','sub54'),
('mdd61','add74'),
('mld62','mod62'),
('mld62','mud62'),
('mod62','mud62'),
('mod62','mdd62'),
('mod62','mdd63'),
('mud62','mdd62'),
('mrd62','mdd62'),
('mdd62','mld63'),
('mdd62','mrd63'),
('mld63','mod63'),
('mld63','mud63'),
('mod63','mud63'),
('mud63','mdd63'),
('mrd63','mdd63'),
('mdd63','sub54'),
('mdd63','add74'),
('mdd63','sub55'),
('mld64','mod64'),
('mld64','mud64'),
('mod64','mud64'),
('mod64','mdd64'),
('mod64','mdd65'),
('mud64','mdd64'),
('mrd64','mdd64'),
('mdd64','mld65'),
('mdd64','mrd65'),
('mld65','mod65'),
('mld65','mud65'),
('mod65','mud65'),
('mud65','mdd65'),
('mrd65','mdd65'),
('mdd65','sub56'),
('sub54','sub55'),
('add74','sub56'),
('sub55','sub58'),
('sub55','sub66'),
('sub56','sub57'),
('sub56','sub59'),
('sub56','sub67'),
('add75','add79'),
('add76','add79'),
('add77','add80'),
('add78','add80'),
('sub57','sub59'),
('sub58','sub60'),
('sub59','add82'),
('sub60','add83'),
('mld66','mod66'),
('mld66','mud66'),
('mod66','mud66'),
('mod66','mdd66'),
('mod66','mdd67'),
('mud66','mdd66'),
('mrd66','mdd66'),
('mdd66','mld67'),
('mdd66','mrd67'),
('mld67','mod67'),
('mld67','mud67'),
('mod67','mud67'),
('mud67','mdd67'),
('mrd67','mdd67'),
('mdd67','sub61'),
('mdd67','add81'),
('mld68','mod68'),
('mld68','mud68'),
('mod68','mud68'),
('mod68','mdd68'),
('mod68','mdd69'),
('mud68','mdd68'),
('mrd68','mdd68'),
('mdd68','mld69'),
('mdd68','mrd69'),
('mld69','mod69'),
('mld69','mud69'),
('mod69','mud69'),
('mud69','mdd69'),
('mrd69','mdd69'),
('mdd69','sub61'),
('mdd69','add81'),
('mdd69','sub62'),
('mld70','mod70'),
('mld70','mud70'),
('mod70','mud70'),
('mod70','mdd70'),
('mod70','mdd71'),
('mud70','mdd70'),
('mrd70','mdd70'),
('mdd70','mld71'),
('mdd70','mrd71'),
('mld71','mod71'),
('mld71','mud71'),
('mod71','mud71'),
('mud71','mdd71'),
('mrd71','mdd71'),
('mdd71','sub63'),
('sub61','sub62'),
('add81','sub63'),
('sub62','sub64'),
('sub63','sub65'),
('sub64','sub66'),
('sub65','sub67'),
('sub66','add105'),
('sub66','sub107'),
('sub66','sub132'),
('sub67','add106'),
('sub67','sub108'),
('sub67','sub133'),
('add82','add103'),
('add82','sub105'),
('add82','sub130'),
('add83','add104'),
('add83','sub106'),
('add83','sub131'),
('sub68','sub72'),
('sub69','sub73'),
('sub70','sub74'),
('sub71','sub75'),
('sub72','sub78'),
('sub73','sub79'),
('sub74','sub77'),
('sub75','add84'),
('add84','sub76'),
('add85','sub77'),
('add86','sub78'),
('add87','sub79'),
('sub76','add103'),
('sub77','add104'),
('sub78','add105'),
('sub79','add106'),
('mld72','mod72'),
('mld72','mud72'),
('mod72','mud72'),
('mod72','mdd72'),
('mod72','mdd73'),
('mud72','mdd72'),
('mrd72','mdd72'),
('mdd72','mld73'),
('mdd72','mrd73'),
('mld73','mod73'),
('mld73','mud73'),
('mod73','mud73'),
('mud73','mdd73'),
('mrd73','mdd73'),
('mdd73','sub80'),
('mdd73','add90'),
('mld74','mod74'),
('mld74','mud74'),
('mod74','mud74'),
('mod74','mdd74'),
('mod74','mdd75'),
('mud74','mdd74'),
('mrd74','mdd74'),
('mdd74','mld75'),
('mdd74','mrd75'),
('mld75','mod75'),
('mld75','mud75'),
('mod75','mud75'),
('mud75','mdd75'),
('mrd75','mdd75'),
('mdd75','sub80'),
('mdd75','add90'),
('mdd75','sub81'),
('mld76','mod76'),
('mld76','mud76'),
('mod76','mud76'),
('mod76','mdd76'),
('mod76','mdd77'),
('mud76','mdd76'),
('mrd76','mdd76'),
('mdd76','mld77'),
('mdd76','mrd77'),
('mld77','mod77'),
('mld77','mud77'),
('mod77','mud77'),
('mud77','mdd77'),
('mrd77','mdd77'),
('mdd77','sub82'),
('sub80','sub81'),
('add90','sub82'),
('sub81','sub93'),
('sub81','add101'),
('sub82','sub94'),
('sub82','add102'),
('mld78','mod78'),
('mld78','mud78'),
('mod78','mud78'),
('mod78','mdd78'),
('mod78','mdd79'),
('mud78','mdd78'),
('mrd78','mdd78'),
('mdd78','mld79'),
('mdd78','mrd79'),
('mld79','mod79'),
('mld79','mud79'),
('mod79','mud79'),
('mud79','mdd79'),
('mrd79','mdd79'),
('mdd79','sub83'),
('mdd79','add93'),
('mld80','mod80'),
('mld80','mud80'),
('mod80','mud80'),
('mod80','mdd80'),
('mod80','mdd81'),
('mud80','mdd80'),
('mrd80','mdd80'),
('mdd80','mld81'),
('mdd80','mrd81'),
('mld81','mod81'),
('mld81','mud81'),
('mod81','mud81'),
('mud81','mdd81'),
('mrd81','mdd81'),
('mdd81','sub83'),
('mdd81','add93'),
('mdd81','sub84'),
('mld82','mod82'),
('mld82','mud82'),
('mod82','mud82'),
('mod82','mdd82'),
('mod82','mdd83'),
('mud82','mdd82'),
('mrd82','mdd82'),
('mdd82','mld83'),
('mdd82','mrd83'),
('mld83','mod83'),
('mld83','mud83'),
('mod83','mud83'),
('mud83','mdd83'),
('mrd83','mdd83'),
('mdd83','sub85'),
('sub83','sub84'),
('add93','sub85'),
('sub84','sub87'),
('sub84','sub95'),
('sub85','sub86'),
('sub85','sub88'),
('sub85','sub96'),
('add94','add98'),
('add95','add98'),
('add96','add99'),
('add97','add99'),
('sub86','sub88'),
('sub87','sub89'),
('sub88','add101'),
('sub89','add102'),
('mld84','mod84'),
('mld84','mud84'),
('mod84','mud84'),
('mod84','mdd84'),
('mod84','mdd85'),
('mud84','mdd84'),
('mrd84','mdd84'),
('mdd84','mld85'),
('mdd84','mrd85'),
('mld85','mod85'),
('mld85','mud85'),
('mod85','mud85'),
('mud85','mdd85'),
('mrd85','mdd85'),
('mdd85','sub90'),
('mdd85','add100'),
('mld86','mod86'),
('mld86','mud86'),
('mod86','mud86'),
('mod86','mdd86'),
('mod86','mdd87'),
('mud86','mdd86'),
('mrd86','mdd86'),
('mdd86','mld87'),
('mdd86','mrd87'),
('mld87','mod87'),
('mld87','mud87'),
('mod87','mud87'),
('mud87','mdd87'),
('mrd87','mdd87'),
('mdd87','sub90'),
('mdd87','add100'),
('mdd87','sub91'),
('mld88','mod88'),
('mld88','mud88'),
('mod88','mud88'),
('mod88','mdd88'),
('mod88','mdd89'),
('mud88','mdd88'),
('mrd88','mdd88'),
('mdd88','mld89'),
('mdd88','mrd89'),
('mld89','mod89'),
('mld89','mud89'),
('mod89','mud89'),
('mud89','mdd89'),
('mrd89','mdd89'),
('mdd89','sub92'),
('sub90','sub91'),
('add100','sub92'),
('sub91','sub93'),
('sub92','sub94'),
('sub93','sub95'),
('sub94','sub96'),
('sub95','sub103'),
('sub96','sub104'),
('add101','sub101'),
('add102','sub102'),
('add107','sub97'),
('add108','sub98'),
('add109','sub99'),
('add110','sub100'),
('sub97','add126'),
('sub98','add127'),
('sub99','add128'),
('sub100','add129'),
('sub101','sub105'),
('sub102','sub106'),
('sub103','sub107'),
('sub104','sub108'),
('sub105','add126'),
('sub106','add127'),
('sub107','add128'),
('sub108','add129'),
('mld90','mod90'),
('mld90','mud90'),
('mod90','mud90'),
('mod90','mdd90'),
('mod90','mdd91'),
('mud90','mdd90'),
('mrd90','mdd90'),
('mdd90','mld91'),
('mdd90','mrd91'),
('mld91','mod91'),
('mld91','mud91'),
('mod91','mud91'),
('mud91','mdd91'),
('mrd91','mdd91'),
('mdd91','sub109'),
('mdd91','add113'),
('mld92','mod92'),
('mld92','mud92'),
('mod92','mud92'),
('mod92','mdd92'),
('mod92','mdd93'),
('mud92','mdd92'),
('mrd92','mdd92'),
('mdd92','mld93'),
('mdd92','mrd93'),
('mld93','mod93'),
('mld93','mud93'),
('mod93','mud93'),
('mud93','mdd93'),
('mrd93','mdd93'),
('mdd93','sub109'),
('mdd93','add113'),
('mdd93','sub110'),
('mld94','mod94'),
('mld94','mud94'),
('mod94','mud94'),
('mod94','mdd94'),
('mod94','mdd95'),
('mud94','mdd94'),
('mrd94','mdd94'),
('mdd94','mld95'),
('mdd94','mrd95'),
('mld95','mod95'),
('mld95','mud95'),
('mod95','mud95'),
('mud95','mdd95'),
('mrd95','mdd95'),
('mdd95','sub111'),
('sub109','sub110'),
('add113','sub111'),
('sub110','sub122'),
('sub110','add124'),
('sub111','sub123'),
('sub111','add125'),
('mld96','mod96'),
('mld96','mud96'),
('mod96','mud96'),
('mod96','mdd96'),
('mod96','mdd97'),
('mud96','mdd96'),
('mrd96','mdd96'),
('mdd96','mld97'),
('mdd96','mrd97'),
('mld97','mod97'),
('mld97','mud97'),
('mod97','mud97'),
('mud97','mdd97'),
('mrd97','mdd97'),
('mdd97','sub112'),
('mdd97','add116'),
('mld98','mod98'),
('mld98','mud98'),
('mod98','mud98'),
('mod98','mdd98'),
('mod98','mdd99'),
('mud98','mdd98'),
('mrd98','mdd98'),
('mdd98','mld99'),
('mdd98','mrd99'),
('mld99','mod99'),
('mld99','mud99'),
('mod99','mud99'),
('mud99','mdd99'),
('mrd99','mdd99'),
('mdd99','sub112'),
('mdd99','add116'),
('mdd99','sub113'),
('mld100','mod100'),
('mld100','mud100'),
('mod100','mud100'),
('mod100','mdd100'),
('mod100','mdd101'),
('mud100','mdd100'),
('mrd100','mdd100'),
('mdd100','mld101'),
('mdd100','mrd101'),
('mld101','mod101'),
('mld101','mud101'),
('mod101','mud101'),
('mud101','mdd101'),
('mrd101','mdd101'),
('mdd101','sub114'),
('sub112','sub113'),
('add116','sub114'),
('sub113','sub116'),
('sub113','sub124'),
('sub114','sub115'),
('sub114','sub117'),
('sub114','sub125'),
('add117','add121'),
('add118','add121'),
('add119','add122'),
('add120','add122'),
('sub115','sub117'),
('sub116','sub118'),
('sub117','add124'),
('sub118','add125'),
('mld102','mod102'),
('mld102','mud102'),
('mod102','mud102'),
('mod102','mdd102'),
('mod102','mdd103'),
('mud102','mdd102'),
('mrd102','mdd102'),
('mdd102','mld103'),
('mdd102','mrd103'),
('mld103','mod103'),
('mld103','mud103'),
('mod103','mud103'),
('mud103','mdd103'),
('mrd103','mdd103'),
('mdd103','sub119'),
('mdd103','add123'),
('mld104','mod104'),
('mld104','mud104'),
('mod104','mud104'),
('mod104','mdd104'),
('mod104','mdd105'),
('mud104','mdd104'),
('mrd104','mdd104'),
('mdd104','mld105'),
('mdd104','mrd105'),
('mld105','mod105'),
('mld105','mud105'),
('mod105','mud105'),
('mud105','mdd105'),
('mrd105','mdd105'),
('mdd105','sub119'),
('mdd105','add123'),
('mdd105','sub120'),
('mld106','mod106'),
('mld106','mud106'),
('mod106','mud106'),
('mod106','mdd106'),
('mod106','mdd107'),
('mud106','mdd106'),
('mrd106','mdd106'),
('mdd106','mld107'),
('mdd106','mrd107'),
('mld107','mod107'),
('mld107','mud107'),
('mod107','mud107'),
('mud107','mdd107'),
('mrd107','mdd107'),
('mdd107','sub121'),
('sub119','sub120'),
('add123','sub121'),
('sub120','sub122'),
('sub121','sub123'),
('sub122','sub124'),
('sub123','sub125'),
('sub124','sub128'),
('sub125','sub129'),
('add124','sub126'),
('add125','sub127'),
('sub126','sub130'),
('sub127','sub131'),
('sub128','sub132'),
('sub129','sub133'),
('sub130','add130'),
('sub131','add131'),
('sub132','add132'),
('sub133','add133')


]
for op1, op2 in dependencies:
	if op1 in adjusted_schedule and op2 in adjusted_schedule:
		if adjusted_schedule[op1][1] < adjusted_schedule[op2][0]:
				adjusted_schedule[op1][1] = adjusted_schedule[op2][0]
		else:
			adjusted_schedule[op1][1] = adjusted_schedule[op1][1]

max_registers = 300

def allocate_registers(adjusted_schedule):
    # 计算每个操作的生命周期
    lifetimes = {op: (times[0], times[1]) for op, times in adjusted_schedule.items()}

    # 使用图着色分配寄存器
    live_ranges = nx.Graph()
    for op1, lt1 in lifetimes.items():
        for op2, lt2 in lifetimes.items():
            if op1 != op2 and not (lt1[1] <= lt2[0] or lt2[1] <= lt1[0]):
                live_ranges.add_edge(op1, op2)

    # 用图着色算法求解寄存器分配
    colors = nx.coloring.greedy_color(live_ranges)
    return colors

def iterative_optimization(adjusted_schedule, max_registers):
    best_registers = None
    min_end_time = float('inf')

    for _ in range(2):  # 迭代次数
        # 使用现有的schedule
        # 分配寄存器
        registers = allocate_registers(adjusted_schedule)

        # 检查寄存器限制
        if max(registers.values()) < max_registers:
            # 计算结束时间
            end_time = max(times[1] for times in adjusted_schedule.values())

            # 更新最优解
            if end_time < min_end_time:
                min_end_time = end_time
                best_registers = registers

    return adjusted_schedule, best_registers

print("\nRegister Allocation:")
for op, reg in best_registers.items():
    # 获取当前操作的所有直接依赖项
    dependencies_for_op = [dep_op for dep_op, dep in dependencies if dep == op]
    dependencies_str = ', '.join(
        f"{dep_op} (reg {best_registers[dep_op]})" for dep_op in dependencies_for_op if dep_op in best_registers
    )
    print(f"{op}:reg{reg}={dependencies_str}")

######打印图形
#if solvers.mip.solve(S, msg=0):
if solvers.cpoptimizer.solve(S,msg=0):
	if ('--test','') in opts:
		assert(mud.start_value == 0)
		assert(mdd.start_value == 0)
		assert(add.start_value == 1)
		print('test passed')
	else:
		plotters.matplotlib.plot(S, fig_size=(40, 25),vertical_text = True)
else:
	print('no solution found')
	#assert(1==0)

