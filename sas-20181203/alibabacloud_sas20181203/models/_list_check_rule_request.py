# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckRuleRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_name: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        rule_type: str = None,
        scope_type: str = None,
        task_sources: List[str] = None,
    ):
        # The ID of the check item.
        # 
        # > You can call the [ListCheckResult](~~ListCheckResult~~) API to get the check item ID.
        self.check_id = check_id
        # The name of the check item.
        self.check_name = check_name
        # The page number displayed in a paginated query.
        self.current_page = current_page
        # Set the language type for the request and response messages. The default is **zh**. Values:
        # 
        # - zh: Chinese
        # - en: English
        self.lang = lang
        # The number of check items displayed per page in a paginated query. The default value is **20**, indicating 20 check items per page.
        self.page_size = page_size
        # The type of rule. Default is **WHITE**. Values:
        # - **WHITE**: Add to whitelist
        self.rule_type = rule_type
        # The scope where the rule applies. Values:
        # - **INSTNACE**: Instance
        # - **ITEM**: Check item
        self.scope_type = scope_type
        # List of task sources.
        self.task_sources = task_sources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        return self

