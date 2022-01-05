# Example Output #

output date: Wed Jan  5 12:49:27 PST 2022

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

A♡	2♡	3♡	4♡	5♡	6♡	7♡	8♡	9♡	10♡	J♡	Q♡	K♡	
A♠	2♠	3♠	4♠	5♠	6♠	7♠	8♠	9♠	10♠	J♠	Q♠	K♠	
A♣	2♣	3♣	4♣	5♣	6♣	7♣	8♣	9♣	10♣	J♣	Q♣	K♣	
A♢	2♢	3♢	4♢	5♢	6♢	7♢	8♢	9♢	10♢	J♢	Q♢	K♢	
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
-- (1 shuffle) D_clean d_from_cards=2.769230769230769 len=52 current_deck=[ A♡, A♠, 7♣, A♣, A♢, 2♡, 7♢, 2♠, 2♣, 8♡, 2♢, 3♡, 8♠, 8♣, 3♠, 8♢, 3♣, 9♡, 3♢, 9♠, 9♣, 9♢, 4♡, 10♡, 4♠, 4♣, 4♢, 10♠, 5♡, 5♠, 10♣, 10♢, 5♣, 5♢, J♡, J♠, J♣, 6♡, 6♠, 6♣, J♢, Q♡, Q♠, 6♢, Q♣, 7♡, 7♠, Q♢, K♡, K♠, K♣, K♢ ]
-- (5 shuffle) D_clean **d_from_cards=11.666666666666666** len=52 current_deck=[ 9♢, 7♢, J♠, 8♣, A♡, Q♣, 9♡, 3♢, K♡, J♣, 4♢, Q♡, A♣, K♠, Q♠, 5♠, 10♣, 2♢, 6♡, 2♠, 4♡, 7♠, 3♡, 3♠, 10♢, 10♠, 5♡, 2♣, 10♡, A♢, 8♢, 6♠, Q♢, J♢, 4♠, 5♣, 8♠, 6♢, K♣, 9♠, 2♡, 9♣, 3♣, K♢, A♠, 7♣, 6♣, 5♢, 8♡, 4♣, 7♡, J♡ ]

* D_joker d_from_cards=1.0 len=54 current_deck=[ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
-- (1 shuffle) D_joker d_from_cards=3.0238095238095233 len=54 current_deck=[ A♡, A♠, 7♢, A♣, 8♡, 8♠, 8♣, A♢, 2♡, 8♢, 9♡, 9♠, 2♠, 9♣, 9♢, 2♣, 10♡, 10♠, 2♢, 3♡, 10♣, 10♢, J♡, 3♠, 3♣, 3♢, J♠, J♣, 4♡, 4♠, J♢, Q♡, 4♣, 4♢, 5♡, Q♠, Q♣, Q♢, 5♠, 5♣, 5♢, K♡, K♠, 6♡, 6♠, 6♣, K♣, K♢, 6♢, 7♡, 7♠, JKR, JKR, 7♣ ]
-- (5 shuffle) D_joker **d_from_cards=11.04761904761905** len=54 current_deck=[ K♡, A♣, 8♡, 6♡, K♢, Q♣, 8♠, 2♡, 3♡, 8♢, Q♢, 5♠, J♢, 9♣, 6♢, J♣, 5♣, 10♣, K♠, 4♢, 7♡, 9♢, 4♡, 8♣, 10♢, 2♣, 3♣, J♡, 3♠, 6♠, A♡, 5♢, Q♡, 6♣, A♠, 7♢, 7♠, 5♡, Q♠, K♣, JKR, 4♣, 10♡, A♢, 9♡, 9♠, 2♠, JKR, 7♣, 10♠, 3♢, 4♠, 2♢, J♠ ]

* D_clean_s d_from_cards=13.0 len=52 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
-- (1 shuffle) D_clean_s d_from_cards=11.461538461538462 len=52 current_deck=[ A♣, 2♣, A♡, 3♣, 4♣, 5♣, 2♡, 6♣, 7♣, 8♣, 3♡, 4♡, 9♣, 5♡, 6♡, 10♣, J♣, Q♣, 7♡, K♣, A♢, 2♢, 8♡, 3♢, 4♢, 5♢, 9♡, 6♢, 10♡, J♡, Q♡, 7♢, 8♢, K♡, A♠, 2♠, 9♢, 10♢, 3♠, 4♠, J♢, 5♠, 6♠, 7♠, Q♢, K♢, 8♠, 9♠, 10♠, J♠, Q♠, K♠ ]
-- (5 shuffle) D_clean_s **d_from_cards=10.23076923076923** len=52 current_deck=[ A♣, Q♡, 5♣, 7♠, 6♡, 4♢, 7♢, 9♡, 2♠, 2♡, 4♡, A♢, 3♠, 9♠, 10♡, 2♣, Q♢, K♢, 6♣, 4♠, 9♢, 10♢, 10♠, 5♢, J♢, 9♣, 5♡, J♠, Q♠, 8♢, 7♣, 10♣, A♡, Q♣, 5♠, K♠, 2♢, 8♠, 8♡, 8♣, 6♠, 3♣, 6♢, 7♡, J♣, K♡, A♠, K♣, J♡, 3♢, 4♣, 3♡ ]

* D_joker_s d_from_cards=12.142857142857142 len=54 current_deck=[ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
-- (1 shuffle) D_joker_s d_from_cards=11.238095238095239 len=54 current_deck=[ 2♣, 3♣, 4♣, A♡, 5♣, 6♣, 7♣, 2♡, 3♡, 4♡, 8♣, 9♣, 10♣, 5♡, 6♡, 7♡, J♣, Q♣, K♣, 8♡, A♢, 9♡, 10♡, 2♢, J♡, Q♡, K♡, 3♢, A♠, 4♢, 5♢, 6♢, 2♠, 7♢, 8♢, 9♢, 3♠, 4♠, 5♠, 10♢, J♢, 6♠, 7♠, 8♠, Q♢, K♢, JKR, 9♠, JKR, 10♠, J♠, Q♠, K♠, A♣ ]
-- (5 shuffle) D_joker_s **d_from_cards=13.54761904761905** len=54 current_deck=[ J♣, 2♡, 4♠, 9♣, 5♢, A♡, 2♣, JKR, 5♠, 9♠, K♠, 10♠, 5♣, 6♣, 10♢, A♢, 8♠, Q♢, Q♣, 10♣, 7♣, 3♢, 6♢, K♣, 8♢, 9♢, J♡, 8♡, A♠, 2♠, 5♡, J♠, 9♡, 7♢, 3♡, 4♢, 3♣, 3♠, 4♡, 6♡, K♢, 10♡, Q♡, K♡, 4♣, A♣, JKR, 7♡, 8♣, 2♢, Q♠, J♢, 6♠, 7♠ ]

```

## python analysis.py ##
```
-- D_clean --
* initial deck: [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢ ]
A♡	A♠	A♣	A♢	2♡	2♠	2♣	2♢	3♡	3♠	3♣	3♢	4♡	
4♠	4♣	4♢	5♡	5♠	5♣	5♢	6♡	6♠	6♣	6♢	7♡	7♠	
7♣	7♢	8♡	8♠	8♣	8♢	9♡	9♠	9♣	9♢	10♡	10♠	10♣	
10♢	J♡	J♠	J♣	J♢	Q♡	Q♠	Q♣	Q♢	K♡	K♠	K♣	K♢	
* [shuff_num, d_avg_number, d_avg_suit] = [0, 1.000n, 4.000s] [1, 1.385n, 3.917s] [2, 1.692n, 3.896s] [3, 1.923n, 3.917s] [4, 2.077n, 3.854s] [5, 2.205n, 3.938s] [6, 2.154n, 3.875s] [7, 2.333n, 3.833s] [8, 2.487n, 3.896s] [9, 2.744n, 3.875s] [10, 2.897n, 3.917s] [11, 2.692n, 3.875s] [12, 3.051n, 3.896s] [13, 3.051n, 3.917s] [14, 2.872n, 3.917s] [15, 2.821n, 3.917s] [16, 2.872n, 3.833s] [17, 2.795n, 3.875s] [18, 2.872n, 3.917s] [19, 2.974n, 3.917s]
* shuffld deck: [ K♢, Q♡, Q♢, K♣, K♠, 10♠, K♡, 10♣, Q♣, 10♡, 9♡, Q♠, J♢, J♠, J♣, 9♠, 9♣, J♡, 10♢, 7♣, 9♢, 8♣, 8♠, 6♢, 7♠, 8♡, 8♢, 7♢, 7♡, 6♡, 6♣, 5♣, 5♡, 3♠, 4♡, 4♢, 6♠, 5♠, A♢, 5♢, 3♣, A♣, 3♡, 3♢, 4♠, 4♣, 2♡, 2♢, 2♣, 2♠, A♠, A♡ ]
K♢	Q♡	Q♢	K♣	K♠	10♠	K♡	10♣	Q♣	10♡	9♡	Q♠	J♢	
J♠	J♣	9♠	9♣	J♡	10♢	7♣	9♢	8♣	8♠	6♢	7♠	8♡	
8♢	7♢	7♡	6♡	6♣	5♣	5♡	3♠	4♡	4♢	6♠	5♠	A♢	
5♢	3♣	A♣	3♡	3♢	4♠	4♣	2♡	2♢	2♣	2♠	A♠	A♡	
* 20 shuffles, first d_avg -> last d_avg = 1.000n, 4.000s -> 2.974n, 3.917s


-- D_joker --
* initial deck: [ A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠, 7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR, JKR ]
A♡	A♠	A♣	A♢	2♡	2♠	2♣	2♢	3♡	3♠	3♣	3♢	4♡	
4♠	4♣	4♢	5♡	5♠	5♣	5♢	6♡	6♠	6♣	6♢	7♡	7♠	
7♣	7♢	8♡	8♠	8♣	8♢	9♡	9♠	9♣	9♢	10♡	10♠	10♣	
10♢	J♡	J♠	J♣	J♢	Q♡	Q♠	Q♣	Q♢	K♡	K♠	K♣	K♢	
JKR	JKR	
* [shuff_num, d_avg_number, d_avg_suit] = [0, 1.000n, 3.400s] [1, 1.452n, 3.350s] [2, 1.595n, 3.433s] [3, 1.762n, 3.367s] [4, 1.810n, 3.350s] [5, 2.071n, 3.333s] [6, 2.333n, 3.300s] [7, 2.548n, 3.550s] [8, 2.667n, 3.467s] [9, 2.762n, 3.450s] [10, 2.643n, 3.283s] [11, 2.905n, 3.283s] [12, 3.119n, 3.717s] [13, 3.000n, 3.300s] [14, 2.833n, 3.283s] [15, 2.976n, 3.267s] [16, 2.976n, 3.300s] [17, 3.214n, 3.750s] [18, 3.286n, 3.817s] [19, 3.452n, 3.850s]
* shuffld deck: [ Q♣, Q♢, K♡, K♢, JKR, K♠, Q♡, JKR, J♠, 8♢, J♣, K♣, J♢, Q♠, 9♠, 10♢, J♡, 10♡, 9♢, 10♠, 10♣, 5♡, 9♡, 7♢, 9♣, 8♣, 6♢, 7♠, 7♣, 8♡, 6♠, 8♠, 6♣, 7♡, 6♡, 5♢, 5♠, 3♢, 4♠, 5♣, 4♢, 3♣, 2♠, 4♣, 2♢, 2♡, 4♡, 2♣, A♠, 3♠, A♣, A♢, A♡, 3♡ ]
Q♣	Q♢	K♡	K♢	JKR	K♠	Q♡	JKR	J♠	8♢	J♣	K♣	J♢	
Q♠	9♠	10♢	J♡	10♡	9♢	10♠	10♣	5♡	9♡	7♢	9♣	8♣	
6♢	7♠	7♣	8♡	6♠	8♠	6♣	7♡	6♡	5♢	5♠	3♢	4♠	
5♣	4♢	3♣	2♠	4♣	2♢	2♡	4♡	2♣	A♠	3♠	A♣	A♢	
A♡	3♡	
* 20 shuffles, first d_avg -> last d_avg = 1.000n, 3.400s -> 3.452n, 3.850s


-- D_clean_s --
* initial deck: [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢ ]
A♡	2♡	3♡	4♡	5♡	6♡	7♡	8♡	9♡	10♡	J♡	Q♡	K♡	
A♠	2♠	3♠	4♠	5♠	6♠	7♠	8♠	9♠	10♠	J♠	Q♠	K♠	
A♣	2♣	3♣	4♣	5♣	6♣	7♣	8♣	9♣	10♣	J♣	Q♣	K♣	
A♢	2♢	3♢	4♢	5♢	6♢	7♢	8♢	9♢	10♢	J♢	Q♢	K♢	
* [shuff_num, d_avg_number, d_avg_suit] = [0, 13.000n, 1.000s] [1, 13.000n, 1.062s] [2, 12.949n, 1.188s] [3, 12.949n, 1.188s] [4, 12.872n, 1.229s] [5, 12.897n, 1.188s] [6, 12.846n, 1.292s] [7, 12.795n, 1.375s] [8, 12.744n, 1.333s] [9, 12.769n, 1.354s] [10, 12.846n, 1.396s] [11, 12.846n, 1.417s] [12, 12.846n, 1.479s] [13, 12.846n, 1.438s] [14, 12.846n, 1.417s] [15, 12.795n, 1.438s] [16, 12.744n, 1.458s] [17, 12.692n, 1.500s] [18, 12.564n, 1.604s] [19, 12.564n, 1.646s]
* shuffld deck: [ K♢, J♢, 2♢, Q♢, 6♢, 5♢, 7♢, 8♣, 8♢, 9♢, A♢, 4♢, 10♢, J♣, Q♣, 3♢, 9♣, 6♣, 5♣, 7♣, K♠, 4♣, 10♠, K♣, 9♠, 2♣, 10♣, 5♠, Q♠, 3♣, 6♠, 7♠, 3♠, A♣, J♠, 8♠, 6♡, A♠, 9♡, Q♡, 8♡, 2♠, K♡, 4♠, J♡, 3♡, 5♡, 7♡, 2♡, 4♡, 10♡, A♡ ]
K♢	J♢	2♢	Q♢	6♢	5♢	7♢	8♣	8♢	9♢	A♢	4♢	10♢	
J♣	Q♣	3♢	9♣	6♣	5♣	7♣	K♠	4♣	10♠	K♣	9♠	2♣	
10♣	5♠	Q♠	3♣	6♠	7♠	3♠	A♣	J♠	8♠	6♡	A♠	9♡	
Q♡	8♡	2♠	K♡	4♠	J♡	3♡	5♡	7♡	2♡	4♡	10♡	A♡	
* 20 shuffles, first d_avg -> last d_avg = 13.000n, 1.000s -> 12.564n, 1.646s


-- D_joker_s --
* initial deck: [ A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR ]
A♡	2♡	3♡	4♡	5♡	6♡	7♡	8♡	9♡	10♡	J♡	Q♡	K♡	
A♠	2♠	3♠	4♠	5♠	6♠	7♠	8♠	9♠	10♠	J♠	Q♠	K♠	
A♣	2♣	3♣	4♣	5♣	6♣	7♣	8♣	9♣	10♣	J♣	Q♣	K♣	
A♢	2♢	3♢	4♢	5♢	6♢	7♢	8♢	9♢	10♢	J♢	Q♢	K♢	
JKR	JKR	
* [shuff_num, d_avg_number, d_avg_suit] = [0, 12.143n, 1.000s] [1, 12.190n, 1.033s] [2, 12.095n, 1.050s] [3, 12.214n, 1.533s] [4, 12.333n, 1.717s] [5, 12.167n, 1.600s] [6, 12.071n, 1.250s] [7, 12.262n, 1.850s] [8, 12.500n, 2.250s] [9, 12.262n, 1.933s] [10, 12.381n, 2.500s] [11, 12.119n, 2.133s] [12, 11.929n, 1.800s] [13, 11.667n, 1.667s] [14, 11.595n, 1.783s] [15, 11.714n, 1.983s] [16, 11.524n, 1.883s] [17, 11.690n, 2.317s] [18, 11.786n, 2.483s] [19, 11.643n, 2.100s]
* shuffld deck: [ 3♢, J♢, JKR, 4♢, 8♢, JKR, J♣, Q♣, K♢, Q♢, A♢, 7♢, 4♣, K♣, 6♢, 9♢, 2♢, 5♢, 9♣, 10♣, 8♣, 6♠, 6♣, 2♣, 10♢, 7♣, 10♠, 9♠, J♠, 8♠, 5♣, 4♠, A♣, 3♣, 2♠, A♠, Q♠, K♠, 5♠, 7♡, 2♡, Q♡, K♡, 8♡, 7♠, 9♡, 3♠, 3♡, J♡, A♡, 5♡, 4♡, 6♡, 10♡ ]
3♢	J♢	JKR	4♢	8♢	JKR	J♣	Q♣	K♢	Q♢	A♢	7♢	4♣	
K♣	6♢	9♢	2♢	5♢	9♣	10♣	8♣	6♠	6♣	2♣	10♢	7♣	
10♠	9♠	J♠	8♠	5♣	4♠	A♣	3♣	2♠	A♠	Q♠	K♠	5♠	
7♡	2♡	Q♡	K♡	8♡	7♠	9♡	3♠	3♡	J♡	A♡	5♡	4♡	
6♡	10♡	
* 20 shuffles, first d_avg -> last d_avg = 12.143n, 1.000s -> 11.643n, 2.100s
```
