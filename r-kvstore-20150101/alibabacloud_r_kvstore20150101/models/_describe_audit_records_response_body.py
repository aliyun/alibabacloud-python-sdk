# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeAuditRecordsResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_name: str = None,
        items: main_models.DescribeAuditRecordsResponseBodyItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        total_record_count: int = None,
    ):
        # The end time of the query.
        self.end_time = end_time
        # The name of the instance.
        self.instance_name = instance_name
        # The collection of returned audit log entries.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The maximum number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time
        # The total number of returned entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeAuditRecordsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeAuditRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        sql: List[main_models.DescribeAuditRecordsResponseBodyItemsSQL] = None,
    ):
        self.sql = sql

    def validate(self):
        if self.sql:
            for v1 in self.sql:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SQL'] = []
        if self.sql is not None:
            for k1 in self.sql:
                result['SQL'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sql = []
        if m.get('SQL') is not None:
            for k1 in m.get('SQL'):
                temp_model = main_models.DescribeAuditRecordsResponseBodyItemsSQL()
                self.sql.append(temp_model.from_map(k1))

        return self

class DescribeAuditRecordsResponseBodyItemsSQL(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        database_name: str = None,
        execute_time: str = None,
        host_address: str = None,
        ipaddress: str = None,
        node_id: str = None,
        sqltext: str = None,
        sqltype: str = None,
        total_execution_times: str = None,
    ):
        # The username of the account.
        self.account_name = account_name
        # The database name.
        self.database_name = database_name
        # The time when the command was run.
        self.execute_time = execute_time
        # The IP address of the client.
        self.host_address = host_address
        # The IP address of the instance.
        self.ipaddress = ipaddress
        # The ID of the node.
        # 
        # > A specific node ID is returned only if the instance uses the cluster or read/write splitting architecture.
        self.node_id = node_id
        # The command that was run.
        self.sqltext = sqltext
        # The type of the command.
        self.sqltype = sqltype
        # The amount of time consumed to run the command.
        self.total_execution_times = total_execution_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.sqltype is not None:
            result['SQLType'] = self.sqltype

        if self.total_execution_times is not None:
            result['TotalExecutionTimes'] = self.total_execution_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')

        if m.get('TotalExecutionTimes') is not None:
            self.total_execution_times = m.get('TotalExecutionTimes')

        return self

