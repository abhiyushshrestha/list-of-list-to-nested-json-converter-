import json

class JsonConverter():

    # def __init__(self, response_list):
    #     self.response_list = response_list

    # To create dictionaries for main category
    # {
    #   'category' : 'main_category',
    #   'sub_category': []
    #  }
    def create_main_dict_category(self, category, sub_category = []):
        main_dict = {}
        main_dict['category'] = category
        main_dict['sub_category'] = sub_category
        return main_dict

    # To create dictionaries for sub category
    # {
    #   'name' : 'sub_category',
    #   'sub_category': []
    #  }
    def create_sub_dict_category(self, name, sub_category = []):
        # name = 'Relation'
        sub_dict = {}
        sub_dict['name'] = name
        sub_dict['sub_category'] = sub_category
        # print('sub_dict::', sub_dict)
        return sub_dict

    # This function search and returns index for the main category
    def find_main_category(self, find_dict, current_category):
        flag = 0
        for index, d in enumerate(find_dict):
            # print(index)
            # print(index)
            if d['category'] == current_category:
                current_index = index
                flag = 1
        if flag == 0:
            return 'Null'
        else:
            return current_index

    # This function search and returns index for the sub category
    def find_sub_category(self, find_dict, category, starting_index):
        flag = 0
        for index, d in enumerate(find_dict):
            # print(index)
            # print(index)
            if d['name'] == category[starting_index]:
                current_index = index
                flag = 1
        if flag == 0:
            return 'Null'
        else:
            return current_index

    # This is the main fuction where all the process takes place
    def create_json(self, response):

        # This for loop creates dictionaries for main category if that main category does not exit in a list
        for index in range(len(response)):
            # print(index)

            if index == 0:
                main_dict_category = []
                main_category_list = []

                current_category = response[index][0]
                main_dict_category = [self.create_main_dict_category(current_category, sub_category=[])]
                previous_category = response[index][0]
                main_category_list.append(current_category)
            else:
                current_category = response[index][0]
                previous_category = response[index-1][0]
                if current_category not in main_category_list:
                    main_category_list.append(current_category)
                    main_dict_category.append(self.create_main_dict_category(current_category, sub_category=[]))

            res = response[index]
            main_search_index = self.find_main_category(main_dict_category, current_category)

            # This is done to handle if the list contains only two items in it
            length_response = len(res)
            if length_response == 2:
                length_response = 3

            # This for loop check if the sub catogory exist in the main category or not. If not it creates a dictionaries
            # for sub category otherwise it does not create dictionary for sub category
            for i in range(length_response-1):
                cat = res[i]
                # i = 1
                if i == 0:
                    continue

                length = len(res)
                length1 = length - 1
                starting_index = length - length1
                current_index = self.find_sub_category(main_dict_category[main_search_index]['sub_category'], res, starting_index)

                # this condition checks if the sub category of main category section exist or not. If not it adds that
                # sub category dictionary to its desired location
                if current_index == 'Null':
                    sub_dict_category = self.create_sub_dict_category(cat, sub_category=[])
                    main_dict_category[main_search_index]['sub_category'].append(sub_dict_category)

                    try:
                        current_index = self.find_sub_category(main_dict_category[main_search_index]['sub_category'], res, starting_index)
                        add = ''
                        search_index = current_index
                        add += str([search_index]) + str(['sub_category'])
                        sub_dict_category = str(self.create_sub_dict_category(res[i + 1], sub_category=[]))
                        eval("main_dict_category[main_search_index]['sub_category']" + add).append(eval(sub_dict_category))

                    except(IndexError):
                        print(IndexError)

                else:
                    add = ''

                    # This loop is created to find the exact location where sub category dictionary needs to created and
                    # append that dictionary
                    for loop in range(i):
                        # print(loop)
                        search_index = current_index
                        if loop > 0:
                            dict_new = eval("main_dict_category[main_search_index]['sub_category']" + add)
                            search_index = self.find_sub_category(dict_new, res, loop+1)
                            # loop = 2
                        add += str([search_index])+str(['sub_category'])

                    try:
                        search_index = self.find_sub_category(eval("main_dict_category[main_search_index]['sub_category']"+add), res, i+1)
                    except:
                        break

                    # this condition checks if the sub category exist or not. If not it adds that sub category dictionary
                    # to its desired location
                    if search_index == 'Null':
                        try:
                            sub_dict_category = str(self.create_sub_dict_category(res[i+1], sub_category=[]))
                            eval("main_dict_category[main_search_index]['sub_category']"+ add).append(eval(sub_dict_category))
                        except:
                            print(IndexError)
                    else:
                        continue
        return  main_dict_category

if __name__ == '__main__':
    json_converter = JsonConverter()
    response = [
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
    created_json = json_converter.create_json(response)
    pretty_created_json = json.dumps(created_json, sort_keys = True, indent = 4)
    print(pretty_created_json)



