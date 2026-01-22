# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreCheckSqlFlashbackTaskRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        polardbx_instance_id: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.polardbx_instance_id = polardbx_instance_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.polardbx_instance_id is not None:
            result['PolardbxInstanceId'] = self.polardbx_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PolardbxInstanceId') is not None:
            self.polardbx_instance_id = m.get('PolardbxInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

