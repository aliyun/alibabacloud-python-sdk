# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class EventRule(DaraModel):
    def __init__(
        self,
        conditional: List[main_models.ConditionalRule] = None,
        enable: bool = None,
        event_id: str = None,
        modify_time: str = None,
        operator: str = None,
        sample_rate: float = None,
    ):
        self.conditional = conditional
        self.enable = enable
        self.event_id = event_id
        self.modify_time = modify_time
        self.operator = operator
        self.sample_rate = sample_rate

    def validate(self):
        if self.conditional:
            for v1 in self.conditional:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditional'] = []
        if self.conditional is not None:
            for k1 in self.conditional:
                result['Conditional'].append(k1.to_map() if k1 else None)

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditional = []
        if m.get('Conditional') is not None:
            for k1 in m.get('Conditional'):
                temp_model = main_models.ConditionalRule()
                self.conditional.append(temp_model.from_map(k1))

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        return self

