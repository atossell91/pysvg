import math

class Svg_Document:
    header = '<svg xmlns="http://www.w3.org/2000/svg">'
    footer = '</svg>'
    lines = []

    def make_multi_spaces(self, num):
        spacer = '    '
        spaces = ''
        for i in range(num):
            spaces = spaces + spacer
        return spaces

    def rectangle(self, width, height, x, y, fill='none', stroke='black', level=1):
        spaces = self.make_multi_spaces(level)
        self.lines.append(f'{spaces}<rect width="{width}" height="{height}" x="{x}" y="{y}" fill="{fill}" stroke="{stroke}"/>')

    def arc(self, sx, sy, ex, ey, fill='none', stroke='black', level=1):
            spaces = self.make_multi_spaces(level)
            self.lines.append(f'{spaces}<path d="M{sx} {sy} A {ex-sx} {ey-sy}, 0, 0, 0, {ex} {ey}" fill="{fill}" stroke="{stroke}"/>')

    def text(self, text, x, y, length='none', lengthAdjust='spacing', rotation='0', level=1):
        tagSpaces = self.make_multi_spaces(level)
        contentSpaces = self.make_multi_spaces(level+1)
        self.lines.append(f'{tagSpaces}<text x="{x}" y="{y}" textLength="{length}" lengthAdjust="{lengthAdjust}" rotate="{rotation}">')
        self.lines.append(f'{contentSpaces}{text}')
        self.lines.append(f'{tagSpaces}</text>')
    
    def write(self, filename):
        with open(filename, 'w') as outfile:
            outfile.write(self.header)
            outfile.write('\n')
            for i in range(len(self.lines)):
                outfile.write(self.lines[i])
                if i < (len(self.lines)):
                    outfile.write('\n')
            outfile.write(self.footer)

# -- Drawing Code --

shelf_width = 160
shelf_height = 160
shelf_count = 5

rack_count = 4
rack_gap = 80

def rack(doc, x, y):
    for i in range(shelf_count):
        doc.rectangle(shelf_width, shelf_height, x, y + i * shelf_height)

doc = Svg_Document()

for i in range(rack_count):
    rack(doc, i * (shelf_width + rack_gap), 0)

doc.arc(100, 850, 50, 800)

doc.write('joscelyn.svg')
