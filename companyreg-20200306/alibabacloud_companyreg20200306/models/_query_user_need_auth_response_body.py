# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserNeedAuthResponseBody(DaraModel):
    def __init__(
        self,
        need_auth: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.need_auth = need_auth
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_auth is not None:
            result['NeedAuth'] = self.need_auth

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedAuth') is not None:
            self.need_auth = m.get('NeedAuth')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

