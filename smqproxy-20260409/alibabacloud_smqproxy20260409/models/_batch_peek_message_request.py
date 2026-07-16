# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchPeekMessageRequest(DaraModel):
    def __init__(
        self,
        num_of_messages: int = None,
        peekonly: bool = None,
    ):
        self.num_of_messages = num_of_messages
        self.peekonly = peekonly

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.num_of_messages is not None:
            result['numOfMessages'] = self.num_of_messages

        if self.peekonly is not None:
            result['peekonly'] = self.peekonly

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('numOfMessages') is not None:
            self.num_of_messages = m.get('numOfMessages')

        if m.get('peekonly') is not None:
            self.peekonly = m.get('peekonly')

        return self

