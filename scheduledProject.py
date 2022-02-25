from project import Project
from contributor import Contributor

class ScheduledProject:
        def __init__(self, project, contributors, days):
                self.__project = project
                self.__contributors = {}
                self.__days = days
                for s, c in contributors.items():
                        self.__contributors[s] = c
        
        def decreaseDay(self):
                self.__days -= 1
                
        def isCompleted(self):
                if self.__days == 0:
                        return True
                else:
                        return False
                
        def getProjectName(self):
                return self.__project.getProjectName()
                
        def upgradeSkill(self):
                for skillName, contri in self.__contributors.items():
                        contri.upgradeSkill(skillName)
                        contri.deassignWork()
                        
