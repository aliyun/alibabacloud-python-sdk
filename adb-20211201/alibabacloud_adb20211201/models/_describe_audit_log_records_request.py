# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditLogRecordsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        engine_type: str = None,
        host_address: str = None,
        order: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        process_id: str = None,
        proxy_user: str = None,
        query_keyword: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sql_type: str = None,
        start_time: str = None,
        succeed: str = None,
        user: str = None,
    ):
        # <props="china">The cluster ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The cluster ID of the Data Lakehouse Edition cluster.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the cluster IDs of all clusters in a specified region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database on which the SQL statement is executed.
        self.dbname = dbname
        # The end of the time range to query. Specify the time in UTC in the yyyy-MM-ddTHH:mmZ format.
        # > - The end time must be later than the start time.
        # > - The interval between the start time and the end time cannot exceed 24 hours.
        self.end_time = end_time
        # The engine type. Valid values:
        # - XIHE: audit logs of the default compute engine.
        # - AGENT_SERVERLESS: audit logs of the Serverless analytics feature.
        # 
        # If this parameter is not specified, the default value is XIHE.
        self.engine_type = engine_type
        # The IP address and port number of the client that executes the SQL statement.
        self.host_address = host_address
        # The sorting order based on specified fields. The value is in JSON format and is an ordered JSON array. Compound sorting is performed in the order of the input array. The array contains the `Field` and `Type` fields. Example: `[{"Field":"ExecutionStartTime","Type":"Desc"},{"Field":"ScanRows","Type":"Asc"}]`.
        # * `Field` specifies the field name for sorting. Valid values:
        #     * **HostAddress**: the address of the client that connects to the database.
        #     * **UserName**: the username.
        #     * **ExecutionStartTime**: the execution start time of the SQL statement.
        #     * **QueryTime**: the execution duration of the SQL statement.
        #     * **PeakMemoryUsage**: the peak memory usage during the execution of the SQL statement.
        #     * **ScanRows**: the number of rows scanned by tasks with data sources.
        #     * **ScanSize**: the amount of scanned data.
        #     * **ScanTime**: the total time consumed for scanning data.
        #     * **PlanningTime**: the time consumed for generating the execution plan.
        #     * **WallTime**: the cumulative CPU time of all operators across all nodes in the query.
        #     * **ProcessID**: the process ID.
        # 
        # * `Type` specifies the sorting type. Valid values:
        #     * **Desc**: descending order.
        #     * **Asc**: ascending order.
        self.order = order
        # The order in which the results are sorted by SQL execution time. Valid values:
        # * **asc**: ascending order.
        # * **desc**: descending order.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that does not exceed the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # - **10** (default)
        # - **30**
        # - **50**
        # - **100**
        self.page_size = page_size
        self.process_id = process_id
        # A reserved parameter.
        self.proxy_user = proxy_user
        # The keyword used to search the returned results.
        self.query_keyword = query_keyword
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the region ID of the cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the SQL statement. Valid values:
        # - **DELETE**
        # - **SELECT**
        # - **UPDATE**
        # - **INSERT INTO SELECT**
        # - **ALTER**
        # - **DROP**
        # - **CREATE**
        # 
        # > Only one type can be specified per request. If this parameter is not specified, all types are queried by default.
        self.sql_type = sql_type
        # The beginning of the time range to query. Specify the time in UTC in the yyyy-MM-ddTHH:mmZ format.
        # > SQL audit logs can be queried only when SQL audit is enabled, and only logs from the last 30 days are supported. If SQL audit is disabled and then re-enabled, only logs generated after re-enabling can be queried.
        self.start_time = start_time
        # Specifies whether the SQL statement is executed successfully. Valid values:
        # * **true**: Executed successfully.
        # * **false**: Execution failed.
        self.succeed = succeed
        # The username that executes the SQL statement.
        self.user = user

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

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.order is not None:
            result['Order'] = self.order

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user

        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.succeed is not None:
            result['Succeed'] = self.succeed

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')

        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

