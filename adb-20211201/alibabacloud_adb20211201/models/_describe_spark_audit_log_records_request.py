# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSparkAuditLogRecordsRequest(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        process_id: str = None,
        proxy_user: str = None,
        region_id: str = None,
        resource_group_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sqltext: str = None,
        start_time: str = None,
        statement_id: str = None,
        statement_source: str = None,
        status: str = None,
        total_time: str = None,
        user: str = None,
    ):
        # The source IP address.
        self.client_ip = client_ip
        # The cluster ID.
        # 
        # > 
        # 
        # *   You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Query end time. The end time must be later than the start time, and the interval between them must be less than 1 day. Format: yyyy-MM-ddTHH:mmZ (UTC time).
        self.end_time = end_time
        # Sort the SQL statements based on specified fields. The format is a JSON array that preserves order, and composite sorting is performed according to the sequence of objects in the array. Each object contains two fields: `Field` and `Type`. For example:`[{"Field":"CreateTime", "Type": "desc" }]`. Where:
        # 
        # *   `Field` specifies the field that is used to sort the SQL statements. Valid values:
        # 
        #     *   `ResourceGroupName`: The name of the resource group.
        #     *   `Status` :SQL execution status.
        #     *   `User`: The username that is used to execute the SQL statement.
        #     *   `ExecuteTime`: The start time of SQL execution.
        #     *   `TotalTime`: The amount of time consumed to execute the SQL statement.
        #     *   `ProcessId`: Query ID.
        #     *   `ClientIp`: The source IP address.
        #     *   `StatementSource`: The source from which the query was initiated.
        # 
        # *   `Type` specifies the sorting order. Valid values (case-insensitive):
        # 
        #     *   `Desc`: Descending order.
        #     *   `Asc`: Ascending order.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The query ID.
        self.process_id = process_id
        # This parameter is deprecated.
        self.proxy_user = proxy_user
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/612293.html) operation to query the available regions and zones, including region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group name.
        # 
        # >  You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/612410.html) operation to query the resource group ID within a cluster.
        self.resource_group_name = resource_group_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The keyword in the SQL statement.
        self.sqltext = sqltext
        # Query start time. Format: *yyyy-MM-ddTHH:mmZ* (UTC time).
        # 
        # >  We recommend that you set the query start time to any point in time within 30 days.
        self.start_time = start_time
        # The ID of the statement.
        self.statement_id = statement_id
        # The source from which the query was initiated.
        # 
        # Valid values:
        # 
        # *   SQL_EDITOR: SQL_EDITOR.
        # *   JDBC: JDBC.
        self.statement_source = statement_source
        # The execution status of the SQL statement.
        # 
        # Valid values:
        # 
        # *   cancel: The task is canceled .
        # *   finished: The execution succeeds .
        # *   error:The execution fails .
        # *   timeout: The execution timed out .
        self.status = status
        # The duration of the SQL statement. Unit: milliseconds.
        self.total_time = total_time
        # The username that is used to execute SQL statements.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

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
            result['ProcessId'] = self.process_id

        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        if self.statement_source is not None:
            result['StatementSource'] = self.statement_source

        if self.status is not None:
            result['Status'] = self.status

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

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

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        if m.get('StatementSource') is not None:
            self.statement_source = m.get('StatementSource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

