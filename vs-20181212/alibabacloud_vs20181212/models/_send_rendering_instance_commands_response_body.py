# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendRenderingInstanceCommandsResponseBody(DaraModel):
    def __init__(
        self,
        cmd_id: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.cmd_id = cmd_id
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd_id is not None:
            result['CmdId'] = self.cmd_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CmdId') is not None:
            self.cmd_id = m.get('CmdId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

