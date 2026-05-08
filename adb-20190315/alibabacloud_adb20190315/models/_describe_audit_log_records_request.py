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
        query_keyword: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sql_type: str = None,
        start_time: str = None,
        succeed: str = None,
        user: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database on which you want to execute the SQL statement.
        self.dbname = dbname
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # > - The end time must be later than the start time.
        # > - The maximum time range that can be specified is 24 hours.
        self.end_time = end_time
        # The IP address and port number of the client that is used to execute the SQL statement.
        self.host_address = host_address
        # The order in which specified fields are sorted. Specify this parameter as an ordered JSON array that consists of the Field and Type fields.
        # 
        # *   Field specifies the field that is used to sort the retrieved entries. Valid values:
        # 
        #     *   HostAddress: the IP address of the client that is used to connect to the database.
        #     *   Succeed: specifies whether the SQL statement is successfully executed.
        #     *   TotalTime: the total amount of time that is consumed to execute the SQL statement.
        #     *   DBName: the name of the database on which the SQL statement is executed.
        #     *   SQLType: the type of the SQL statement.
        #     *   User: the username that is used to execute the SQL statement.
        #     *   ExecuteTime: the time to start executing the SQL statement.
        # 
        # *   Type specifies the sorting order. Valid values:
        # 
        #     *   Desc: descending order.
        #     *   Asc: ascending order.
        self.order = order
        # The sorting order of the retrieved entries. Valid values:
        # 
        # *   **asc**: sorts the retrieved entries by time in ascending order.
        # *   **desc**: sorts the retrieved entries by time in descending order.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. The value is an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **10**
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # >  If you leave this parameter empty, the value 10 is used.
        self.page_size = page_size
        # The keywords that are included in the SQL statement to query.
        self.query_keyword = query_keyword
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the SQL statement. Valid values:
        # 
        # *   **DELETE**
        # *   **SELECT**
        # *   **UPDATE**
        # *   **INSERT_INTO_SELECT**
        # *   **ALTER**
        # *   **DROP**
        # *   **CREATE**
        # 
        # > You can query only a single type of SQL statements at a time. If you leave this parameter empty, the **SELECT** statements are queried.
        self.sql_type = sql_type
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # > SQL audit logs can be queried only when SQL audit is enabled. Only SQL audit logs within the last 30 days can be queried. If SQL audit was disabled and re-enabled, only SQL audit logs from the time when SQL audit was re-enabled can be queried.
        self.start_time = start_time
        # Specifies whether the execution of the SQL statement succeeds. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.succeed = succeed
        # The name of the user who executed the SQL statement.
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

