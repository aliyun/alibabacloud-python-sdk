# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DetectImageScoreResponseBody(DaraModel):
    def __init__(
        self,
        image_score: main_models.DetectImageScoreResponseBodyImageScore = None,
        request_id: str = None,
    ):
        # The quality score of the image.
        self.image_score = image_score
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.image_score:
            self.image_score.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScore') is not None:
            temp_model = main_models.DetectImageScoreResponseBodyImageScore()
            self.image_score = temp_model.from_map(m.get('ImageScore'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DetectImageScoreResponseBodyImageScore(DaraModel):
    def __init__(
        self,
        overall_quality_score: float = None,
    ):
        # The overall quality score.
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

