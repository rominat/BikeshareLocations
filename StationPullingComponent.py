# -*- coding: utf-8 -*-

def find_nearby_stations(dictionary, given_terminal, given_distance):
    result_list = []
    for k, v in dictionary.items():
        if v < given_distance and k[1] == given_terminal:
            result_list.append(k[0])
        elif v < given_distance and k[0] == given_terminal:
            result_list.append(k[1])

    return result_list

