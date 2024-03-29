import pandas as pd

startDate = pd.to_datetime("2014-09-11"); #start date for NO
endDate = pd.to_datetime("2017-08-08"); #end date for NO
datelist = (pd.date_range(startDate,endDate, freq='M').tolist())


fake_news_accounts = [
'NewOrleansON',
'ElPasoTopNews',
'DailySanJose',
'ChicagoDailyNew',
'DailySanFran',
'DetroitDailyNew',
'TodayCincinnati',
'MinneapolisON',
'KansasDailyNews',
'TodayBostonMA',
'TodayPittsburgh',
'Seattle_Post',
'PhiladelphiaON',
'DailyLosAngeles',
'HoustonTopNews',
'DailySanDiego',
'DallasTopNews',
'WashingtOnline',
'TodayNYCity',
'OnlineCleveland',
'SanAntoTopNews',
'PhoenixDailyNew',
'TodayMiami',
'Atlanta_Online',
'Baltimore0nline',
'OaklandOnline',
'StLouisOnline']

counters ={}

counters['NewOrleansON']= [[0, 0, 4, 3294, 2831, 3122, 3077, 3389, 3393, 2927, 2270, 3549, 3411, 2828, 2861, 2869, 1720, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6],
[0, 0, 467, 218, 32, 28, 23, 17, 31, 25, 23, 27, 21, 26, 62, 119, 167, 0, 0, 0, 0, 0, 0, 842, 925, 255, 381, 396, 358, 410, 433, 448, 399, 336, 336]]

counters['ElPasoTopNews']=[[0, 0, 0, 157, 255, 285, 487, 518, 587, 643, 42, 0, 0, 0, 5, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 3, 13, 13],
[0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 0, 11, 3, 6, 2, 0, 0, 0, 0, 0, 87, 14, 95, 295, 307, 288, 285, 285, 276, 217, 331, 331]]


counters['DailySanJose'] = [[0, 0, 0, 38, 50, 50, 150, 1746, 1625, 1553, 1408, 1355, 1394, 1227, 1306, 1223, 1400, 1537, 1556, 1771, 1705, 1315, 183, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6]
,[0, 0, 0, 0, 0, 0, 1, 2, 6, 4, 0, 2, 4, 8, 12, 32, 8, 43, 20, 3, 2, 0, 0, 1, 0, 269, 131, 36, 37, 41, 29, 39, 40, 30, 30]]

counters['ChicagoDailyNew'] = [[0, 0, 0, 2733, 3310, 3355, 3446, 3896, 3201, 2899, 2601, 2510, 2605, 2331, 1705, 61, 10, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 8],
[0, 0, 0, 1, 4, 2, 0, 1, 204, 433, 405, 328, 336, 325, 584, 1087, 160, 3, 0, 0, 0, 0, 0, 753, 1684, 1720, 2052, 1904, 1185, 1420, 1451, 1465, 1475, 1451, 1451]]

counters['DailySanFran'] = [[0, 0, 0, 1145, 1249, 1547, 1622, 2074, 1703, 2029, 1784, 1886, 2130, 1798, 1801, 1821, 1939, 2121, 979, 0, 6, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 6, 6]
,[0, 0, 0, 1, 1, 1, 1, 0, 7, 2, 0, 2, 1, 3, 6, 34, 14, 60, 1114, 1885, 756, 0, 0, 734, 1804, 641, 1336, 1411, 1278, 1526, 1505, 1576, 1511, 1542, 1542]]

counters['DetroitDailyNew'] = [[0, 0, 0, 1182, 1586, 1381, 1456, 1845, 1315, 971, 831, 714, 747, 625, 663, 221, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 9, 9],
[0, 0, 0, 101, 138, 140, 147, 176, 484, 871, 705, 637, 604, 556, 570, 210, 0, 0, 0, 0, 0, 0, 0, 259, 398, 729, 315, 788, 796, 903, 884, 920, 719, 892, 892]]

counters['TodayCincinnati'] = [[0, 0, 0, 753, 946, 859, 852, 1061, 1009, 1024, 789, 765, 29, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 32, 0, 1, 13, 13]
,[0, 0, 0, 1, 1, 0, 0, 0, 6, 3, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 151, 25, 359, 602, 1035, 1048, 1173, 1255, 1332, 1148, 1467, 1467]]

counters['MinneapolisON'] = [[0, 0, 0, 543, 1324, 1214, 1149, 1466, 1215, 1186, 1021, 859, 821, 676, 366, 309, 321, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 6, 5, 1, 4, 7, 135, 422, 403, 439, 0]]

counters['KansasDailyNews'] = [[0, 0, 0, 1790, 2146, 2149, 2274, 2345, 2382, 2354, 2336, 2412, 2357, 2144, 1502, 29, 15, 14, 4, 2, 17, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 6],
[0, 0, 0, 297, 1, 1, 1, 0, 6, 3, 0, 0, 0, 1, 609, 2206, 2282, 1924, 2388, 1914, 1938, 521, 0, 1836, 2211, 1149, 1081, 1142, 1030, 1127, 1045, 1028, 1100, 1138, 1138]]

counters['TodayBostonMA'] = [[0, 0, 0, 596, 712, 585, 807, 896, 857, 466, 853, 814, 687, 773, 748, 813, 781, 914, 854, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
,[0, 0, 0, 2, 0, 0, 0, 0, 6, 5, 1, 1, 5, 3, 4, 18, 36, 72, 118, 0, 0, 0, 0, 106, 36, 136, 329, 343, 300, 379, 0]]

counters['TodayPittsburgh'] = [[0, 0, 0, 1428, 2012, 1865, 1984, 2023, 1987, 1738, 1834, 1931, 1836, 1718, 1704, 1964, 1983, 2196, 1990, 1790, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
,[0, 0, 0, 3, 2, 4, 0, 2, 18, 4, 0, 1, 11, 5, 3, 20, 17, 66, 119, 26, 0, 0, 0, 355, 425, 165, 289, 325, 302, 350, 0]]

counters['Seattle_Post'] = [[0, 0, 0, 2039, 1823, 227, 231, 502, 1482, 1848, 1520, 1130, 1171, 1107, 1294, 889, 830, 1020, 954, 1030, 578, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 7],
[0, 0, 0, 177, 180, 41, 35, 84, 215, 319, 254, 184, 185, 173, 216, 747, 788, 1001, 1001, 1052, 539, 0, 0, 126, 20, 128, 410, 549, 434, 504, 497, 498, 506, 491, 491]]

counters['PhiladelphiaON'] = [[0, 0, 0, 1340, 1950, 1751, 1659, 2021, 715, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 7]
,[0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 234, 386, 47, 1292, 1481, 1251, 1398, 1288, 1237, 1265, 1244, 1244]]

counters['DailyLosAngeles'] = [[0, 0, 9, 457, 461, 536, 461, 472, 458, 334, 278, 202, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8],
[0, 0, 0, 372, 342, 333, 335, 393, 364, 309, 292, 277, 190, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 258, 458, 730, 1200, 1284, 1278, 1496, 1447, 1390, 1396, 1336, 1336]]

counters['HoustonTopNews'] = [[0, 0, 85, 1611, 1489, 1520, 1574, 1925, 1570, 1720, 1645, 1450, 1376, 1323, 672, 1, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 1, 1, 1]
,[0, 0, 0, 0, 2, 1, 1, 0, 2, 4, 0, 1, 3, 2, 48, 9, 14, 15, 0, 0, 0, 0, 0, 178, 4, 200, 645, 395, 230, 285, 289, 276, 199, 657, 657]]

counters['DailySanDiego'] = [[0, 0, 0, 68, 63, 73, 168, 1699, 1444, 1662, 1374, 1195, 1123, 886, 922, 900, 1045, 1105, 1100, 1324, 870, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5]
,[0, 0, 0, 0, 0, 0, 0, 0, 9, 5, 0, 0, 1, 6, 12, 36, 11, 47, 18, 7, 31, 0, 0, 294, 42, 320, 591, 719, 575, 724, 739, 770, 755, 804, 804]]

counters['DallasTopNews'] = [[0, 0, 73, 1253, 1229, 1184, 1127, 1484, 1229, 1257, 1107, 964, 1044, 925, 713, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 2, 13, 13]
,[0, 0, 2, 12, 6, 4, 6, 6, 9, 8, 4, 18, 17, 8, 23, 0, 0, 0, 0, 0, 0, 0, 0, 82, 6, 328, 964, 870, 751, 887, 862, 882, 784, 888, 888]]

counters['WashingtOnline'] = [[0, 0, 59, 1728, 1837, 2427, 2439, 2664, 2545, 2435, 2198, 1951, 1940, 1629, 1549, 1659, 1591, 2, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 1, 7, 7]
,[0, 0, 1, 1, 1, 0, 0, 0, 20, 6, 4, 25, 54, 51, 70, 125, 280, 3, 0, 0, 0, 0, 0, 214, 455, 464, 590, 593, 387, 386, 534, 610, 563, 402, 402]]

counters['TodayNYCity'] = [[0, 0, 0, 2339, 2714, 2842, 3525, 3889, 4032, 4095, 3968, 3769, 3534, 2901, 2977, 2435, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 21, 0, 4, 17, 17]
,[0, 0, 0, 0, 0, 0, 1, 0, 4, 1, 22, 12, 8, 8, 3, 23, 0, 0, 0, 0, 0, 0, 0, 148, 524, 1270, 1803, 1710, 1549, 1856, 1898, 2066, 2057, 2407, 2407]]

counters['OnlineCleveland'] = [[0, 0, 0, 335, 859, 775, 806, 1015, 946, 888, 831, 946, 273, 711, 816, 968, 611, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 7],
[0, 0, 0, 0, 0, 0, 0, 0, 477, 864, 735, 587, 169, 536, 564, 441, 267, 9, 2, 0, 0, 0, 0, 166, 261, 210, 1533, 1705, 1562, 1675, 1652, 1713, 1143, 1034, 1034]]

counters['SanAntoTopNews'] = [[0, 0, 48, 996, 547, 667, 987, 1137, 964, 959, 864, 775, 837, 803, 765, 781, 852, 813, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 1, 13, 13]
,[0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 0, 4, 6, 5, 64, 61, 91, 44, 0, 0, 0, 0, 0, 266, 435, 378, 727, 728, 665, 822, 718, 820, 711, 813, 813]]


counters['PhoenixDailyNew'] = [[0, 0, 0, 1103, 1357, 1322, 1289, 1475, 1449, 1416, 1187, 1001, 1011, 897, 910, 911, 936, 1100, 1022, 624, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 6]
,[0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 2, 9, 17, 26, 91, 133, 13, 0, 0, 0, 243, 465, 577, 424, 785, 790, 882, 896, 859, 764, 879, 879]]

counters['TodayMiami'] = [[0, 0, 25, 462, 135, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 1, 13, 13]
,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 358, 784, 942, 682, 810, 788, 833, 769, 940, 940]]

counters['Atlanta_Online'] = [[0, 0, 57, 380, 330, 312, 369, 1234, 1083, 1136, 823, 235, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9]
,[0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 4, 6, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 342, 58, 2, 368, 470, 431, 525, 465, 500, 455, 263, 263]]

counters['Baltimore0nline'] = [[0, 0, 0, 0, 0, 0, 0, 0, 535, 1231, 1511, 1214, 1120, 690, 395, 483, 500, 1, 2, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 3, 9, 9]
,[0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 19, 38, 376, 509, 771, 775, 4, 1, 0, 0, 0, 0, 483, 476, 167, 1123, 1278, 1140, 822, 473, 511, 554, 399, 399]]

counters['OaklandOnline'] = [[0, 0, 0, 0, 0, 0, 0, 0, 517, 1443, 1113, 721, 736, 669, 730, 816, 733, 848, 794, 1017, 871, 717, 0, 88, 21, 0, 0, 0, 0, 0, 0, 0, 2, 7, 7]
,[0, 0, 0, 0, 0, 0, 0, 0, 133, 368, 299, 192, 191, 168, 202, 233, 307, 288, 241, 246, 210, 175, 0, 0, 0, 4, 65, 22, 15, 32, 17, 12, 20, 22, 22]]

counters['StLouisOnline'] = [[0, 0, 0, 0, 0, 0, 0, 0, 383, 1868, 1582, 1415, 1401, 1302, 1238, 1120, 1155, 1322, 1335, 1319, 610, 0, 0, 473, 175, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6]
,[0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 15, 21, 33, 58, 71, 77, 54, 42, 22, 12, 0, 0, 169, 460, 111, 605, 670, 641, 818, 796, 836, 839, 779, 779]]
