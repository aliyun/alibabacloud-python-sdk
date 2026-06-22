# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAegisContainerPluginRuleRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        rule_type: int = None,
    ):
        # The query conditions. The format is as follows:
        # ```json
        # [
        #   {
        #     "name": "ruleName",
        #     "value": "test"
        #   }
        # ]
        # ```
        # **- name**: The condition name. The following conditions are supported:
        # - **ruleName**: The rule name.
        # 
        # **- value**: The condition value.
        self.criteria = criteria
        # The page number of the current page in a paginated query.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Specifies the language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The number of entries to return on each page in a paginated query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The rule type. Valid values:
        # - **0**: User-defined.
        # - **1**: System built-in.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

