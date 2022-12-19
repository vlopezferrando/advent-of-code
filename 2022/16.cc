#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int N;
vector<int> FLOW;
vector<vector<int>> D;

// Part 1

unordered_map<int, int> mem;

int solve(int t, int v, int opened) {
  if (t <= 0 or opened & (1<<v))
    return 0;
  int id = (opened << 10) | (t << 5) | v;
  if (mem.find(id) != mem.end())
    return mem[id];

  int ret = 0;
  for (int i = 1; i < N; ++i)
    if (v == 0)
      ret = max(ret, solve(t - D[v][i], i, opened));
    else
      ret = max(ret, (t-1)*FLOW[v] + solve((t-1) - D[v][i], i, opened | (1<<v)));
  return mem[id] = ret;
}

// Part 2

unordered_map<uint64_t, int> mem2;

inline bool pending(int a, int b, int opened) {
  return (opened & ((1<<a) | (1<<b))) == 0;
}

int solve2(int ta, int tb, int a, int b, uint64_t opened) {
  if (ta < tb) {
    swap(ta, tb);
    swap(a, b);
  }

  uint64_t id = (opened << 20) | (ta << 15) | (tb << 10) | (a << 5) | b;
  if (mem2.find(id) != mem2.end())
    return mem2[id];

  int ret = 0;
  for (int i = 1; i < N; ++i)
    if (a == 0 and pending(i, b, opened))
      ret = max(ret, solve2(ta - D[a][i], tb, i, b, opened));
    else if (a != 0 and i != a and i != b and ta > D[a][i] + 2 and pending(i, b, opened | (1<<a)))
      ret = max(ret, solve2(ta - 1 - D[a][i], tb, i, b, opened | (1<<a)));

  if (ret == 0)
    ret = solve(tb, b, opened);

  return mem2[id] = ret + (ta-1)*FLOW[a];
}

int main() {
  // Read graph
  cin >> N;
  FLOW = vector<int>(N);
  for (int i = 0; i < N; ++i)
    cin >> FLOW[i];

  D = vector<vector<int>>(N);
  for (int i = 0; i < N; ++i) {
    D[i] = vector<int>(N);
    for (int j = 0; j < N; ++j)
      cin >> D[i][j];
  }

  // Solve
  int p1 = solve(30, 0, 0);
  assert(p1 == 2320);
  int p2 = solve2(26, 26, 0, 0, 0);
  assert(p2 == 2967);
}

