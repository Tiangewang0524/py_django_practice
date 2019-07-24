import random


repeat_list = []


class Card:
    '''牌的属性'''

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


class HandCard:
    '''三张手牌，可以随机生成，也可以指定'''

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

class Player:
    def __init__(self, name, handcard):
        self.name = name
        self.handcard = handcard

    def show_handcard(self):
        return self.handcard.__str__()

    # 与其他玩家比较
    def cmp_player(self, other_player):
        pass

    # 打印赢家
    def print_winner(self):
        pass


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
    player_1 = Player('张飞')
    player_2 = Player('关羽')
    print("{} 的牌为:{}".format(player_1.name, player_1.show_handcard()))
    print("{} 的牌为:{}".format(player_2.name, player_2.show_handcard()))
    print(repeat_list)
    



