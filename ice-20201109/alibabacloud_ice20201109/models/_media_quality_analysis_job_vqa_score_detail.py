# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaQualityAnalysisJobVqaScoreDetail(DaraModel):
    def __init__(
        self,
        intensity_value: float = None,
        perceptual_score: float = None,
    ):
        self.intensity_value = intensity_value
        self.perceptual_score = perceptual_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intensity_value is not None:
            result['IntensityValue'] = self.intensity_value

        if self.perceptual_score is not None:
            result['PerceptualScore'] = self.perceptual_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntensityValue') is not None:
            self.intensity_value = m.get('IntensityValue')

        if m.get('PerceptualScore') is not None:
            self.perceptual_score = m.get('PerceptualScore')

        return self

