class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 深度优先
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }

        min_count = len(bank) + 1

        def dfs(current, count, current_bank):
            nonlocal min_count

            # terminator
            if count > min_count:
                return
            if current == end:
                if count < min_count:
                    min_count = count
                return
            if not current_bank:
                return

            # process
            for i, s in enumerate(current):
                for char in change_map[s]:  # 在i处发生替换 后的新字符串new
                    new = current[:i] + char + current[i + 1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)  # 基因库里移除new
                    # drill down
                    dfs(new, count + 1, current_bank)

                    # reverse state
                    current_bank.add(new)

        dfs(start, 0, bank)

        return min_count if min_count <= len(bank) else -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 广度优先 用队列实现
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }
        queue = [(start, 0)]

        while queue:
            node, step = queue.pop(0)

            if node == end:
                return step

            for i, s in enumerate(node):
                for c in change_map[s]:  # 在i处发生替换 后的新字符串new
                    new = node[:i] + c + node[i + 1:]
                    if new in bank:
                        queue.append((new, step + 1))
                        bank.remove(new)
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 双向广度优先
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i + 1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1
