# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFileProtectClientRuleRequest(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        current_page: int = None,
        page_size: int = None,
        platform: str = None,
        rule_action: str = None,
        rule_name: str = None,
    ):
        # The alert notification level. Valid values:
        # 
        # - 0: no alert
        # 
        # - 1: reminder
        # 
        # - 2: suspicious
        # 
        # - 3: high-risk.
        self.alert_level = alert_level
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # The maximum number of entries per page for a paged query.
        self.page_size = page_size
        # The operating system type. Valid values:
        # 
        # - **windows**: Windows
        # - **linux**: Linux.
        self.platform = platform
        # The rule action. Valid values:
        # 
        # - **block**: blocks the request.
        # 
        # - **monitor**: monitors the request.
        # 
        # - **pass**: allows the request.
        self.rule_action = rule_action
        # The rule name.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

