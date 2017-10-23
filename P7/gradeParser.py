import gradeSettings
class gradeParser:
    def __init__(self, parseRules):
        self.rules = parseRules
        self.ruleTable = {'add': self.parseAdd,
                          'and': self.parseAnd,
                          'range':self.parseRange,
                          'groupadd':self.parseGroupAdd,
                          'sum':self.parseSum,
                          'select':self.parseSelect}
        self. objectTable = {'func': self.parseFunc,
                             'script': self.parseScript,
                             'all': self.parseAll}
    
    def parseAll(self, test, FuncResult, ScriptResult):
        error = ''
        score = 0
        output = ''
        points = 1
        res = True
        index = test['index']
        if 'points' in test.keys():
            points = test['points']
        if test['subtype'] == 'script':
            for funcName, result in ScriptResult['all_function']['test'][index]:
                ScriptResult['temp_' + funcName] = {'test':[result]}
                subTest = test.copy()
                subTest['error'] = subTest['error'].replace('{func_name}',funcName)
                subTest['type'] = 'script'
                subTest['func_name'] = 'temp_' + funcName
                subTest['index'] = 0
                tmpScore, tmpError, tmpOutput = self.parseScript(subTest, FuncResult, ScriptResult)
                error += tmpError
                output += tmpOutput
                res = res and (tmpScore > 0)
            if res:    
                return points, '', ''
            else:
                return 0, error, output
        else:
            print 'parseAll for func has not been implemented.'
            raise SyntaxError
    
    def parseScript(self, test, FuncResult, ScriptResult):
        funcName = test['func_name']
        if 'runtime_error' in ScriptResult[funcName]:
            return 0, '<strong> runtime error. </strong> ;>' + ScriptResult[funcName]['runtime_error_message'] + '; ','runtime error ;>' + ScriptResult[funcName]['runtime_error_message'] + '; '
        else:
            index = test['index']
            check = test['check']
            if 'points' in test.keys():
                points = test['points']
            else:
                points = 1
            error = ''
            output = ''
            if check in ScriptResult[funcName]['test'][index]:
                if check != 'script_pat_count':
                    if ScriptResult[funcName]['test'][index][check] ^ ('inverse' in test.keys()):
                        return points, '', ''
                    else:
                        if 'error' in test:
                            error = error + '<strong>' + test['error'].replace('{func_name}', funcName) + ' - unsatisfied</strong>; '
                            output = output + test['error'].replace('{func_name}', funcName)  + ' - unsatisfied '
                        return 0, error, output
                else:
                    if ScriptResult[funcName]['test'][index][check]:
                        return ScriptResult[funcName]['test'][index][check], '',''
                    else:
                        if 'error' in test:
                            error = error + '<strong>' + test['error'].replace('{func_name}', funcName) + ' - unsatisfied</strong>; '
                            output = output + test['error'].replace('{func_name}', funcName)  + ' - unsatisfied '
                        return 0, error, output


    def parseFunc(self, test, FuncResult, ScriptResult):
        funcName = test['func_name']
        index = test['index']
        check = test['check']
        if 'runtime_error' in FuncResult[funcName][index]:
            return 0, '<strong>runtime error for ' + test['error'] + '</strong>;> ' + FuncResult[funcName][index]['runtime_error_message'] + '; ', 'runtime error for ' + test['error'].replace('{func_name}', funcName)  + ';> ' + FuncResult[funcName][index]['runtime_error_message'] + '; '
        if 'points' in test.keys():
            points = test['points']
        else:
            points = 1
        error = ''
        output = ''
        if check in FuncResult[funcName][index]:
            if FuncResult[funcName][index][check]:
                return points,'',''
            else:
                if 'error' in test:
                    error = error + '<strong>' + test['error'].replace('{func_name}', funcName) + ' - unsatisfied</strong>; '
                    output = output + test['error'] + ' - unsatisfied '
                if not ('output' in test and test['output'] == False):
                    if check == 'stdout_pat':
                        if 'input_file' in gradeSettings.TEST_FUNC[funcName][index]:
                            error = error + '> std input file:' + str(gradeSettings.TEST_FUNC[funcName][index]['input_file']) + ';'
                        error = error + '> stdout:|' + FuncResult[funcName][index]['student_output'] 
                        error = error + '|, answer(RegEx):|' + str(gradeSettings.TEST_FUNC[funcName][index][check]) + '|;'
                        output = output + '(your output:' + ',answer key word:' + str(gradeSettings.TEST_FUNC[funcName][index][check]) + ');'
                    elif check == 'return_val':
                        if 'input_args' in gradeSettings.TEST_FUNC[funcName][index]:
                            error = error + '> input argv:' + str(gradeSettings.TEST_FUNC[funcName][index]['input_args']) + ';'
                        error = error + '> ret value:' + str(FuncResult[funcName][index]['student_return_val'])
                        error = error + ', answer:' + str(gradeSettings.TEST_FUNC[funcName][index][check]) + ';'
                        output = output + '(your return value:' + str(FuncResult[funcName][index]['student_return_val']) + ', answer:' + str(gradeSettings.TEST_FUNC[funcName][index][check]) + ');'
                return 0, error, output
        else:
            print 'Check:',check, 'not in:',FuncResult[funcName][index], 'when parsing func ',funcName,' index ',index
            raise SyntaxError 
    
    def parseSelect(self, ruleNum, testList, FuncResult, ScriptResult):
        score = 0
        error = ''
        output = ''
        for test in testList['test']:
            tmpScore, tmpError, tmpOutput = self.objectTable[test['type']](test, FuncResult, ScriptResult)
            error = error + tmpError
            output = output + tmpOutput
            if (tmpScore):
                score = test['points']
                break
        error = error + 'Score for part ' + str(ruleNum) + ':(' + str(score) + '/' + str(testList['points']) + ') ;;' if score < testList['points'] else ''
        output = output + 'Score for part ' + str(ruleNum) + ':(' + str(score) + '/' + str(testList['points']) + ') ;;' if score < testList['points'] else ''
        return score, error, output

    def parseGroupAdd(self, ruleNum, testList, FuncResult, ScriptResult):
        score = 0
        error = ''
        output = ''
        for point, group in testList['groups']:
            tmpchecker = True
            for test in group:
                tmpScore, tmpError, tmpOutput = self.objectTable[test['type']](test, FuncResult, ScriptResult)
                error = error + tmpError
                output = output + tmpOutput
                tmpchecker = tmpchecker and (tmpScore > 0)
            if tmpchecker:
                score = score + point
        error = error + 'Score for part ' + str(ruleNum) + ':(' + str(score) + '/' + str(testList['points']) + ') ;;' if score < testList['points'] else ''
        output = output + 'Score for part ' + str(ruleNum) + ':(' + str(score) + '/' + str(testList['points']) + ') ;;' if score < testList['points'] else ''
        return score, error, output 


    def parseAdd(self, ruleNum, testList, FuncResult, ScriptResult):
        score = 0
        error = ''
        output = ''
        for test in testList['test']:
            tmpScore, tmpError, tmpOutput = self.objectTable[test['type']](test, FuncResult, ScriptResult)
            error = error + tmpError
            output = output + tmpOutput
            score = score + tmpScore
        return score, error + 'Score for part ' + str(ruleNum) + ':(' + str(score) + '/' + str(testList['points']) + ') ;;' if score < testList['points'] else error,  output + 'Score for part ' + str(ruleNum) + ':(' + str(score) + '/' + str(testList['points']) + ') ;;' if score < testList['points'] else output

    def parseAnd(self, ruleNum, testList, FuncResult, ScriptResult):
        score = True
        error = ''
        output = ''
        for test in testList['test']:
            tmpScore, tmpError, tmpOutput = self.objectTable[test['type']](test, FuncResult, ScriptResult)
            error = error + tmpError
            output = output + tmpOutput
            score = score and (tmpScore > 0)

        return testList['points'] if score else 0, error + 'Score for part ' + str(ruleNum) + ':(' + str(testList['points'] if score else 0) + '/' + str(testList['points']) + ') ;;' if not score  else error, output + 'Score for part ' + str(ruleNum) + ':(' + str(testList['points'] if score else 0) + '/' + str(testList['points']) + ') ;;' if not score else output

    def parseRange(self, ruleNum, testList, FuncResult, ScriptResult):
        times = 0
        error = ''
        output = ''
        upperBound = len(testList)
        lowerBound = 0
        if 'lowerBound' in testList:
            lowerBound = testList['lowerBound']
        if 'upperBound' in testList:
            upperBound = testList['upperBound']
        for test in testList['test']:
            tmpScore, tmpError, tmpOutput = self.objectTable[test['type']](test, FuncResult, ScriptResult)
            error = error + tmpError
            output = output + tmpOutput
            times = times + (1 if tmpScore else 0)
        finalScore = testList['points'] if lowerBound <= times <= upperBound else 0
        finalEror = error + 'Score for part ' + str(ruleNum) + ':(' + str(testList['points'] if lowerBound <= times <= upperBound else 0) + '/' + str(testList['points']) + ') ;;' if not(lowerBound <= times <= upperBound) else ''
        finalOutput = output + 'Score for part ' + str(ruleNum) + ':(' + str(testList['points'] if lowerBound <= times <= upperBound else 0) + '/' + str(testList['points']) + ') ;;' if not(lowerBound <= times <= upperBound) else ''
        return finalScore, finalEror, finalOutput

    def parseSum(self, ruleNum, testList, FuncResult, ScriptResult):
        times = 0
        error = ''
        output = ''
        upperBound = 100000
        lowerBound = 0
        if 'lowerBound' in testList:
            lowerBound = testList['lowerBound']
        if 'upperBound' in testList:
            upperBound = testList['upperBound']
        for test in testList['test']:
            tmpScore, tmpError, tmpOutput = self.objectTable[test['type']](test, FuncResult, ScriptResult)
            error = error + tmpError
            output = output + tmpOutput
            times = times + tmpScore
        finalScore = testList['points'] if lowerBound <= times <= upperBound else 0
        finalEror = error + 'Score for part ' + str(ruleNum) + ':(' + str(testList['points'] if lowerBound <= times <= upperBound else 0) + '/' + str(testList['points']) + ') ;;' if not(lowerBound <= times <= upperBound) else ''
        finalOutput = output + 'Score for part ' + str(ruleNum) + ':(' + str(testList['points'] if lowerBound <= times <= upperBound else 0) + '/' + str(testList['points']) + ') ;;' if not(lowerBound <= times <= upperBound) else ''
        return finalScore, finalEror, finalOutput
        

    def parse(self, FuncResult, ScriptResult):
        res = [0] * len(self.rules.keys())
        error = ''
        output = ''
        i = 0
        for ruleName in gradeSettings.GRADING_RULES_ORDER:
            i += 1
            rule = gradeSettings.GRADING_RULES[ruleName]
            ruleType = rule['rules']
            index =rule['order']
            tmpScore, tmpError, tmpOutput = self.ruleTable[ruleType](i, rule, FuncResult, ScriptResult)
            error = error + tmpError
            output = output + tmpOutput
            res[index] = tmpScore
            print ruleName,':',tmpScore
        return res, error, output




