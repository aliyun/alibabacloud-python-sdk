# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Boundary(DaraModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        polygon: List[main_models.PointInt64] = None,
        top: int = None,
        width: int = None,
    ):
        # The height. Unit: pixel.
        self.height = height
        # The distance from the X-coordinate of the vertex to the left edge.
        self.left = left
        # The polygon formed by a number of points. This parameter takes effect only when the boundary describes a polygon rather than a rectangle.
        # 
        # >  This parameter is mutually exclusive to the following parameters that form a rectangle: Width, Height, Left, and Top. A boundary describes only a rectangle or a polygon.
        self.polygon = polygon
        # The distance from the Y-coordinate of the vertex to the top.
        self.top = top
        # The width. Unit: pixel.
        self.width = width

    def validate(self):
        if self.polygon:
            for v1 in self.polygon:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.left is not None:
            result['Left'] = self.left

        result['Polygon'] = []
        if self.polygon is not None:
            for k1 in self.polygon:
                result['Polygon'].append(k1.to_map() if k1 else None)

        if self.top is not None:
            result['Top'] = self.top

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        self.polygon = []
        if m.get('Polygon') is not None:
            for k1 in m.get('Polygon'):
                temp_model = main_models.PointInt64()
                self.polygon.append(temp_model.from_map(k1))

        if m.get('Top') is not None:
            self.top = m.get('Top')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

