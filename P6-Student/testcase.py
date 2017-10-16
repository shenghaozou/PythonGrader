import gradeSettings
for func in gradeSettings.FUNCTION_ORDER:
    print 'Function - ', func
    for test in gradeSettings.TEST_FUNC[func]:
        if 'input_args' in test:
            print ' |- input:',
            for x in test['input_args']:
                print str(x),' ',
            print
        if 'input_file' in test:
            print ' |- input file:',test['input_file']
        if 'return_val' in test:
            print ' |- output:',str(test['return_val'])
        if 'stdout' in test:
            print ' |- output regex:',str(test['stdout'])
        print '  '



