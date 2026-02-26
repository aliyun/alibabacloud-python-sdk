# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Codes(DaraModel):
    def __init__(
        self,
        boundary: main_models.Boundary = None,
        confidence: float = None,
        content: str = None,
        type: str = None,
    ):
        # The boundary of the code.
        self.boundary = boundary
        # The confidence level of the code. A greater value indicates a higher confidence level. A value exceeding 0.8 signifies a high degree of confidence in the result.
        self.confidence = confidence
        # The content of the code.
        self.content = content
        # The type of the code.
        # 
        # Enumerated values:
        # 
        # *   qrcode
        # *   barcode
        self.type = type

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.content is not None:
            result['Content'] = self.content

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = main_models.Boundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

