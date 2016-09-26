prog = ReadAlphabets("loop.ab");
system = "loop";
outDir = "output/"+system;

Split(prog, system, "Temp", "Temp_split", "{i,t | i>=N/2}");

Normalize(prog);

CoB(prog, system, "Temp_split", "(i,t->N-1-i,t)");

Normalize(prog);

setSpaceTimeMap(prog, system, "Temp", "(i,t->t,i)");
setSpaceTimeMap(prog, system, "Temp_split", "(i,t->t,i)");
setSpaceTimeMap(prog, system, "Output", "(i->T+1,i)");

setMemoryMap(prog, system, "Temp", "Temp_space", "(i,t->i,t)");
setMemoryMap(prog, system, "Temp_split", "Temp_split_space", "(i,t->i,t)");

CheckProgram(prog);

generateScheduledCode(prog, system, outDir);
generateVerificationCode(prog, system, outDir);
generateWrapper(prog, system, outDir);
generateMakefile(prog, system, outDir);