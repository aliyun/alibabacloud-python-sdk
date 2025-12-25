# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentEscalationPolicyForModify(DaraModel):
    def __init__(
        self,
        description: str = None,
        enable: bool = None,
        escalation_stage_list: List[main_models.IncidentEscalationStageForView] = None,
        name: str = None,
    ):
        self.description = description
        self.enable = enable
        self.escalation_stage_list = escalation_stage_list
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.escalation_stage_list:
            for v1 in self.escalation_stage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        result['escalationStageList'] = []
        if self.escalation_stage_list is not None:
            for k1 in self.escalation_stage_list:
                result['escalationStageList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.escalation_stage_list = []
        if m.get('escalationStageList') is not None:
            for k1 in m.get('escalationStageList'):
                temp_model = main_models.IncidentEscalationStageForView()
                self.escalation_stage_list.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

