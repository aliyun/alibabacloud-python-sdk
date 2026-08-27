# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        token: str = None,
        token_masked: str = None,
    ):
        # The status code.
        self.code = code
        # The description of the status code.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The new token in plaintext. This value is returned only in this response. Store it securely.
        self.token = token
        # The masked token value.
        self.token_masked = token_masked

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.token is not None:
            result['token'] = self.token

        if self.token_masked is not None:
            result['tokenMasked'] = self.token_masked

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('tokenMasked') is not None:
            self.token_masked = m.get('tokenMasked')

        return self

