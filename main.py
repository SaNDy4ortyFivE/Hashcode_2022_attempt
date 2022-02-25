from contributor import Contributor
from project import Project
from c_skill import C_Skill
from skillrepo import SkillRepo
from scheduledProject import ScheduledProject

def sortOnDays(project):
        return project.getDays()

def fileParser(input_file):
        
        global skill_repo
        global total_projects
        global total_contributors
        
        global contributors
        global projects
        
        with open(input_file ,"r") as f:
                lines = f.readlines()
                
                t = lines.pop(0).strip().split(" ")
                total_contributors, total_projects = int(t[0]), int(t[1])
                
                line_pointer = 0
                
                ##Read contributors here
                for i in range(total_contributors):
                        ##Read name and total skills here
                        t = lines[line_pointer].strip().split(" ")
                        ##Individual name
                        n = t[0]
                        ##Individual skills
                        i_skills = int(t[1])
                        ##Read skills on next i_skills line
                        skills = []
                        for j in range(i_skills):
                                line_pointer += 1
                                t1 = lines[line_pointer].strip().split(" ")
                                skill_name, skill_level = t1[0], int(t1[1])
                                skills.append(C_Skill(skill_name, skill_level))
                        
                        contributors.append(Contributor(n, i_skills, skills))
                        print("Name:{}\tSkills:{}".format(n, i_skills))
                        for s in skills:
                                skill_repo.addNewSkill(s.getSkill())
                                skill_repo.addNewContributor(contributors[-1], s.getSkill())
                                print("Skill name:{}\tSkill level:{}".format(s.getSkill(), s.getLevel()))
                        print("#"*100)
                        
                        ##Move to next user
                        line_pointer += 1
                        
                
                ##Read projects here
                for i in range(total_projects):
                        t = lines[line_pointer].strip().split(" ")
                        p_name, p_days, p_score, p_dead, p_roles = t[0],int(t[1]),int(t[2]),int(t[3]),int(t[4])
                        
                        ##Read roles required for projects
                        roles = []
                        for j in range(p_roles):
                                line_pointer += 1
                                t1 = lines[line_pointer].strip().split(" ")
                                roles.append(C_Skill(t1[0], int(t1[1])))
                        
                        print("P_Name:{}\tP_Days:{}\tP_Score:{}\tP_dead:{}".format(p_name, p_days, p_score, p_dead))
                        for r in roles:
                                print("Role:{}\tLevel:{}".format(r.getSkill(), r.getLevel()))
                        print("_"*100)
                        line_pointer += 1
                        projects.append(Project(p_name, p_days, p_score, p_dead, roles))


##Driver
skill_repo = SkillRepo()
total_projects, total_contributors = 0,0
        
contributors = []
projects = []

fileParser("data.txt")

sorted_projects = sorted(projects, key=sortOnDays)
max_days = 0

for p in sorted_projects:
        print("Name:{}\tDays{}".format(p.getProjectName(), p.getDays()))
        max_days += p.getDays()
        
print("_"*100)        
print("WorstDays:{}".format(max_days))

scheduled = []

total_count = 0
op_lines = []

for i in range(max_days):
        print("Day {}".format(i))
        ##Decrease Days for scheduled projects
        for p in scheduled:
                if p.isCompleted():
                        print("#"*100)
                        print("{} is completed".format(p.getProjectName()))
                        print("#"*100)
                        p.upgradeSkill()
                        scheduled.remove(p)
                else:
                        print("Decreasing days for {}".format(p.getProjectName()))
                        p.decreaseDay()
        ##Check is project can be added
        for p in sorted_projects:
                print("Checking if {} can start...".format(p.getProjectName()))
                can_start = True
                ##Check if contri are available
                d = {}
                for r in p.getRoles():
                        print("Checking role {} , level {}".format(r.getSkill(), r.getLevel()))
                        t = skill_repo.findContri(r.getSkill(), r.getLevel())
                        d[r.getSkill()] = t
                
                ##Check if all roles are filled
                for r in p.getRoles():
                        if d[r.getSkill()] is None:
                                can_start = False
                                break
                
                print("Name:{}:{}".format(p.getProjectName(),can_start))
                
                if can_start:
                        total_count += 1
                        op_lines.append(p.getProjectName())
                        x = ""
                        for r in p.getRoles():
                                x += d[r.getSkill()].getName() + " "
                                d[r.getSkill()].assignWork()
                        op_lines.append(x)
                                
                
                if can_start:
                        print("#"*100)
                        print("Adding this project to queue")
                        print("#"*100)
                        
                        scheduled.append(ScheduledProject(p, d, p.getDays()))
                        sorted_projects.remove(p)

op_lines.insert(0, str(total_count))
with open("out.txt", "w") as f:
        for o in op_lines:
                f.write(o + "\n")
        
