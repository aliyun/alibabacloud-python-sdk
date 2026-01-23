# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListEventCenterRuleNameResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        rule_names: List[main_models.ListEventCenterRuleNameResponseBodyRuleNames] = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The list of names of event notification rules.
        self.rule_names = rule_names

    def validate(self):
        if self.rule_names:
            for v1 in self.rule_names:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleNames'] = []
        if self.rule_names is not None:
            for k1 in self.rule_names:
                result['RuleNames'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_names = []
        if m.get('RuleNames') is not None:
            for k1 in m.get('RuleNames'):
                temp_model = main_models.ListEventCenterRuleNameResponseBodyRuleNames()
                self.rule_names.append(temp_model.from_map(k1))

        return self

class ListEventCenterRuleNameResponseBodyRuleNames(DaraModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The ID of the event notification rule.
        self.rule_id = rule_id
        # The name of the event notification rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

