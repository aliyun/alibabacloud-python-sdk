# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportStatisticalDataRequest(DaraModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        export_type: str = None,
        instance_id: str = None,
        time_unit: str = None,
    ):
        # The start of the query time range. The value must be a Unix timestamp in milliseconds.
        self.begin_time_left_range = begin_time_left_range
        # The end of the query time range. The value must be a Unix timestamp in milliseconds.
        self.begin_time_right_range = begin_time_right_range
        # The export type.
        # 
        # This parameter is required.
        self.export_type = export_type
        # The ID of the Voice Navigator instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The time unit.
        # 
        # This parameter is required.
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range

        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')

        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        return self

