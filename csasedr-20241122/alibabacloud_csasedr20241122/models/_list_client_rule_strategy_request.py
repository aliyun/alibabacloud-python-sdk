# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClientRuleStrategyRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_type: int = None,
    ):
        # The current page number for the paged query with paging. Default value: 1.
        self.current_page = current_page
        # The policy name for substring matching. If this parameter is not specified, policies are not filtered by name.
        self.name = name
        # The number of entries per page for the paged query with paging. Default value: 20.
        self.page_size = page_size
        # The policy type. Valid values:
        # 
        # - **0**: Software hardening.
        # - **1**: Firewall.
        # - **2**: Proactive defense.
        # 
        # This parameter is required.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

