# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetUserPasswordResponseBody(DaraModel):
    def __init__(
        self,
        random_password: str = None,
        request_id: str = None,
    ):
        self.random_password = random_password
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.random_password is not None:
            result['RandomPassword'] = self.random_password

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RandomPassword') is not None:
            self.random_password = m.get('RandomPassword')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

