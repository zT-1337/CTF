with open("fsocity.dic.complete", "r") as wordlist_complete:
    with open("fsocity.dic.filtered", "w") as wordlist_filtered:
            filtered_lines = []
            all_lines = wordlist_complete.readlines()

            for i in range(len(all_lines)):
                word = all_lines[i]

                if word not in filtered_lines:
                    filtered_lines.append(word)

                if i % 1000 == 0:
                    print(i)

            wordlist_filtered.writelines(filtered_lines)
