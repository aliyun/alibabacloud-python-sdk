# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RdsCustomInitResponseBody(DaraModel):
    def __init__(
        self,
        register_uid_success: bool = None,
        request_id: str = None,
    ):
        self.register_uid_success = register_uid_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.register_uid_success is not None:
            result['RegisterUidSuccess'] = self.register_uid_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegisterUidSuccess') is not None:
            self.register_uid_success = m.get('RegisterUidSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

