# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class CreateRulesResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        rule_ids: List[main_models.CreateRulesResponseBodyRuleIds] = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id
        # The priority of the forwarding rule. Valid values: **1 to 10000**. A lower value specifies a higher priority.
        # 
        # > The priorities of the forwarding rules created for the same listener is unique.
        self.rule_ids = rule_ids

    def validate(self):
        if self.rule_ids:
            for v1 in self.rule_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleIds'] = []
        if self.rule_ids is not None:
            for k1 in self.rule_ids:
                result['RuleIds'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_ids = []
        if m.get('RuleIds') is not None:
            for k1 in m.get('RuleIds'):
                temp_model = main_models.CreateRulesResponseBodyRuleIds()
                self.rule_ids.append(temp_model.from_map(k1))

        return self

class CreateRulesResponseBodyRuleIds(DaraModel):
    def __init__(
        self,
        priority: int = None,
        rule_id: str = None,
    ):
        # The priority of the forwarding rule. Valid values: **1 to 10000**. A smaller value indicates a higher priority.
        # 
        # > The priorities of the forwarding rules created for the same listener must be unique.
        self.priority = priority
        # The forwarding rule ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

