# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        key_id: str = None,
        request_id: str = None,
    ):
        self.api_key = api_key
        self.key_id = key_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

