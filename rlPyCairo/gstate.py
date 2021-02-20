__all__ = (
        'GState',
        )
import sys, cairo
from reportlab.lib.colors import toColor
from reportlab.graphics.transform import mmult, inverse

class GState:
    __fill_rule_values = {1:0, 0:1}
    def __init__(self, width=1, height=1, bg='white', fmt='RGB24'):
        self._fmt = fmt
        self.surface = cairo.ImageSurface(getattr(cairo,'FORMAT_'+fmt), width, height)
        self.width = width
        self.height = height
        self.canv = canv = cairo.Context(self.surface)
        if fmt=='RGB24':
            self.__set_source_color__ = lambda c:canv.set_source_rgb(*c.rgb())
        elif fmt=='ARGB32':
            self.__set_source_color__ = lambda c:canv.set_source_rgba(*c.rgba())
        else:
            raise ValueError('Bad fmt=%r for rlPyCairo.GState' % fmt)
        canv.set_antialias(cairo.Antialias.BEST)
        self._in_transform = (1,0,0,-1,0,height)
        self._out_transform = inverse(self._in_transform)
        self.ctm = (1,0,0,1,0,0)
        self.fillColor = bg
        canv.rectangle(0,0,width,height)
        self.pathFill()
        self.pathBegin()
        self.__fillColor = self.__strokeColor = None

    @property
    def pixBuf(self):
        ba = self.surface.get_data()
        if self._fmt=='RGB24':
            #despite the name they store it in 32 bits; we need to remove 8
            ba = bytearray(ba)
            if sys.byteorder=='little':
                #we expect spare blue green red 
                for i in range(0,len(ba),4):
                    ba[i:i+4] = bytearray(reversed(ba[i:i+4]))
            del ba[0::4] #we have spare red green blue so remove the spare
        return bytes(ba)

    @property
    def ctm(self):
        return mmult(tuple(self.canv.get_matrix()), self._out_transform)

    @ctm.setter
    def ctm(self,mx):
        nctm = mmult(self._in_transform,mx)
        self.canv.set_matrix(cairo.Matrix(*nctm))

    @property
    def fillColor(self):
        return self.__fillColor

    @fillColor.setter
    def fillColor(self,c):
        self.__fillColor = toColor(c) if c is not None else c

    @property
    def strokeColor(self):
        return self.__strokeColor

    @strokeColor.setter
    def strokeColor(self,c):
        print(f'{self.__strokeColor=}')
        self.__strokeColor = toColor(c) if c is not None else c

    @property
    def strokeWidth(self):
        return self.canv.get_line_width()

    @strokeWidth.setter
    def strokeWidth(self, w):
        print(f'strokeWidth={w}')
        return self.canv.set_line_width(w)

    @property
    def dashArray(self):
        return self.canv.get_dash()

    @dashArray.setter
    def dashArray(self, da):
        if not da:
            da = 0, []
        return self.canv.set_dash(da[1], da[0])

    #lucky Cairo uses the same linCap/Join number values as PDF
    @property
    def lineCap(self):
        return int(self.canv.get_line_cap())

    @lineCap.setter
    def lineCap(self, v):
        return self.canv.set_line_cap(int(v))

    @property
    def lineJoin(self):
        return int(self.canv.get_line_join())

    @lineJoin.setter
    def lineJoin(self, v):
        return self.canv.set_line_join(int(v))

    #the values are the other way round from PDF
    @property
    def fillMode(self):
        return self.__fill_rule_values[int(self.canv.get_fill_rule())]

    @fillMode.setter
    def fillMode(self, v):
        return self.canv.set_fill_rule(self.__fill_rule_values[int(v)])

    def beginPath(self):
        self.canv.new_path()

    def moveTo(self, x, y):
        self.canv.move_to(float(x), float(y))

    def lineTo(self, x, y):
        self.canv.line_to(float(x), float(y))

    def pathClose(self):
        self.canv.close_path()

    def pathFill(self,fillMode=None):
        if self.__fillColor:
            if fillMode is not None:
                ofm = self.fillMode
                if ofm!=fillMode: self.fillMode = fillMode
            self.__set_source_color__(self.__fillColor)
            self.canv.fill_preserve()
            if fillMode is not None and ofm!=fillMode: self.fillMode = ofm

    def pathStroke(self):
        print(f'{self.__strokeColor=} {self.strokeWidth=}')
        if self.__strokeColor and self.strokeWidth>0:
            self.__set_source_color__(self.__strokeColor)
            self.canv.stroke_preserve()

    def curveTo(self, x1, y1, x2, y2, x3, y3):
        self.canv.curve_to(float(x1), float(y1),float(x2), float(y2),float(x3), float(y3))

    def pathBegin(self):
        self.canv.new_path()

    def setFont(self, fontName, fontSize):
        self.fontName = fontName
        self.fontSize = fontSize
