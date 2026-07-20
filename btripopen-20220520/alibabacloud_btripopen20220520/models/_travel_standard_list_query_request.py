# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TravelStandardListQueryRequest(DaraModel):
    def __init__(
        self,
        from_group: bool = None,
        page_no: int = None,
        page_size: int = None,
        rule_name: str = None,
        user_id: str = None,
    ):
        # Applicable to parent-subsidiary enterprises. Set this parameter to true to query the unified group travel standards. If left empty, the system returns the travel rules that are currently in effect for the enterprise.
        self.from_group = from_group
        # The page number, starting from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the travel standard to search for.
        self.rule_name = rule_name
        # The user ID. Specify this parameter to query the travel standards bound to an employee.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_group is not None:
            result['from_group'] = self.from_group

        if self.page_no is not None:
            result['page_no'] = self.page_no

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.rule_name is not None:
            result['rule_name'] = self.rule_name

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from_group') is not None:
            self.from_group = m.get('from_group')

        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('rule_name') is not None:
            self.rule_name = m.get('rule_name')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

