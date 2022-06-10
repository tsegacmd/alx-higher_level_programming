#!/usr/bin/python

def search_replace(my_list,search,replace):
return list(map(lambda e:replace if e==search else e,mylist))
