# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSignatureRequest(DaraModel):
    def __init__(
        self,
        security_token: str = None,
        signature_id: str = None,
    ):
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The ID of the key to be deleted.
        # 
        # This parameter is required.
        self.signature_id = signature_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')

        return self

