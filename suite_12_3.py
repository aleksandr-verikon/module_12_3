import unittest
import module_12_1
import tests_12_3

proizvol = unittest.TestSuite()
proizvol.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
proizvol.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(proizvol)




