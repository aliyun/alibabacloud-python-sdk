# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEventTypeStatusRequest(DaraModel):
    def __init__(
        self,
        feature_type: int = None,
        lang: str = None,
        sub_type_ids: str = None,
    ):
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the content within the request and response. Valid values: **zh** and **en**. The value zh indicates Chinese, and the value en indicates English.
        self.lang = lang
        # The ID of the anomalous event subtype. Separate multiple IDs with commas (,).
        # 
        # > You can call the **DescribeEventTypes** operation to query the ID of anomalous event subtype.
        self.sub_type_ids = sub_type_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sub_type_ids is not None:
            result['SubTypeIds'] = self.sub_type_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SubTypeIds') is not None:
            self.sub_type_ids = m.get('SubTypeIds')

        return self

