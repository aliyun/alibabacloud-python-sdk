# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CroppingSuggestion(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        boundary: main_models.Boundary = None,
        confidence: float = None,
    ):
        # The aspect ratio.
        self.aspect_ratio = aspect_ratio
        # The boundary of the cropping.
        self.boundary = boundary
        # The confidence score. Valid values: 0 to 1. A higher score indicates greater confidence in the result.
        self.confidence = confidence

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio

        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('Boundary') is not None:
            temp_model = main_models.Boundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        return self

