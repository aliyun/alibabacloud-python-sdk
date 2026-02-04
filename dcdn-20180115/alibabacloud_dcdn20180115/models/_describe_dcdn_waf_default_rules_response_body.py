# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafDefaultRulesResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeDcdnWafDefaultRulesResponseBodyContent] = None,
        request_id: str = None,
    ):
        # The rule configurations.
        self.content = content
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeDcdnWafDefaultRulesResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnWafDefaultRulesResponseBodyContent(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        rules: List[main_models.DescribeDcdnWafDefaultRulesResponseBodyContentRules] = None,
    ):
        # The protection scenario. Valid values:
        # 
        # *   **waf_group**: basic web protection.
        # *   **anti_scan**: scan protection.
        self.defense_scene = defense_scene
        # The rules.
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
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeDcdnWafDefaultRulesResponseBodyContentRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeDcdnWafDefaultRulesResponseBodyContentRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        config: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The default action of the rule. Valid values:
        # 
        # *   **monitor**
        # *   **deny**
        # *   **block**
        self.action = action
        # The default configuration of the rule.
        self.config = config
        # The default name of the rule.
        self.name = name
        # The default status of the rule. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.status = status
        # The type of the rule. Valid values:
        # 
        # *   **waf_group**: basic web protection.
        # *   **high_frequency**: high-frequency scanning blocking.
        # *   **directory_traversal**: directory traversal blocking.
        # *   **scan_tools**: scanner blocking.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

