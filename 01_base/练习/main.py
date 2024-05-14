def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (j, i, i * j), end=' ')  # 输出
        print("\n")  # 每一行结束换行


def sort_list(obj_list: list, mode: bool) -> list:  # mode = True means descending
    for i in range(len(obj_list)):
        for j in range(i, len(obj_list)):
            if mode:
                if obj_list[i] < obj_list[j]:
                    obj_list[i], obj_list[j] = obj_list[j], obj_list[i]
            else:
                if obj_list[i] > obj_list[j]:
                    obj_list[i], obj_list[j] = obj_list[j], obj_list[i]
    return obj_list

def ID():
    '''
    学校有440人参加考试，1号考场有80个座位，要求座位号为0101--0180
    后面每个考场40个座位：
    2号考场考试号要求为0201--0240
    3号考场考试号要求为0301--0440
    后续考场以此类推，请你打印出来这些考场号吧
    '''
    for i in range(1, 440):
        if i <= 80:
            print('01{:0>2d}'.format(i))
        elif i <= 440:
            if i % 40 == 0:
                print('{:0>2d}{:0>2d}'.format(i // 40 - 1, 40))
            else:
                print('{:0>2d}{:0>2d}'.format(i // 40, i % 40))


def main():
    # 九九乘法表
    # multiplication_table()

    #冒泡法排序
    # test_list = [12, 47, 49, -8, -1, 24]
    # sorted_test_list = sort_list(test_list, False)
    # print(sorted_test_list)

    ID()




if __name__ == '__main__':
    main()
