# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListManagedRulesGroupsResponseBody(DaraModel):
    def __init__(
        self,
        managed_rules_groups: List[main_models.ListManagedRulesGroupsResponseBodyManagedRulesGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # List of managed rule group information.
        self.managed_rules_groups = managed_rules_groups
        # Current page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Total number of records after filtering.
        self.total_count = total_count

    def validate(self):
        if self.managed_rules_groups:
            for v1 in self.managed_rules_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ManagedRulesGroups'] = []
        if self.managed_rules_groups is not None:
            for k1 in self.managed_rules_groups:
                result['ManagedRulesGroups'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.managed_rules_groups = []
        if m.get('ManagedRulesGroups') is not None:
            for k1 in m.get('ManagedRulesGroups'):
                temp_model = main_models.ListManagedRulesGroupsResponseBodyManagedRulesGroups()
                self.managed_rules_groups.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListManagedRulesGroupsResponseBodyManagedRulesGroups(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_count: int = None,
    ):
        # Name of the managed rule group.
        self.name = name
        # Number of rules within the managed rule group.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

