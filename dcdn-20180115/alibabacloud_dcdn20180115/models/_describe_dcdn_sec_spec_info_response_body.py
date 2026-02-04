# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnSecSpecInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        spec_infos: List[main_models.DescribeDcdnSecSpecInfoResponseBodySpecInfos] = None,
        version: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The code and configurations of the security rules.
        self.spec_infos = spec_infos
        # The version of secure DCDN.
        self.version = version

    def validate(self):
        if self.spec_infos:
            for v1 in self.spec_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpecInfos'] = []
        if self.spec_infos is not None:
            for k1 in self.spec_infos:
                result['SpecInfos'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spec_infos = []
        if m.get('SpecInfos') is not None:
            for k1 in m.get('SpecInfos'):
                temp_model = main_models.DescribeDcdnSecSpecInfoResponseBodySpecInfos()
                self.spec_infos.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeDcdnSecSpecInfoResponseBodySpecInfos(DaraModel):
    def __init__(
        self,
        rule_code: str = None,
        rule_configs: List[main_models.DescribeDcdnSecSpecInfoResponseBodySpecInfosRuleConfigs] = None,
    ):
        # The code of the security rule.
        self.rule_code = rule_code
        # The configurations of the security rule.
        self.rule_configs = rule_configs

    def validate(self):
        if self.rule_configs:
            for v1 in self.rule_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code

        result['RuleConfigs'] = []
        if self.rule_configs is not None:
            for k1 in self.rule_configs:
                result['RuleConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')

        self.rule_configs = []
        if m.get('RuleConfigs') is not None:
            for k1 in m.get('RuleConfigs'):
                temp_model = main_models.DescribeDcdnSecSpecInfoResponseBodySpecInfosRuleConfigs()
                self.rule_configs.append(temp_model.from_map(k1))

        return self

class DescribeDcdnSecSpecInfoResponseBodySpecInfosRuleConfigs(DaraModel):
    def __init__(
        self,
        code: str = None,
        expr: str = None,
        value: str = None,
    ):
        # The configuration code of the security rule.
        self.code = code
        # The configuration expression of the security rule.
        self.expr = expr
        # The value of the configuration expression of the security rule.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.expr is not None:
            result['Expr'] = self.expr

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Expr') is not None:
            self.expr = m.get('Expr')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

