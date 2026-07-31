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
        host_address: str = None,
        order: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
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
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the IDs of all clusters in a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database on which the SQL statement was executed.
        self.dbname = dbname
        # The end of the time range to query. The time must be in UTC and in the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # > - The end time must be later than the start time.
        # >
        # > - The time range cannot exceed 24 hours.
        self.end_time = end_time
        # The client IP address and port number.
        self.host_address = host_address
        # Specifies the fields for sorting the results. The value is a JSON string that is an array of objects. The order of objects in the array defines the sort priority. Each object contains the`Field` and`Type` parameters. Example: `[{"Field":"ExecutionStartTime","Type":"Desc"},{"Field":"ScanRows","Type":"Asc"}]`.
        # 
        # - `Field`: the field by which to sort the results. Valid values:
        # 
        #   - **HostAddress**: the client IP address.
        # 
        #   - **UserName**: the username.
        # 
        #   - **ExecutionStartTime**: the execution start time of the SQL statement.
        # 
        #   - **QueryTime**: the execution duration.
        # 
        #   - **PeakMemoryUsage**: the peak memory usage of the SQL statement.
        # 
        #   - **ScanRows**: the number of rows scanned by a task that involves a data source.
        # 
        #   - **ScanSize**: the amount of data scanned.
        # 
        #   - **ScanTime**: the time taken for the data scan.
        # 
        #   - **PlanningTime**: the time taken to generate the execution plan.
        # 
        #   - **WallTime**: the total CPU time of all operators on all nodes.
        # 
        #   - **ProcessID**: the process ID.
        # 
        # - `Type`: the sort order. Valid values:
        # 
        #   - **Desc**: descending order.
        # 
        #   - **Asc**: ascending order.
        self.order = order
        # The sort order for the results based on execution time. Valid values:
        # 
        # - **asc**: ascending order.
        # 
        # - **desc**: descending order.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The page size. Valid values:
        # 
        # - **10** (default)
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # A reserved parameter.
        self.proxy_user = proxy_user
        # A keyword used to perform a fuzzy search on the returned results.
        self.query_keyword = query_keyword
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the SQL statement. Valid values:
        # 
        # - **DELETE**
        # 
        # - **SELECT**
        # 
        # - **UPDATE**
        # 
        # - **INSERT INTO SELECT**
        # 
        # - **ALTER**
        # 
        # - **DROP**
        # 
        # - **CREATE**
        # 
        # > You can specify only one type per request. If this parameter is not specified, all types are queried by default.
        self.sql_type = sql_type
        # The start of the time range to query. The time must be in UTC and in the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # > You can query SQL audit logs only when this feature is enabled. Logs are available for the last 30 days. If you disable and then re-enable SQL audit, only logs generated after the feature was re-enabled are returned.
        self.start_time = start_time
        # Indicates whether the SQL statement was successfully executed. Valid values:
        # 
        # - **true**: The SQL statement succeeded.
        # 
        # - **false**: The SQL statement failed.
        self.succeed = succeed
        # The username that executed the SQL statement.
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

