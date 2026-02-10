# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageBaselineDetailRequest(DaraModel):
    def __init__(
        self,
        baseline_item_key: str = None,
        image_uuid: str = None,
        lang: str = None,
    ):
        # The information about the baseline.
        self.baseline_item_key = baseline_item_key
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_item_key is not None:
            result['BaselineItemKey'] = self.baseline_item_key

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineItemKey') is not None:
            self.baseline_item_key = m.get('BaselineItemKey')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

