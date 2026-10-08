# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancePerformanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        key: str = None,
        node_id: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end time of the query. Format: <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z (UTC).
        # > The interval between the start time and end time must be greater than the monitoring frequency of your instance. Otherwise, an empty list may be returned.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The performance metrics that you want to query. Separate multiple values with commas (,). You can specify up to 30 metrics. For more information, see [Performance parameters](https://help.aliyun.com/document_detail/26316.html).
        # > If **Key** is set to **MySQL_SpaceUsage** or **SQLServer_SpaceUsage**, only monitoring data within the last day can be queried.
        # 
        # This parameter is required.
        self.key = key
        # The unique identifier of the instance.
        self.node_id = node_id
        self.resource_owner_id = resource_owner_id
        # The start time of the query. Format: <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z (UTC).
        # > The interval between the start time and end time must be greater than the monitoring frequency of your instance. Otherwise, an empty list may be returned.
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key is not None:
            result['Key'] = self.key

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

