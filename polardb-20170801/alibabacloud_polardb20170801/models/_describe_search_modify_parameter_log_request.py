# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSearchModifyParameterLogRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The ID of the PolarDB primary cluster. This ID is used to query the parameter modification history of the Search cluster associated with the current account.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Only records modified before this time are returned. The end time cannot be earlier than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start time of the query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. Only records modified after this time are returned.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

