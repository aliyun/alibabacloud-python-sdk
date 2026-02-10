# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmVirusEventsRequest(DaraModel):
    def __init__(
        self,
        operation_all: int = None,
        operation_code: str = None,
        operation_range: str = None,
    ):
        # Specifies whether to handle all alert events. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # This parameter is required.
        self.operation_all = operation_all
        # The operation that you want to perform on the alert events. Valid values:
        # 
        # *   **default**: performs in-depth detection and removal
        # *   **ignore**: ignores the alert event
        # *   **advance_mark_mis_info**: adds the alert events to the whitelist
        # *   **manual_handled**: marks the alert events as manually handled
        # 
        # This parameter is required.
        self.operation_code = operation_code
        # The server on which you want to perform the alert events.
        self.operation_range = operation_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_all is not None:
            result['OperationAll'] = self.operation_all

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_range is not None:
            result['OperationRange'] = self.operation_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationAll') is not None:
            self.operation_all = m.get('OperationAll')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationRange') is not None:
            self.operation_range = m.get('OperationRange')

        return self

