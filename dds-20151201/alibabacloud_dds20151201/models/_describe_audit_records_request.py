# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditRecordsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        form: str = None,
        logical_operator: str = None,
        node_id: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_keywords: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        user: str = None,
    ):
        # The instance ID.
        # 
        # > If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database to be queried. By default, all databases are queried.
        self.database = database
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > The end time must be within 24 hours from the start time. Otherwise, the query fails.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The form of the audit log that the operation returns. Valid values:
        # 
        # *   **File**: triggers the generation of audit logs. If this parameter is set to File, only common parameters are returned.
        # *   **Stream** (default): returns data streams.
        self.form = form
        # The logical relationship between multiple keywords. Valid values:
        # 
        # *   **or**
        # *   **and** (default value)
        self.logical_operator = logical_operator
        # The ID of the mongos node or shard node in the instance.
        # 
        # > This parameter takes effect only when you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id
        # The order of time in which the log entries to return are sorted. Valid values:
        # 
        # *   **asc**: The log entries are sorted by time in ascending order.
        # *   **desc**: The log entries are sorted by time in descending order.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return. The valid value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: 1.
        self.page_number = page_number
        # The number of entries to return per page. Default value: 30. Valid values: **30**, **50**, and **100**.
        self.page_size = page_size
        # The keywords used for query. You can enter up to 10 keywords at a time. If you enter multiple keywords, separate the keywords with spaces.
        self.query_keywords = query_keywords
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The user of the database. If you do not specify this parameter, this operation returns records of all users.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database is not None:
            result['Database'] = self.database

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.form is not None:
            result['Form'] = self.form

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Form') is not None:
            self.form = m.get('Form')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

