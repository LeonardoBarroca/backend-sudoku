import sudoko_validate

board = [
    #### VALID BOARDS
    [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],
    [[4, 1, 2, 3], [2, 3, 4, 1], [1, 4, 3, 2], [3, 2, 1, 4]],
    [[2, 3, 4, 1], [1, 4, 2, 3], [3, 2, 1, 4], [4, 1, 3, 2]],
    [[3, 4, 1, 2], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3]],
    [[4, 3, 2, 1], [2, 1, 4, 3], [1, 2, 3, 4], [3, 4, 1, 2]],
    [[2, 4, 1, 3], [3, 1, 2, 4], [4, 2, 3, 1], [1, 3, 4, 2]],
    [[1, 3, 4, 2], [4, 2, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4]],
    #### INVALID BOARDS
    [[1, 2, 3, 3], [3, 4, 1, 2], [2, 1, 4, 4], [4, 3, 2, 1]],
    [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [1, 1, 2, 3]],
    [[1, 2, 3, 4], [1, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],
]


def validate_using_nfa(nfa, word_list, error):
    if sudoko_validate.is_word_list_accepted(nfa, word_list):
        return True
    else:
        print(word_list, error)
        return False


def run_validation_test():
    passed = 0
    failed = 0
    for i in board:
        if sudoko_validate.check_solution(i):
            passed += 1
        else:
            failed += 1
    print(f"Valid boards: {passed}")
    print(f"Invalid boards: {failed}")
    if passed == 7 and failed == 3:
        print("Passed")
    else:
        print("Failed")


run_validation_test()
