function shortestPath(s, v) {
    if (s === v) {
        return 0;
    } else {
        
    }
}

function getAdjacent(graph, node) {
    const getAdjNodes = function(add, adj, node) {
        if (adj === 1) {
            acc.push(node);
        }
    }
    return graph[node].reduce(getAdjNodes, []);
}

function getGraph() {
    return [
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
}