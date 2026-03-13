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
        # The trigger period expression. You can specify to trigger based on a time interval. For example, the expression @every 4m indicates that the triggering is performed every four minutes. You can also specify to trigger based on a cron expression, for example, 0 0 4 \\* \\* \\*.
        self.cron_expression = cron_expression
        # Specify whether to enable the trigger.
        self.enable = enable
        # Enter custom parameters. The trigger message is used as the value of the payload in the event.
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

