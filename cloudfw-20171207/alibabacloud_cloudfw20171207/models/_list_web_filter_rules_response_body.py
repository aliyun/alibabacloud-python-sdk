# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ListWebFilterRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[main_models.ListWebFilterRulesResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of web filtering rules.
        self.rules = rules
        # The total number of web filtering rules that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListWebFilterRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWebFilterRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.ListWebFilterRulesResponseBodyRulesConditions] = None,
        create_time: int = None,
        rule_action: str = None,
        update_time: int = None,
        web_filter_rule_id: str = None,
        web_filter_template_id: str = None,
    ):
        # The list of match conditions for the rule. The list contains only one condition.
        self.conditions = conditions
        # The time when the web filtering rule was created. The value is a UNIX timestamp in seconds.
        self.create_time = create_time
        # The action performed after the rule is matched. Valid values:
        # - **Allow**: Allows the request.
        # - **Alert**: Monitors the request.
        # - **Deny**: Blocks the request.
        self.rule_action = rule_action
        # The time when the web filtering rule was last modified. The value is a UNIX timestamp in seconds.
        self.update_time = update_time
        # The ID of the web filtering rule.
        self.web_filter_rule_id = web_filter_rule_id
        # The ID of the web filtering template to which the rule belongs.
        self.web_filter_template_id = web_filter_template_id

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.web_filter_rule_id is not None:
            result['WebFilterRuleId'] = self.web_filter_rule_id

        if self.web_filter_template_id is not None:
            result['WebFilterTemplateId'] = self.web_filter_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ListWebFilterRulesResponseBodyRulesConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WebFilterRuleId') is not None:
            self.web_filter_rule_id = m.get('WebFilterRuleId')

        if m.get('WebFilterTemplateId') is not None:
            self.web_filter_template_id = m.get('WebFilterTemplateId')

        return self

class ListWebFilterRulesResponseBodyRulesConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: str = None,
    ):
        # The type of the match condition. Valid values: **URL**, which indicates matching by URL.
        self.key = key
        # The URL to match. A single asterisk (*) matches all URLs. A value ending with /* indicates prefix wildcard matching.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

