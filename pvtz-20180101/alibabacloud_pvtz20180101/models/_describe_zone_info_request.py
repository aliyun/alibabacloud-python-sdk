# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeZoneInfoRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

