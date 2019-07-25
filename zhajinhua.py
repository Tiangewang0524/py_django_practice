"""
一个炸金花的小程序

written by Tiangewang0524 on 25/07/2019
"""

import random
repeat_list = []


# 玩家数量与名字数量不匹配的异常
class PlayersNumError(Exception):
    def __init__(self, error_info):
        super().__init__(self)  # 初始化父类
        self.error_info = error_info

    def __str__(self):
        return self.error_info


# 牌类
class Card:
    """
    牌的属性
    """
    def __init__(self, point, color):
        self.point = point
        self.color = color

    def cmp_other(self, other):
        if self.point > other.point:
            return 1
        elif self.point < other.point:
            return -1
        else:
            if self.color != other.color:
                return -2
            else:
                return 0

    def __str__(self):
        points = 'XX23456789TJQKA'
        colors = ['方片', '梅花', '红心', '黑桃']
        tmp_point = points[self.point]
        if self.point == 10:
            tmp_point = '10'
        print_str = colors[self.color] + tmp_point
        return print_str


# 手牌类
class HandCard:
    """
    三张手牌，可以随机生成，也可以指定
    """
    def __init__(self, tmp_list=None):
        if not tmp_list:
            tmp_list = []
            while len(tmp_list) < 3:
                point = random.randint(2, 14)
                color = random.randint(0, 3)
                if (point, color) not in repeat_list:
                    repeat_list.append((point, color))
                    tmp_list.append(Card(point, color))
            self.cards = tmp_list
        else:
            self.cards = tmp_list
        self.level = self.get_level()
        # 三张牌确定之后，确定牌型

    # 打印牌
    # def card_print(self):
    #     print("该玩家的牌为{} {} {}".format(self.cards[0], self.cards[1], self.cards[2]))


    # 替换一张牌
    def repalce_card(self, old, new):
        for i in range(3):
            # 找到点数和花色都相等的一张牌
            if self.cards[i].cmp_other(old) == 0:
                # 把旧牌的花色和点数都替换掉
                self.cards[i].point = new.point
                self.cards[i].color = new.color

    # 扑克牌排序
    # 破坏了Class Handcard 的数据结构，已作废
    # def poker_sort(self):
    #     list_b = ['J', 'Q', 'K', 'A']
    #     dict_a = dict()
    #     for each_card in self.cards:
    #         # 保存牌大小
    #         val = str(each_card)[2]
    #         print(val)
    #         if val in list_b:
    #             if val == 'J':
    #                 dict_a[str(each_card)] = 11
    #             elif val == 'Q':
    #                 dict_a[str(each_card)] = 12
    #             elif val == 'K':
    #                 dict_a[str(each_card)] = 13
    #             else:
    #                 dict_a[str(each_card)] = 14
    #         elif val == '1' and str(each_card)[3] == '0':
    #             dict_a[str(each_card)] = int(val + str(each_card)[3])
    #         else:
    #             dict_a[str(each_card)] = int(val)
    #     list_new = sorted(dict_a.items(), key=lambda x: x[1], reverse=True)
    #     list_poker_new, b = zip(*list_new)
    #     self.cards = list(list_poker_new)
    #     # print(self.cards)

    # 确定牌型
    def get_level(self):
        self.cards.sort(key=lambda x: x.point, reverse=True)
        card1_point = self.cards[0].point
        card2_point = self.cards[1].point
        card3_point = self.cards[2].point
        card1_color = self.cards[0].color
        card2_color = self.cards[1].color
        card3_color = self.cards[2].color
        if card1_point == card2_point == card3_point:
            # print("豹子")
            self.cards.append('豹子')
            return 6
        elif card1_color == card2_color == card3_color:
            if card1_point == card2_point + 1 == card3_point + 2:
                # print("同花顺")
                self.cards.append('同花顺')
                return 5
            else:
                # print("金花")
                self.cards.append('金花')
                return 4
        elif card1_point == card2_point + 1 == card3_point + 2:
            # print("顺子")
            self.cards.append('顺子')
            return 3
        elif card1_point == card2_point or card1_point == card3_point or card2_point == card3_point:
            # print("对子")
            self.cards.append('对子')
            return 2
        else:
            # print("单牌")
            self.cards.append('单牌')
            return 1

    def __str__(self):
        return "{} {} {}, 牌型为:{}。".format(self.cards[0], self.cards[1], self.cards[2], self.cards[3])


# 玩家类
class Player:
    """
    玩家的属性
    """
    def __init__(self, name, handcard):
        self.name = name
        self.handcard = handcard

    # 与其他玩家比较
    # 返回值1代表前者牌大，-1代表后者牌大，0代表一样大
    def cmp_player(self, other_player):
        # 牌型一样，比单牌
        if self.handcard.level == other_player.handcard.level:
            if self.handcard.level == 1:
                # 都是单牌，比较每一张牌
                # print("进入单牌比较")
                return compare_each_card(self.handcard, other_player.handcard)
            elif self.handcard.level == 6:
                # 都是豹子，比较第一张牌的大小即可
                return compare_first_card(self.handcard, other_player.handcard)
            elif self.handcard.level == 5:
                # 都是同花顺，比较第一张牌的大小即可
                return compare_first_card(self.handcard, other_player.handcard)
            elif self.handcard.level == 4:
                # 都是金花，比较每一张牌
                # print("进入单牌比较")
                return compare_each_card(self.handcard, other_player.handcard)
            elif self.handcard.level == 3:
                # 都是顺子，比较第一张牌的大小即可
                return compare_first_card(self.handcard, other_player.handcard)
            else:
                # 对子情况
                # 双方先提取对子的值，即第二张牌的大小
                # 如果对子一样大，则第一张和第三张牌接着比较
                if self.handcard.cards[1].point > other_player.handcard.cards[1].point:
                    return 1
                elif self.handcard.cards[1].point < other_player.handcard.cards[1].point:
                    return -1
                else:
                    if self.handcard.cards[0].point > other_player.handcard.cards[0].point:
                        return 1
                    elif self.handcard.cards[0].point < other_player.handcard.cards[0].point:
                        return -1
                    else:
                        if self.handcard.cards[2].point > other_player.handcard.cards[2].point:
                            return 1
                        elif self.handcard.cards[2].point < other_player.handcard.cards[2].point:
                            return -1
                        else:
                            return 0
        elif self.handcard.level > other_player.handcard.level:
            return 1
        else:
            return -1

    def __str__(self):
        return_str = "{} 的牌为:{}".format(self.name, self.handcard.__str__())
        return return_str

    # 打印赢家
    def print_winner(self, other_player):
        result_str = self.cmp_player(other_player)
        if result_str == 1:
            print('{}获胜'.format(self.name))
            winner = self.name
        elif result_str == -1:
            print('{}获胜'.format(other_player.name))
            winner = other_player.name
        else:
            print('{}和{}平手'.format(self.name, other_player.name))
            winner = self.name + '和' + other_player.name
        return winner


# 桌子类
class Table:
    """
    桌子的属性
    """
    def __init__(self, num, name_list):
        self.num = num
        self.players = []
        try:
            if num != len(name_list):
                raise PlayersNumError('玩家数量和名字数量不匹配')
            else:
                for i in range(num):
                    player = Player(name_list[i], HandCard())
                    self.players.append(player)
        except PlayersNumError as e:
            print(e)

    def get_winner(self):
        try:
            # 初始化，假设第一名玩家的牌最大
            max_player = self.players[0]
            multi_winner = [max_player.name]
            for i in range(1, len(self.players)):
                result = max_player.cmp_player(self.players[i])
                # 结果为1就不做处理
                if result == -1:
                    max_player = self.players[i]
                    multi_winner = [max_player.name]
                elif result == 0:
                    multi_winner.append(self.players[i].name)
            winner_str = '获胜的玩家是'
            for i in range(len(multi_winner)):
                winner_str += multi_winner[i]
                if i+1 != len(multi_winner):
                    winner_str += '和'
            return winner_str
        except IndexError:
            print("玩家数量和名字数量分配出错，游戏终止。")
            return ''

    def __str__(self):
        result_str = ''
        for i in self.players:
            result_str += (i.__str__() + '\n')
        return result_str


# Handcard类的两个参数，单牌一直比较
def compare_each_card(handcard_1, handcard_2):
    if handcard_1.cards[0].point > handcard_2.cards[0].point:
        return 1
    elif handcard_1.cards[0].point < handcard_2.cards[0].point:
        return -1
    else:
        if handcard_1.cards[1].point > handcard_2.cards[1].point:
            return 1
        elif handcard_1.cards[1].point < handcard_2.cards[1].point:
            return -1
        else:
            if handcard_1.cards[2].point > handcard_2.cards[2].point:
                return 1
            elif handcard_1.cards[2].point < handcard_2.cards[2].point:
                return -1
            else:
                return 0


def compare_first_card(handcard_1, handcard_2):
    if handcard_1.cards[0].point > handcard_2.cards[0].point:
        # print("玩家1牌大")
        return 1
    elif handcard_1.cards[0].point == handcard_2.cards[0].point:
        # print("玩家1和玩家2牌一样大")
        return 0
    else:
        # print("玩家2牌大")
        return -1


if __name__ == '__main__':
    # point1 = random.randint(2, 14)
    # color1 = random.randint(0,3)
    # s1 = Card(5, 1)
    # print(s1)
    # point2 = random.randint(2, 14)
    # color2 = random.randint(0, 3)
    # s2 = Card(5, 1)
    # print(s2)
    # cards = [Card(8,9), Card(6,7)]
    # print(Card(8,9) in cards)
    # a = Card(7, 2)
    # print(a)
    # player1_cards = HandCard()
    # cards.card_print()
    # player1_cards.get_level()
    # player_1 = Player('张飞')
    # player_2 = Player('关羽')
    # print("{} 的牌为:{}".format(player_1.name, player_1.show_handcard()))
    # print("{} 的牌为:{}".format(player_2.name, player_2.show_handcard()))
    judge_i = 1
    player_num = ''
    while judge_i > 0:
        try:
            player_num = int(input("请输入玩家数量(小于17):\n"))
            if player_num > 17:
                print("人数超过了允许玩家数量的最大值，请重新输入", end='\n')
            else:
                judge_i = 0
        except ValueError:
            print("输入错误，请重新输入", end='\n')
    player_name = input("请输入玩家姓名，以逗号分割:\n")
    list_name = player_name.split(',')
    t = Table(player_num, list_name)
    print(t)
    print(t.get_winner())

    # print(repeat_list)
    



