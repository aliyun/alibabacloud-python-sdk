# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLakebaseMountParameterGroupChangeLogsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        parameter_group_id: str = None,
        polar_fs_instance_id: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The end time of the query (UTC).
        self.end_time = end_time
        # The parameter name filter.
        self.name = name
        # The parameter template ID.
        # 
        # This parameter is required.
        self.parameter_group_id = parameter_group_id
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time of the query (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

