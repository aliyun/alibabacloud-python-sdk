# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlowLogRecordsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
        end_time: str = None,
        logical_operator: str = None,
        node_id: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_keywords: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The instance ID.
        # 
        # > If you set this parameter to the ID of a sharded cluster instance, you must also specify the `NodeId` parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.dbname = dbname
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # > 
        # 
        # *   The end time must be later than the start time.
        # 
        # *   The end time must be within 24 hours from the start time. Otherwise, the query fails.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The logical relationship among multiple keywords.
        # 
        # *   **or**
        # *   **and** (default value)
        self.logical_operator = logical_operator
        # The ID of the shard node.
        # 
        # > This parameter is required only when you specify the `DBInstanceId` parameter to the ID of a sharded cluster instance.
        self.node_id = node_id
        # The order of time in which the log entries to return are sorted. Valid values:
        # 
        # *   asc: The log entries are sorted by time in ascending order.
        # *   desc: The log entries are sorted by time in descending order.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return. The value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **30** to **100**.
        self.page_size = page_size
        # The keywords used for query. You can enter up to 10 keywords at a time. If you enter multiple keywords, separate the keywords with spaces.
        self.query_keywords = query_keywords
        # The ID of the resource group to which the instances you want to query belong.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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

        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator

        if self.node_id is not None:
            result['NodeId'] = self.node_id

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

        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

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

        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

