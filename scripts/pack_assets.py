"""Packs many small files (libs, fonts, sprites) into one blob + JSON index for serving with HTTP ranges."""
import json, os, sys
root, out_bin, out_idx = sys.argv[1], sys.argv[2], sys.argv[3]
idx, off = {}, 0
with open(out_bin, 'wb') as f:
    for dp, _, fs in os.walk(root):
        for fn in sorted(fs):
            p = os.path.join(dp, fn); rel = os.path.relpath(p, root).replace(os.sep, '/')
            data = open(p, 'rb').read(); f.write(data); idx[rel] = [off, len(data)]; off += len(data)
json.dump(idx, open(out_idx, 'w'), separators=(',', ':'))
print(len(idx), 'files,', off, 'bytes')
