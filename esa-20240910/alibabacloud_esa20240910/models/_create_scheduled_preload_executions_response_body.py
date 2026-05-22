# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateScheduledPreloadExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        failed_executions: List[main_models.CreateScheduledPreloadExecutionsResponseBodyFailedExecutions] = None,
        failed_messages: List[str] = None,
        request_id: str = None,
        success_count: int = None,
        success_executions: List[main_models.CreateScheduledPreloadExecutionsResponseBodySuccessExecutions] = None,
        total_count: int = None,
    ):
        # The information about prefetch plans that failed to be created.
        self.failed_executions = failed_executions
        # The information about plan failures.
        self.failed_messages = failed_messages
        # The request ID.
        self.request_id = request_id
        # The number of prefetch plans that are created.
        self.success_count = success_count
        # The information about created prefetch plans.
        self.success_executions = success_executions
        # The total number of new plans requested.
        self.total_count = total_count

    def validate(self):
        if self.failed_executions:
            for v1 in self.failed_executions:
                 if v1:
                    v1.validate()
        if self.success_executions:
            for v1 in self.success_executions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedExecutions'] = []
        if self.failed_executions is not None:
            for k1 in self.failed_executions:
                result['FailedExecutions'].append(k1.to_map() if k1 else None)

        if self.failed_messages is not None:
            result['FailedMessages'] = self.failed_messages

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        result['SuccessExecutions'] = []
        if self.success_executions is not None:
            for k1 in self.success_executions:
                result['SuccessExecutions'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_executions = []
        if m.get('FailedExecutions') is not None:
            for k1 in m.get('FailedExecutions'):
                temp_model = main_models.CreateScheduledPreloadExecutionsResponseBodyFailedExecutions()
                self.failed_executions.append(temp_model.from_map(k1))

        if m.get('FailedMessages') is not None:
            self.failed_messages = m.get('FailedMessages')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.success_executions = []
        if m.get('SuccessExecutions') is not None:
            for k1 in m.get('SuccessExecutions'):
                temp_model = main_models.CreateScheduledPreloadExecutionsResponseBodySuccessExecutions()
                self.success_executions.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class CreateScheduledPreloadExecutionsResponseBodySuccessExecutions(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The end time of the prefetch plans.
        self.end_time = end_time
        # The ID of the prefetch plan.
        self.id = id
        # The time interval between each batch execution. Unit: seconds.
        self.interval = interval
        # The ID of the prefetch task.
        self.job_id = job_id
        # The number of URLs prefetched in each batch.
        self.slice_len = slice_len
        # The start time of the prefetch plans.
        self.start_time = start_time
        # The status of the prefetch plan. Valid values:
        # 
        # *   **waiting**
        # *   **running**
        # *   **finished**
        # *   **failed**
        # *   **stopped**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreateScheduledPreloadExecutionsResponseBodyFailedExecutions(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        job_id: str = None,
        slice_len: int = None,
        start_time: str = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The end time of the prefetch plans.
        self.end_time = end_time
        # The ID of the prefetch plan.
        self.id = id
        # The time interval between each batch execution. Unit: seconds.
        self.interval = interval
        # The ID of the prefetch task.
        self.job_id = job_id
        # The number of URLs prefetched in each batch.
        self.slice_len = slice_len
        # The start time of the prefetch plans.
        self.start_time = start_time
        # The status of the prefetch plan. Valid values:
        # 
        # *   **waiting**
        # *   **running**
        # *   **finished**
        # *   **failed**
        # *   **stopped**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

