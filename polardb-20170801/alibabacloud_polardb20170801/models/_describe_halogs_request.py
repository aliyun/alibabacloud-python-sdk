# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHALogsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbnode_id: str = None,
        end_time: str = None,
        log_type: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The node ID.
        # 
        # > 这是一个optional 字段，需要增加一个条件If specified,If specified, queries the high availability (HA) switchover records of `DBNodeId`. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to view the detailed information about all clusters under your account, including node IDs.
        self.dbnode_id = dbnode_id
        # The end of the time range to query. The end time must be later than the start time. The time follows the `YYYY-MM-DDThh:mm:ssZ` format (UTC time).
        self.end_time = end_time
        # The log type.
        # 
        # This parameter is required.
        self.log_type = log_type
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 5 to 50. Default value: 10.
        self.page_size = page_size
        # The beginning of the time range to query. The time follows the `YYYY-MM-DDThh:mm:ssZ` format (UTC time).
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

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

