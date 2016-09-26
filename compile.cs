prog=ReadAlphabets("geodesics.ab");
system="geodesics";
outDir = "output/"+system;

Split(prog, system, "A", "A_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "B", "B_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "C", "C_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "D", "D_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "E", "E_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "F", "F_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "G", "G_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "H", "H_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "I", "I_split", "{i,j,t | i+j<=N-1}");
Split(prog, system, "J", "J_split", "{i,j,t | i+j<=N-1}");

Normalize(prog);

CoB(prog, system, "A", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "B_split", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "A", "(i,j,t->i,i+j+1,t)");
CoB(prog, system, "B_split", "(i,j,t->i,j-N+1+i,t)");
Merge(prog, system, "A", "B_split","Slice_0");
CoB(prog, system, "A_split", "(i,j,t->i,i+j,t)");
CoB(prog, system, "B", "(i,j,t->i,j-N+i,t)");
Merge(prog, system, "A_split", "B", "Slice_1");

CoB(prog, system, "C", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "D_split", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "C", "(i,j,t->i,i+j+1,t)");
CoB(prog, system, "D_split", "(i,j,t->i,j-N+1+i,t)");
Merge(prog, system, "C", "D_split","Slice_2");
CoB(prog, system, "C_split", "(i,j,t->i,i+j,t)");
CoB(prog, system, "D", "(i,j,t->i,j-N+i,t)");
Merge(prog, system, "C_split", "D", "Slice_3");

CoB(prog, system, "E", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "F_split", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "E", "(i,j,t->i,i+j+1,t)");
CoB(prog, system, "F_split", "(i,j,t->i,j-N+1+i,t)");
Merge(prog, system, "E", "F_split","Slice_4");
CoB(prog, system, "E_split", "(i,j,t->i,i+j,t)");
CoB(prog, system, "F", "(i,j,t->i,j-N+i,t)");
Merge(prog, system, "E_split", "F", "Slice_5");

CoB(prog, system, "G", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "H_split", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "G", "(i,j,t->i,i+j+1,t)");
CoB(prog, system, "H_split", "(i,j,t->i,j-N+1+i,t)");
Merge(prog, system, "G", "H_split","Slice_6");
CoB(prog, system, "G_split", "(i,j,t->i,i+j,t)");
CoB(prog, system, "H", "(i,j,t->i,j-N+i,t)");
Merge(prog, system, "G_split", "H", "Slice_7");

CoB(prog, system, "I", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "J_split", "(i,j,t->N-1-j,N-1-i,t)");
CoB(prog, system, "I", "(i,j,t->i,i+j+1,t)");
CoB(prog, system, "J_split", "(i,j,t->i,j-N+1+i,t)");
Merge(prog, system, "I", "J_split","Slice_8");
CoB(prog, system, "I_split", "(i,j,t->i,i+j,t)");
CoB(prog, system, "J", "(i,j,t->i,j-N+i,t)");
Merge(prog, system, "I_split", "J", "Slice_9");

Normalize(prog);

setSpaceTimeMap(prog, system, "Slice_0", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_1", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_2", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_3", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_4", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_5", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_6", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_7", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_8", "(i,j,t->t,i,j)");
setSpaceTimeMap(prog, system, "Slice_9", "(i,j,t->t,i,j)");

setSpaceTimeMap(prog, system, "FINAL", "(i,j,k->k+1+T,i,j)");


setMemoryMap(prog, system, "Slice_0", "Slice_0_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_1", "Slice_1_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_2", "Slice_2_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_3", "Slice_3_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_4", "Slice_4_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_5", "Slice_5_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_6", "Slice_6_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_7", "Slice_7_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_8", "Slice_8_space", "(i,j,t->i,j,t)");
setMemoryMap(prog, system, "Slice_9", "Slice_9_space", "(i,j,t->i,j,t)");

#options = createTiledCGOptionForScheduledC();
#setDefaultDTilerConfiguration(prog, system, "sequential");

CheckProgram(prog);

#generateScheduledCode(prog, system, options, outDir);
#generateWrapper(prog, system, options, outDir);
generateScheduledCode(prog, system, outDir);
generateWrapper(prog, system, outDir);
generateMakefile(prog, system, outDir);
