# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafTemplateRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[main_models.ListWafTemplateRulesResponseBodyRules] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The list of returned template rules.
        self.rules = rules

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListWafTemplateRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ListWafTemplateRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        config: main_models.WafRuleConfig = None,
        name: str = None,
        phase: str = None,
        status: str = None,
        type: str = None,
    ):
        # Rule configuration.
        self.config = config
        # Rule name.
        self.name = name
        # WAF operation phase.
        self.phase = phase
        # Rule status.
        self.status = status
        # Rule type.
        self.type = type

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

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.WafRuleConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

