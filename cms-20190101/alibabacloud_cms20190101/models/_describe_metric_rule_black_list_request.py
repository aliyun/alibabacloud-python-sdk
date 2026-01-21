# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeMetricRuleBlackListRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        ids: List[str] = None,
        instance_ids: List[str] = None,
        is_enable: bool = None,
        name: str = None,
        namespace: str = None,
        order: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        scope_type: str = None,
    ):
        # The ID of the blacklist policy.
        self.category = category
        self.ids = ids
        # The IDs of the instances in the blacklist policy.
        # 
        # Valid values of N: 0 to 10.
        self.instance_ids = instance_ids
        # The status of the blacklist policy. Valid values:
        # 
        # *   true: The blacklist policy is enabled.
        # *   false: The blacklist policy is disabled.
        self.is_enable = is_enable
        # The name of the blacklist policy.
        # 
        # This parameter supports fuzzy match.
        self.name = name
        # The timestamp when the blacklist policy expired.
        # 
        # Unit: milliseconds.
        self.namespace = namespace
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call was successful.
        self.order = order
        # The name of the metric.
        self.page_number = page_number
        # The categories of the Alibaba Cloud service. For example, ApsaraDB for Redis includes the following categories: ApsaraDB for Redis (standard architecture), ApsaraDB for Redis (cluster architecture), and ApsaraDB for Redis (read/write splitting architecture). In this case, the valid values of this parameter for ApsaraDB for Redis include `kvstore_standard`, `kvstore_sharding`, and `kvstore_splitrw`.
        self.page_size = page_size
        self.region_id = region_id
        # The effective scope of the blacklist policy. Valid values:
        # 
        # *   USER: The blacklist policy takes effect only within the current Alibaba Cloud account.
        # *   GROUP: The blacklist policy takes effect only within the specified application group.
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

