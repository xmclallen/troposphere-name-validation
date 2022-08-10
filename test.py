
from logging import exception
import troposphere.cloudformation as cloudformation

import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_troposphereCloudFormationStackInitializerAllowsHyphens(self):
      name = 'Name-withAHyphen'
      raised = False
      try: 
        cloudformation.Stack(name)
      except: 
        raised = True
        self.fail("troposhpere.cloudformation.Stack( stackName ) threw an error")
      
      self.assertFalse(raised, "troposhpere.cloudformation.Stack( stackName ) threw an error")