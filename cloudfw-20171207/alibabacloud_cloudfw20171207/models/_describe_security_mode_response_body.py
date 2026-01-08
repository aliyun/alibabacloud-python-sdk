# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityModeResponseBody(DaraModel):
    def __init__(
        self,
        module: str = None,
        request_id: str = None,
        security_mode: int = None,
    ):
        self.module = module
        self.request_id = request_id
        self.security_mode = security_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')

        return self

