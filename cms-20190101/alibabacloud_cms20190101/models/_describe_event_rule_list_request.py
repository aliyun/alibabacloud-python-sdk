# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventRuleListRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        is_enable: bool = None,
        name_prefix: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The ID of the application group.
        self.group_id = group_id
        # Specifies whether to enable the event-triggered alert rule. Valid values:
        # 
        # - true (default)
        # - false
        self.is_enable = is_enable
        # The prefix in the name of the event-triggered alert rule.
        self.name_prefix = name_prefix
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Pages start from page 1. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

