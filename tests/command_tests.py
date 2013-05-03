'''
Created on 02/mag/2013

@author: sreghenzi
'''
import unittest
import os
import filecmp
from pydev.management.commands.eclipse import Command
from django.core.management import call_command


class Test(unittest.TestCase):
    
    stage_dir= os.path.join(os.path.dirname(os.path.abspath(__file__)),"staging")

    def setUp(self):
        self.command = Command()       
        self.assure_path_exists()
        try:
            os.remove(os.path.join(self.stage_dir,'.project'))
            os.remove(os.path.join(self.stage_dir,'.pydevproject'))
        except:
            pass

    def assure_path_exists(self):
        print "Staging dir: " , self.stage_dir   
        if not os.path.exists( self.stage_dir):
                os.makedirs( self.stage_dir)
                print "Staging created"

    def tearDown(self):
        pass


    def testSrcFormat(self):
         
        opts = {'src':True}
        args = ['testenv','2.7','target_path='+os.path.join(self.stage_dir,'src')]
        call_command('eclipse', *args, **opts)
        self._verifiy_fixtures('src')
        
    def testPlainFormat(self):
        opts = {}
        args = ['testenv','2.7','target_path='+self.stage_dir]
        call_command('eclipse', *args, **opts)
        self._verifiy_fixtures('plain')
        
    def testWithRelatedProjects(self):
        opts = {}
        args = ['testenv','2.7','target_path='+self.stage_dir,'related-projects=shooter,bower']
        call_command('eclipse', *args, **opts)
        self._verifiy_fixtures('rel')
        
    def _verifiy_fixtures(self,test_case):
        self.assertTrue( filecmp.cmp(os.path.join(self.stage_dir,'.project'), "fixtures/fixture.%s.project" % test_case) , ".project file not as expected")
        self.assertTrue( filecmp.cmp(os.path.join(self.stage_dir,'.pydevproject'), "fixtures/fixture.%s.pydevproject " % test_case) , ".pydevproject file not as expected")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSrcFormat']
    unittest.main()