output date: Sat, Jan  1, 2022  3:31:15 PM
# card.py
```
TEST PRODUCTION OF ALL CARDS:

HEART ace = A♡
HEART 2 = 2♡
HEART 3 = 3♡
HEART 4 = 4♡
HEART 5 = 5♡
HEART 6 = 6♡
HEART 7 = 7♡
HEART 8 = 8♡
HEART 9 = 9♡
HEART 10 = 10♡
HEART jack = J♡
HEART queen = Q♡
HEART king = K♡
HEART None = FAIL: Joker Fail -> suit of `None` must have value of `'JOKER'`
SPADE ace = A♠
SPADE 2 = 2♠
SPADE 3 = 3♠
SPADE 4 = 4♠
SPADE 5 = 5♠
SPADE 6 = 6♠
SPADE 7 = 7♠
SPADE 8 = 8♠
SPADE 9 = 9♠
SPADE 10 = 10♠
SPADE jack = J♠
SPADE queen = Q♠
SPADE king = K♠
SPADE None = FAIL: Joker Fail -> suit of `None` must have value of `'JOKER'`
CLUB ace = A♣
CLUB 2 = 2♣
CLUB 3 = 3♣
CLUB 4 = 4♣
CLUB 5 = 5♣
CLUB 6 = 6♣
CLUB 7 = 7♣
CLUB 8 = 8♣
CLUB 9 = 9♣
CLUB 10 = 10♣
CLUB jack = J♣
CLUB queen = Q♣
CLUB king = K♣
CLUB None = FAIL: Joker Fail -> suit of `None` must have value of `'JOKER'`
DIAMOND ace = A♢
DIAMOND 2 = 2♢
DIAMOND 3 = 3♢
DIAMOND 4 = 4♢
DIAMOND 5 = 5♢
DIAMOND 6 = 6♢
DIAMOND 7 = 7♢
DIAMOND 8 = 8♢
DIAMOND 9 = 9♢
DIAMOND 10 = 10♢
DIAMOND jack = J♢
DIAMOND queen = Q♢
DIAMOND king = K♢
DIAMOND None = FAIL: Joker Fail -> suit of `None` must have value of `'JOKER'`
JOKER ace = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 2 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 3 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 4 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 5 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 6 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 7 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 8 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 9 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER 10 = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER jack = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER queen = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER king = FAIL: Joker Fail -> value of 'JOKER' must be suit of `None`
JOKER None = JKR

PRINT ALL CARDS NICELY:

A♡      2♡      3♡      4♡      5♡      6♡      7♡      8♡      9♡      10♡     J♡      Q♡      K♡
A♠      2♠      3♠      4♠      5♠      6♠      7♠      8♠      9♠      10♠     J♠      Q♠      K♠
A♣      2♣      3♣      4♣      5♣      6♣      7♣      8♣      9♣      10♣     J♣      Q♣      K♣
A♢      2♢      3♢      4♢      5♢      6♢      7♢      8♢      9♢      10♢     J♢      Q♢      K♢
JKR

CLEAN DECK (NO JOKERS):

52
[A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢]

NORMAL DECK (2 JOKERS):

53
[A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR]
```

# deck.py
```
* D_clean d_from_cards=1.0 len=52 current_deck=[ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢ ]
-- (1 shuffle) D_clean d_from_cards=2.974358974358974 len=52 current_deck=[ 7♣, 7♢, A♡, A♠, 8♡, 8♠, A♣, 8♣, 8♢, A♢, 9♡, 9♠, 9♣, 2♡, 2♠, 2♣, 9♢, 2♢, 3♡, 10♡, 3♠, 3♣, 10♠, 10♣, 3♢, 10♢, 4♡, 4♠, 4♣, J♡, J♠, J♣, 4♢, J♢, Q♡, Q♠, 5♡, Q♣, Q♢, 5♠, 5♣, 5♢, K♡, 6♡, 6♠, 6♣, K♠, K♣, 6♢, 7♡, K♢, 7♠ ]
-- (5 shuffle) D_clean **d_from_cards=8.948717948717949** len=52 current_deck=[ 5♠, J♡, 2♡, 6♡, 10♢, 2♢, 5♡, Q♣, 10♠, 3♡, 2♠, 4♢, 6♠, 4♡, 2♣, 5♣, 10♣, J♠, A♡, 6♢, 8♣, 4♠, Q♠, 7♡, 5♢, 6♣, 8♢, A♢, K♢, 7♠, 9♢, 3♢, A♠, 4♣, K♡, 8♡, K♠, J♢, 10♡, 7♣, 7♢, 9♡, 3♠, J♣, 8♠, 9♠, K♣, Q♢, A♣, 9♣, 3♣, Q♡ ]

* D_joker d_from_cards=1.0 len=54 current_deck=[ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
-- (1 shuffle) D_joker d_from_cards=2.6190476190476195 len=54 current_deck=[ A♡, A♠, A♣, 7♢, A♢, 2♡, 2♠, 8♡, 2♣, 8♠, 8♣, 2♢, 3♡, 8♢, 9♡, 3♠, 3♣, 9♠, 3♢, 4♡, 9♣, 4♠, 4♣, 9♢, 4♢, 5♡, 10♡, 10♠, 5♠, 5♣, 5♢, 10♣, 6♡, 6♠, 10♢, J♡, J♠, 6♣, 6♢, J♣, 7♡, J♢, 7♠, 7♣, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
-- (5 shuffle) D_joker **d_from_cards=9.92857142857143** len=54 current_deck=[ 7♠, J♡, Q♢, 4♣, 2♢, K♢, 3♠, 7♢, J♣, 6♡, 7♣, 8♡, 6♠, 3♢, 7♡, 9♢, 4♢, 3♡, 10♠, A♡, 8♢, A♠, 2♣, 4♡, K♡, 3♣, A♢, 2♡, JKR, 9♠, K♠, JKR, 5♡, 8♠, A♣, 5♣, 9♣, 5♠, 8♣, K♣, J♠, 9♡, J♢, 6♣, 10♢, Q♡, 6♢, 10♡, 2♠, Q♠, Q♣, 4♠, 5♢, 10♣ ]

* D_clean_s d_from_cards=13.0 len=52 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
-- (1 shuffle) D_clean_s d_from_cards=9.948717948717947 len=52 current_deck=[ A♡, 2♡, 3♡, A♣, 4♡, 2♣, 3♣, 4♣, 5♡, 6♡, 7♡, 5♣, 6♣, 8♡, 9♡, 10♡, 7♣, 8♣, J♡, Q♡, 9♣, 10♣, J♣, K♡, A♠, Q♣, 2♠, 3♠, K♣, A♢, 4♠, 2♢, 3♢, 4♢, 5♠, 6♠, 7♠, 5♢, 6♢, 7♢, 8♠, 9♠, 10♠, 8♢, 9♢, J♠, Q♠, K♠, 10♢, J♢, Q♢, K♢ ]
-- (5 shuffle) D_clean_s **d_from_cards=11.333333333333332** len=52 current_deck=[ J♢, 3♠, Q♢, Q♠, 10♣, 4♢, 5♠, J♡, 6♣, 6♠, 8♢, 8♡, 8♠, 9♢, 4♣, A♡, J♣, K♢, K♡, 2♡, 6♡, 9♠, 7♡, K♣, K♠, 4♠, 9♡, 7♠, 5♢, 5♣, 10♡, Q♡, A♣, 2♢, 3♢, 10♢, 6♢, 3♡, 7♢, 7♣, 2♠, A♠, 4♡, 2♣, 9♣, 10♠, 8♣, 5♡, J♠, Q♣, A♢, 3♣ ]

* D_joker_s d_from_cards=12.142857142857142 len=54 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
-- (1 shuffle) D_joker_s d_from_cards=9.904761904761903 len=54 current_deck=[ 2♣, 3♣, 4♣, A♡, 2♡, 3♡, 5♣, 6♣, 4♡, 5♡, 6♡, 7♣, 8♣, 7♡, 8♡, 9♣, 9♡, 10♡, J♡, 10♣, J♣, Q♣, Q♡, K♡, A♠, K♣, A♢, 2♢, 2♠, 3♢, 3♠, 4♢, 5♢, 4♠, 6♢, 7♢, 8♢, 5♠, 6♠, 9♢, 10♢, 7♠, J♢, 8♠, Q♢, K♢, 9♠, 10♠, JKR, JKR, J♠, Q♠, K♠, A♣ ]
-- (5 shuffle) D_joker_s **d_from_cards=10.54761904761905** len=54 current_deck=[ 7♠, 3♢, 10♣, 2♡, K♡, J♣, 6♢, 7♡, Q♠, 7♢, 6♣, 6♠, 8♠, Q♢, JKR, 8♡, K♠, 3♠, 2♣, 3♡, 4♡, 3♣, K♢, 9♢, 8♢, 6♡, 4♢, 5♡, 4♣, J♡, 9♠, 7♣, 9♣, JKR, J♠, A♠, 2♢, 5♢, 2♠, A♣, K♣, 8♣, Q♣, 5♠, J♢, 4♠, 5♣, 9♡, 10♡, 10♠, 10♢, Q♡, A♢, A♡ ]

```

# analysis.py
```
-- D_clean --
initial deck: [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢ ]
A♡      A♠      A♣      A♢      2♡      2♠      2♣      2♢      3♡      3♠      3♣      3♢      4♡
4♠      4♣      4♢      5♡      5♠      5♣      5♢      6♡      6♠      6♣      6♢      7♡      7♠
7♣      7♢      8♡      8♠      8♣      8♢      9♡      9♠      9♣      9♢      10♡     10♠     10♣
10♢     J♡      J♠      J♣      J♢      Q♡      Q♠      Q♣      Q♢      K♡      K♠      K♣      K♢

* [shuff_num, d_avg] = [0, 1.0000] [1, 2.7179] [2, 5.4103] [3, 8.1795] [4, 10.2564] [5, 11.1282] [6, 9.6154] [7, 10.8974] [8, 10.4359] [9, 11.3077]
shuffld deck: [ 7♡, 4♠, K♠, J♡, 6♡, 4♣, 2♣, 9♢, A♢, 7♢, Q♣, 10♢, 3♣, 8♡, 8♣, 9♡, K♡, 3♡, 5♠, 7♠, 6♢, Q♠, 7♣, 6♠, 3♢, J♠, J♣, 9♠, 3♠, K♣, 9♣, 10♣, A♠, 5♡, 8♠, A♣, 10♠, J♢, 2♠, 4♢, 5♢, 10♡, 2♢, A♡, 5♣, Q♢, 2♡, 8♢, Q♡, 6♣, K♢, 4♡ ]
7♡      4♠      K♠      J♡      6♡      4♣      2♣      9♢      A♢      7♢      Q♣      10♢     3♣
8♡      8♣      9♡      K♡      3♡      5♠      7♠      6♢      Q♠      7♣      6♠      3♢      J♠
J♣      9♠      3♠      K♣      9♣      10♣     A♠      5♡      8♠      A♣      10♠     J♢      2♠
4♢      5♢      10♡     2♢      A♡      5♣      Q♢      2♡      8♢      Q♡      6♣      K♢      4♡



-- D_joker --
initial deck: [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
A♡      A♠      A♣      A♢      2♡      2♠      2♣      2♢      3♡      3♠      3♣      3♢      4♡
4♠      4♣      4♢      5♡      5♠      5♣      5♢      6♡      6♠      6♣      6♢      7♡      7♠
7♣      7♢      8♡      8♠      8♣      8♢      9♡      9♠      9♣      9♢      10♡     10♠     10♣
10♢     J♡      J♠      J♣      J♢      Q♡      Q♠      Q♣      Q♢      K♡      K♠      K♣      K♢
JKR     JKR
* [shuff_num, d_avg] = [0, 1.0000] [1, 2.8333] [2, 5.0952] [3, 8.4286] [4, 9.5952] [5, 10.4762] [6, 10.6667] [7, 13.0476] [8, 11.7857] [9, 10.7381]
shuffld deck: [ 7♡, Q♠, J♡, J♠, 7♣, K♡, 7♠, 9♠, K♢, 6♢, A♣, A♢, Q♡, 5♣, A♠, 2♣, A♡, 4♡, 5♡, 3♠, 2♠, 2♢, 5♠, JKR, 8♠, 10♢, 3♡, Q♣, 8♡, 4♢, 6♡, 9♡, 9♢, 6♠, 4♣, JKR, K♠, Q♢, J♣, 4♠, 9♣, J♢, K♣, 3♣, 5♢, 8♢, 10♠, 10♣, 6♣, 8♣, 7♢, 2♡, 3♢, 10♡ ]
7♡      Q♠      J♡      J♠      7♣      K♡      7♠      9♠      K♢      6♢      A♣      A♢      Q♡
5♣      A♠      2♣      A♡      4♡      5♡      3♠      2♠      2♢      5♠      JKR     8♠      10♢
3♡      Q♣      8♡      4♢      6♡      9♡      9♢      6♠      4♣      JKR     K♠      Q♢      J♣
4♠      9♣      J♢      K♣      3♣      5♢      8♢      10♠     10♣     6♣      8♣      7♢      2♡
3♢      10♡


-- D_clean_s --
initial deck: [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
A♡      2♡      3♡      4♡      5♡      6♡      7♡      8♡      9♡      10♡     J♡      Q♡      K♡
A♠      2♠      3♠      4♠      5♠      6♠      7♠      8♠      9♠      10♠     J♠      Q♠      K♠
A♣      2♣      3♣      4♣      5♣      6♣      7♣      8♣      9♣      10♣     J♣      Q♣      K♣
A♢      2♢      3♢      4♢      5♢      6♢      7♢      8♢      9♢      10♢     J♢      Q♢      K♢

* [shuff_num, d_avg] = [0, 13.0000] [1, 10.7692] [2, 9.6923] [3, 10.6410] [4, 10.7436] [5, 11.7692] [6, 9.5897] [7, 11.2308] [8, 10.0256] [9, 11.2051]
shuffld deck: [ 2♢, 3♠, 3♡, 8♡, 5♠, 3♢, 10♣, A♠, K♠, Q♣, 8♢, 9♢, Q♢, J♢, 6♣, 4♠, K♣, 6♢, 8♠, 5♣, 4♡, 6♠, 7♢, 4♢, 2♣, 2♡, 3♣, K♡, 10♡, 5♡, 10♢, 8♣, A♣, 7♡, 4♣, J♣, 7♣, Q♡, A♡, K♢, J♠, 5♢, 9♡, A♢, 9♣, 6♡, Q♠, 9♠, 7♠, J♡, 10♠, 2♠ ]
2♢      3♠      3♡      8♡      5♠      3♢      10♣     A♠      K♠      Q♣      8♢      9♢      Q♢
J♢      6♣      4♠      K♣      6♢      8♠      5♣      4♡      6♠      7♢      4♢      2♣      2♡
3♣      K♡      10♡     5♡      10♢     8♣      A♣      7♡      4♣      J♣      7♣      Q♡      A♡
K♢      J♠      5♢      9♡      A♢      9♣      6♡      Q♠      9♠      7♠      J♡      10♠     2♠



-- D_joker_s --
initial deck: [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
A♡      2♡      3♡      4♡      5♡      6♡      7♡      8♡      9♡      10♡     J♡      Q♡      K♡
A♠      2♠      3♠      4♠      5♠      6♠      7♠      8♠      9♠      10♠     J♠      Q♠      K♠
A♣      2♣      3♣      4♣      5♣      6♣      7♣      8♣      9♣      10♣     J♣      Q♣      K♣
A♢      2♢      3♢      4♢      5♢      6♢      7♢      8♢      9♢      10♢     J♢      Q♢      K♢
JKR     JKR
* [shuff_num, d_avg] = [0, 12.1429] [1, 9.4048] [2, 4.1667] [3, 8.7381] [4, 11.2857] [5, 12.6429] [6, 13.0714] [7, 13.4524] [8, 12.4762] [9, 14.0476]
shuffld deck: [ 9♣, K♡, JKR, A♢, 6♣, 2♡, Q♢, 4♡, 10♡, A♠, 6♡, J♢, 3♢, K♣, K♠, 5♣, 9♠, 7♢, 10♠, 8♣, 2♣, 2♢, Q♡, J♠, 8♠, 5♢, A♣, 3♡, 4♢, 10♢, 2♠, Q♣, 9♡, A♡, 4♣, 7♡, 6♢, 7♣, Q♠, J♡, 6♠, JKR, 8♢, 5♡, K♢, 3♠, 10♣, J♣, 7♠, 8♡, 5♠, 9♢, 4♠, 3♣ ]
9♣      K♡      JKR     A♢      6♣      2♡      Q♢      4♡      10♡     A♠      6♡      J♢      3♢
K♣      K♠      5♣      9♠      7♢      10♠     8♣      2♣      2♢      Q♡      J♠      8♠      5♢
A♣      3♡      4♢      10♢     2♠      Q♣      9♡      A♡      4♣      7♡      6♢      7♣      Q♠
J♡      6♠      JKR     8♢      5♡      K♢      3♠      10♣     J♣      7♠      8♡      5♠      9♢
4♠      3♣
```