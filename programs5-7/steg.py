import os
import sys
import re

DEBUG = False
if DEBUG:
    log = open('if DEBUG \r log.txt','w')
    for i in sys.argv[1:]:
        log.write(i[:2] + '\r')
        log.write(i[2:] + '\r')
    

store = False
bitmode = False
wrapper = object
hidden = object
offset = 0
interval = 1
for i in sys.argv[1:]:
    if i[:2] == "-s" and i[:2] != "-r":
        store = True
    if i[:2] == "-b" and i[:2] != "-B":
        bitmode = True
    if i[:2] == "-o":
        offset = int(i[2:])
    if i[:2] == "-i":
        interval = int(i[2:])
    if i[:2] == "-w":
        wrapper = open(str(i[2:]),"rb")
    if i[:2] == "-h":
        hidden = open(str(i[2:]),"rb")

wrapper = wrapper.read()
wrapper = bytearray(wrapper)
if store:
    hidden = hidden.read()
    hidden = bytearray(hidden)
sentinal = b'\x00\xff\x00\x00\xff\x00'

if DEBUG:
    log.write('length of wrapper: ' + str(len(wrapper)) + '\r')

fp = os.fdopen(sys.stdout.fileno(),'wb')
end = 0

def compare_list(l1 = [], l2 = []):
    for i,j in zip(l1,l2):
        if i != j:
            return False
    return True

if not store:
    if not bitmode:
        bytes_ = []
        if DEBUG:
            log.write('end: ' + str(end) + '\r')
        for B in range(offset, len(wrapper), interval):
            bytes_.append(wrapper[B])
            if len(bytes_) > 6:
                if compare_list(bytes_[-6:],sentinal):
                    fp.write(bytes(bytes_[:-6]))
    if bitmode:
        bytes_ = []
        end = len(wrapper)
        for b in range(offset, end, interval * 8):
            bits = 0
            for i in range(b, b + 8 * interval, interval):
                bits = (bits << 1) & (2**8 - 1)
                bits |= wrapper[i] & 1
            bytes_.append(bits)
            if DEBUG:
                log.write(str(bits) + ":")
            if len(bytes_) > 6:
                if compare_list(bytes_[-6:], sentinal):
                    fp.write(bytes(bytes_[:-6]))
                    break

if store:
    if not bitmode:
        for h in hidden:
            wrapper[offset] = h
            offset += interval
        for s in sentinal:
            wrapper[offset] = s
            offset += interval
        fp.write(wrapper)
    if bitmode:
        for i in hidden:
            B = i
            for b in range(8):
                wrapper[offset] &= 254
                wrapper[offset] |= ((B & (1<<7)) >> 7)
                B = B<<1 & (2**8 - 1)
                offset += interval
        for i in sentinal:
            B = i
            for b in range(8):
                wrapper[offset] &= 254
                wrapper[offset] |= ((B & (1<<7)) >> 7)
                B = B<<1 & (2**8 - 1)
                offset += interval
        fp.write(wrapper)