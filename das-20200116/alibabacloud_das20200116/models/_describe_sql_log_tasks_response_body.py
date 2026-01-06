# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlLogTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSqlLogTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeSqlLogTasksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSqlLogTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.DescribeSqlLogTasksResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The details of the data returned.
        self.list = list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The number of tasks.
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
                temp_model = main_models.DescribeSqlLogTasksResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeSqlLogTasksResponseBodyDataList(DaraModel):
    def __init__(
        self,
        analysis_task_finish_time: int = None,
        analysis_task_status: str = None,
        create_time: int = None,
        end: int = None,
        expire: bool = None,
        filters: List[main_models.DescribeSqlLogTasksResponseBodyDataListFilters] = None,
        inner_result: str = None,
        instance_id: str = None,
        log_count: int = None,
        name: str = None,
        progress: int = None,
        result: str = None,
        scan_file_size: int = None,
        start: int = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The time when the analysis task was complete. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.analysis_task_finish_time = analysis_task_finish_time
        # The state of the analysis task.
        # 
        # >  This parameter is a system parameter. You do not need to pay attention to the parameter.
        self.analysis_task_status = analysis_task_status
        # The time when the task was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The time when the task ended. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end = end
        # Indicates whether the task expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.expire = expire
        # The filter parameters.
        self.filters = filters
        self.inner_result = inner_result
        # The ID of the database instance.
        self.instance_id = instance_id
        # The number of log records.
        self.log_count = log_count
        # The task name.
        self.name = name
        # The task progress.
        self.progress = progress
        # The URL that is returned if the value of TaskType is **Export**.
        self.result = result
        # The number of files that are scanned.
        self.scan_file_size = scan_file_size
        # The time when the task started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start = start
        # The task state. Valid values:
        # 
        # *   **INIT**: The task is to be scheduled.
        # *   **RUNNING**: The task is running.
        # *   **FAILED**: The task failed.
        # *   **CANCELED**: The task is canceled.
        # *   **COMPLETED**: The task is complete.
        # 
        # >  If a task is in the **COMPLETED** state, you can view the results of the task.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The task type. Valid values:
        # 
        # *   **Export**
        # *   **Query**
        self.task_type = task_type

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_task_finish_time is not None:
            result['AnalysisTaskFinishTime'] = self.analysis_task_finish_time

        if self.analysis_task_status is not None:
            result['AnalysisTaskStatus'] = self.analysis_task_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end is not None:
            result['End'] = self.end

        if self.expire is not None:
            result['Expire'] = self.expire

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.inner_result is not None:
            result['InnerResult'] = self.inner_result

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_count is not None:
            result['LogCount'] = self.log_count

        if self.name is not None:
            result['Name'] = self.name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.result is not None:
            result['Result'] = self.result

        if self.scan_file_size is not None:
            result['ScanFileSize'] = self.scan_file_size

        if self.start is not None:
            result['Start'] = self.start

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisTaskFinishTime') is not None:
            self.analysis_task_finish_time = m.get('AnalysisTaskFinishTime')

        if m.get('AnalysisTaskStatus') is not None:
            self.analysis_task_status = m.get('AnalysisTaskStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeSqlLogTasksResponseBodyDataListFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InnerResult') is not None:
            self.inner_result = m.get('InnerResult')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ScanFileSize') is not None:
            self.scan_file_size = m.get('ScanFileSize')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class DescribeSqlLogTasksResponseBodyDataListFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter parameter.
        # 
        # >  For more information about the filter parameters, see the **Valid values of Key** section of this topic.
        self.key = key
        # The value of the filter parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

