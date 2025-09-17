

# Author  陈玺 72510363 glaxry
# Reviewer 1:邓梦涛，72510744，Tonydmt
# Reviewer 2：崔颢 ，72510596，chch0212
# Reviewer 3: 文艺翔，72510836 EthanGotIt
# Reviewer 4:王芃程. 72510258 wxy1669386846
def is_win(game):
    # 所有可能的胜利情况：3行、3列、2对角线
    lines = []

    # 行
    lines.extend(game)
    # 列
    lines.extend([[game[r][c] for r in range(3)] for c in range(3)])
    # 对角线
    lines.append([game[i][i] for i in range(3)])
    lines.append([game[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] != ' ' and line.count(line[0]) == 3:
            return True
    return False


def print_board(game):
    print("\n".join([" ".join(row) for row in game]))
    print()


def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # 初始化棋盘
    players = ['X', 'O']
    print("X = Player 1")
    print("O = Player 2")

    for n in range(9):
        player = players[n % 2]
        print(f"Player {n % 2 + 1} ({player}): Which cell to mark? i:[1..3], j:[1..3]: ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1

        # 如果位置被占用，提示重选
        if game[i][j] != ' ':
            print("Cell already taken. Try again.")
            continue

        game[i][j] = player
        print_board(game)

        if is_win(game):
            print(f"Player {n % 2 + 1} ({player}) wins!")
            return

    print("Tie!")


if __name__ == "__main__":
    main()
