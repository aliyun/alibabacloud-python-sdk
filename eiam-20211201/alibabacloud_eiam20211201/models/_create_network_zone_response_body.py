# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkZoneResponseBody(DaraModel):
    def __init__(
        self,
        network_zone_id: str = None,
        request_id: str = None,
    ):
        self.network_zone_id = network_zone_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_zone_id is not None:
            result['NetworkZoneId'] = self.network_zone_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkZoneId') is not None:
            self.network_zone_id = m.get('NetworkZoneId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

