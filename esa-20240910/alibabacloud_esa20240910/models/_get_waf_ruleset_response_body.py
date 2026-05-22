# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetWafRulesetResponseBody(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        phase: str = None,
        request_id: str = None,
        rules: List[main_models.WafRuleConfig] = None,
        shared: main_models.WafBatchRuleShared = None,
        status: str = None,
        update_time: str = None,
    ):
        # Ruleset ID.
        self.id = id
        # Ruleset name.
        # 
        # This parameter is required.
        self.name = name
        # The WAF operation phase applicable to the ruleset.
        # 
        # This parameter is required.
        self.phase = phase
        # Request ID.
        self.request_id = request_id
        # List of rule configurations in the ruleset.
        self.rules = rules
        # Shared configurations for the rules in the ruleset.
        self.shared = shared
        # Ruleset status.
        self.status = status
        # The last modified time of the ruleset.
        self.update_time = update_time

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.shared is not None:
            result['Shared'] = self.shared.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.WafRuleConfig()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Shared') is not None:
            temp_model = main_models.WafBatchRuleShared()
            self.shared = temp_model.from_map(m.get('Shared'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

