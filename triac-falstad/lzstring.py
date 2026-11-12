"""compressToEncodedURIComponent do lz-string (porte Python do algoritmo de P. Ouellet)."""

KEY_URI = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-$"


def _compress(uncompressed, bits_per_char, get_char):
    if uncompressed is None:
        return ""
    ctx_dict, ctx_create = {}, {}
    ctx_w = ""
    ctx_enlarge, ctx_size, ctx_numbits = 2, 3, 2
    data, data_val, data_pos = [], 0, 0

    def emit_bits(value, nbits, invert=False):
        nonlocal data_val, data_pos
        for _ in range(nbits):
            if invert:
                data_val = (data_val << 1) | value
                value = 0
            else:
                data_val = (data_val << 1) | (value & 1)
                value >>= 1
            if data_pos == bits_per_char - 1:
                data_pos = 0
                data.append(get_char(data_val))
                data_val = 0
            else:
                data_pos += 1

    def flush_w(w):
        nonlocal ctx_enlarge, ctx_numbits
        if w in ctx_create:
            if ord(w[0]) < 256:
                emit_bits(0, ctx_numbits)
                emit_bits(ord(w[0]), 8)
            else:
                emit_bits(1, ctx_numbits, invert=True)
                emit_bits(ord(w[0]), 16)
            ctx_enlarge -= 1
            if ctx_enlarge == 0:
                ctx_enlarge = 1 << ctx_numbits
                ctx_numbits += 1
            del ctx_create[w]
        else:
            emit_bits(ctx_dict[w], ctx_numbits)
        ctx_enlarge -= 1
        if ctx_enlarge == 0:
            ctx_enlarge = 1 << ctx_numbits
            ctx_numbits += 1

    for ch in uncompressed:
        if ch not in ctx_dict:
            ctx_dict[ch] = ctx_size
            ctx_size += 1
            ctx_create[ch] = True
        ctx_wc = ctx_w + ch
        if ctx_wc in ctx_dict:
            ctx_w = ctx_wc
        else:
            flush_w(ctx_w)
            ctx_dict[ctx_wc] = ctx_size
            ctx_size += 1
            ctx_w = ch

    if ctx_w != "":
        flush_w(ctx_w)

    emit_bits(2, ctx_numbits)          # marca de fim de fluxo

    while True:                         # descarrega o ultimo caractere
        data_val <<= 1
        if data_pos == bits_per_char - 1:
            data.append(get_char(data_val))
            break
        data_pos += 1
    return "".join(data)


def compress_to_encoded_uri_component(text):
    return _compress(text, 6, lambda i: KEY_URI[i])
