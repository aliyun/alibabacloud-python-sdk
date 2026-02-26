# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class LicensePlate(DaraModel):
    def __init__(
        self,
        boundary: main_models.Boundary = None,
        confidence: float = None,
        content: str = None,
    ):
        # The boundary information of the license plate.
        self.boundary = boundary
        # The confidence level.
        self.confidence = confidence
        # The license plate number.
        self.content = content

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

        return self

