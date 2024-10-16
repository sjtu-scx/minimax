def process_operations(s, q, tp):
    max_length = 0
    upper_count = [0]
    lower_count = [0]
    for char in s:
        upper_count.append(upper_count[-1] + (1 if char.isupper() else 0))
        lower_count.append(lower_count[-1] + (1 if char.islower() else 0))
    print(len(upper_count), len(lower_count))
    for _ in range(q):
        t, p = tp[_]
        p = int(p)
        
        s = s[:p] + t + s[p:]
        for start in range(len(s)):
            for end in range(start, len(s)-1):
                upper_sub_count = upper_count[end + 1] - upper_count[start]
                lower_sub_count = lower_count[end + 1] - lower_count[start]
                if abs(upper_sub_count - lower_sub_count) % 2 == 0:
                    max_length = max(max_length, end - start + 1)
    return max_length

s = 'AA'
q = 2
tp = [('Ab', 1), ('c', 2)]
print(process_operations(s, q, tp))