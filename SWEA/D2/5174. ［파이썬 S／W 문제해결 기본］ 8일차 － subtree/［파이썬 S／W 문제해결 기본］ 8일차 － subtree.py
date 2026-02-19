# 전위 순회
def preorder(node):
    nodes = []
    if node != 0:
        nodes.append(node)
        nodes += preorder(tree[node][0])
        nodes += preorder(tree[node][1])
    return nodes


T = int(input())
for tc in range(1, T + 1):
    # V = int(input())  # 정점의 수
    # E = int(input())  # 간선의 수
    E , N = map(int, input().split())
    V = E + 1
    arr = list(map(int, input().split()))
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    parents = [0] * (V + 1)

    tree = [[0] * 3 for _ in range(V + 1)]
    # 0번 인덱스: 좌측노드, 1번 인덱스: 우측노드, 2번 인덱스 부모
    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i + 1]
        parents[child] = parent
        tree[child][2] = parent
        if left[parent] == 0:  # if tree[0][parent] == 0:
            left[parent] = child
            tree[parent][0] = child
        else:
            right[parent] = child
            tree[parent][1] = child

    # print(left)
    # print(right)
    # print(parents)
    #
    # pprint.pprint(tree)

    # root 찾기
    # c = V
    # # 부모 노드가 0이 아니면
    # while tree[c][2] != 0:
    #     c = tree[c][2]
    # print(c)

    subtrees = preorder(N)
    print(f"#{tc} {len(subtrees)}")