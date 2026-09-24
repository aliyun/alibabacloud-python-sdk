# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryAiCallTaskPageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryAiCallTaskPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The task details.
        self.data = data
        # The error message. This parameter is not returned if the call is successful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: successful.
        # - **false**: failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAiCallTaskPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAiCallTaskPageResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryAiCallTaskPageResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The task data.
        self.list = list
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryAiCallTaskPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryAiCallTaskPageResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        application_code: str = None,
        application_name: str = None,
        call_expire_date: str = None,
        call_expire_minutes: int = None,
        call_expire_type: int = None,
        calling_count: int = None,
        complete_rate: str = None,
        concurrent_count: int = None,
        create_time: int = None,
        day_call_count: int = None,
        day_connect_rate: str = None,
        day_import_count: int = None,
        failed_count: int = None,
        history_connect_rate: str = None,
        real_start_time: int = None,
        start_failed_reason: str = None,
        start_time: int = None,
        status: int = None,
        succeed_count: int = None,
        task_id: str = None,
        task_name: str = None,
        total_call_count: int = None,
        total_count: int = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The agent name.
        self.agent_name = agent_name
        self.application_code = application_code
        self.application_name = application_name
        self.call_expire_date = call_expire_date
        self.call_expire_minutes = call_expire_minutes
        self.call_expire_type = call_expire_type
        # The number of ongoing calls.
        self.calling_count = calling_count
        # The task completion rate.
        self.complete_rate = complete_rate
        # The task concurrency.
        self.concurrent_count = concurrent_count
        # The creation time. This value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The number of calls made on the current day.
        self.day_call_count = day_call_count
        # The daily connection rate. Daily connection rate = number of connections on the current day ÷ number of calls on the current day (DayCallCount).
        self.day_connect_rate = day_connect_rate
        # The amount of data imported on the current day.
        self.day_import_count = day_import_count
        # The total number of failed task executions.
        self.failed_count = failed_count
        # The historical connection rate. Historical connection rate = historical number of connections ÷ total number of calls (TotalCallCount).
        self.history_connect_rate = history_connect_rate
        # The actual start time of the task. This value is a UNIX timestamp in milliseconds.
        self.real_start_time = real_start_time
        # The reason for startup failure.
        self.start_failed_reason = start_failed_reason
        # The scheduled start time of the task. This value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The task status.
        self.status = status
        # The total number of successful task executions.
        self.succeed_count = succeed_count
        # The task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The total number of calls made by the task.
        self.total_call_count = total_call_count
        # The total number of task items.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.call_expire_date is not None:
            result['CallExpireDate'] = self.call_expire_date

        if self.call_expire_minutes is not None:
            result['CallExpireMinutes'] = self.call_expire_minutes

        if self.call_expire_type is not None:
            result['CallExpireType'] = self.call_expire_type

        if self.calling_count is not None:
            result['CallingCount'] = self.calling_count

        if self.complete_rate is not None:
            result['CompleteRate'] = self.complete_rate

        if self.concurrent_count is not None:
            result['ConcurrentCount'] = self.concurrent_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.day_call_count is not None:
            result['DayCallCount'] = self.day_call_count

        if self.day_connect_rate is not None:
            result['DayConnectRate'] = self.day_connect_rate

        if self.day_import_count is not None:
            result['DayImportCount'] = self.day_import_count

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.history_connect_rate is not None:
            result['HistoryConnectRate'] = self.history_connect_rate

        if self.real_start_time is not None:
            result['RealStartTime'] = self.real_start_time

        if self.start_failed_reason is not None:
            result['StartFailedReason'] = self.start_failed_reason

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.succeed_count is not None:
            result['SucceedCount'] = self.succeed_count

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.total_call_count is not None:
            result['TotalCallCount'] = self.total_call_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CallExpireDate') is not None:
            self.call_expire_date = m.get('CallExpireDate')

        if m.get('CallExpireMinutes') is not None:
            self.call_expire_minutes = m.get('CallExpireMinutes')

        if m.get('CallExpireType') is not None:
            self.call_expire_type = m.get('CallExpireType')

        if m.get('CallingCount') is not None:
            self.calling_count = m.get('CallingCount')

        if m.get('CompleteRate') is not None:
            self.complete_rate = m.get('CompleteRate')

        if m.get('ConcurrentCount') is not None:
            self.concurrent_count = m.get('ConcurrentCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DayCallCount') is not None:
            self.day_call_count = m.get('DayCallCount')

        if m.get('DayConnectRate') is not None:
            self.day_connect_rate = m.get('DayConnectRate')

        if m.get('DayImportCount') is not None:
            self.day_import_count = m.get('DayImportCount')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('HistoryConnectRate') is not None:
            self.history_connect_rate = m.get('HistoryConnectRate')

        if m.get('RealStartTime') is not None:
            self.real_start_time = m.get('RealStartTime')

        if m.get('StartFailedReason') is not None:
            self.start_failed_reason = m.get('StartFailedReason')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SucceedCount') is not None:
            self.succeed_count = m.get('SucceedCount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TotalCallCount') is not None:
            self.total_call_count = m.get('TotalCallCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

