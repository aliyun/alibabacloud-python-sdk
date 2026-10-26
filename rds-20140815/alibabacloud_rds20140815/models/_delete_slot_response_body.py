# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSlotResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        slot_name: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The name of the replication slot.
        self.slot_name = slot_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slot_name is not None:
            result['SlotName'] = self.slot_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlotName') is not None:
            self.slot_name = m.get('SlotName')

        return self

