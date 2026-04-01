# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeMaskingRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeMaskingRulesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeMaskingRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMaskingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        rules: List[main_models.DescribeMaskingRulesResponseBodyDataRules] = None,
    ):
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
        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeMaskingRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeMaskingRulesResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        default_algo: str = None,
        enabled: str = None,
        masking_algo: str = None,
        rule_config: main_models.DescribeMaskingRulesResponseBodyDataRulesRuleConfig = None,
        rule_name: str = None,
    ):
        self.default_algo = default_algo
        self.enabled = enabled
        self.masking_algo = masking_algo
        self.rule_config = rule_config
        self.rule_name = rule_name

    def validate(self):
        if self.rule_config:
            self.rule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_algo is not None:
            result['DefaultAlgo'] = self.default_algo

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.masking_algo is not None:
            result['MaskingAlgo'] = self.masking_algo

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultAlgo') is not None:
            self.default_algo = m.get('DefaultAlgo')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MaskingAlgo') is not None:
            self.masking_algo = m.get('MaskingAlgo')

        if m.get('RuleConfig') is not None:
            temp_model = main_models.DescribeMaskingRulesResponseBodyDataRulesRuleConfig()
            self.rule_config = temp_model.from_map(m.get('RuleConfig'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class DescribeMaskingRulesResponseBodyDataRulesRuleConfig(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        databases: List[str] = None,
        tables: List[str] = None,
    ):
        self.columns = columns
        self.databases = databases
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['Columns'] = self.columns

        if self.databases is not None:
            result['Databases'] = self.databases

        if self.tables is not None:
            result['Tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('Databases') is not None:
            self.databases = m.get('Databases')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        return self

