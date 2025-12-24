# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListGatewayIntranetSupportedZoneResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The zones that are supported by the region.
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.zones is not None:
            result['Zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Zones') is not None:
            self.zones = m.get('Zones')

        return self

