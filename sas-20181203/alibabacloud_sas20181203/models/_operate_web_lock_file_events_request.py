# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateWebLockFileEventsRequest(DaraModel):
    def __init__(
        self,
        deal_all: int = None,
        event_ids: List[int] = None,
        operation_code: str = None,
    ):
        # Specifies whether to handle all alert events that are generated for web tamper proofing. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # This parameter is required.
        self.deal_all = deal_all
        # The IDs of alert events.
        # 
        # This parameter is required.
        self.event_ids = event_ids
        # The operation that you want to perform on the alert events. Valid values:
        # 
        # *   **mark_mis_info**: marks the alert events as false positives
        # *   **rm_mark_mis_info**: cancels marking the alerts events as false positives
        # *   **offline_handled**: marks the alert events as handled offline
        # *   **whitelist**: adds the alert events to the whitelist
        # *   **rm_whitelist**: cancels adding the alert events to the whitelist
        # 
        # This parameter is required.
        self.operation_code = operation_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deal_all is not None:
            result['DealAll'] = self.deal_all

        if self.event_ids is not None:
            result['EventIds'] = self.event_ids

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DealAll') is not None:
            self.deal_all = m.get('DealAll')

        if m.get('EventIds') is not None:
            self.event_ids = m.get('EventIds')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        return self

