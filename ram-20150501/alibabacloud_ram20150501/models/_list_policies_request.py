# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class ListPoliciesRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        policy_type: str = None,
        tag: List[main_models.ListPoliciesRequestTag] = None,
    ):
        # The marker. If the response is truncated, you can use `Marker` to obtain the content that starts from the position after the truncation point.
        self.marker = marker
        # The number of entries to return. If the response is truncated because it reaches the `MaxItems` limit, the `IsTruncated` response parameter equals `true`.
        # 
        # Valid values: 1 to 1000. Default value: 100.
        self.max_items = max_items
        # The type of the access policy. Valid values: `System` and `Custom`. If this parameter is not specified, all access policies are listed.
        self.policy_type = policy_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.marker is not None:
            result['Marker'] = self.marker

        if self.max_items is not None:
            result['MaxItems'] = self.max_items

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListPoliciesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListPoliciesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

