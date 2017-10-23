import os
class WebView():
    def __init__(self,fileName, submissionFolder):
        self.num = 0
        self.error = ''
        self.f = open('../' + fileName,'w')
        self.f.write('<!DOCTYPE html><html>')
        css = open('../webview','r')
        self.f.write(css.read())
        self.submissionFolder = submissionFolder
        css.close()

    def createBody(self):
        self.f.write('<body>')

    def endBody(self):
        self.f.write('<p>Error:</p>' + self.error)
        self.f.write('</body></html>')
        self.f.close()

    def insertTitle(self, title):
        self.f.write('<h1 id="toc_0">'+title+'</h1>')

    def insertError(self, error):
        self.error = self.error + error.replace('\n','<br>')


    def createGradingTable(self):
        gradingTableTitle = """
        <table><thead><tr>
        <th style="text-align: center">Number</th>
        <th style="text-align: center">Student Name</th>
        <th style="text-align: center">Student ID</th>
        <th style="text-align: center">Student Partner</th>
        <th style="text-align: center">Grade</th>
        <th>Error</th><th style="text-align: center">Source Code</th></tr></thead><tbody>"""
        self.f.write(gradingTableTitle)
    
    def insertGradingTable(self,studentName, studentID, partnerName, GradeInfo, Error, fileName):
        self.num = self.num + 1
        entryStr = """
        <tr>
        <td style="text-align: center">{6}</td>
        <td style="text-align: center">{0}</td>
        <td style="text-align: center">{1}</td>
        <td style="text-align: center">{2}</td>
        <td style="text-align: center">{3}</td>
        <td>{4}</td>
        <td style="text-align: center"><a href="{5}" target="_blank" title="Title">View</a></td></tr>"""
        cwd = os.getcwd()
        self.f.write(entryStr.format(studentName, studentID, partnerName, GradeInfo, Error.replace(';','<br>'),'./{0}/'.format(self.submissionFolder) + fileName + ".py", self.num))


    def endTable(self):
        self.f.write('</tbody></table>')
    


