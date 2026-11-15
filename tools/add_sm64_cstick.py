#!/usr/bin/env python3
"""Super Mario 64 DS: add Circle Pad / C-stick / ZL / ZR to the stereo-3D file.

usage:  python add_sm64_cstick.py <ASMK-53AF.bin of this package> <shocoman's AR code text> <output ASMK-53AF.bin>

The Circle Pad patch is shocoman's "Analog Controls for NDS Games on 3DS"
(https://github.com/shocoman/Analog-Controls-for-NDS-Games-on-3DS). It is not included here. Take the Action Replay
code for the KOREAN version with nub support, "ASMK-3C73EADE ... [with Nub stick, ZL and ZR]", from that repository
and save its code lines (pairs of 8 hex digits) as a text file; other lines in the file are ignored.
This script appends that code to the 3D engine file and changes 76 bytes of it in 2 places (the engine's input
filter is put in front of the patch, and the 3DS-side C-stick read is made lighter so the picture does not hitch).
"""
import hashlib, re, struct, sys

ENGINE_SHA256 = 'b615ae56232b2eb85d436ed5de66bea686579a9755a02527acaddca63d24691b'     # ASMK-53AF.bin of this package (3D only)
CODE_SHA256 = 'a4adaeaebbe5efe341e27f4f010ac0d41361d2d284e2cd8bef347dc6869aa40e'       # shocoman's code as binary (351 lines)
OUT_SHA256 = 'a6f95989475aa299fbcbc07a2369c42eca7592459a3db410ae792b6f898ea9b2'        # result
PATCH = [
    (0x860, 'b510a42068104b1864104a117892781202114309025963c0211a880a431a8001218907401820600cd300230e22072007b4694603310648804707bc1002c9b2084320607fbd00000000'),
    (0xA94, 'a00f00'),
]


def main():
    if len(sys.argv) != 4:
        print(__doc__); return 1
    eng = open(sys.argv[1], 'rb').read()
    h = hashlib.sha256(eng).hexdigest()
    if h == OUT_SHA256:
        print('this file already contains the Circle Pad / C-stick patch'); return 1
    if h != ENGINE_SHA256:
        print('error: %s is not the ASMK-53AF.bin of this package' % sys.argv[1]); return 1
    pairs = re.findall(r'^\s*([0-9A-Fa-f]{8})\s+([0-9A-Fa-f]{8})\s*$', open(sys.argv[2], encoding='utf-8', errors='replace').read(), re.M)
    code = bytearray(b''.join(struct.pack('<II', int(a, 16), int(b, 16)) for a, b in pairs))
    if hashlib.sha256(code).hexdigest() != CODE_SHA256:
        print('error: the code text is not the expected one (%d code lines found, 351 expected).' % len(pairs))
        print('       Use the code "ASMK-3C73EADE ... [with Nub stick, ZL and ZR]" and only that one.'); return 1
    for o, hx in PATCH:
        b = bytes.fromhex(hx); code[o:o + len(b)] = b
    out = eng + bytes(code)
    assert hashlib.sha256(out).hexdigest() == OUT_SHA256
    open(sys.argv[3], 'wb').write(out)
    print('written: %s (%d bytes)' % (sys.argv[3], len(out)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
