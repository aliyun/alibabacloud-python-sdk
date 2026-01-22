# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceTopologyRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        end_time: str = None,
        minute_simple: bool = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.end_time = end_time
        self.minute_simple = minute_simple
        # This parameter is required.
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.minute_simple is not None:
            result['MinuteSimple'] = self.minute_simple

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MinuteSimple') is not None:
            self.minute_simple = m.get('MinuteSimple')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

