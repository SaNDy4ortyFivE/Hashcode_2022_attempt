class C_Skill:
        def __init__(self, skillname, level):
                self.__skillname = skillname
                self.__level = level
                
        def incrementLevel(self):
                self.__level += 1
                
        def getLevel(self):
                return self.__level
                
        def getSkill(self):
                return self.__skillname

  
