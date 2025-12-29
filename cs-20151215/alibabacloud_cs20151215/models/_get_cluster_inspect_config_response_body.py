# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetClusterInspectConfigResponseBody(DaraModel):
    def __init__(
        self,
        disabled_check_items: List[str] = None,
        enabled: bool = None,
        recurrence: str = None,
        request_id: str = None,
    ):
        # The list of disabled inspection items.
        self.disabled_check_items = disabled_check_items
        # Specifies whether to enable inspection.
        self.enabled = enabled
        # The inspection schedule defined through the RFC5545 Recurrence Rule syntax. You must specify BYHOUR and BYMINUTE. Only FREQ=DAILY is supported. COUNT and UNTIL are not supported.
        self.recurrence = recurrence
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disabledCheckItems') is not None:
            self.disabled_check_items = m.get('disabledCheckItems')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('recurrence') is not None:
            self.recurrence = m.get('recurrence')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

