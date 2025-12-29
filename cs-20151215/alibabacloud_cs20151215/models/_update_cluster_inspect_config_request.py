# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateClusterInspectConfigRequest(DaraModel):
    def __init__(
        self,
        disabled_check_items: List[str] = None,
        enabled: bool = None,
        schedule_time: str = None,
    ):
        # The list of disabled inspection check items.
        self.disabled_check_items = disabled_check_items
        # Specifies whether to enable cluster inspection.
        self.enabled = enabled
        # The inspection period defined using RFC5545 Recurrence Rule. You must specify BYHOUR and BYMINUTE. Only FREQ=DAILY is supported. COUNT or UNTIL is not supported.
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled_check_items is not None:
            result['disabledCheckItems'] = self.disabled_check_items

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disabledCheckItems') is not None:
            self.disabled_check_items = m.get('disabledCheckItems')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')

        return self

