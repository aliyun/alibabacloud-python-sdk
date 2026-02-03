# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        instance_id: str = None,
        items: main_models.DescribeSlowLogRecordsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        total_record_count: int = None,
    ):
        # The database engine that the instance runs.
        self.engine = engine
        # The ID of the instance.
        self.instance_id = instance_id
        # The slow query log entries.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of log entries returned on the current page.
        self.page_record_count = page_record_count
        # The maximum number of log entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time
        # The total number of returned log entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

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
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSlowLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        log_records: List[main_models.DescribeSlowLogRecordsResponseBodyItemsLogRecords] = None,
    ):
        self.log_records = log_records

    def validate(self):
        if self.log_records:
            for v1 in self.log_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogRecords'] = []
        if self.log_records is not None:
            for k1 in self.log_records:
                result['LogRecords'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_records = []
        if m.get('LogRecords') is not None:
            for k1 in m.get('LogRecords'):
                temp_model = main_models.DescribeSlowLogRecordsResponseBodyItemsLogRecords()
                self.log_records.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogRecordsResponseBodyItemsLogRecords(DaraModel):
    def __init__(
        self,
        account: str = None,
        account_name: str = None,
        command: str = None,
        dbname: str = None,
        data_base_name: str = None,
        elapsed_time: int = None,
        execute_time: str = None,
        ipaddress: str = None,
        node_id: str = None,
    ):
        # The ID of the account.
        self.account = account
        # The username of the account.
        self.account_name = account_name
        # The slow query statement.
        self.command = command
        # The database name.
        self.dbname = dbname
        # The database name. This parameter serves the same purpose as the **DBName** parameter. We recommend that you use the **DBName** parameter.
        self.data_base_name = data_base_name
        # The amount of time consumed to execute the slow query statement. Unit: microseconds.
        self.elapsed_time = elapsed_time
        # The start time when the slow query statement was executed. The time is displayed in the YYYY-MM-DDTHH:mm:ssZ format.
        self.execute_time = execute_time
        # The IP address of the client.
        self.ipaddress = ipaddress
        # The node ID.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.command is not None:
            result['Command'] = self.command

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

