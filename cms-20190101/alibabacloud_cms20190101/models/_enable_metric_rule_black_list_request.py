# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableMetricRuleBlackListRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        is_enable: bool = None,
        region_id: str = None,
    ):
        # The IDs of the blacklist policies. Separate multiple IDs with commas (,). You can specify up to 50 IDs.
        # 
        # For information about how to obtain the ID of a blacklist policy, see [DescribeMetricRuleBlackList](https://help.aliyun.com/document_detail/457257.html).
        # 
        # > You can also set this parameter to a JSON array. Example: `["a9ad2ac2-3ed9-11ed-b878-0242ac12****","5cb8a9a4-198f-4651-a353-f8b28788****"]`.
        # 
        # This parameter is required.
        self.id = id
        # Specifies whether to enable the blacklist policy. Valid values:
        # 
        # *   true: The blacklist policy is enabled.
        # *   false (default): The blacklist policy is disabled.
        # 
        # This parameter is required.
        self.is_enable = is_enable
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

