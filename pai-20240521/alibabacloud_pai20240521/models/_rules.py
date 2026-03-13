# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai20240521 import models as main_models
from darabonba.model import DaraModel

class Rules(DaraModel):
    def __init__(
        self,
        scheduling_rule: main_models.SchedulingRule = None,
    ):
        self.scheduling_rule = scheduling_rule

    def validate(self):
        if self.scheduling_rule:
            self.scheduling_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheduling_rule is not None:
            result['SchedulingRule'] = self.scheduling_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchedulingRule') is not None:
            temp_model = main_models.SchedulingRule()
            self.scheduling_rule = temp_model.from_map(m.get('SchedulingRule'))

        return self

