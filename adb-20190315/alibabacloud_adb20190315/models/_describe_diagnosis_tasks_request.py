# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiagnosisTasksRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        host: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        process_id: str = None,
        region_id: str = None,
        stage_id: str = None,
        state: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The IP address from which the query was initiated.
        self.host = host
        # The order in which to sort the tasks by field. Specify the value in the JSON format. Example: `[{"Field":"CreateTime", "Type":"desc"}]`.
        # 
        # > 
        # 
        # *   `Field` specifies the field that is used to sort the tasks. Valid values of Field: `State`, `CreateTime`, `DBName`, `ProcessID`, `UpdateTime`, `JobName`, and `ProcessRows`.
        # 
        # *   `Type` specifies the sort order. Valid values of Type: `Desc` and `Asc`. The values are case-insensitive.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   30 (default)
        # *   50
        # *   100
        self.page_size = page_size
        # The query ID.
        # 
        # > You can call the [DescribeProcessList](https://help.aliyun.com/document_detail/190092.html) operation to query the IDs of queries that are being executed.
        # 
        # This parameter is required.
        self.process_id = process_id
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of a stage in the query that is specified by the `ProcessId` parameter.
        # 
        # This parameter is required.
        self.stage_id = stage_id
        # The state of the asynchronous import or export task to be queried. Valid values:
        # 
        # *   **RUNNING**
        # *   **FINISHED**
        # *   **FAILED**
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.host is not None:
            result['Host'] = self.host

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

