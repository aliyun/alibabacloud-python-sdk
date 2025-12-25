# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEventInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_event_id: str = None,
        request_id: str = None,
        success_count: int = None,
        success_event_id: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error ID.
        self.error_event_id = error_event_id
        # The request ID.
        self.request_id = request_id
        # The number of successful records.
        self.success_count = success_count
        # The ID of the successful event.
        self.success_event_id = success_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_event_id is not None:
            result['ErrorEventId'] = self.error_event_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.success_event_id is not None:
            result['SuccessEventId'] = self.success_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorEventId') is not None:
            self.error_event_id = m.get('ErrorEventId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('SuccessEventId') is not None:
            self.success_event_id = m.get('SuccessEventId')

        return self

