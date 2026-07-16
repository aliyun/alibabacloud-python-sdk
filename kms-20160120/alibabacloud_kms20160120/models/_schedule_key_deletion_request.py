# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduleKeyDeletionRequest(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        pending_window_in_days: int = None,
    ):
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The scheduled period after which the CMK is deleted. During this period, the CMK is in the PendingDeletion state. After this period ends, you cannot cancel the key deletion task.
        # 
        # Valid values: 7 to 366.
        # 
        # Unit: days.
        # 
        # This parameter is required.
        self.pending_window_in_days = pending_window_in_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.pending_window_in_days is not None:
            result['PendingWindowInDays'] = self.pending_window_in_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('PendingWindowInDays') is not None:
            self.pending_window_in_days = m.get('PendingWindowInDays')

        return self

