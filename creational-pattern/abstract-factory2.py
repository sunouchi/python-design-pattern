def main():
    #...
    txtDiagram = create_diagram(DiagramFactory)
    txtDiagram.save(txtFilename)

    svgDiagram = create_diagram(SvgDiagramFactory)
    svgDiagram.save(svgFilename)

def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

class DiagramFactory:

    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)

    @classmethod
    def make_rectangle(Class, x, y, width, height, fill="white", stroke="black"):
        return Class.Rectangle(x, y, width, height, fill="white", stroke="black")

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.Text(x, y, text, fontsize)

    class Text:
        def __init__(self, x, y, text, fontsize):
            self.x = x
            self.y = y
            self.rows = [list(text)]

    class Diagram:
        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, row in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char


class SvgDiagramFactory:
    @classmethod
    def make_diagram(Class, width, height):
        return Class.SvgDiagram(width, height)

    @classmethod
    def make_rectangle(Class, x, y, width, height, fill="white", stroke="black"):
        return Class.SvgRectangle(x, y, width, height, fill="white", stroke="black")

    @classmethod
    def make_text(Class, x, y, text, fontsize=12):
        return Class.SvgText(x, y, text, fontsize)

    class Text:
        def __init__(self, x, y, text, fontsize):
            self.x = x
            self.y = y
            self.rows = [list(text)]

    class Diagram:
        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, row in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char


SVG_TEXT = """<text x="{x}" y="{y} text-anchor="left" \
font-family="sans-serif" font-size="{fontsize}">{text}</text>"""
SVG_SCALE = 20
class SvgText:
    def __init__(self, x, y, text, fontsize):
        x *= SVG_SCALE
        y *= SVG_SCALE
        fontsize *= SVG_SCALE // 10
        self.svg = SVG_TEXT.format(**locals())

class SvgDiagram:
    def add(self, component):
        self.diagram.append(component.svg)
