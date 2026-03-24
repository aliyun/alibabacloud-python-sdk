# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribePreloadDetailByIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        url_details: List[main_models.DescribePreloadDetailByIdResponseBodyUrlDetails] = None,
    ):
        # The ID of the request. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # The number of queried tasks.
        self.total_count = total_count
        # The details of the task, including the task ID, start time, end time, domain name, success rate, status, returned error code, and completion details of all URL resources.
        self.url_details = url_details

    def validate(self):
        if self.url_details:
            for v1 in self.url_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UrlDetails'] = []
        if self.url_details is not None:
            for k1 in self.url_details:
                result['UrlDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.url_details = []
        if m.get('UrlDetails') is not None:
            for k1 in m.get('UrlDetails'):
                temp_model = main_models.DescribePreloadDetailByIdResponseBodyUrlDetails()
                self.url_details.append(temp_model.from_map(k1))

        return self

class DescribePreloadDetailByIdResponseBodyUrlDetails(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        domain: str = None,
        end_time: str = None,
        process: str = None,
        ret_code: str = None,
        status: str = None,
        task_id: str = None,
        urls: List[main_models.DescribePreloadDetailByIdResponseBodyUrlDetailsUrls] = None,
    ):
        # The time when the task was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The domain name for prefetching resources.
        self.domain = domain
        # The time when the task ended. The time is displayed in UTC.
        self.end_time = end_time
        # The progress of the prefetch task, which indicates the number of points of presence (POPs) on which the prefetch task is completed.
        self.process = process
        # The turned error code. A value of `0` indicates that the task succeeded.
        self.ret_code = ret_code
        # The status of the task. Valid values:
        # 
        # *   **Complete**
        # *   **Refreshing**
        # *   **Failed**
        self.status = status
        # The ID of the task that you want to query.
        # 
        # You can call the PushObjectCache operation to query task IDs. Then, you can use the task IDs to query task status.
        # 
        # You can query one task ID at a time.
        self.task_id = task_id
        # The completion details of all URL resources in the task.
        self.urls = urls

    def validate(self):
        if self.urls:
            for v1 in self.urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.process is not None:
            result['Process'] = self.process

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['Urls'] = []
        if self.urls is not None:
            for k1 in self.urls:
                result['Urls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.urls = []
        if m.get('Urls') is not None:
            for k1 in m.get('Urls'):
                temp_model = main_models.DescribePreloadDetailByIdResponseBodyUrlDetailsUrls()
                self.urls.append(temp_model.from_map(k1))

        return self

class DescribePreloadDetailByIdResponseBodyUrlDetailsUrls(DaraModel):
    def __init__(
        self,
        description: str = None,
        success: str = None,
        url: str = None,
    ):
        # The details of resource prefetch.
        # 
        # *   If the resource is prefetched on all POPs, "Successfully preloaded" is returned.
        # *   If the resource fails to be prefetched on some POPs, the failure details separated by vertical bars (|) are returned.
        self.description = description
        # The success percentage, which indicates the number of POPs on which the resource is prefetched.
        self.success = success
        # The URL of the prefetched resource.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.success is not None:
            result['Success'] = self.success

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

