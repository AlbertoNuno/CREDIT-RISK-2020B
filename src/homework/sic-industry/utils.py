# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:51:11 2020

@author: Esteban
"""

import json
from difflib import SequenceMatcher

class StringWrapper:
    """
    This is the string wrapper.
    """

    def __init__(self, value: str, case_sensitive: bool = False):
        self._value = value
        self.case_sensitive = case_sensitive

    def _sensitivity_matching(self, string: str) -> str:
        return string if self.case_sensitive else string.lower()

    @property
    def value(self) -> str:
        return self._sensitivity_matching(string=self._value)

    def contains(self, pattern: str, reverse: bool = False):
        pattern = self._sensitivity_matching(string=pattern)
        return (pattern in self.value) if not reverse else (self.value in pattern)

    def similarity_ratio(self, pattern: str) -> float:
        pattern = self._sensitivity_matching(string=pattern)
        return SequenceMatcher(None, self.value, pattern).ratio()

    def similar_enough(self, pattern: str, threshold: float) -> bool:
        pattern = self._sensitivity_matching(string=pattern)
        return self.similarity_ratio(pattern) > threshold

    def boolean_search(self, pattern: str, exact: bool, threshold: float, reverse: bool = False):
        pattern = self._sensitivity_matching(string=pattern)
        return self.contains(pattern, reverse=reverse) if exact \
            else self.similar_enough(pattern, threshold=threshold)

with open('industries.json', "r") as f:
    content = f.read()
dictionary = json.loads(content)

def last_level(dictionary):
    while dictionary['children'] != []:
        n = len(dictionary['children'])
        level = [dictionary['children'][i]['title'] 
                 for i in range(n)]
        dictionary = dictionary['children'][0]
    return  level

#if StringWrapper(title).boolean_search(pattern = title, exact = True, threshold = 0.5):
			#print("YES")



#%%

dictionari = {
    "title": "SIC",
    "children": [
        {
            "title": "Division A: Agriculture, Forestry, And Fishing",
            "children": [
                {
                    "title": "Major Group 01: Agricultural Production Crops",
                    "children": [
                        {
                            "title": "Industry Group 011: Cash Grains",
                            "children": [
                                {
                                    "title": "0111 Wheat",
                                    "children": []
                                },
                                {
                                    "title": "0112 Rice",
                                    "children": []
                                },
                                {
                                    "title": "0115 Corn",
                                    "children": []
                                },
                                {
                                    "title": "0116 Soybeans",
                                    "children": []
                                },
                                {
                                    "title": "0119 Cash Grains, Not Elsewhere Classified",
                                    "children": []
                                }
                            ]
                        },
                        {
                            "title": "Industry Group 013: Field Crops, Except Cash Grains",
                            "children": [
                                {
                                    "title": "0131 Cotton",
                                    "children": []
                                },
                                {
                                    "title": "0132 Tobacco",
                                    "children": []
                                },
                                {
                                    "title": "0133 Sugarcane and Sugar Beets",
                                    "children": []
                                },
                                {
                                    "title": "0134 Irish Potatoes",
                                    "children": []
                                },
                                {
                                    "title": "0139 Field Crops, Except Cash Grains, Not Elsewhere Classified",
                                    "children": []
                                }
                            ]
                        }
					]
				}
			]
		}
	]
}
							
#%%
def match(dic_title: str, pattern: str, exact: bool, threshold: float = 0.5) -> bool:
	return StringWrapper(dic_title).boolean_search(pattern = pattern, exact = exact, threshold = threshold)





def titles_dictionary(dictionary: dict, title: str, exact: bool, final_titles: list, all_titles: list):
	
	title_dic = dictionary['title']
	all_titles.append(title_dic)
	
	if match(title_dic, title, True):
		final_titles.append(title_dic)
		
	if not dictionary['children'] == []:
		for i in range(len(dictionary['children'])):
			 titles_dictionary(dictionary['children'][i], title, exact, final_titles, all_titles)

	return final_titles, all_titles



def return_title(word_search, till, all_titles):
	short_list = all_titles[::-1]
	for i in short_list:
		if i[:till] == word_search:
			return i
	#return next(i for i in short_list if i[:till] == word_search)



def construir(a_title, final_titles, all_titles, final_dict):

	find_in = all_titles[:all_titles.index(a_title)]
	global dic
	if a_title.startswith('Division'):
		if final_dict != {}:
			dic = final_dict
		else:
			dic = final_dict
			
		return dictionary
	
	elif a_title.startswith('Major Group'):
		division = return_title('Division', 8, find_in)
		
		if division in final_titles:
			final_dict["children"] = [{"title": a_title}]
			
		elif final_dict != {}:
			final_dict = {"title": division , "children": [final_dict]}
			construir(division, final_titles, all_titles, final_dict)
		else:
			final_dict["children"] = {"title": division, "children": [{"title": a_title}]}
			construir(division, final_titles, all_titles, final_dict)
			
	elif a_title.startswith('Industry Group'):
		major_group = return_title('Major Group', 11, find_in)
		
		if major_group in final_titles:
			final_dict["children"] = [{"title": a_title}]
			
		elif final_dict != {}:
			final_dict = {"title": major_group , "children": [final_dict]}
			construir(major_group, final_titles, all_titles, final_dict)
		else:
			construir(major_group, final_titles, all_titles, final_dict)
			final_dict["children"] = {"title": major_group , "children": [{"title": a_title, "children": []}]}
	else:
		ind_group = return_title('Industry Group', 14, find_in)
		lista_children = {"title": ind_group , "children": [{"title": a_title, "children": []}]}
		construir(ind_group, final_titles, all_titles, lista_children)
		return dic



def final_search(dictionary, title, exact):
	final_titles, all_titles = titles_dictionary(dictionary, title, False, [], [])
	answer = [construir(i, final_titles, all_titles, {}) for i in final_titles]
	final_answer = filter(None.__ne__, answer)
	return {final_answer}

title = "aquaculture"
#title = 'cash'
ans = final_search(dictionary, title, False)
	
	