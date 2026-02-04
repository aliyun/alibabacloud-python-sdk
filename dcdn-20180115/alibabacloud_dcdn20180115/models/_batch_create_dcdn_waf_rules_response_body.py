# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class BatchCreateDcdnWafRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_ids: main_models.BatchCreateDcdnWafRulesResponseBodyRuleIds = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The IDs of created rules.
        self.rule_ids = rule_ids

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleIds') is not None:
            temp_model = main_models.BatchCreateDcdnWafRulesResponseBodyRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        return self

class BatchCreateDcdnWafRulesResponseBodyRuleIds(DaraModel):
    def __init__(
        self,
        rule_id: List[str] = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

