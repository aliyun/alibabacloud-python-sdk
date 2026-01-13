# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceRulesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        instance_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_rule_id: str = None,
        resource_rule_name: str = None,
        sort_by: str = None,
    ):
        self.all = all
        # This parameter is required.
        self.instance_id = instance_id
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.resource_rule_id = resource_rule_id
        self.resource_rule_name = resource_rule_name
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_rule_id is not None:
            result['ResourceRuleId'] = self.resource_rule_id

        if self.resource_rule_name is not None:
            result['ResourceRuleName'] = self.resource_rule_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceRuleId') is not None:
            self.resource_rule_id = m.get('ResourceRuleId')

        if m.get('ResourceRuleName') is not None:
            self.resource_rule_name = m.get('ResourceRuleName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

