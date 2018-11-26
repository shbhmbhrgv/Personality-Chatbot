lines = []
joey_lines = []
# i = 0
def func(filename):
    with open(filename, 'r',encoding='utf8') as f:
        for line in f:
            try:
                if ":" not in line:
                    if joey_lines and joey_lines[-1] != "===":
                        joey_lines.append("===")
                        lines.append("===")
                else:
                    l = line[line.index(":") + 1:].strip()  # Strip name of speaker.
                    lines.append(l)
                    if "Sheldon:" in l:
                        print (lines[-2])
                        print (lines[-1])
                        print(joey_lines[-1])
                    if "Sheldon:" in line:
                        if joey_lines and lines[-2] != "===":
                            joey_lines.append(lines[-2])
                            joey_lines.append(lines[-1])
                        elif not joey_lines:
                            joey_lines.append(lines[-2])
                            joey_lines.append(lines[-1])


            except Exception as e:
                print (e)


# print (lines)
# func('friends_transcript.txt')
func('tbbt_transcript.txt')
with open('res_sheldon.txt','w',encoding='utf8') as outfile:
    for line in joey_lines:
        try:
            outfile.write("%s\n" %line)
        except Exception as e:
            print (e)