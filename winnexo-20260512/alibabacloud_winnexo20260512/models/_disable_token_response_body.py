# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        disabled: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # Indicates whether the token is disabled. Valid values:
        # - true: Disabled.
        # - false: Not disabled.
        self.disabled = disabled
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.disabled is not None:
            result['disabled'] = self.disabled

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

