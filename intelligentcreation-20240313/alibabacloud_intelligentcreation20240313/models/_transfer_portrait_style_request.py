# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferPortraitStyleRequest(DaraModel):
    def __init__(
        self,
        height: int = None,
        image_url: str = None,
        numbers: int = None,
        redraw_amplitude: int = None,
        style: int = None,
        width: int = None,
    ):
        self.height = height
        self.image_url = image_url
        self.numbers = numbers
        self.redraw_amplitude = redraw_amplitude
        self.style = style
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['height'] = self.height

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.numbers is not None:
            result['numbers'] = self.numbers

        if self.redraw_amplitude is not None:
            result['redrawAmplitude'] = self.redraw_amplitude

        if self.style is not None:
            result['style'] = self.style

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('numbers') is not None:
            self.numbers = m.get('numbers')

        if m.get('redrawAmplitude') is not None:
            self.redraw_amplitude = m.get('redrawAmplitude')

        if m.get('style') is not None:
            self.style = m.get('style')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

