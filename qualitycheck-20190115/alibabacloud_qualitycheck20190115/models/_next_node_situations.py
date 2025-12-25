# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class NextNodeSituations(DaraModel):
    def __init__(
        self,
        condition_group: List[main_models.NextNodeSituationsConditionGroup] = None,
        type: str = None,
    ):
        self.condition_group = condition_group
        self.type = type

    def validate(self):
        if self.condition_group:
            for v1 in self.condition_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionGroup'] = []
        if self.condition_group is not None:
            for k1 in self.condition_group:
                result['ConditionGroup'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_group = []
        if m.get('ConditionGroup') is not None:
            for k1 in m.get('ConditionGroup'):
                temp_model = main_models.NextNodeSituationsConditionGroup()
                self.condition_group.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class NextNodeSituationsConditionGroup(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.JudgeNodeMetaDesc] = None,
        type: str = None,
    ):
        self.conditions = conditions
        self.type = type

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.JudgeNodeMetaDesc()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

