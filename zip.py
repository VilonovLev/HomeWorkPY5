import itertools


def zip(zip_text):
    return [(len(list(g)), k) for k, g in itertools.groupby(zip_text)]


def restored(restored_text):
    return "".join(list(i*j for i, j in restored_text))
