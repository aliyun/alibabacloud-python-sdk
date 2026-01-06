# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetRangeResponseBody(DaraModel):
    def __init__(
        self,
        background_colors: List[List[main_models.GetRangeResponseBodyBackgroundColors]] = None,
        display_values: List[List[str]] = None,
        formulas: List[List[str]] = None,
        hyperlinks: List[List[main_models.GetRangeResponseBodyHyperlinks]] = None,
        request_id: str = None,
        values: List[List[Any]] = None,
    ):
        self.background_colors = background_colors
        self.display_values = display_values
        self.formulas = formulas
        self.hyperlinks = hyperlinks
        # requestId
        self.request_id = request_id
        self.values = values

    def validate(self):
        if self.background_colors:
            for v1 in self.background_colors:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.hyperlinks:
            for v1 in self.hyperlinks:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['backgroundColors'] = []
        if self.background_colors is not None:
            for k1 in self.background_colors:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['backgroundColors'].append(l1)

        if self.display_values is not None:
            result['displayValues'] = self.display_values

        if self.formulas is not None:
            result['formulas'] = self.formulas

        result['hyperlinks'] = []
        if self.hyperlinks is not None:
            for k1 in self.hyperlinks:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['hyperlinks'].append(l1)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.background_colors = []
        if m.get('backgroundColors') is not None:
            for k1 in m.get('backgroundColors'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.GetRangeResponseBodyBackgroundColors()
                    l1.append(temp_model.from_map(k2))
                self.background_colors.append(l1)

        if m.get('displayValues') is not None:
            self.display_values = m.get('displayValues')

        if m.get('formulas') is not None:
            self.formulas = m.get('formulas')

        self.hyperlinks = []
        if m.get('hyperlinks') is not None:
            for k1 in m.get('hyperlinks'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.GetRangeResponseBodyHyperlinks()
                    l1.append(temp_model.from_map(k2))
                self.hyperlinks.append(l1)

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class GetRangeResponseBodyHyperlinks(DaraModel):
    def __init__(
        self,
        type: str = None,
        link: str = None,
        text: str = None,
    ):
        self.type = type
        self.link = link
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.link is not None:
            result['link'] = self.link

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class GetRangeResponseBodyBackgroundColors(DaraModel):
    def __init__(
        self,
        red: int = None,
        green: int = None,
        blue: int = None,
        hex_string: str = None,
    ):
        # red
        self.red = red
        # green
        self.green = green
        # blue
        self.blue = blue
        # hexString
        self.hex_string = hex_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.red is not None:
            result['Red'] = self.red

        if self.green is not None:
            result['Green'] = self.green

        if self.blue is not None:
            result['Blue'] = self.blue

        if self.hex_string is not None:
            result['HexString'] = self.hex_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Red') is not None:
            self.red = m.get('Red')

        if m.get('Green') is not None:
            self.green = m.get('Green')

        if m.get('Blue') is not None:
            self.blue = m.get('Blue')

        if m.get('HexString') is not None:
            self.hex_string = m.get('HexString')

        return self

