import gradeSettings

i = 0
rules = {'and': 'Pass All Tests to Get Points',
         'add': 'Pass Each Test Can Get Some Points',
         'groupadd':'Group Tests. Pass One Group of Test for Some Points.'}
types = {'script': 'Check script of function',
         'func': 'Test Function'}
checks = {'stdout_pat':'String Regular Expression Match For Standard Output',
          'script_pat':'String Regular Expression Match For Scripts',
          'return_val':'Return Value'}

def funcRet(j, test):
    print ' \033[94mTest ' + str(j) + ': ' + types[test['type']] + ' - ' + checks[test['check']] + '\033[0m'
    print ' Function Name: ' + test['func_name']
    index = int(test['index'])
    if test['type'] == 'func':
        funcTest = gradeSettings.TEST_FUNC[test['func_name']][index]
        if 'prerun' in funcTest:
            print ' |- Before Running the Test, I will run: ' + funcTest['prerun']
        if 'mapper' in funcTest:
            print ' |- This function has a function for student result: ' + funcTest['mapper']
        if 'input_args' in funcTest:
            print ' |- input:',
            for x in funcTest['input_args']:
                print str(x),' ',
        print
        if 'input_file' in funcTest:
            print ' |- input file:',funcTest['input_file']

        if 'return_val' in funcTest and test['check'] == 'return_val':
            print ' |- return value:',str(funcTest['return_val'])

        if 'stdout_pat' in funcTest and test['check'] == 'stdout_pat':
            print ' |- output regex:',str(funcTest['stdout_pat'])
        if 'stdout_pat_file' in funcTest and test['check'] == 'stdout_pat':
            print ' |- output regex(store regex in file):',str(funcTest['stdout_pat_file'])
        print '  '
    if test['type'] == 'script':
        scriptTest = gradeSettings.TEST_SCRIPT[test['func_name']][index]
        if 'script_pat' in scriptTest:
            print ' |- Regex:' + scriptTest['script_pat']
        print '  '

for key in gradeSettings.GRADING_RULES_ORDER:
    dicts = gradeSettings.GRADING_RULES[key]
    i += 1
    print '\033[95mRubric ' + str(i) + ': ' + key + ' - Rules: ' + rules[dicts['rules']] + ' - Points: ' + str(dicts['points']) + '\033[0m'
    
    if dicts['rules'] == 'groupadd':
        k = 0
        for point, tests in dicts['groups']:
            k += 1
            z = 0
            print ' Group ' + str(k)
            for test in tests:
                z += 1
                funcRet(z, test)
            print ''
    else:
        j = 0
        for test in dicts['test']:
            j += 1
            funcRet(j,test)
        
        
        
    
tips = """
TIPS:
If I will run some scripts before the test, you can find them in 'prerun' folder.
If you need find some input_file, try to search them in 'tester' folder.
If you need to test single file, copy them to folder 'test'. Assume the test file is 'hw1.py'. In the folder where GraderP6.py is in, run:
    python GraderP6.py hw1.py
It will show score on screen.
    """
print tips
        










