# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDingTalkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        rule_action_name: str = None,
    ):
        # The page number of the current page to display in a paged query.
        self.current_page = current_page
        # The maximum number of notifications to display per page in a paged query. Default value: **20**, which indicates that up to 20 entries are displayed per page.
        self.page_size = page_size
        # The notification name.
        self.rule_action_name = rule_action_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_action_name is not None:
            result['RuleActionName'] = self.rule_action_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleActionName') is not None:
            self.rule_action_name = m.get('RuleActionName')

        return self

