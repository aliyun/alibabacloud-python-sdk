# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTokenInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        enabled: bool = None,
        gmt_create: str = None,
        message: str = None,
        request_id: str = None,
        token_masked: str = None,
    ):
        # The error code.
        self.code = code
        # Indicates whether the token is enabled.
        self.enabled = enabled
        # The creation time.
        self.gmt_create = gmt_create
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
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

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.token_masked is not None:
            result['tokenMasked'] = self.token_masked

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('tokenMasked') is not None:
            self.token_masked = m.get('tokenMasked')

        return self

