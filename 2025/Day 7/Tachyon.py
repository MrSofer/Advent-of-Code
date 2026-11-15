PATH : str = "input.txt"

with open(PATH, "r", encoding="utf-8") as file:
    content = file.read().strip()

manifold : list[str] = content.split("\n")

def count_total_splits(tachyon_manifold : list[str]) -> int:

    total_splits = 0

    current_beams = {tachyon_manifold[0].find("S")}

    for i in range(1, len(tachyon_manifold)):
        for beam in current_beams.copy():
            if tachyon_manifold[i][beam] == "^":
                total_splits+=1
                current_beams.remove(beam)
                current_beams.add(beam+1)
                current_beams.add(beam-1)
    return total_splits

def count_total_timelines(tachyon_manifold : list[str]) -> int:

    current_timelines = {tachyon_manifold[0].find("S"):1}

    for i in range(1,len(tachyon_manifold)):
        for beam in current_timelines.copy():
            if tachyon_manifold[i][beam] == "^":
                for new_beam in [beam-1,beam+1]:
                    if new_beam in current_timelines:
                        current_timelines[new_beam] += current_timelines[beam]
                    else:
                        current_timelines[new_beam] = current_timelines[beam]
                del current_timelines[beam]

    return sum(current_timelines.values())


if __name__ == "__main__":
    print(count_total_splits(manifold))
    print(count_total_timelines(manifold))