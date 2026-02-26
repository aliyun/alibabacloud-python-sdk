# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Insights(DaraModel):
    def __init__(
        self,
        image: main_models.ImageInsight = None,
        video: main_models.VideoInsight = None,
    ):
        # The summary and description of the image.
        self.image = image
        # The summary and description of the video.
        self.video = video

    def validate(self):
        if self.image:
            self.image.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = main_models.ImageInsight()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('Video') is not None:
            temp_model = main_models.VideoInsight()
            self.video = temp_model.from_map(m.get('Video'))

        return self

