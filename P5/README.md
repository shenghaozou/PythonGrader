#Introduction
This is my auto-grading scripts for Python course CS301 in University of Wisconsin-Madison. It can generate report for graders. Submissions are downloaded from Canvas. Filename will be studentName\_sid\_filename.py.
Author:Shenghao Zou

When grading, you should:
1. **Test a group of submissions in a folder with default location:**Put them into one folder. I suggest you name it as 'submissions'. You can enter 'python GraderP5.py' in terminal. It will automatically run grading scripts for submissions.

2. **Test a group of submissions in a folder:**put them in one folder with other name, for example 'submissions2'. You can run the auto-grading script by 'python GraderP5.py submission2'

3. **Test single file**: If you need to test one submission, move it to 'test' folder. Run 'python GraderP5.py hw.py' if the file name is 'hw.py'. If you only test one file, program will not require the format of filename. 

#Edit Test Case
When editing test cases, you should change gradeSettings.py.
ASSIGNMENT\_NAME: name for the assignment
ASSIGNMENT\_TEST\_NUM: how many test cases Canvas asks for
TEST\_FUNC: test cases for functions
TEST\_SCRIPT: test scripts of each function. It is useful when checking whether they use 'for loop' or some other key word in their function.
GRADING\_RULES: garding rules for each rubric. It defines which function to test, what to check(return value or std output), how many points, what's relationship between each test(and means only all tests are passed points will be given, add means give points for each small tests, groupadd menas give points for each group of tests). Relationship operator is still developing and will be more powerful in the future.

#File Requirement
create a file 'NameTable.csv' in main folder, which includes:
First column: student name
Second column: Student Canvas ID(for example:180001)
Third column: anything(reserved for other purpose)
Forth column: section number(for example 333)

Section number is used to dvided students into different groups, which will be easier to sepearate tasks between multiple graders.

#Dependence Requirement
openpyxl
python 2.7+

#Next Version
1. Send emails to students who got 0.
2. Apply MOSS system to detect similarity between python codes.
