# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDesensitizationRuleRequest(DaraModel):
    def __init__(
        self,
        func_type: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_type: str = None,
        tid: int = None,
    ):
        # The type of the masking algorithm.
        self.func_type = func_type
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is 100.
        self.page_size = page_size
        # The ID of the masking rule.
        self.rule_id = rule_id
        # The name of the masking rule.
        self.rule_name = rule_name
        # The algorithm used for masking.
        self.rule_type = rule_type
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.func_type is not None:
            result['FuncType'] = self.func_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FuncType') is not None:
            self.func_type = m.get('FuncType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

