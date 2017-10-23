
def quiet(scriptInput, scriptOutput, quietFlag):
    fr = open(scriptInput,'r')
    fw = open(scriptOutput,'w')
    print 'INPUT:', scriptInput
    if quietFlag:
        ClearStatus = False
        for line in fr.readlines():
            if ClearStatus:
                if len(line) > 4 and line[0:4] == 'def ':
                    ClearStatus = False
                    fw.write(line)
            else:
                if len(line) >= 1 and line[0:1] != ' ' and line[0:1] != '#':
                    if len(line) >= 4 and line[0:4] != 'def ':
                        ClearStatus = True
                        continue
                fw.write(line)
    else:
        fw.write(fr.read())
    fr.close()
    fw.close()



        

