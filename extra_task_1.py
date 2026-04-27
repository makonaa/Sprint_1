import copy

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_duplicate_tickets(tickets_dict:dict) -> None:
    for key, value in tickets_dict.items():
        #checks that the iterable values are not last in dictionary, if last - function stops
        if key == list(tickets_dict.keys())[-1]:
            break
        #removes extra tickets if they are duplicates in the values, except for the first entry
        for ticket in value:
            for i in range(key, len(tickets_dict)):
                if ticket in tickets_dict[i+1]:
                    tickets_dict[i+1].remove(ticket)

def rename_ticket_type(types_dict:dict, tickets_dict:dict) -> None:
    #adds a new value with the new key wording, deletes the old one
    for key, value in types_dict.items():
        tickets_dict[value] = tickets_dict[key]
        del tickets_dict[key]


delete_duplicate_tickets(tickets)
rename_ticket_type(types, tickets)

print(tickets)