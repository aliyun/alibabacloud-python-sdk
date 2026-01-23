# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditZeroCreditShutdownResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        # Success or not</br>
        self.code = code
        # Request ID</br>
        self.data = data
        # Message</br>
        self.message = message
        # NO_STOP
        self.msg = msg
        # success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

