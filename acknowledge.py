from config import s
try:
    from config import h
except ImportError:
    h = '以下为本文致谢名单（排名不分先后，以字符串（UTF-8 编码）字典序为准）:'

l = [i.replace('&', '\\&').replace('~', '\\textasciitilde') for i in sorted(
    [i.replace('-', ' ') for i in s.split(' ')], key=lambda x: x.replace('-', ' ').lower()
)]

m = 5
t4 = '    '
par = '\\par '
ans = '\\acknowledgement{\n'
ans += t4 + par + h + '\n\n'
ans += t4 + '\\begin{center}\n'
ans += t4 + '\\begin{tabular}{' + 'c' * m + '}\n'
for i, n in enumerate(l):
    if i % m == 0:
        ans += t4 * 2
    ans += n
    if i % m == m - 1:
        ans += ' \\\\\n'
    else:
        ans += ' & '
if len(l) % m != 0:
    ans += '\\\\\n'
ans += t4 + '\\end{tabular}\n'
ans += t4 + '\\end{center}\n\n'
ans += t4 + par + 'And you.'
ans += '\n}\n'

open('data/acknowledge.tex', 'wb').write(ans.encode('utf8'))
