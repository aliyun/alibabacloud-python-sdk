# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNatFirewallPreCheckResponseBody(DaraModel):
    def __init__(
        self,
        pre_check_id: str = None,
        request_id: str = None,
    ):
        self.pre_check_id = pre_check_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pre_check_id is not None:
            result['PreCheckId'] = self.pre_check_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreCheckId') is not None:
            self.pre_check_id = m.get('PreCheckId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

