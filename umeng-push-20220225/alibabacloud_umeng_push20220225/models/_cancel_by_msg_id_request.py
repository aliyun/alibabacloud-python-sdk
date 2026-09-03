# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelByMsgIdRequest(DaraModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        return self

