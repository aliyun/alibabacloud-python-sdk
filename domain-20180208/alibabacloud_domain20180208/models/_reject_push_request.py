# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RejectPushRequest(DaraModel):
    def __init__(
        self,
        push_no: str = None,
    ):
        # Push编号
        # 
        # This parameter is required.
        self.push_no = push_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_no is not None:
            result['PushNo'] = self.push_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushNo') is not None:
            self.push_no = m.get('PushNo')

        return self

