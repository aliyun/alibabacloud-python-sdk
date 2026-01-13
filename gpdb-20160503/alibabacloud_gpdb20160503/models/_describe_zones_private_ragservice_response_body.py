# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeZonesPrivateRAGServiceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zone_ids: List[str] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The list of zones.
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

