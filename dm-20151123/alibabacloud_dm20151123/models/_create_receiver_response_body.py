# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReceiverResponseBody(DaraModel):
    def __init__(
        self,
        receiver_id: str = None,
        request_id: str = None,
    ):
        # Receiver list ID
        self.receiver_id = receiver_id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

