# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Body(DaraModel):
    def __init__(
        self,
        boundary: main_models.Boundary = None,
        confidence: float = None,
    ):
        # The boundary of the human body.
        self.boundary = boundary
        # The confidence level of the result. A higher value indicates greater confidence. Specifically, a value exceeding 0.8 signifies a high degree of confidence in the result.
        self.confidence = confidence

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = main_models.Boundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        return self

