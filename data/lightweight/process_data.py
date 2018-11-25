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
                else:
                    l = line[line.index(":") + 1:].strip()  # Strip name of speaker.
                    lines.append(l)
                    if ("Sheldon:" in line):
                        joey_lines.append(lines[-2])
                        joey_lines.append(lines[-1])
                # i += 1
            except Exception as e:
                print (e)


# print (lines)
# func('friends_transcript.txt')
func('tbbt_transcript.txt')
with open('res.txt','w',encoding='utf8') as outfile:
    for line in joey_lines:
        try:
            outfile.write("%s\n" %line)
        except Exception as e:
            print (e)
