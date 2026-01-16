# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TimerTriggerConfig(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        enable: bool = None,
        payload: str = None,
    ):
        self.cron_expression = cron_expression
        self.enable = enable
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.enable is not None:
            result['enable'] = self.enable

        if self.payload is not None:
            result['payload'] = self.payload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('payload') is not None:
            self.payload = m.get('payload')

        return self

