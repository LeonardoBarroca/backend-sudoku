from automathon import NFA


def create_nfa():
    q = {
        "ini",
        "A1",
        "A2",
        "A3",
        "A4",
        "B12",
        "B13",
        "B14",
        "B23",
        "B24",
        "B34",
        "C123",
        "C124",
        "C134",
        "C234",
        "fim",
    }
    sigma = {"1", "2", "3", "4"}
    delta = {
        "ini": {"1": {"A1"}, "2": {"A2"}, "3": {"A3"}, "4": {"A4"}},
        "A1": {"2": {"B12"}, "3": {"B13"}, "4": {"B14"}},
        "A2": {"1": {"B12"}, "3": {"B23"}, "4": {"B24"}},
        "A3": {"1": {"B13"}, "2": {"B23"}, "4": {"B34"}},
        "A4": {"1": {"B14"}, "2": {"B24"}, "3": {"B34"}},
        "B12": {"3": {"C123"}, "4": {"C124"}},
        "B13": {"2": {"C123"}, "4": {"C134"}},
        "B14": {"2": {"C124"}, "3": {"C134"}},
        "B23": {"1": {"C123"}, "4": {"C234"}},
        "B24": {"1": {"C124"}, "3": {"C234"}},
        "B34": {"1": {"C134"}, "2": {"C234"}},
        "C123": {"4": {"fim"}},
        "C124": {"3": {"fim"}},
        "C134": {"2": {"fim"}},
        "C234": {"1": {"fim"}},
    }
    i = "ini"
    f = {"fim"}
    return NFA(q, sigma, delta, i, f)


automata = create_nfa()


def extract_elements(board_matrix):
    rows = ["".join(str(num) for num in row) for row in board_matrix]

    columns = [
        "".join(str(board_matrix[row][col]) for row in range(len(board_matrix)))
        for col in range(len(board_matrix[0]))
    ]

    miniboards = []
    for row in range(0, len(board_matrix), 2):
        for col in range(0, len(board_matrix[0]), 2):
            subgrid = "".join(
                str(board_matrix[row + i][col + j]) for i in range(2) for j in range(2)
            )
            miniboards.append(subgrid)

    return rows, columns, miniboards


def is_word_list_accepted(automata, list):
    for i in list:
        if automata.accept(i) == False:
            return False
    return True


def check_solution(board_matrix):
    rows, columns, miniboards = extract_elements(board_matrix)

    is_rows_accepted = is_word_list_accepted(automata, rows)
    is_columns_accepted = is_word_list_accepted(automata, columns)
    is_miniboards_accepted = is_word_list_accepted(automata, miniboards)

    if is_rows_accepted and is_columns_accepted and is_miniboards_accepted:
        return True
    else:
        return False
