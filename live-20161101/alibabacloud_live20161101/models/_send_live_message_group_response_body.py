# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendLiveMessageGroupResponseBody(DaraModel):
    def __init__(
        self,
        msg_tid: str = None,
        request_id: str = None,
    ):
        # The ID of the message, which is a unique identifier that can be used to delete the message. The ID can be up to 64 bytes in length and can contain letters and digits.
        self.msg_tid = msg_tid
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg_tid is not None:
            result['MsgTid'] = self.msg_tid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgTid') is not None:
            self.msg_tid = m.get('MsgTid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

