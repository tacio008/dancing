#!/usr/bin/env python3
import time
import os

# ANSI code para limpiar pantalla
def clear():
    print("\033[H\033[J", end="")

# frames del muñequito
frames = [
    r"""
     (•_•)
    <)   )╯♪♪♪♪♪♪
     /   \
    """,
    r"""
     (•_•)
    ╰(   (>♪♪♪♪♪
     /   \
    """,
    r"""
     (•_•)
    <)   )╯♪♪♪♪
     \   \
    """,
    r"""
     (•_•)
    ╰(   (>♪♪♪
     /   /
    """,
    r"""
     (•_•)
    <)   )╯♪♪
     /   \
    """,
    r"""
     (•_•)
    ╰(   (>♪
     /   \
    """,
    r"""
     (•_•)
    ╰(   (>♪♪
     /   \
    """,
    r"""
     (•_•)
    <)   )╯♪♪♪
     /   \
    """,
    r"""
     (•_•)
    ╰(   (>♪♪♪♪
     /   /
    """,
    r"""     
     (•_•)
    <)   )╯♪♪♪♪♪
     /   \
    """,
    r"""     
     (•_•)
    ╰(   (>♪♪♪♪♪♪
     /   \
    """,
]


def dance():
    try:
        while True:
            for frame in frames:
                clear()
                print(frame)
                time.sleep(0.2)  # Velocidad del "baile"
    except KeyboardInterrupt:
        clear()
        print("Gracias por ver el show 🕺💃")

if __name__ == "__main__":
    dance()
