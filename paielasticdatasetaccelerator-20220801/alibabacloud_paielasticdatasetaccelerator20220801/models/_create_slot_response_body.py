# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSlotResponseBody(DaraModel):
    def __init__(
        self,
        endpoint_ids: str = None,
        request_id: str = None,
        slot_id: str = None,
    ):
        self.endpoint_ids = endpoint_ids
        self.request_id = request_id
        self.slot_id = slot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slot_id is not None:
            result['SlotId'] = self.slot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')

        return self

