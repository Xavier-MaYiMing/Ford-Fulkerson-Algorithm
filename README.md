### Ford-Fulkerson Algorithm

##### Reference: Ford, L. R.; Fulkerson, D. R. (1956). Maximal flow through a network. Canadian Journal of Mathematics. 8: 399–404.

The Ford-Fulkerson algorithm for the maximum flow problem

| Variables   | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| network     | The residual graph, network\[i\]\[j\] is the residual flow from node i to node j (list) |
| source      | The source node                                              |
| destination | The destination node                                         |
| nn          | The number of nodes                                          |
| max_flow    | The maximum flow                                             |
| pred_node   | pred_node[i] = j means node j is the predecessor node of node i in the augmenting path (list) |

#### Example

![](https://github.com/Xavier-MaYiMing/Ford-Fulkerson-Algorithm/blob/main/maximum%20flow%20problem.png)

```python
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
```

##### Output

```python
11  # The maximum flow is 11
```

