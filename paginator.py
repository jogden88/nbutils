import xml.etree.ElementTree as ET
from sys import argv as argv

PREPEND_SVG = '{http://www.w3.org/2000/svg}'


def load_svg(file_name):
    return ET.parse(file_name)


def paginator(tree, max_pgn, out_dir, side='right'):
    base_page = tree.getroot()
    # This reference to the text is no help, we need a reference to the object
    # before the .text. Only then can we update the page number and writeout.
    base_pgn_obj = base_page.find(".//" + PREPEND_SVG + "*[@id='pgn']")[0]
    base_pgn = int(base_pgn_obj.text)
    for pgn in range(base_pgn, int(max_pgn) + 1, 2):
        pgn_text = '{: 3d}'.format(pgn) if side == 'right' else str(pgn)
        file_name = out_dir + '{:03d}'.format(int(pgn_text.strip())) + '.svg'

        base_pgn_obj.text = pgn_text
        tree.write(file_name)


def cli(args):
    # <base_page_svg> <max_page> <output_directory> <page side>
    if len(args) > 3:
        print("Opening SVG:", args[1], args[2], args[3], args[4])
        paginator(load_svg(args[1]), args[2], args[3], args[4])
    else:
        print("page_numerator.py <base_page_svg> <max_page> <output_directory>")


if __name__ == "__main__":
    cli(argv)
