# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobDebugDataRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        end_time: int = None,
        instance_id: str = None,
        job_name: str = None,
        limit: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.cursor = cursor
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_name = job_name
        self.limit = limit
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
        if self.cursor is not None:
            result['Cursor'] = self.cursor

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

