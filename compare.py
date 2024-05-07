#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kayma
#
# Created:     07-05-2024
# Copyright:   (c) kayma 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


d1 = {'A1':'india','A2':'india' ,'A3':'america','A4':'india' ,'A5': {'1': ['A1','A2','A4','A6'], '2': ['A3','A7'] ,'3': ['A5'] },'A6': 'india','A7': 'america' }
d2 = {'A1':'india','A2':'india' ,'A3':'americax','A4':'india' ,'A5': {'1': ['A1','A4','A6'], '2': ['A3','A7','A8'] ,'3': ['A5'] },'A7': 'america', 'A9': 'va' }

from deepdiff import DeepDiff

def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same

print('----')

diff = DeepDiff(d1, d2)
for each in diff:
    print ('{} = {}'.format(each,diff[each]))

print('----')

dif2 = dict_compare(d1,d2)
print('Added: {}'.format(dif2[0]))
print('Removed: {}'.format(dif2[1]))
print('Modified: {}'.format(dif2[2]))


##----
##dictionary_item_added = [root['A9']]
##dictionary_item_removed = [root['A6']]
##values_changed = {"root['A3']": {'new_value': 'americax', 'old_value': 'america'}}
##iterable_item_added = {"root['A5']['2'][2]": 'A8'}
##iterable_item_removed = {"root['A5']['1'][1]": 'A2'}
##----
##Added: {'A6'}
##Removed: {'A9'}
##Modified: {'A3': ('america', 'americax'), 'A5': ({'1': ['A1', 'A2', 'A4', 'A6'], '2': ['A3', 'A7'], '3': ['A5']}, {'1': ['A1', 'A4', 'A6'], '2': ['A3', 'A7', 'A8'], '3': ['A5']})}



