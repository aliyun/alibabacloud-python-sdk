# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class RulesInfo(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.ConditionBasicInfo] = None,
        count: int = None,
        dialogues: List[main_models.RuleTestDialogue] = None,
        page_number: int = None,
        page_size: int = None,
        rules: List[main_models.RuleInfo] = None,
    ):
        self.conditions = conditions
        self.count = count
        self.dialogues = dialogues
        self.page_number = page_number
        self.page_size = page_size
        self.rules = rules

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.dialogues:
            for v1 in self.dialogues:
                 if v1:
                    v1.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        result['Dialogues'] = []
        if self.dialogues is not None:
            for k1 in self.dialogues:
                result['Dialogues'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ConditionBasicInfo()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.dialogues = []
        if m.get('Dialogues') is not None:
            for k1 in m.get('Dialogues'):
                temp_model = main_models.RuleTestDialogue()
                self.dialogues.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.RuleInfo()
                self.rules.append(temp_model.from_map(k1))

        return self

