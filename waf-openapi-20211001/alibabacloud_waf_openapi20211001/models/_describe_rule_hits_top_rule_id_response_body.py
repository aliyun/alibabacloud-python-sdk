# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleHitsTopRuleIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_hits_top_rule_id: List[main_models.DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The array of the IDs of the top 10 rules that are matched by requests.
        self.rule_hits_top_rule_id = rule_hits_top_rule_id

    def validate(self):
        if self.rule_hits_top_rule_id:
            for v1 in self.rule_hits_top_rule_id:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleHitsTopRuleId'] = []
        if self.rule_hits_top_rule_id is not None:
            for k1 in self.rule_hits_top_rule_id:
                result['RuleHitsTopRuleId'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_hits_top_rule_id = []
        if m.get('RuleHitsTopRuleId') is not None:
            for k1 in m.get('RuleHitsTopRuleId'):
                temp_model = main_models.DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId()
                self.rule_hits_top_rule_id.append(temp_model.from_map(k1))

        return self

class DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId(DaraModel):
    def __init__(
        self,
        count: int = None,
        resource: str = None,
        rule_id: str = None,
    ):
        # The number of requests that match the rule.
        self.count = count
        # The protected object.
        self.resource = resource
        # The ID of the rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

