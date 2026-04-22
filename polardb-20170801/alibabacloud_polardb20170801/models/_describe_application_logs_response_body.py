# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationLogsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        items: main_models.DescribeApplicationLogsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.application_id = application_id
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeApplicationLogsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeApplicationLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        log_records: List[main_models.DescribeApplicationLogsResponseBodyItemsLogRecords] = None,
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
                temp_model = main_models.DescribeApplicationLogsResponseBodyItemsLogRecords()
                self.log_records.append(temp_model.from_map(k1))

        return self

class DescribeApplicationLogsResponseBodyItemsLogRecords(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        container_name: str = None,
        content: str = None,
        date: str = None,
        file_line: str = None,
        file_name: str = None,
        full_file_path: str = None,
        hostname: str = None,
        log_level_id: int = None,
        log_level_name: str = None,
        method: str = None,
        name: str = None,
        runtime: str = None,
        runtime_version: str = None,
        time: str = None,
    ):
        self.component_name = component_name
        self.container_name = container_name
        self.content = content
        self.date = date
        self.file_line = file_line
        self.file_name = file_name
        self.full_file_path = full_file_path
        self.hostname = hostname
        self.log_level_id = log_level_id
        self.log_level_name = log_level_name
        self.method = method
        self.name = name
        self.runtime = runtime
        self.runtime_version = runtime_version
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.content is not None:
            result['Content'] = self.content

        if self.date is not None:
            result['Date'] = self.date

        if self.file_line is not None:
            result['FileLine'] = self.file_line

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.full_file_path is not None:
            result['FullFilePath'] = self.full_file_path

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.log_level_id is not None:
            result['LogLevelId'] = self.log_level_id

        if self.log_level_name is not None:
            result['LogLevelName'] = self.log_level_name

        if self.method is not None:
            result['Method'] = self.method

        if self.name is not None:
            result['Name'] = self.name

        if self.runtime is not None:
            result['Runtime'] = self.runtime

        if self.runtime_version is not None:
            result['RuntimeVersion'] = self.runtime_version

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('FileLine') is not None:
            self.file_line = m.get('FileLine')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FullFilePath') is not None:
            self.full_file_path = m.get('FullFilePath')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('LogLevelId') is not None:
            self.log_level_id = m.get('LogLevelId')

        if m.get('LogLevelName') is not None:
            self.log_level_name = m.get('LogLevelName')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')

        if m.get('RuntimeVersion') is not None:
            self.runtime_version = m.get('RuntimeVersion')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

