# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateClusterInspectConfigRequest(DaraModel):
    def __init__(
        self,
        disabled_check_items: List[str] = None,
        enabled: bool = None,
        recurrence: str = None,
    ):
        # The list of disabled inspection items.
        self.disabled_check_items = disabled_check_items
        # Specifies whether to enable cluster inspection.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The inspection period defined using RFC5545 Recurrence Rule. You must specify BYHOUR and BYMINUTE. Only FREQ=DAILY is supported. COUNT or UNTIL is not supported.
        # 
        # This parameter is required.
        self.recurrence = recurrence

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

        if self.recurrence is not None:
            result['recurrence'] = self.recurrence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disabledCheckItems') is not None:
            self.disabled_check_items = m.get('disabledCheckItems')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('recurrence') is not None:
            self.recurrence = m.get('recurrence')

        return self

