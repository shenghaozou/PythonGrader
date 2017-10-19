from openpyxl import Workbook
from webview import WebView
import gradeSettings
from wiscemail import sendEmail

class outputControl():
    def __init__(self, sectionList, name, submissionFolder):
        self.sectionList = sectionList
        self.name = name
        self.database = {}
        self.submissionFolder = submissionFolder
        self.section = dict([(sect,{'workbook':Workbook(),'webview': WebView(name + '-' + sect + '-' + submissionFolder + '.html', submissionFolder)}) for sect in sectionList])
        for key in self.section:
            self.section[key]['worksheet'] = self.section[key]['workbook'].active
            self.section[key]['webview'].createBody() 
            self.section[key]['webview'].insertTitle('Auto Grading Sheet For ' + name + ' Section:' + key)
            self.section[key]['webview'].createGradingTable()
            self.section[key]['worksheet'].append(['Student Name','Student UID','Comment']+ gradeSettings.GRADING_RULES_ORDER)
    
    def close(self):
        for key in self.section:
            self.section[key]['webview'].endTable()
            self.section[key]['webview'].endBody()
            self.section[key]['workbook'].save('../' + self.name + '-' + key + '-' + self.submissionFolder +".xlsx")
    
    def insert(self, studentName, studentID, submissionNum, partner, section, errorMessage, detailedGrade, output, fileName):
        if studentID in self.database.keys():
            print 'insert student:', studentID
            if submissionNum < self.database[studentID]['submissionNum']:
                return False
        self.database[studentID] = {
            'studentName':studentName,
            'studentID':studentID,
            'submissionNum':submissionNum,
            'partner':partner,
            'section':section,
            'errorMessage':errorMessage,
            'detailedGrade':detailedGrade,
            'output':output,
            'fileName':fileName
        }
    def emailSend(self, emailList):
        for sid, data in self.database.iteritems():
            print data['detailedGrade']
            grade = sum(data['detailedGrade'])
            if grade <= gradeSettings.EAMIL_SEND_UPPER_BOUND:
                sendEmail(gradeSettings.EMAIL_SEND == 1, data['studentName'], data['output'].replace(';','\n'), emailList[data['studentID']], '../report.txt', gradeSettings.ASSIGNMENT_NAME)
    
    def dump(self):
        for key, values in self.database.iteritems():
            self.section[values['section']]['webview'].insertGradingTable(values['studentName'], 
                                                                          key,
                                                                          values['partner'], 
                                                                          sum(values['detailedGrade']), 
                                                                          values['errorMessage'], 
                                                                        values['fileName'])

            self.section[values['section']]['worksheet'].append([values['studentName'], key, values['output'].replace(';','\n')] + values['detailedGrade'])
        self.close()



            


