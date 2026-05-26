# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class VideoInsightsConfig(DaraModel):
    def __init__(
        self,
        caption: main_models.VideoInsightsCaptionConfig = None,
    ):
        self.caption = caption

    def validate(self):
        if self.caption:
            self.caption.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            temp_model = main_models.VideoInsightsCaptionConfig()
            self.caption = temp_model.from_map(m.get('Caption'))

        return self

