#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/6 22:30
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : Ford_Fulkerson.py
# @Statement : The Ford-Fulkerson algorithm for the maximum flow problem
# @Reference :  Ford, L. R.; Fulkerson, D. R. (1956). Maximal flow through a network. Canadian Journal of Mathematics. 8: 399–404.


def main(network, source, destination):
    """
    The main function of the Ford-Fulkerson algorithm
    :param network: residual graph
    :param source: the source node
    :param destination: the destination node
    :return:
    """
    # Step 1. Initialization
    nn = len(network)  # node number
    max_flow = 0  # the maximum flow
    pred_node = [-1] * nn  # predecessor node

    # Step 2. The main loop
    while True:
        visited = [0] * nn
        queue = [source]
        visited[source] = 1

        # Step 2.1. Find the augmenting path
        while queue:
            node = queue.pop()
            for next_node, val in enumerate(network[node]):
                if visited[next_node] == 0 and val > 0:
                    queue.append(next_node)
                    visited[next_node] = 1
                    pred_node[next_node] = node

        # Step 2.2. Termination judgement: if there is no augmenting path, the maximum flow is found
        if visited[destination] == 0:
            break

        # Step 2.3. Calculate the augmenting flow
        flow = float('inf')
        node = destination
        while node != source:
            flow = min(flow, network[pred_node[node]][node])
            node = pred_node[node]
        max_flow += flow

        # Step 2.4. Update the residual graph
        node = destination
        while node != source:
            network[node][pred_node[node]] += flow
            network[pred_node[node]][node] -= flow
            node = pred_node[node]
    return max_flow


if __name__ == '__main__':
    test_network = [
        [0, 5, 4, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 3, 0, 0],
        [0, 0, 0, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0, 2, 0],
        [0, 5, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    s = 0
    d = 7
    print(main(test_network, s, d))
