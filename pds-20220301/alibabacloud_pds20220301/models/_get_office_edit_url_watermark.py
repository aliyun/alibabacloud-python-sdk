# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOfficeEditUrlWatermark(DaraModel):
    def __init__(
        self,
        fillstyle: str = None,
        font: str = None,
        horizontal: int = None,
        rotate: float = None,
        type: int = None,
        value: str = None,
        vertical: int = None,
    ):
        self.fillstyle = fillstyle
        self.font = font
        self.horizontal = horizontal
        self.rotate = rotate
        self.type = type
        self.value = value
        self.vertical = vertical

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fillstyle is not None:
            result['fillstyle'] = self.fillstyle

        if self.font is not None:
            result['font'] = self.font

        if self.horizontal is not None:
            result['horizontal'] = self.horizontal

        if self.rotate is not None:
            result['rotate'] = self.rotate

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        if self.vertical is not None:
            result['vertical'] = self.vertical

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fillstyle') is not None:
            self.fillstyle = m.get('fillstyle')

        if m.get('font') is not None:
            self.font = m.get('font')

        if m.get('horizontal') is not None:
            self.horizontal = m.get('horizontal')

        if m.get('rotate') is not None:
            self.rotate = m.get('rotate')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('vertical') is not None:
            self.vertical = m.get('vertical')

        return self

