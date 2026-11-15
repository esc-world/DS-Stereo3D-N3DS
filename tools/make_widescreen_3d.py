#!/usr/bin/env python3
"""Make the stereo-3D Widescreen.cxi from YOUR OWN TWPatch widescreen TwlBg.

usage:  python make_widescreen_3d.py <your Widescreen.cxi> <output Widescreen.cxi>

The input is the file TWPatch made on your console (sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi, the same file as
sd:/luma/sysmodules/TwlBg.cxi). This script contains no Nintendo code: it unpacks the code of your file, checks that it
is the exact build the patch was made for, changes 630 bytes in 30 places and packs the file again.
If your file is a different build (other system version, other TWPatch version or options) the script stops
without writing anything.
"""
import hashlib, struct, sys

BASE_CODE_SHA256 = '0b7aaca07c957df6093342a5c33c84dbc54af70d58c4264805b26963d3ce5afb'      # decompressed .code of the supported TWPatch build
OUT_CODE_SHA256 = '43b77aa4c471174369f130d548ad128b31838ac449c2d490cbb641de200742f7'       # the same code with the patch (build "stereo29")
REF_OUT_SHA256 = '052bfa98621c4185bec7b9dbd1d07ef4f24605d43e67e763f6646e8b4271f8f2'        # output file when the input is byte-identical to the author's
PATCH = [
    (0x9F0, '0000000010b50a4b0b600df67bfc0ba402e0c0460000000009cc002801d00360fae710bd0000000000000000000000000200220300000000000000002404f01e3b03000000000000000000000000000000000000000000000000000000'),
    (0x4924, 'cf208000'),
    (0x4946, 'c925ad00'),
    (0x4A2A, 'fbf7e3ff'),
    (0x4DD0, '24032803'),
    (0x215F2, 'c5208001c019c17f8c430e43817f0c43'),
    (0x218FA, 'c8'),
    (0x22D88, '1df098f8'),
    (0x22E24, '0be0c046ec109fe5001091e5001081e0481081e2b76200eac046'),
    (0x22EB0, '10b5406b00680cf00cee10bd000e043000091fe0'),
    (0x22EFC, '00b5e06b0002dbe70c214843a16c884202d0a0641cf0bdffa16a304600bdc046c8a41200'),
    (0x23FB4, '1bf04dff'),
    (0x2451C, '214b18680130186081070cd10120009001a90322082305f09efc002803d001a80078194b1871184b00221868042803d31879102800d20122da71587b002806d001385873032817d10021002212e01868400a11d01879197b411a07310e290bd91873c02101408206920f1143303106205873f3229973da73034bda7902b002bc002a00d0214600bdb8a412000000000000000000'),
    (0x25074, '20'),
    (0x2A25C, '15f0d6fdc046c046c0'),
    (0x30E1C, 'c046c046'),
    (0x30EB0, 'c046c046'),
    (0x30EBA, 'c046c046'),
    (0x3B918, '429dffea'),
    (0x3FE08, '000000000a4b1b6801200a4a0399002900d10432834204d1516d002906d1214604e02146946a002c00d10c4604e0000094a412004004f01e02b582b0184bdb795b420be0'),
    (0x3FE50, '0000e168496dc907c90f40184008216908607047114812490a460193f1f78ef80d4bd8799979002803d1132904d2013102e0002900d001399971e4f747fb7746084d2878002803d028460121eef7befb2846eef7a7fb3847b8a412002070c41e00080008c8c31200f810000000b52346ff337d33196a1868421a00d001226261e3f714f800bd'),
    (0x4009B, '00'),
    (0x46408, '3b03'),
    (0x46410, '22030000220300002203'),
    (0x46424, '22032603'),
    (0x4643E, '220320'),
    (0x46C28, '3b03'),
    (0x46C30, '22030000220300002203'),
    (0x46C44, '22032603'),
    (0x46C5E, '2203'),
]


def blz_decompress(data):
    """3DS ExeFS .code backward LZ"""
    data = bytearray(data)
    top_bottom, extra = struct.unpack_from('<II', data, len(data) - 8)
    enc_size, header_len = top_bottom & 0xFFFFFF, top_bottom >> 24
    out = bytearray(len(data) + extra)
    out[:len(data)] = data
    src, end, dst = len(data) - header_len, len(data) - enc_size, len(out)
    while src > end:
        src -= 1
        flags = out[src]
        for _ in range(8):
            if src <= end: break
            if flags & 0x80:
                src -= 2
                v = out[src] | (out[src + 1] << 8)
                disp = (v & 0xFFF) + 3
                for _ in range((v >> 12) + 3):
                    dst -= 1
                    out[dst] = out[dst + disp]
            else:
                src -= 1; dst -= 1
                out[dst] = out[src]
            flags = (flags << 1) & 0xFF
    return bytes(out)


def main():
    if len(sys.argv) != 3:
        print(__doc__); return 1
    d = open(sys.argv[1], 'rb').read()
    if d[0x100:0x104] != b'NCCH':
        print('error: not a .cxi (NCCH) file'); return 1
    eo = struct.unpack_from('<I', d, 0x1A0)[0] * 0x200                      # ExeFS
    name, off, size = struct.unpack_from('<8sII', d, eo)
    if name.rstrip(b'\0') != b'.code':
        print('error: no .code in the ExeFS'); return 1
    raw = d[eo + 0x200 + off:eo + 0x200 + off + size]
    code = blz_decompress(raw) if d[0x200 + 0xD] & 1 else raw
    h = hashlib.sha256(code).hexdigest()
    if h == OUT_CODE_SHA256:
        print('this file already is the stereo-3D build - nothing to do'); return 1
    if h != BASE_CODE_SHA256:
        print('error: this TwlBg is not the build the patch was made for (code sha256 %s...).' % h[:16])
        print('       Nothing was written. See the README (requirements).'); return 1
    code = bytearray(code)
    for o, hx in PATCH:
        b = bytes.fromhex(hx); code[o:o + len(b)] = b
    code = bytes(code)
    assert hashlib.sha256(code).hexdigest() == OUT_CODE_SHA256
    pad = (len(code) + 0x1FF) & ~0x1FF
    hdr = bytearray(0x200)
    hdr[0:8] = b'.code\0\0\0'
    struct.pack_into('<II', hdr, 8, 0, len(code))
    hdr[0xC0 + 9 * 0x20:0xC0 + 10 * 0x20] = hashlib.sha256(code).digest()
    out = bytearray(d[:eo]) + hdr + code + bytes(pad - len(code))
    out[0x200 + 0xD] &= ~1                                                 # exheader: code not compressed
    out[0x160:0x180] = hashlib.sha256(out[0x200:0x600]).digest()           # exheader hash
    struct.pack_into('<I', out, 0x1A4, (0x200 + pad) // 0x200)             # ExeFS size
    struct.pack_into('<I', out, 0x1A8, 1)                                  # ExeFS hash region
    out[0x1C0:0x1E0] = hashlib.sha256(out[eo:eo + 0x200]).digest()
    struct.pack_into('<I', out, 0x104, len(out) // 0x200)                  # content size
    open(sys.argv[2], 'wb').write(out)
    ho = hashlib.sha256(out).hexdigest()
    print('written: %s (%d bytes, sha256 %s...)' % (sys.argv[2], len(out), ho[:16]))
    print('identical to the reference build' if ho == REF_OUT_SHA256 else
          'note: the code is the reference build; the file header differs from the author\'s file (that is fine)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
