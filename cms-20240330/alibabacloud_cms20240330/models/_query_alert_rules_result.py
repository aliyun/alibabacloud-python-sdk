# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryAlertRulesResult(DaraModel):
    def __init__(
        self,
        alert_rules: List[main_models.AlertRuleV2] = None,
        total_count: int = None,
    ):
        # 告警规则列表
        self.alert_rules = alert_rules
        # 符合查询条件的总告警规则数
        self.total_count = total_count

    def validate(self):
        if self.alert_rules:
            for v1 in self.alert_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['alertRules'] = []
        if self.alert_rules is not None:
            for k1 in self.alert_rules:
                result['alertRules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rules = []
        if m.get('alertRules') is not None:
            for k1 in m.get('alertRules'):
                temp_model = main_models.AlertRuleV2()
                self.alert_rules.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

