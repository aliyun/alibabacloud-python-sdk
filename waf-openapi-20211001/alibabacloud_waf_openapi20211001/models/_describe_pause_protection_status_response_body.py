# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePauseProtectionStatusResponseBody(DaraModel):
    def __init__(
        self,
        pause_status: int = None,
        request_id: str = None,
    ):
        # Indicates whether WAF protection is paused.
        # 
        # *   **0**: indicates that WAF protection is not paused. This is the default value.
        # *   **1**: indicates that WAF protection is paused.
        self.pause_status = pause_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pause_status is not None:
            result['PauseStatus'] = self.pause_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PauseStatus') is not None:
            self.pause_status = m.get('PauseStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

