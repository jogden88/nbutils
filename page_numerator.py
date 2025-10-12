import xml.etree.ElementTree as ET
from sys import argv as argv

PREPEND_SVG = '{http://www.w3.org/2000/svg}'


def load_svg(file_name):
    return ET.parse(file_name)


def inc_pgn(tree):
    root = tree.getroot()
    gs = root.findall(PREPEND_SVG + 'g')
    # g2 = gs[1]
    # print(g2)
    g2text = gs[1].find(PREPEND_SVG + 'text')
    # print(g2text)
    g2texttspan = g2text.find(PREPEND_SVG + 'tspan')
    # print(g2texttspan.text)
    g2texttspanpgn = int(g2texttspan.text)
    page_number = '{:03d}'.format(g2texttspanpgn + 2)
    g2texttspan.text = page_number
    tree.write('left_page_{}'.format(page_number) + '.svg')


def paginator(tree, max_pgn):
    base_page = tree.getroot()
    base_pgn = int(base_page.findall(PREPEND_SVG + 'g')[1]
                   .find(PREPEND_SVG + 'text')
                   .find(PREPEND_SVG + 'tspan')
                   .text)
    for pgn in range(base_pgn, max_pgn, 2):
        print(pgn)


def next_page():
    # Open base page (left or right)
    # From base page number to max page number
    #   Increment page number by +2 until page number >= max page number
    #   Write page out 1 by 1 (filename is <page_number>.svg)
    pass


def cli(args):
    # python3 page_numerator.py <base_page_svg> <max_page>
    if len(args) > 1:
        print("Opening SVG:", args[1])
        # inc_pgn(load_svg(args[1]))
        paginator(load_svg(args[1]), 10)
    else:
        print("Missing file name")


if __name__ == "__main__":
    cli(argv)
