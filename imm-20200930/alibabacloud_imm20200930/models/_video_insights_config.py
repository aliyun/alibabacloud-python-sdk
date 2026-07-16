# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class VideoInsightsConfig(DaraModel):
    def __init__(
        self,
        caption: main_models.VideoInsightsCaptionConfig = None,
        label: main_models.VideoInsightsLabelConfig = None,
        multi_stream: main_models.VideoInsightsMultiStreamConfig = None,
    ):
        # The video synopsis configuration.
        self.caption = caption
        self.label = label
        self.multi_stream = multi_stream

    def validate(self):
        if self.caption:
            self.caption.validate()
        if self.label:
            self.label.validate()
        if self.multi_stream:
            self.multi_stream.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption.to_map()

        if self.label is not None:
            result['Label'] = self.label.to_map()

        if self.multi_stream is not None:
            result['MultiStream'] = self.multi_stream.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            temp_model = main_models.VideoInsightsCaptionConfig()
            self.caption = temp_model.from_map(m.get('Caption'))

        if m.get('Label') is not None:
            temp_model = main_models.VideoInsightsLabelConfig()
            self.label = temp_model.from_map(m.get('Label'))

        if m.get('MultiStream') is not None:
            temp_model = main_models.VideoInsightsMultiStreamConfig()
            self.multi_stream = temp_model.from_map(m.get('MultiStream'))

        return self

