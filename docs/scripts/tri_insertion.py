from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.pyplot import gca, figure, axis
from matplotlib.animation import ArtistAnimation
from numpy.random import permutation


def tri_insertion(tab):
    for i in range(1, len(tab)):
        val = tab[i]
        pos = i
        move_up(tab, i)
        while pos > 0 and tab[pos - 1] > val:
            pos -= 1
            move_right(tab, i, pos, val)
            tab[pos + 1] = tab[pos]
        tab[pos] = val
        move_down(tab, pos)
    draw_tab(tab)


def draw_tab(tab):
    for j in range(10):
        patches = []
        annotations = []
        for i, v in enumerate(tab):
            x, y = i * 10, 0
            patches.append(Rectangle((x, y), 9, 9))
            annotations.append(
                gca().annotate(v, (x, y), (x + 4.5, y + 4.5), color='w', weight='bold', fontsize=20, ha='center',
                               va='center'))
        collection = gca().add_collection(PatchCollection(patches))
        collection.set_color((['green'] if j % 2 == 0 else ['orange']) * len(tab))
        frames.append((collection, *annotations))


def move_up(tab, pos):
    for j in range(10):
        patches = []
        annotations = []
        gca().axis('equal')
        gca().axis([0, len(tab) * 10, 0, 10])
        for i, v in enumerate(tab):
            x, y = i * 10, j if i == pos else 0
            patches.append(Rectangle((x, y), 9, 9))
            annotations.append(
                gca().annotate(v, (x, y), (x + 4.5, y + 4.5), color='w', weight='bold', fontsize=20, ha='center',
                               va='center'))
        collection = gca().add_collection(PatchCollection(patches))
        colors = ['red' if i == pos else 'blue' for i in range(len(tab))]
        collection.set_color(colors)
        frames.append((collection, *annotations))


def move_down(tab, pos):
    for j in range(10):
        patches = []
        annotations = []
        for i, v in enumerate(tab):
            x, y = i * 10, 10 - j if i == pos else 0
            patches.append(Rectangle((x, y), 9, 9))
            annotations.append(
                gca().annotate(v, (x, y), (x + 4.5, y + 4.5), color='w', weight='bold', fontsize=20, ha='center',
                               va='center'))
        collection = gca().add_collection(PatchCollection(patches))
        colors = ['red' if i == pos else 'blue' for i in range(len(tab))]
        collection.set_color(colors)
        frames.append((collection, *annotations))


def move_right(tab, i, pos, val):
    for j in range(10):
        patches = []
        annotations = []
        for k, v in enumerate(tab):
            if k == pos:
                x, y = k * 10 + j, 0
            elif pos < k < i:
                x, y = k * 10 + 10, 0
            elif k == i:
                x, y = pos * 10 + 10 - j, 10
            else:
                x, y = k * 10, 0
            patches.append(Rectangle((x, y), 9, 9))
            annotations.append(
                gca().annotate(val if k == i else (tab[k + 1] if pos < k < i else v), (x, y), (x + 4.5, y + 4.5),
                               color='w',
                               weight='bold', fontsize=20,
                               ha='center',
                               va='center'))
        collection = gca().add_collection(PatchCollection(patches))
        colors = ['red' if k == i else 'blue' for k in range(len(tab))]
        collection.set_color(colors)
        frames.append((collection, *annotations))


tab = permutation(10)
frames = []
fig = figure(figsize=(len(tab), 3))
axis('off')
gca().axis('equal')
gca().axis([0, len(tab) * 10, 0, 10])
tri_insertion(tab)
ani = ArtistAnimation(fig, frames, interval=100, repeat_delay=3000)
ani.save('_images/tri_insertion.gif', dpi=80, writer='imagemagick', )
