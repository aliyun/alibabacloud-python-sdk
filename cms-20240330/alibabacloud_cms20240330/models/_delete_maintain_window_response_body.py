# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMaintainWindowResponseBody(DaraModel):
    def __init__(
        self,
        maintain_window_id: str = None,
        request_id: str = None,
    ):
        # The ID of the deleted silence policy.
        self.maintain_window_id = maintain_window_id
        # The unique ID of the request. You can use this ID for troubleshooting and ticket tracking.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maintain_window_id is not None:
            result['maintainWindowId'] = self.maintain_window_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maintainWindowId') is not None:
            self.maintain_window_id = m.get('maintainWindowId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

