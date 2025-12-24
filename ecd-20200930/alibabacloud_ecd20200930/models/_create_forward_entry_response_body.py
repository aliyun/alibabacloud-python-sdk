# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateForwardEntryResponseBody(DaraModel):
    def __init__(
        self,
        forward_entry_id: str = None,
        request_id: str = None,
    ):
        self.forward_entry_id = forward_entry_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

