# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFullRequestSampleByInstanceIdRequest(DaraModel):
    def __init__(
        self,
        end: int = None,
        instance_id: str = None,
        role: str = None,
        sql_id: str = None,
        start: int = None,
    ):
        # The end of the time range to query. Specify a UNIX timestamp in milliseconds.
        # 
        # > The end time must be later than the start time, and the interval between the start time and end time cannot be less than 1 hour.
        # 
        # This parameter is required.
        self.end = end
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node information of a PolarDB-X 2.0 database instance.
        # 
        # - **polarx_cn**: compute node.
        # - **polarx_en**: data node.
        self.role = role
        # SQL ID。
        # 
        # This parameter is required.
        self.sql_id = sql_id
        # The beginning of the time range to query. Specify a UNIX timestamp in milliseconds.
        # 
        # > The start time must be within the storage duration of SQL Explorer for the database instance and cannot be earlier than 90 days before the current time.
        # 
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.role is not None:
            result['Role'] = self.role

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

