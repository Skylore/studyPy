import random

json = {
    'attr_lev_1': {
        'attr_lev2': (
            {
                'attr_lev3': [
                    1,
                    {
                        'some_arr_lev4': [
                            {
                                'some_arr_attr_lev5': 'res_attr24235235'

                            }
                        ]
                    },
                    3,
                    {
                        'deep_attr_lev4': (
                            1,
                            'res_attr)(2341234'
                        )
                    }
                ]
            }
        )
    },
    'attr_lev_2': [
        {
            'attr_lev3': (
                23,
                {
                    'some_attr_lev4': {
                        'new_attr_lev5': {
                            'some_turple': (
                                1,
                                2,
                                'res_attr12341234'

                            )
                        }
                    },
                    'another_attr_lev4': {
                        'final': (
                            'res_attr_p3w589uskdjhf',
                            1,
                            2
                        )
                    }
                }
            )
        }
    ]
}

path = ((
            'attr_lev_1>attr_lev2>attr_lev3>1>some_arr_lev4>0>some_arr_attr_lev5',
            json['attr_lev_1']['attr_lev2']['attr_lev3'][1]['some_arr_lev4'][0]['some_arr_attr_lev5']
        ),
        (
            'attr_lev_1>attr_lev2>attr_lev3>3>deep_attr_lev4>1',
            json['attr_lev_1']['attr_lev2']['attr_lev3'][3]['deep_attr_lev4'][1]
        ),
        (
            'attr_lev_2>0>attr_lev3>1>some_attr_lev4>new_attr_lev5>some_turple>2',
            json['attr_lev_2'][0]['attr_lev3'][1]['some_attr_lev4']['new_attr_lev5']['some_turple'][2]
        ),
        (
            'attr_lev_2>0>attr_lev3>1>another_attr_lev4>final>0',
            json['attr_lev_2'][0]['attr_lev3'][1]['another_attr_lev4']['final'][0]
        )
)


def get_path():
    return path[random.randint(0, 3)]
