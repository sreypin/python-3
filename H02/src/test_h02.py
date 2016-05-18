'''
Created on Jan 13, 2016

@author: sgilbert
'''
import checkresults
import unittest
import salesreport

if __name__ == '__main__':
    unittest.main(module='salesreportTest', 
        testRunner=checkresults.CustomTestRunner(
            assignment='CS 132 Homework #2', 
            student=salesreport.student_id()))