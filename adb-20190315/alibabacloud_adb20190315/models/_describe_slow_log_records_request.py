# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlowLogRecordsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        process_id: str = None,
        range: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        state: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.dbname = dbname
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time. The specified time range must be less than seven days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The order in which to sort the retrieved entries by field. Specify this parameter in the JSON format. The value is an ordered array that uses the order of the input array and contains `Field` and `Type`. Example: `[{"Field":"ExecutionStartTime","Type":"Desc"},{"Field":"ScanRows","Type":"Asc"}]`.
        # 
        # *   `Field`: the field that is used to sort the retrieved entries. Valid values:
        # 
        #     *   **HostAddress**: the IP address of the client that is used to connect to the database.
        #     *   **UserName**: the username.
        #     *   **ExecutionStartTime**: the start time of the query execution.
        #     *   **QueryTime**: the amount of time consumed to execute the SQL statement.
        #     *   **PeakMemoryUsage**: the maximum memory usage when the SQL statement is executed.
        #     *   **ScanRows**: the number of rows to be scanned from a data source in the task.
        #     *   **ScanSize**: the amount of data to be scanned.
        #     *   **ScanTime**: the total amount of time consumed to scan data.
        #     *   **PlanningTime**: the amount of time consumed to generate execution plans.
        #     *   **WallTime**: the accumulated CPU Time values of all operators in the query on each node.
        #     *   **ProcessID**: the ID of the process.
        # 
        # *   `Type`: the sorting type of the retrieved entries. Valid values:
        # 
        #     *   **Desc**: descending order
        #     *   **Asc**: ascending order
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: 30.
        self.page_size = page_size
        # The ID of the process.
        self.process_id = process_id
        # The range conditions used to filter specified fields, including `Max` and `Min`. Specify this parameter in the JSON format. Example: `[{"Field":"ScanSize","Min":"1000000","Max":"10000000"},{"Field":"QueryTime","Min":"1000","Max":"10000"}]`.
        # 
        # `Field`: the field to be filtered. Valid values:
        # 
        # *   **ScanSize**: the amount of data to be scanned. Unit: KB.
        # *   **QueryTime**: the amount of time consumed to execute the statement. Unit: milliseconds.
        # *   **PeakMemoryUsage**: the maximum memory usage when the SQL statement is executed. Unit: KB.
        # 
        # >  `Min` indicates the minimum value of the query range (left operand). `Max` indicates the maximum value of the query range (right operand). Max and Min are both of the String type.
        self.range = range
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The state of the query. Valid values:
        # 
        # *   **Successed**: successful
        # *   **Failed**: failed
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

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_id is not None:
            result['ProcessID'] = self.process_id

        if self.range is not None:
            result['Range'] = self.range

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')

        if m.get('Range') is not None:
            self.range = m.get('Range')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

