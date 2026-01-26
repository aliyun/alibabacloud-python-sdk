# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListDispatchRuleResponseBody(DaraModel):
    def __init__(
        self,
        dispatch_rules: List[main_models.ListDispatchRuleResponseBodyDispatchRules] = None,
        request_id: str = None,
    ):
        # The returned struct.
        self.dispatch_rules = dispatch_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dispatch_rules:
            for v1 in self.dispatch_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k1 in self.dispatch_rules:
                result['DispatchRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k1 in m.get('DispatchRules'):
                temp_model = main_models.ListDispatchRuleResponseBodyDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDispatchRuleResponseBodyDispatchRules(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_id: int = None,
        state: str = None,
    ):
        # The name of the notification policy.
        self.name = name
        # The ID of the notification policy.
        self.rule_id = rule_id
        # Indicates whether the notification policy is enabled. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

