# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendMessageResponseBody(DaraModel):
    def __init__(
        self,
        msg_id: str = None,
        request_id: str = None,
    ):
        # The unique message ID that is returned by the ApsaraMQ for MQTT broker after the message is sent.
        self.msg_id = msg_id
        # The unique ID that the system generates for the request. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

