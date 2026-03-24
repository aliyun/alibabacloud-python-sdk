# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeUserUsageDetailDataExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        usage_data_per_page: main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The usage details returned per page.
        self.usage_data_per_page = usage_data_per_page

    def validate(self):
        if self.usage_data_per_page:
            self.usage_data_per_page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.usage_data_per_page is not None:
            result['UsageDataPerPage'] = self.usage_data_per_page.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UsageDataPerPage') is not None:
            temp_model = main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage()
            self.usage_data_per_page = temp_model.from_map(m.get('UsageDataPerPage'))

        return self

class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data = data
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData(DaraModel):
    def __init__(
        self,
        data_item: List[main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem] = None,
    ):
        self.data_item = data_item

    def validate(self):
        if self.data_item:
            for v1 in self.data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataItem'] = []
        if self.data_item is not None:
            for k1 in self.data_item:
                result['DataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k1 in m.get('DataItem'):
                temp_model = main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem()
                self.data_item.append(temp_model.from_map(k1))

        return self

class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        status: str = None,
        task_config: main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig = None,
        task_id: str = None,
        task_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.download_url = download_url
        self.status = status
        self.task_config = task_config
        self.task_id = task_id
        self.task_name = task_name
        self.update_time = update_time

    def validate(self):
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.status is not None:
            result['Status'] = self.status

        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskConfig') is not None:
            temp_model = main_models.DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig()
            self.task_config = temp_model.from_map(m.get('TaskConfig'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

