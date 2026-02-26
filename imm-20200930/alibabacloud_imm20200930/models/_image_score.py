# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageScore(DaraModel):
    def __init__(
        self,
        overall_quality_score: float = None,
    ):
        # The score for the overall image quality. The image is automatically evaluated by AI. The evaluation is mainly based on subjective aesthetics and is affected by various factors, such as composition, brightness, contrast, color, and definition.
        # 
        # Valid values: 0 to 1. A higher value indicates better quality.
        self.overall_quality_score = overall_quality_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')

        return self

