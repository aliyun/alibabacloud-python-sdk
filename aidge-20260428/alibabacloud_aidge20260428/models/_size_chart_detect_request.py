# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SizeChartDetectRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        threshold: float = None,
    ):
        # The URL of the image to detect.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The detection threshold. Valid values: 0 to 1.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

