# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlowLogRecordsRequest(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        end_time: str = None,
        instance_id: str = None,
        node_id: str = None,
        order_by: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_keyword: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        slow_log_record_type: str = None,
        start_time: str = None,
    ):
        # The database name.
        self.dbname = dbname
        # The end time of the query. The end time must be later than the start time, and the time range cannot exceed 1 day. The recommended time range is 1 hour. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID in the instance. Specify this parameter to query the slow query logs of a specific node.
        # > This parameter is available only when the instance uses the read/write splitting or cluster architecture.
        self.node_id = node_id
        # The field based on which the returned results are sorted. Valid values:
        # * **execution_time**: sorts the results based on the start time of request execution. This is the default value.
        # * **latency**: sorts the results based on the execution duration of requests.
        self.order_by = order_by
        # The sort order of the returned results. Valid values:
        # * **ASC**: ascending order.
        # * **DESC**: descending order. This is the default value.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: **1**.
        self.page_number = page_number
        # The maximum number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: **30**.
        self.page_size = page_size
        # The keyword used to search the returned results.
        self.query_keyword = query_keyword
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The slow log type. Valid values:
        # * **proxy**: Slow query logs on proxy nodes.
        # * **db**: Slow query logs on data nodes. This is the default value.
        self.slow_log_record_type = slow_log_record_type
        # The start time of the query. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z format. The time must be in UTC.
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
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.slow_log_record_type is not None:
            result['SlowLogRecordType'] = self.slow_log_record_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SlowLogRecordType') is not None:
            self.slow_log_record_type = m.get('SlowLogRecordType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

