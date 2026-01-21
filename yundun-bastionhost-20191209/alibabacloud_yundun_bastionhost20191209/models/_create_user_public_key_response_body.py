# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserPublicKeyResponseBody(DaraModel):
    def __init__(
        self,
        public_key_id: str = None,
        request_id: str = None,
    ):
        # The ID of the public key.
        self.public_key_id = public_key_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

