from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
lines = text.splitlines()
for i in range(1924, 1936):
    print(f'{i+1}: {repr(lines[i])}')
# Replace the malfunctioning optional chaining line if present
old = "if (data ? .choices ? .[0] ? .message ? .content) {"
new = "if (data?.choices?.[0]?.message?.content) {"
if old in text:
    print('FOUND OLD LINE')
    p.write_text(text.replace(old, new), encoding='utf-8')
else:
    print('OLD LINE NOT FOUND')
