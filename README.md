# list-of-list-to-nested-json-converter-

# This script converts the list of list into proper nested json format

##Example:  

This is sample for list of list categories:  

categories = [
    ["main_category_1", "sub_category_1"],
    ["main_category_1", "sub_category_2"],
    ["main_category_1", "sub_category_2", "sub_category_2_1", "sub_category_2_1_1"],
    ["main_category_1", "sub_category_2", "sub_category_2_2"],
    ["main_category_1", "sub_category_3", "sub_category_3_1", "sub_category_3_1_1", "sub_category_3_1_1_1"],

    ["main_category_2", "sub_category_1", "sub_category_1_1"],
    ["main_category_2", "sub_category_2", "sub_category_2_1", "sub_category_2_1_1", "sub_category_2_1_1_1",
     "sub_category_2_1_1_1_1"],
    ["main_category_2", "sub_category_3"],
    ["main_category_2", "sub_category_4", "sub_category_4_1", "sub_category_4_1_1"],
    ["main_category_3"]
]  

The script converts the above list of list into following proper nested json format  

[
    {
        "category": "main_category_1",
        "sub_category": [
            {
                "name": "sub_category_1",
                "sub_category": []
            },
            {
                "name": "sub_category_2",
                "sub_category": [
                    {
                        "name": "sub_category_2_1",
                        "sub_category": [
                            {
                                "name": "sub_category_2_1_1",
                                "sub_category": []
                            }
                        ]
                    },
                    {
                        "name": "sub_category_2_2",
                        "sub_category": []
                    }
                ]
            },
            {
                "name": "sub_category_3",
                "sub_category": [
                    {
                        "name": "sub_category_3_1",
                        "sub_category": [
                            {
                                "name": "sub_category_3_1_1",
                                "sub_category": [
                                    {
                                        "name": "sub_category_3_1_1_1",
                                        "sub_category": []
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "category": "main_category_2",
        "sub_category": [
            {
                "name": "sub_category_1",
                "sub_category": [
                    {
                        "name": "sub_category_1_1",
                        "sub_category": []
                    }
                ]
            },
            {
                "name": "sub_category_2",
                "sub_category": [
                    {
                        "name": "sub_category_2_1",
                        "sub_category": [
                            {
                                "name": "sub_category_2_1_1",
                                "sub_category": [
                                    {
                                        "name": "sub_category_2_1_1_1",
                                        "sub_category": [
                                            {
                                                "name": "sub_category_2_1_1_1_1",
                                                "sub_category": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "name": "sub_category_3",
                "sub_category": []
            },
            {
                "name": "sub_category_4",
                "sub_category": [
                    {
                        "name": "sub_category_4_1",
                        "sub_category": [
                            {
                                "name": "sub_category_4_1_1",
                                "sub_category": []
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "category": "main_category_3",
        "sub_category": []
    }
]

