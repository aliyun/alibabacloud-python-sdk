# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachDdosToAcceleratorResponseBody(DaraModel):
    def __init__(
        self,
        ddos_id: str = None,
        ga_id: str = None,
        request_id: str = None,
    ):
        # The ID of the Anti-DDoS Pro/Premium instance that is associated with the GA instance.
        self.ddos_id = ddos_id
        # The ID of the GA instance that is associated with the Anti-DDoS Pro/Premium instance.
        self.ga_id = ga_id
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

        if self.ga_id is not None:
            result['GaId'] = self.ga_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')

        if m.get('GaId') is not None:
            self.ga_id = m.get('GaId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

