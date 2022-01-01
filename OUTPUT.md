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
-- (1 shuffle) D_clean d_from_cards=2.8461538461538463 len=52 current_deck=[ A♡, A♠, A♣, 7♣, 7♢, A♢, 2♡, 2♠, 8♡, 8♠, 2♣, 2♢, 8♣, 8♢, 3♡, 3♠, 9♡, 9♠, 9♣, 3♣, 3♢, 4♡, 9♢, 10♡, 10♠, 4♠, 10♣, 10♢, J♡, 4♣, J♠, J♣, 4♢, 5♡, 5♠, J♢, 5♣, 5♢, 6♡, Q♡, Q♠, 6♠, 6♣, 6♢, Q♣, Q♢, 7♡, 7♠, K♡, K♠, K♣, K♢ ]
-- (5 shuffle) D_clean **d_from_cards=9.615384615384615** len=52 current_deck=[ 7♣, Q♣, Q♢, J♣, Q♠, 6♠, 9♢, 10♣, 4♢, A♢, 10♡, 10♠, 3♠, K♠, 10♢, A♡, 4♣, 7♡, 5♡, 6♣, J♢, 7♠, K♡, K♣, 7♢, 5♣, 3♣, 5♠, 8♣, J♠, 8♢, A♠, 4♠, 2♡, 3♢, A♣, 8♡, J♡, K♢, 3♡, 9♡, 9♠, 8♠, 6♢, 2♣, 9♣, 4♡, 2♠, 5♢, 6♡, Q♡, 2♢ ]

* D_joker d_from_cards=1.0 len=54 current_deck=[ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
-- (1 shuffle) D_joker d_from_cards=2.976190476190476 len=54 current_deck=[ 7♢, 8♡, 8♠, A♡, 8♣, A♠, A♣, A♢, 8♢, 2♡, 9♡, 9♠, 2♠, 2♣, 2♢, 9♣, 3♡, 9♢, 10♡, 10♠, 3♠, 3♣, 10♣, 10♢, J♡, 3♢, J♠, J♣, J♢, 4♡, Q♡, 4♠, 4♣, 4♢, Q♠, 5♡, 5♠, Q♣, Q♢, 5♣, 5♢, K♡, K♠, 6♡, 6♠, 6♣, K♣, K♢, 6♢, 7♡, JKR, JKR, 7♠, 7♣ ]
-- (5 shuffle) D_joker **d_from_cards=10.523809523809524** len=54 current_deck=[ K♠, 6♠, 6♣, K♢, 8♣, 4♠, 8♢, 7♢, J♣, 10♡, 6♢, 5♠, Q♠, 2♡, Q♢, A♠, A♣, 3♡, K♣, 7♡, 5♣, 9♡, 5♡, A♢, 10♠, 10♣, J♢, 6♡, 3♢, Q♣, 8♡, 8♠, 3♠, JKR, 10♢, 9♠, JKR, 4♣, 5♢, 4♢, K♡, 7♠, A♡, 2♠, 2♣, 3♣, J♠, 4♡, J♡, 7♣, Q♡, 9♢, 2♢, 9♣ ]

* D_clean_s d_from_cards=13.0 len=52 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
-- (1 shuffle) D_clean_s d_from_cards=9.820512820512821 len=52 current_deck=[ A♣, A♡, 2♣, 2♡, 3♡, 3♣, 4♣, 5♣, 4♡, 5♡, 6♣, 7♣, 8♣, 6♡, 7♡, 9♣, 10♣, 8♡, J♣, Q♣, 9♡, K♣, 10♡, A♢, 2♢, J♡, 3♢, Q♡, K♡, 4♢, A♠, 2♠, 5♢, 6♢, 3♠, 4♠, 7♢, 5♠, 6♠, 7♠, 8♢, 9♢, 8♠, 10♢, 9♠, J♢, 10♠, J♠, Q♢, K♢, Q♠, K♠ ]
-- (5 shuffle) D_clean_s **d_from_cards=10.999999999999998** len=52 current_deck=[ 3♢, Q♡, 7♡, 9♢, 2♡, 4♠, 6♢, 6♠, A♣, J♠, 5♣, 8♠, 3♣, 4♡, 7♠, A♡, K♡, J♣, 3♡, 4♣, K♣, 4♢, 7♢, J♡, 5♡, 8♢, 9♣, Q♣, J♢, 10♠, 9♡, 6♣, 3♠, 10♣, 10♢, 10♡, Q♢, K♢, 5♢, 2♣, 9♠, A♠, 7♣, 2♠, 5♠, 8♣, Q♠, A♢, K♠, 6♡, 2♢, 8♡ ]

* D_joker_s d_from_cards=12.142857142857142 len=54 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
-- (1 shuffle) D_joker_s d_from_cards=9.785714285714286 len=54 current_deck=[ 2♣, A♡, 2♡, 3♣, 4♣, 5♣, 3♡, 6♣, 7♣, 4♡, 5♡, 8♣, 6♡, 7♡, 8♡, 9♣, 9♡, 10♡, 10♣, J♡, Q♡, J♣, K♡, Q♣, K♣, A♠, 2♠, 3♠, A♢, 2♢, 4♠, 5♠, 6♠, 3♢, 4♢, 7♠, 8♠, 5♢, 6♢, 7♢, 9♠, 10♠, J♠, 8♢, 9♢, 10♢, Q♠, K♠, A♣, J♢, Q♢, K♢, JKR, JKR ]
-- (5 shuffle) D_joker_s **d_from_cards=9.5** len=54 current_deck=[ 7♣, 7♢, 9♠, 4♡, J♢, Q♠, 9♣, 8♢, Q♢, 9♢, 3♠, Q♣, Q♡, 7♠, 3♣, 5♣, 5♡, A♢, 3♡, K♢, 8♣, K♣, 9♡, 10♡, J♣, 10♠, A♠, 10♢, 2♢, 6♡, 8♠, JKR, 2♣, A♡, 5♠, 6♠, K♠, 4♢, 3♢, JKR, A♣, 5♢, K♡, 4♣, J♠, 10♣, 7♡, J♡, 2♠, 4♠, 8♡, 6♢, 6♣, 2♡ ]

```

# analysis.py
```
-- D_clean --
pre deck:  [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢ ]
* [shuff_num, d_avg] = [0, 1.0000] [1, 3.1026] [2, 6.5641] [3, 9.4103] [4, 10.6410] [5, 10.7436] [6, 11.6410] [7, 11.1538] [8, 11.3590] [9, 10.9744]
post deck: [ 9♢, 10♣, 6♠, A♢, 2♡, 7♡, 4♡, 6♡, A♡, 9♡, Q♣, 10♢, 3♢, Q♡, 3♠, 10♠, 8♠, 5♣, K♣, J♢, 2♠, 6♢, 9♣, Q♢, 4♢, 4♠, J♠, J♡, 8♢, K♠, K♡, 10♡, K♢, 9♠, 4♣, 3♣, 7♣, 2♢, 3♡, A♣, 5♢, Q♠, 7♢, J♣, 5♡, 6♣, 5♠, 8♡, 7♠, A♠, 8♣, 2♣ ]


-- D_joker --
pre deck:  [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
* [shuff_num, d_avg] = [0, 1.0000] [1, 2.7857] [2, 5.1190] [3, 8.5952] [4, 10.8333] [5, 9.2381] [6, 10.5476] [7, 10.4524] [8, 10.1429] [9, 12.1429]
post deck: [ 3♣, 8♠, A♣, K♣, 4♡, J♣, 8♣, 8♡, 6♣, Q♣, 3♢, 7♠, 4♣, 5♡, J♠, 2♢, 2♣, 2♡, A♢, 8♢, J♡, 10♢, 9♠, K♡, JKR, 7♡, K♠, 9♣, 9♡, A♡, 7♣, 5♢, 3♠, 6♢, 10♠, 4♠, 9♢, A♠, Q♠, 6♡, 5♣, Q♡, JKR, 7♢, 5♠, 2♠, 4♢, Q♢, J♢, K♢, 10♡, 3♡, 6♠, 10♣ ]


-- D_clean_s --
pre deck:  [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
* [shuff_num, d_avg] = [0, 13.0000] [1, 11.7179] [2, 11.5385] [3, 11.0769] [4, 11.6923] [5, 11.6154] [6, 11.6923] [7, 10.5897] [8, 10.0256] [9, 10.6667]
post deck: [ 3♢, 2♢, 4♡, 5♡, 4♠, 3♡, 10♡, 2♡, 9♣, 7♣, 5♢, K♠, 10♣, A♢, 7♠, Q♠, 5♣, 6♠, 8♣, 10♠, 6♡, 7♢, 9♠, 2♣, K♢, J♡, 2♠, J♣, 5♠, A♡, J♠, 3♠, Q♢, 8♢, 4♣, 10♢, 6♢, 8♡, 3♣, J♢, A♣, K♡, 7♡, Q♡, 9♢, A♠, 9♡, 6♣, 8♠, Q♣, 4♢, K♣ ]


-- D_joker_s --
pre deck:  [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
* [shuff_num, d_avg] = [0, 12.1429] [1, 9.5476] [2, 4.8095] [3, 9.0476] [4, 10.7619] [5, 11.3810] [6, 11.6190] [7, 11.8571] [8, 10.7857] [9, 10.8810]
post deck: [ 8♢, 7♡, 5♣, 4♢, A♡, 6♢, 10♡, Q♢, 10♢, 7♠, J♢, 3♠, 3♢, 6♠, 3♣, 4♣, J♣, 4♡, 5♢, 9♠, 3♡, K♣, 2♣, Q♡, 7♢, 4♠, 8♣, JKR, 6♡, 9♡, J♠, 10♣, A♠, 7♣, 5♠, 8♡, 10♠, 9♣, A♣, 6♣, 8♠, Q♠, JKR, 5♡, Q♣, A♢, 9♢, J♡, 2♢, K♡, K♠, 2♠, K♢, 2♡ ]
```