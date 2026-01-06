# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPfsSqlSampleRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        node_id: str = None,
        sql_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time. You can view the data of up to seven days in the previous 30 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        # 
        # >  Only ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters are supported
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # >  For ApsaraDB RDS for MySQL Cluster Edition instances or PolarDB for MySQL clusters, you must specify the node ID.
        self.node_id = node_id
        # The SQL ID.
        self.sql_id = sql_id
        # The beginning of the time range to query. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

