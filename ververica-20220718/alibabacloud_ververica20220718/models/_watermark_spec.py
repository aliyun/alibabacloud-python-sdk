# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WatermarkSpec(DaraModel):
    def __init__(
        self,
        column: str = None,
        watermark_expression: str = None,
        watermark_type: str = None,
    ):
        self.column = column
        self.watermark_expression = watermark_expression
        self.watermark_type = watermark_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['column'] = self.column

        if self.watermark_expression is not None:
            result['watermarkExpression'] = self.watermark_expression

        if self.watermark_type is not None:
            result['watermarkType'] = self.watermark_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('column') is not None:
            self.column = m.get('column')

        if m.get('watermarkExpression') is not None:
            self.watermark_expression = m.get('watermarkExpression')

        if m.get('watermarkType') is not None:
            self.watermark_type = m.get('watermarkType')

        return self

