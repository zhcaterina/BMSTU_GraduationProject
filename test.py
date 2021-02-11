def diff_files(fname):
    f1 = open("f2_out.txt")
    f2 = open(fname)

    test_lines = f1.readlines()
    correct_lines = f2.readlines()
    flag = True

    for test, correct in zip(test_lines, correct_lines):
        if test != correct:
            flag = False
            break
        else:
            len_diff = len(test_lines) - len(correct_lines)
        if len_diff > 0:
            flag = False
        elif len_diff < 0:
            flag = False
    #print flag
    f1.close()
    f2.close()
    return flag