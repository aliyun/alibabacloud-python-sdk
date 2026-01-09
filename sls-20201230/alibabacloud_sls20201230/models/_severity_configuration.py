# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class SeverityConfiguration(DaraModel):
    def __init__(
        self,
        eval_condition: main_models.ConditionConfiguration = None,
        severity: int = None,
    ):
        self.eval_condition = eval_condition
        self.severity = severity

    def validate(self):
        if self.eval_condition:
            self.eval_condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eval_condition is not None:
            result['evalCondition'] = self.eval_condition.to_map()

        if self.severity is not None:
            result['severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('evalCondition') is not None:
            temp_model = main_models.ConditionConfiguration()
            self.eval_condition = temp_model.from_map(m.get('evalCondition'))

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        return self

