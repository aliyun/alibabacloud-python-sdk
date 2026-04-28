# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageQuality(DaraModel):
    def __init__(
        self,
        overall_score: float = None,
    ):
        # The overall quality score of the image. The image is automatically evaluated by AI. The evaluation is mainly based on subjective aesthetics and is affected by various factors, such as composition, brightness, contrast, color, and definition. Valid values: 0 to 1. The higher the score, the better the quality.
        self.overall_score = overall_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overall_score is not None:
            result['overall_score'] = self.overall_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('overall_score') is not None:
            self.overall_score = m.get('overall_score')

        return self

