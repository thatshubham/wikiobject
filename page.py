import io

""" parsing the wiki markdown into different arrays """

def parse(mainString, headerTopic="", subheaderTopic=""):
    page = {}
    page["headerTopic"] = None
    page["tree"] = {}
    page["desc"] = []
    level = 0
 	listD = [page["desc"]]
     for line in io.StringIO(mainString):
         line = line.rstrip()
         if len(line) == 0:
             continue
        if line.startswith("# ") and page["headerTopic"] == None:
            page["headerTopic"] = line[2:]
            continue
 		elif line[0] == '#':
             while line[0] == '#':
                 line = line[1:]
                 line = line.lstrip()
            page["tree"][line] = []
            listD = [page["tree"][line]]
 			continue
 		else:
             level = 0
             while line[0] == '\t':
                 level += 1
                 line = line[1:]
            if line.startswith("* "):
                line = line[2:]
                line = line.lstrip()
 
 		if level == level:
             listD[-1].append(line)
        elif level < level:
            leveljump = level - level
            if len(listD) > leveljump:
                listD = listD[:-leveljump]
                listD[-1].append(line)
 			elif level > level:
                 linea = [line]
                 listD[-1].append(linea)
                 listD.append(linea)
                 level = level
 			continue
        return page
			