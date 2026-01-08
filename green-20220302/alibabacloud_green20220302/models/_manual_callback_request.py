# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManualCallbackRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        checksum: str = None,
        code: str = None,
        data: str = None,
        msg: str = None,
        req_id: str = None,
    ):
        # Channel field
        self.channel = channel
        # Checksum.
        self.checksum = checksum
        # Code value
        self.code = code
        # Returned data.
        self.data = data
        # Message information
        self.msg = msg
        # Platform request ID, used for troubleshooting assistance
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.checksum is not None:
            result['Checksum'] = self.checksum

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        return self

