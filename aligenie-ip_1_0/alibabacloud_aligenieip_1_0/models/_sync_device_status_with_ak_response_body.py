# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncDeviceStatusWithAkResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        result: bool = None,
        status_code: int = None,
        request_id: str = None,
    ):
        self.message = message
        self.result = result
        self.status_code = status_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.result is not None:
            result['Result'] = self.result

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

