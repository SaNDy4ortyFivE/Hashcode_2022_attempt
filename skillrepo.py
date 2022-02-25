
def sortOnSkillCount(contri):
        return contri.getTotalSkills()

class SkillRepo:
        def __init__(self):
                self.__skills = {}
                
        def getAllSkills(self):
                return self.__skills
                
        def addNewSkill(self, skillName):
                if not skillName in self.__skills.keys():
                        self.__skills[skillName] = []
                        
        def addNewContributor(self, contributor, skillName):
                if not contributor in self.__skills[skillName]:
                        ##self.__skills[skillName] = self.__skills[skillName].append(contributor)
                        self.__skills[skillName].append(contributor)
                        
        def findContri(self, skillName, skillLevel):
                contri = self.__skills[skillName]
                
                ##Get contributor qualified for project
                qualified_contri = []
                for c in contri:
                        if c.getContributorSkillLevel(skillName) >= skillLevel and c.getStatus() == False:
                                print("{} is available".format(c.getName()))
                                qualified_contri.append(c)
                
                ##Break Ties(minimum skill set first)
                qualified_contri.sort(key=sortOnSkillCount)
                
                if len(qualified_contri) > 0:
                        return qualified_contri[0]
                else:
                        return None
