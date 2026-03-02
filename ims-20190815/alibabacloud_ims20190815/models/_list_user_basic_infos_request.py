# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListUserBasicInfosRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        status: str = None,
        tag: List[main_models.ListUserBasicInfosRequestTag] = None,
    ):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 1000. Default value: 100.
        self.max_items = max_items
        # The status of the RAM users that you want to query. Valid values: active, freeze, and active,freeze. If you set the value to active,freeze, RAM users in both active and freeze states are queried. If you leave the parameter empty, the value active is used by default. If the Tag parameter is specified, you cannot specify the Status parameter. In this case, RAM users in both states are queried.
        self.status = status
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

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListUserBasicInfosRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListUserBasicInfosRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.key = key
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
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

