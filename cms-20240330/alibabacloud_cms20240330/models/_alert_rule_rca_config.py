# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlertRuleRcaConfig(DaraModel):
    def __init__(
        self,
        digital_employee_name: str = None,
        enable_rca: bool = None,
    ):
        self.digital_employee_name = digital_employee_name
        self.enable_rca = enable_rca

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.enable_rca is not None:
            result['enableRca'] = self.enable_rca

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('enableRca') is not None:
            self.enable_rca = m.get('enableRca')

        return self

