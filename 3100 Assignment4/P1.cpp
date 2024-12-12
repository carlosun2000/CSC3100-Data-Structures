#include <iostream>
#include <vector>
#include <climits>

class MinHeap {
private:
    std::vector<std::pair<int, int>> array;
    int size;

public:
    MinHeap() : size(0) {
        array.push_back(std::make_pair(0, 0));

        for (int i = size / 2; i > 0; --i) {
            percolateDown(i);
        }
    }

    void percolateDown(int hole) {
        if (size != 0) {
            std::pair<int, int> tmp = array[hole];

            while (hole * 2 <= size) {
                int child = hole * 2;

                if (child != size && array[child + 1].first < array[child].first) {
                    child = child + 1;
                }

                if (array[child].first < tmp.first) {
                    array[hole] = array[child];
                } else {
                    break;
                }

                hole = child;
            }

            array[hole] = tmp;
        }
    }

    bool isEmpty() const {
        return size == 0;
    }

    std::pair<int, int> pop() {
        if (isEmpty()) {
            return std::make_pair(-1, -1); 
        }

        std::pair<int, int> data = array[1];
        array[1] = array[size];
        array.pop_back();
        size--;
        percolateDown(1);

        return data;
    }

    void push(int x, int index) {
        size++;
        array.push_back(std::make_pair(0, 0));
        int hole = size;

        while (hole > 1 && x < array[hole / 2].first) {
            array[hole] = array[hole / 2];
            hole = hole / 2;
        }

        array[hole] = std::make_pair(x, index);
    }
};

class Graph {
private:
    int source;
    int end;
    int nrow;
    int ncol;
    std::vector<bool> visited;
    std::vector<int> pointingto;
    std::vector<int> shortestd;

public:
    Graph(int m, int n) : source(-1), end(-1), nrow(m), ncol(n), visited((n * m) + 1, false),
                          pointingto((n * m) + 1, -1), shortestd((n * m) + 1, INT_MAX) {}

    std::vector<int> getNeighbor(int index) {
        int m = nrow;
        int n = ncol;
        std::vector<int> result;

        if (index % n != 1) {
            result.push_back(index - 1);
        }

        if (index % n != 0) {
            result.push_back(index + 1);
        }

        if (index > n) {
            result.push_back(index - n);
        }

        if (index <= n * m - n) {
            result.push_back(index + n);
        }

        return result;
    }

    void parseLine(const std::string& line, int i) {
        int m = nrow;
        int n = ncol;

        for (int j = 0; j < n; ++j) {
            char character = line[j];
            int index = i * n + j + 1;

            if (character == 'i') {
                source = index;
            } else if (character == 'j') {
                end = index;
            } else if (character == 'w') {
                if (index > n) {
                    pointingto[index] = index - n;
                }
            } else if (character == 'a') {
                if (index % n != 1) {
                    pointingto[index] = index - 1;
                }
            } else if (character == 'd') {
                if (index % n != 0) {
                    pointingto[index] = index + 1;
                }
            } else if (character == 's') {
                if (index <= n * m - n) {
                    pointingto[index] = index + n;
                }
            }
        }
    }

    int STPA() {
        shortestd[source] = 0;
        MinHeap Q;

        Q.push(0, source);

        while (!Q.isEmpty()) {
            int u = Q.pop().second;
            visited[u] = true;

            for (int v : getNeighbor(u)) {
                int w = (pointingto[u] == v || u == source) ? 0 : 1;

                if (shortestd[v] > shortestd[u] + w) {
                    shortestd[v] = shortestd[u] + w;
                    Q.push(shortestd[v], v);
                }
            }
        }

        return shortestd[end];
    }
};

int main() {
    int m, n;
    std::cin >> m >> n;

    Graph k(m, n);

    for (int i = 0; i < m; ++i) {
        std::string line;
        std::cin >> line;
        k.parseLine(line, i);
    }

    std::cout << k.STPA() << std::endl;

    return 0;
}