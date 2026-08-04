# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUnreadMessageCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: int = None,
    ):
        # Status code returned by the service
        self.code = code
        # Error message
        self.message = message
        # Number of unread messages
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

