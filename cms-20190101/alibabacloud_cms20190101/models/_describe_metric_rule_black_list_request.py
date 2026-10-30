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
        # The category of the Alibaba Cloud service. For example, ApsaraDB for Redis has `kvstore_standard` (Standard Edition), `kvstore_sharding` (Cluster Edition), and `kvstore_splitrw` (read/write splitting Edition).
        self.category = category
        # The IDs of the alert blacklist policies.
        self.ids = ids
        # The instance ID list in the alert blacklist policy.
        # 
        # Valid values of N: 0 to 10.
        self.instance_ids = instance_ids
        # The status of the alert blacklist policy. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.is_enable = is_enable
        # The name of the alert blacklist policy.
        # 
        # This parameter supports fuzzy match.
        self.name = name
        # The namespace of the Alibaba Cloud service.
        # 
        # For information about the namespaces of Alibaba Cloud services, see [Cloud service metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The order in which the query results are sorted by time. Valid values:
        # 
        # 0: ascending order (ASC).
        # 
        # 1: descending order (DESC). This is the default value.
        self.order = order
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The effective scope of the alert blacklist policy. Valid values:
        # 
        # - USER: The alert blacklist policy takes effect only within the current Alibaba Cloud account.
        # 
        # - GROUP: The alert blacklist policy takes effect in the specified application groups.
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

