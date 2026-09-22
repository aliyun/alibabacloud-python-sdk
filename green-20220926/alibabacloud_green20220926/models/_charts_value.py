# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ChartsValue(DaraModel):
    def __init__(
        self,
        x: List[str] = None,
        y: List[main_models.ChartsValueY] = None,
    ):
        # The X-axis.
        self.x = x
        # The Y-axis.
        self.y = y

    def validate(self):
        if self.y:
            for v1 in self.y:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        result['Y'] = []
        if self.y is not None:
            for k1 in self.y:
                result['Y'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        self.y = []
        if m.get('Y') is not None:
            for k1 in m.get('Y'):
                temp_model = main_models.ChartsValueY()
                self.y.append(temp_model.from_map(k1))

        return self



class ChartsValueY(DaraModel):
    def __init__(
        self,
        name: str = None,
        data: List[int] = None,
    ):
        # The name.
        self.name = name
        # The QPS at the point in time.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

