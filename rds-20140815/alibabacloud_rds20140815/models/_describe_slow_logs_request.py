# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlowLogsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sort_key: str = None,
        start_time: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.dbname = dbname
        # The end of the time range to query. The end time must be later than the start time. The time span between the start time and the end time cannot exceed 31 days. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*Z format. The time must be in UTC.
        # 
        # >  If the end date of the query is the same as the start date of the query, you can query the logs that are generated at 08:00 on the start date of the query. You can query the slow logs within a maximum time range of 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from 1.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30** to **100**. Default value: **30**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The dimension based on which the system sorts the entries to return. Valid values:
        # 
        # *   **TotalExecutionCounts**: The system sorts the entries to return based on the number of times that SQL statements are executed.
        # *   **TotalQueryTimes**: The system sorts the entries to return based on the total execution duration.
        # *   **TotalLogicalReads**: The system sorts the entries to return based on the total number of logical reads.
        # *   **TotalPhysicalReads**: The system sorts the entries to return based on the total number of physical reads.
        # 
        # > This parameter is supported only for instances that run SQL Server 2008 R2.
        self.sort_key = sort_key
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*Z format. The time must be in UTC.
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

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sort_key is not None:
            result['SortKey'] = self.sort_key

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

