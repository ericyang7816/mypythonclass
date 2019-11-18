from func import *
fund_A_drug={'code': '123',
             'name': '某医药基金A',
             'shares': [{'code': '002399', 'name': '海普瑞', 'price': 17.23, 'number': 10.79, 'pe': 1442.22},
                    {'code': '600085', 'name': '同仁堂', 'price': 33.35, 'number': 8.26, 'pe': 38.13},
                    {'code': '601607', 'name': '上海医药',	'price': 25.13, 'number': 7.04, 'pe': 17.55} 
                    ]
              }
fund_B_medical={'code': '456',
            'name': '某医疗基金B',
            'shares': [ {'code': '002044', 'name': '美年健康', 'price': 18.52, 'number': 290.00, 'pe': 786.19},
                    {'code': '300003', 'name': '乐普医疗', 'price': 22.58, 'number': 184.53, 'pe': 40.61},
                          {'code': '002223', 'name': '鱼跃医疗',  'price': 21.79, 'number': 86.53, 'pe': 31.06} 
                         ] 
              }
funds = [fund_A_drug, fund_B_medical]

calcAvgPE(funds)
sortedPECode(funds)


