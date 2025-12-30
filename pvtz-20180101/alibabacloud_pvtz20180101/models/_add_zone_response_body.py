# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddZoneResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id
        # The name of the zone.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

