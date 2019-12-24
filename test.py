test = [20102, 20101, 20105, 20105, 20105, 20105, 20105, 20107, 20105]
reports_list2 = []
for i in range(len(test)):
    sign = 0
    for j in range(len(reports_list2)):
        if test[i] in reports_list2[j].values():
            reports_list2[j]['value'] = reports_list2[j]['value'] + 1
            sign = 1
    if sign == 0:
        reports_list2.append({'type': test[i], 'value': 1})


# print(reports_list)
print(reports_list2)



