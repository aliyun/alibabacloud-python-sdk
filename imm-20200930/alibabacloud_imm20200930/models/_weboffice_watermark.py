# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebofficeWatermark(DaraModel):
    def __init__(
        self,
        fill_style: str = None,
        font: str = None,
        horizontal: int = None,
        rotate: float = None,
        type: int = None,
        value: str = None,
        vertical: int = None,
    ):
        # The color and transparency of the text watermark.
        self.fill_style = fill_style
        # The font of the text watermark.
        self.font = font
        # The horizontal spacing of the text watermark. Unit: pixel.
        self.horizontal = horizontal
        # The rotation of the text watermark. Unit: radian.
        self.rotate = rotate
        # The watermark type. Valid values:
        # 
        # *   0: no watermark.
        # *   1: text watermark.
        self.type = type
        # The watermark text.
        # 
        # >  This parameter takes effect only if you set the Type parameter to 1.
        self.value = value
        # The vertical spacing of the text watermark. Unit: pixel.
        self.vertical = vertical

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fill_style is not None:
            result['FillStyle'] = self.fill_style

        if self.font is not None:
            result['Font'] = self.font

        if self.horizontal is not None:
            result['Horizontal'] = self.horizontal

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.vertical is not None:
            result['Vertical'] = self.vertical

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FillStyle') is not None:
            self.fill_style = m.get('FillStyle')

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('Horizontal') is not None:
            self.horizontal = m.get('Horizontal')

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')

        return self

