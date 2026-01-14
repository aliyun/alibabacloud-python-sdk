# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachDdosFromAcceleratorResponseBody(DaraModel):
    def __init__(
        self,
        ddos_id: str = None,
        request_id: str = None,
    ):
        # The ID of the Anti-DDoS Pro/Premium instance that was disassociated from the GA instance.
        self.ddos_id = ddos_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

