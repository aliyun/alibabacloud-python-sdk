# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DeleteForwardingRulesResponseBody(DaraModel):
    def __init__(
        self,
        forwarding_rules: List[main_models.DeleteForwardingRulesResponseBodyForwardingRules] = None,
        request_id: str = None,
    ):
        # The forwarding rules.
        self.forwarding_rules = forwarding_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.forwarding_rules:
            for v1 in self.forwarding_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k1 in self.forwarding_rules:
                result['ForwardingRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k1 in m.get('ForwardingRules'):
                temp_model = main_models.DeleteForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteForwardingRulesResponseBodyForwardingRules(DaraModel):
    def __init__(
        self,
        forwarding_rule_id: str = None,
    ):
        # The forwarding rule ID.
        self.forwarding_rule_id = forwarding_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')

        return self

