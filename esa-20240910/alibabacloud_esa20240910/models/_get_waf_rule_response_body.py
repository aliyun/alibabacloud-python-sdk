# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetWafRuleResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.WafRuleConfig = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        position: int = None,
        request_id: str = None,
        ruleset_id: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # Rule configuration.
        self.config = config
        # The ID of the WAF rule, which can be obtained by calling the [ListWafRules](https://help.aliyun.com/document_detail/2878257.html) interface.
        self.id = id
        # Rule name.
        # 
        # This parameter is required.
        self.name = name
        # WAF operation phase.
        # 
        # This parameter is required.
        self.phase = phase
        # The position of the rule in the rule set.
        self.position = position
        # Request ID.
        self.request_id = request_id
        self.ruleset_id = ruleset_id
        # Rule status.
        self.status = status
        # The last modified time of the rule.
        self.update_time = update_time

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.position is not None:
            result['Position'] = self.position

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.WafRuleConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

