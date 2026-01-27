# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EncryptPasswordResponseBody(DaraModel):
    def __init__(
        self,
        encrypted_password: str = None,
        request_id: str = None,
    ):
        # The encrypted password.
        self.encrypted_password = encrypted_password
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_password is not None:
            result['EncryptedPassword'] = self.encrypted_password

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedPassword') is not None:
            self.encrypted_password = m.get('EncryptedPassword')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

