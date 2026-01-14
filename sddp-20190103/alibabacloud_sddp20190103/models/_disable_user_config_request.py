# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableUserConfigRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        feature_type: int = None,
        lang: str = None,
    ):
        # The code of the configuration item. You can call the [DescribeConfigs](~~DescribeConfigs~~) operation to obtain the code of the configuration item.
        self.code = code
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh_cn**: Chinese (default)
        # *   **en_us**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

