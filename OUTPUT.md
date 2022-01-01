# Example Output #

output date: Sat, Jan  1, 2022  3:38:41 PM

## python card.py ##
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

## python deck.py ##
```
* D_clean d_from_cards=1.0 len=52 current_deck=[ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢ ]
-- (1 shuffle) D_clean d_from_cards=2.897435897435898 len=52 current_deck=[ A♡, 7♣, A♠, A♣, A♢, 7♢, 2♡, 2♠, 8♡, 8♠, 8♣, 2♣, 2♢, 8♢, 9♡, 3♡, 3♠, 9♠, 3♣, 3♢, 4♡, 9♣, 4♠, 9♢, 10♡, 4♣, 4♢, 5♡, 10♠, 10♣, 5♠, 10♢, 5♣, 5♢, J♡, J♠, J♣, 6♡, J♢, Q♡, 6♠, 6♣, 6♢, Q♠, Q♣, Q♢, 7♡, K♡, 7♠, K♠, K♣, K♢ ]
-- (5 shuffle) D_clean **d_from_cards=10.153846153846152** len=52 current_deck=[ J♡, J♠, 5♠, 4♣, 3♢, 2♡, A♡, Q♠, 4♢, Q♣, 7♣, 10♢, 5♣, 4♡, 10♣, 6♠, 2♠, J♣, 8♢, 8♡, 8♣, Q♡, 6♡, A♠, 2♣, 9♣, Q♢, 7♡, A♣, 3♠, K♡, 9♠, 6♣, 4♠, 6♢, 5♡, A♢, 8♠, 9♡, 3♡, 10♠, 2♢, 10♡, 7♠, 9♢, 5♢, J♢, 7♢, K♠, K♣, 3♣, K♢ ]

* D_joker d_from_cards=1.0 len=54 current_deck=[ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
-- (1 shuffle) D_joker d_from_cards=3.1428571428571432 len=54 current_deck=[ A♡, A♠, 7♢, A♣, 8♡, A♢, 8♠, 2♡, 8♣, 8♢, 2♠, 2♣, 9♡, 9♠, 9♣, 2♢, 3♡, 9♢, 10♡, 10♠, 3♠, 10♣, 10♢, 3♣, 3♢, 4♡, J♡, 4♠, J♠, J♣, 4♣, 4♢, 5♡, J♢, Q♡, 5♠, 5♣, Q♠, Q♣, Q♢, 5♢, 6♡, K♡, 6♠, K♠, 6♣, 6♢, 7♡, K♣, K♢, JKR, 7♠, 7♣, JKR ]
-- (5 shuffle) D_joker **d_from_cards=11.047619047619047** len=54 current_deck=[ 9♠, 3♠, 9♢, 4♡, J♢, 6♡, K♡, 5♣, 8♢, 4♠, 10♣, A♠, 4♢, 10♡, Q♡, A♢, J♠, Q♠, A♡, 5♠, K♠, 6♣, 10♢, 9♣, 2♢, J♡, 5♡, 8♠, JKR, Q♣, 6♢, 7♠, JKR, 10♠, 7♡, J♣, 3♣, Q♢, 2♠, 7♢, 2♡, 4♣, 2♣, 9♡, 5♢, 8♣, 3♡, A♣, 8♡, K♣, 7♣, K♢, 3♢, 6♠ ]

* D_clean_s d_from_cards=13.0 len=52 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
-- (1 shuffle) D_clean_s d_from_cards=10.743589743589743 len=52 current_deck=[ A♣, 2♣, 3♣, A♡, 4♣, 2♡, 5♣, 6♣, 3♡, 4♡, 5♡, 7♣, 6♡, 8♣, 9♣, 10♣, 7♡, J♣, Q♣, K♣, 8♡, 9♡, A♢, 2♢, 3♢, 10♡, J♡, 4♢, Q♡, 5♢, K♡, A♠, 6♢, 7♢, 8♢, 2♠, 3♠, 4♠, 9♢, 5♠, 6♠, 10♢, 7♠, 8♠, J♢, 9♠, Q♢, K♢, 10♠, J♠, Q♠, K♠ ]
-- (5 shuffle) D_clean_s **d_from_cards=11.717948717948719** len=52 current_deck=[ 4♠, 2♣, 5♢, 9♡, Q♢, 7♡, 6♢, 3♡, 9♢, 6♡, 8♠, J♢, 8♣, J♡, 3♢, K♡, 3♣, 2♡, 5♣, A♡, Q♠, K♢, 4♡, J♣, 6♠, 10♠, 5♡, Q♣, 7♣, A♢, 7♢, 10♢, K♠, K♣, A♣, 4♢, 10♡, 5♠, 8♢, 6♣, Q♡, 4♣, 9♠, 7♠, 9♣, J♠, 8♡, A♠, 2♠, 3♠, 10♣, 2♢ ]

* D_joker_s d_from_cards=12.142857142857142 len=54 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
-- (1 shuffle) D_joker_s d_from_cards=9.285714285714286 len=54 current_deck=[ 2♣, A♡, 2♡, 3♣, 4♣, 3♡, 5♣, 4♡, 5♡, 6♡, 6♣, 7♣, 7♡, 8♡, 8♣, 9♣, 10♣, 9♡, 10♡, J♡, J♣, Q♣, Q♡, K♡, K♣, A♢, 2♢, A♠, 2♠, 3♠, 3♢, 4♢, 4♠, 5♠, 6♠, 5♢, 6♢, 7♢, 7♠, 8♠, 9♠, 8♢, 10♠, 9♢, J♠, Q♠, K♠, 10♢, A♣, J♢, Q♢, K♢, JKR, JKR ]
-- (5 shuffle) D_joker_s **d_from_cards=11.261904761904761** len=54 current_deck=[ 9♠, 8♣, 6♠, J♢, 10♠, 6♡, 2♣, 9♣, K♣, A♠, Q♠, 4♡, 9♢, A♢, Q♢, K♠, A♡, 6♣, 4♢, 8♢, 5♡, 4♠, 7♠, 8♠, Q♡, J♡, 2♠, 5♢, 2♡, J♣, 3♠, 10♣, K♢, J♠, 5♠, K♡, 6♢, 4♣, JKR, 9♡, 7♢, 10♢, Q♣, 10♡, 3♢, 3♣, 3♡, 5♣, 2♢, A♣, 7♣, JKR, 7♡, 8♡ ]

```

## python analysis.py ##
```
-- D_clean --
initial deck: [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢ ]
A♡      A♠      A♣      A♢      2♡      2♠      2♣      2♢      3♡      3♠      3♣      3♢      4♡
4♠      4♣      4♢      5♡      5♠      5♣      5♢      6♡      6♠      6♣      6♢      7♡      7♠
7♣      7♢      8♡      8♠      8♣      8♢      9♡      9♠      9♣      9♢      10♡     10♠     10♣
10♢     J♡      J♠      J♣      J♢      Q♡      Q♠      Q♣      Q♢      K♡      K♠      K♣      K♢

* [shuff_num, d_avg] = [0, 1.000] [1, 3.000] [2, 4.538] [3, 8.462] [4, 9.974] [5, 8.923] [6, 11.692] [7, 11.590] [8, 9.641] [9, 9.872]
shuffld deck: [ 10♠, 10♣, K♠, 8♣, K♢, 2♣, 7♢, Q♢, Q♠, 9♡, 4♢, A♡, 5♠, 10♡, 4♠, A♠, 3♣, 6♠, K♡, J♠, 4♣, 9♠, A♢, Q♡, A♣, 7♣, 4♡, 10♢, 3♠, K♣, 5♡, 3♡, 2♡, 3♢, 8♠, J♡, 7♡, 6♣, 5♢, Q♣, 9♣, 7♠, 6♢, 9♢, 6♡, 8♢, 8♡, J♣, 2♢, J♢, 2♠, 5♣ ]
10♠     10♣     K♠      8♣      K♢      2♣      7♢      Q♢      Q♠      9♡      4♢      A♡      5♠
10♡     4♠      A♠      3♣      6♠      K♡      J♠      4♣      9♠      A♢      Q♡      A♣      7♣
4♡      10♢     3♠      K♣      5♡      3♡      2♡      3♢      8♠      J♡      7♡      6♣      5♢
Q♣      9♣      7♠      6♢      9♢      6♡      8♢      8♡      J♣      2♢      J♢      2♠      5♣



-- D_joker --
initial deck: [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
A♡      A♠      A♣      A♢      2♡      2♠      2♣      2♢      3♡      3♠      3♣      3♢      4♡
4♠      4♣      4♢      5♡      5♠      5♣      5♢      6♡      6♠      6♣      6♢      7♡      7♠
7♣      7♢      8♡      8♠      8♣      8♢      9♡      9♠      9♣      9♢      10♡     10♠     10♣
10♢     J♡      J♠      J♣      J♢      Q♡      Q♠      Q♣      Q♢      K♡      K♠      K♣      K♢
JKR     JKR
* [shuff_num, d_avg] = [0, 1.000] [1, 2.952] [2, 5.310] [3, 7.452] [4, 9.857] [5, 10.476] [6, 11.548] [7, 11.095] [8, 11.833] [9, 10.857]
shuffld deck: [ 4♣, 8♠, 7♣, 4♢, K♡, K♠, K♢, Q♠, 3♡, 9♡, A♠, 2♢, Q♢, 7♡, 9♢, Q♣, 2♣, 10♡, 3♠, 10♣, 8♡, 9♠, 10♠, 9♣, 4♠, JKR, J♠, A♡, Q♡, 7♠, 6♡, 5♡, 3♣, 4♡, 5♢, 7♢, 8♢, 6♠, 5♣, 2♠, J♣, 2♡, 3♢, A♣, 10♢, J♡, JKR, 6♢, K♣, A♢, 6♣, 5♠, 8♣, J♢ ]
4♣      8♠      7♣      4♢      K♡      K♠      K♢      Q♠      3♡      9♡      A♠      2♢      Q♢
7♡      9♢      Q♣      2♣      10♡     3♠      10♣     8♡      9♠      10♠     9♣      4♠      JKR
J♠      A♡      Q♡      7♠      6♡      5♡      3♣      4♡      5♢      7♢      8♢      6♠      5♣
2♠      J♣      2♡      3♢      A♣      10♢     J♡      JKR     6♢      K♣      A♢      6♣      5♠
8♣      J♢


-- D_clean_s --
initial deck: [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
A♡      2♡      3♡      4♡      5♡      6♡      7♡      8♡      9♡      10♡     J♡      Q♡      K♡
A♠      2♠      3♠      4♠      5♠      6♠      7♠      8♠      9♠      10♠     J♠      Q♠      K♠
A♣      2♣      3♣      4♣      5♣      6♣      7♣      8♣      9♣      10♣     J♣      Q♣      K♣
A♢      2♢      3♢      4♢      5♢      6♢      7♢      8♢      9♢      10♢     J♢      Q♢      K♢

* [shuff_num, d_avg] = [0, 13.000] [1, 9.410] [2, 4.846] [3, 8.077] [4, 10.487] [5, 10.538] [6, 8.974] [7, 10.231] [8, 9.256] [9, 10.333]
shuffld deck: [ 7♢, 8♠, A♣, K♣, 10♡, 7♠, K♡, 7♡, 4♠, 2♣, 7♣, 8♣, A♠, 9♢, Q♡, 9♠, Q♠, 5♡, 3♣, 8♢, 6♣, 2♡, 3♢, 5♢, K♠, J♡, Q♣, 4♢, J♣, 6♢, 4♣, 4♡, J♢, 10♢, 3♡, 10♠, Q♢, J♠, 9♡, 5♠, 2♢, A♡, 6♠, A♢, 10♣, 9♣, 2♠, 3♠, 5♣, 8♡, 6♡, K♢ ]
7♢      8♠      A♣      K♣      10♡     7♠      K♡      7♡      4♠      2♣      7♣      8♣      A♠
9♢      Q♡      9♠      Q♠      5♡      3♣      8♢      6♣      2♡      3♢      5♢      K♠      J♡
Q♣      4♢      J♣      6♢      4♣      4♡      J♢      10♢     3♡      10♠     Q♢      J♠      9♡
5♠      2♢      A♡      6♠      A♢      10♣     9♣      2♠      3♠      5♣      8♡      6♡      K♢



-- D_joker_s --
initial deck: [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
A♡      2♡      3♡      4♡      5♡      6♡      7♡      8♡      9♡      10♡     J♡      Q♡      K♡
A♠      2♠      3♠      4♠      5♠      6♠      7♠      8♠      9♠      10♠     J♠      Q♠      K♠
A♣      2♣      3♣      4♣      5♣      6♣      7♣      8♣      9♣      10♣     J♣      Q♣      K♣
A♢      2♢      3♢      4♢      5♢      6♢      7♢      8♢      9♢      10♢     J♢      Q♢      K♢
JKR     JKR
* [shuff_num, d_avg] = [0, 12.143] [1, 9.310] [2, 5.690] [3, 9.667] [4, 10.262] [5, 10.738] [6, 11.833] [7, 11.786] [8, 11.381] [9, 10.762]
shuffld deck: [ 9♢, K♣, 9♡, 4♢, A♢, Q♢, 2♡, 10♢, K♢, 9♣, J♠, 8♣, 10♣, J♣, 6♢, K♠, A♠, 5♢, 4♣, 7♣, 9♠, 3♡, 7♡, J♡, 6♣, K♡, A♣, J♢, 8♡, 6♡, 4♠, 8♠, 5♡, 2♢, 5♣, 10♡, 3♠, 3♢, 7♢, JKR, A♡, 10♠, Q♡, 7♠, 4♡, 8♢, 2♠, 2♣, 5♠, 6♠, Q♣, JKR, 3♣, Q♠ ]
9♢      K♣      9♡      4♢      A♢      Q♢      2♡      10♢     K♢      9♣      J♠      8♣      10♣
J♣      6♢      K♠      A♠      5♢      4♣      7♣      9♠      3♡      7♡      J♡      6♣      K♡
A♣      J♢      8♡      6♡      4♠      8♠      5♡      2♢      5♣      10♡     3♠      3♢      7♢
JKR     A♡      10♠     Q♡      7♠      4♡      8♢      2♠      2♣      5♠      6♠      Q♣      JKR
3♣      Q♠
```