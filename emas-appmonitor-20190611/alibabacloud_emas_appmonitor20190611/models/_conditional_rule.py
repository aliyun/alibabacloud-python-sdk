# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class ConditionalRule(DaraModel):
    def __init__(
        self,
        filter: main_models.EventFilter = None,
        modify_time: str = None,
        name: str = None,
        operator: str = None,
        sample_rate: float = None,
    ):
        self.filter = filter
        self.modify_time = modify_time
        self.name = name
        self.operator = operator
        self.sample_rate = sample_rate

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = main_models.EventFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        return self

