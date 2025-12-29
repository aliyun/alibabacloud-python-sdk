# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAuthKeyResponseBody(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        request_id: str = None,
    ):
        # The key that can be used for authorization activation. The authorization key is valid for 30 minutes and cannot be reused. It is recommended to re-obtain it before each activation.
        self.auth_key = auth_key
        # The ID of this request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

