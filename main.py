from hashlib import md5
from random import sample
from html2image import Html2Image
from tqdm import tqdm
hti = Html2Image(size=(301, 319), output_path='./lots')

f = open('static/index.html', 'r')
html = f.read();
f.close()

f = open('static/style.css', 'r')
css = f.read()
f.close()

hashes = []

for i in tqdm(range(160)):
    randsINT = sample(range(1, 100), 16)
    rands = list(map(str, randsINT))
    rands.append("Karpinsk")
    lotHash = md5(''.join(rands).encode('utf-8')).hexdigest()
    hashes.append(lotHash)
    html_t = html
    for j in range(1, 17):
        html_t = html_t.replace(f'\{j:03d}', rands[j - 1]).replace('\hash', lotHash+f' {randsINT[3]+randsINT[7]+randsINT[11]+randsINT[15]}')
    hti.screenshot(html_str=html_t, css_str=css, save_as=f'{i:03d}.png')

hashes = map(lambda x: x+'\n', hashes)
open('hashes.txt', 'w').writelines(hashes)