def calcula_horas(dic):
    result = 0
    for dia in dic:
        for horas in dic[dia]:
            for hora in horas:
                if horas.index(hora) % 2 != 0:
                        result += hora
    return result


def horario(ucs, alunos):
    result = []
    for aluno in alunos:
        dic = {}
        flag = True
        ucs_aluno = alunos[aluno]
        for uc in ucs_aluno:
            if not flag:
                break
            if uc not in ucs:
                flag = False
                break
            dia = ucs[uc]
            if dia[0] not in dic:
                dic[dia[0]] = [[dia[1], dia[2]]]
            else:
                for [horas, duracao] in dic[dia[0]]:
                    if horas < dia[1] < horas + duracao or dia[1] + dia[2] > horas:
                        flag = False
                        break
                    dic[dia[0]].append([dia[1], dia[2]])
        if flag:
            result.append((aluno, calcula_horas(dic)))
    return sorted(sorted(result, key=lambda t: t[0]), key=lambda t: t[1], reverse=True)


ucs = {"la2": ("quarta", 16, 2), "pi": ("terca", 15, 1), "cp": ("terca", 14, 2), "so": ("quinta", 9, 3)}
alunos = {5000: {"la2", "cp"}, 2000: {"la2", "cp", "pi"}, 3000: {"cp", "poo"}, 1000: {"la2", "cp", "so"}}

print(horario(ucs, alunos))
