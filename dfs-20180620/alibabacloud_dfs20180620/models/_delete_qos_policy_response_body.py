# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteQosPolicyResponseBody(DaraModel):
    def __init__(
        self,
        error_messages: str = None,
        request_id: str = None,
    ):
        self.error_messages = error_messages
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_messages is not None:
            result['ErrorMessages'] = self.error_messages

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessages') is not None:
            self.error_messages = m.get('ErrorMessages')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

