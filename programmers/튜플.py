import re
from collections import Counter
 
def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, _ in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
    
if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{20,111},{111}}"))