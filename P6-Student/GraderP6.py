#File Name Rules: Student_ID_SIS Login ID_File Name
import os
import glob
import sys
import gradeSettings
import re
import csv
import subprocess
import inspect
from quiet import quiet
from gradeParser import gradeParser

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class Grader():
    """Summary:

    This is an Auto Grader for CS 301 Course in UW Madison. It will automatically check whether
    the script and output satisfies our requirement.

    """
    def __init__(self, submissionFolder, outputFlag):
        self.scriptRegPat = [re.compile(exp) for (exp,reason) in gradeSettings.SCRIPT_REG_EXP]
        self.stdResRegPat = [re.compile(exp)for (exp,reason) in gradeSettings.OUTPUT_RESULT_REG_EXP]
        self.scriptExistenceRegPat = [re.compile(exp) for (exp,reason) in gradeSettings.SCRIPT_EXISTENCE_REG_EXP]
        self.outputFlag = outputFlag
        self.partnerNamePat = re.compile('#[\s\S]*?[pP]artner(.*?)\n')
        self.name2sid = {}
        self.sid2email = {}
        self.gradeSettingsPreprocessing()
        self.submissionFolder = submissionFolder

    def gradeSettingsPreprocessing(self):
        for key, tests in gradeSettings.TEST_FUNC.iteritems():
            for i in range(len(tests)):
                if 'stdout_pat_file' in gradeSettings.TEST_FUNC[key][i]:
                    with open('tester/' + gradeSettings.TEST_FUNC[key][i]['stdout_pat_file'],'r') as fr:
                        gradeSettings.TEST_FUNC[key][i]['stdout_pat'] = fr.read()[:-1]
    
    def partnerName(self, script):
        name = self.partnerNamePat.findall(script)
        if name:
            loc = name[0].find(':')
            return name[0][loc + 1:] if loc >= 0 else None
        else:
            return None

    def decomposeFileName(self, fileName):
        tokens = fileName.split('_')
        sid = tokens[2] if tokens[1] == 'late' else tokens[1]
        submissionNum = tokens[3] if tokens[1] == 'late' else tokens[2]
        return tokens[0], sid, submissionNum

    def loadFiles(self, fileList):
        parser = gradeParser(gradeSettings.GRADING_RULES)
        for fileName in fileList:
            if fileName == '__init__':
                continue
            errorInfo = ''
            if self.outputFlag:
                studentName, sid, submissionNum = self.decomposeFileName(fileName)
                studentName = self.sid2name[sid]
                section = self.sid2section[sid]
            else:
                studentName = 'TEST'
                sid = '0'
                section = '0'
                submissionNum = '0'
            
            with open(fileName + '.py','r') as fr:
                script = fr.read()
                partner = self.partnerName(script)
            if '# -*- coding: utf-8 -*-' not in script:
                script = '# -*- coding: utf-8 -*- \n' + script
                with open(fileName + '.py','w') as fw:
                    fw.write(script)
            funcRes = self.testFunction(fileName, sid, submissionNum)
            scriptRes = self.testScript(fileName, sid, submissionNum)
            grading, errorMessage, stdOutput = parser.parse(funcRes, scriptRes)
            print '\033[94m--------------Report---------------\033[0m'
            print 'filename:' + fileName + '.py'
            print errorMessage.replace(';','\n').replace('<strong>','\033[95m').replace('</strong>','\033[0m')
            print '\033[94m-------------- Score --------------\033[0m'
            for name, score in zip(gradeSettings.GRADING_RULES_ORDER, grading):
                print name,':',score
    
    def testScript(self, fileName, sid, submissionNum):
        res = {}
        old_stdin = sys.stdin
        for key, tests in gradeSettings.TEST_SCRIPT.iteritems():
            script = ''
            res[key] = {}
            try:
                sys.stdin = mystdin = open('tester/default.txt','r')
                if key == 'main':
                    with open(fileName + '.py', 'r') as fr:
                        script = fr.read()
                else:
                    exec('from {0} import {1}'.format(fileName, key))
                    exec('script = inspect.getsource({0})'.format(key))
            except Exception as e:
                res[key]['runtime_error'] = True
                res[key]['runtime_error_message'] = str(e)
                print 'catched exception:' + str(e)
            res[key]['test'] = []
            for test in tests:
                testRes = {}
                if 'script_pat' in test.keys():
                    if 'script_pat_setting' not in test.keys():
                        testRes['script_pat'] = re.search(test['script_pat'], script) != None
                    else:
                        testRes['script_pat'] = re.search(test['script_pat'], script,test['script_pat_setting']) != None
                if 'script_pat_count' in test.keys():
                    if 'script_pat_setting' not in test.keys():
                        testRes['script_pat_count'] = len(re.findall(test['script_pat_count'], script))
                    else:
                        testRes['script_pat_count'] = len(re.findall(test['script_pat_count'], script, test['script_pat_setting']))
                if 'selfdef-func' in test.keys():
                    if test['mode'] == 'whole':
                        testRes['selfdef-func'] = test['selfdef-func'](script)
                    elif test['mode'] == 'line':
                        with open(fileName + '.py','r') as fr:
                            tmpRes = fr.readlines()
                            testRes['selfdef-func'] = test['selfdef-func'](tmpRes)
                res[key]['test'].append(testRes)
        sys.stdin = old_stdin
        return res

    def testFunction(self, fileName, sid, submissionNum):
        old_stdout = sys.stdout
        old_stdin = sys.stdin
        res = {}
        returnVal = None
        stdPat = None
        systemExitFlag = None
        print fileName
        # quiet(fileName + '.py', '../temp/f' + sid + '_' + submissionNum + '.py', False)
       
        for key, tests in gradeSettings.TEST_FUNC.iteritems():
            sys.stdout = old_stdout
            # print 'Now Test:',key
            res[key] = []
            # if key == 'main':
            #    continue
            for test in tests:
                ret = None
                testRes = {}
                if 'prerun' in test.keys():
                    d = dict(locals(), **globals())
                    execfile('prerun/{0}'.format(test['prerun']),d ,d)
                sys.stdout = mystdout = StringIO()
                if 'input_file' in test.keys():
                    sys.stdin = mystdin = open('tester/' + test['input_file'],'rU')
                else:
                    sys.stdin = mystdin = open('tester/default.txt','r')
                inputArgs = () if 'input_args' not in test.keys() else test['input_args']
                try:
                    if key == 'main':
                        d = dict(locals(), **globals())
                        execfile(fileName + '.py',d ,d)
                    else:
                        exec('from {0} import {1}'.format(fileName, key))
                        exec("ret = {0}(*inputArgs)".format(key))
                except KeyboardInterrupt:
                    testRes['runtime_error'] = True
                    testRes['runtime_error_message'] = 'Your program fails into infinite loop.;'
                    sys.stdout = old_stdout
                    print 'KeyboradInterrupt Catched.'

                except SystemExit as se:
                    if 'systemExit' not in test.keys():
                        testRes['runtime_error'] = True
                        testRes['runtime_error_message'] = str(se)
                    sys.stdout = old_stdout
                    print 'SystemExit Catched. Output:', mystdout.getvalue()

                except Exception as e:
                    sys.stdout = old_stdout
                    print 'OtherException Catched.' + str(e)
                    testRes['runtime_error'] = True
                    testRes['runtime_error_message'] = str(e)
                if 'return_val' in test.keys():
                    try:
                        if ret != None:
                            if type(test['return_val']) is float:
                                testRes['return_val'] = abs(ret - test['return_val']) < 0.01
                            else:
                                testRes['return_val'] = ret == test['return_val']
                        else:
                            testRes['return_val'] = False
                        testRes['student_return_val'] = ret
                    except:
                        testRes['return_val'] = False
                        testRes['student_return_val'] = None
                if 'stdout_pat' in test.keys():
                    if 'stdout_pat_setting' in test.keys():
                        testRes['stdout_pat'] = re.search(test['stdout_pat'], mystdout.getvalue()) != None
                    else:
                        testRes['stdout_pat'] = re.search(test['stdout_pat'], mystdout.getvalue(), test['stdout_pat_setting']) != None
                    testRes['student_output'] = mystdout.getvalue()
                res[key].append(testRes)
        sys.stdout = old_stdout
        sys.stdin = old_stdin
        return res

if __name__ == "__main__":
    submissionFolder = '.'
    if (len(sys.argv) >=2 and sys.argv[1] > 3 and sys.argv[1][-3:] == '.py'):
        a = Grader(submissionFolder, False)
        a.loadFiles([sys.argv[1][:-3]])
    else:
        print 'Invalid Format. What\'s your file name?'
        fileName = raw_input()
        a = Grader(submissionFolder, False)
        a.loadFiles([fileName[:-3]])

    



