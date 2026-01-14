# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateRealisticPortraitRequest(DaraModel):
    def __init__(
        self,
        ages: List[int] = None,
        cloth: int = None,
        color: int = None,
        custom: str = None,
        face: List[int] = None,
        figure: int = None,
        gender: int = None,
        hair_color: int = None,
        hairstyle: int = None,
        height: int = None,
        image_url: str = None,
        numbers: int = None,
        ratio: str = None,
        width: int = None,
    ):
        self.ages = ages
        self.cloth = cloth
        self.color = color
        self.custom = custom
        self.face = face
        self.figure = figure
        self.gender = gender
        self.hair_color = hair_color
        self.hairstyle = hairstyle
        self.height = height
        self.image_url = image_url
        self.numbers = numbers
        self.ratio = ratio
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ages is not None:
            result['ages'] = self.ages

        if self.cloth is not None:
            result['cloth'] = self.cloth

        if self.color is not None:
            result['color'] = self.color

        if self.custom is not None:
            result['custom'] = self.custom

        if self.face is not None:
            result['face'] = self.face

        if self.figure is not None:
            result['figure'] = self.figure

        if self.gender is not None:
            result['gender'] = self.gender

        if self.hair_color is not None:
            result['hairColor'] = self.hair_color

        if self.hairstyle is not None:
            result['hairstyle'] = self.hairstyle

        if self.height is not None:
            result['height'] = self.height

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.numbers is not None:
            result['numbers'] = self.numbers

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ages') is not None:
            self.ages = m.get('ages')

        if m.get('cloth') is not None:
            self.cloth = m.get('cloth')

        if m.get('color') is not None:
            self.color = m.get('color')

        if m.get('custom') is not None:
            self.custom = m.get('custom')

        if m.get('face') is not None:
            self.face = m.get('face')

        if m.get('figure') is not None:
            self.figure = m.get('figure')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('hairColor') is not None:
            self.hair_color = m.get('hairColor')

        if m.get('hairstyle') is not None:
            self.hairstyle = m.get('hairstyle')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('numbers') is not None:
            self.numbers = m.get('numbers')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

