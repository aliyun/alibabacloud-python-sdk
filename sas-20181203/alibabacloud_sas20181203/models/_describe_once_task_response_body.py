# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeOnceTaskResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeOnceTaskResponseBodyPageInfo = None,
        request_id: str = None,
        task_manage_response_list: List[main_models.DescribeOnceTaskResponseBodyTaskManageResponseList] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use the request ID to troubleshoot issues.
        self.request_id = request_id
        # The list of client task query results.
        self.task_manage_response_list = task_manage_response_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.task_manage_response_list:
            for v1 in self.task_manage_response_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskManageResponseList'] = []
        if self.task_manage_response_list is not None:
            for k1 in self.task_manage_response_list:
                result['TaskManageResponseList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeOnceTaskResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_manage_response_list = []
        if m.get('TaskManageResponseList') is not None:
            for k1 in m.get('TaskManageResponseList'):
                temp_model = main_models.DescribeOnceTaskResponseBodyTaskManageResponseList()
                self.task_manage_response_list.append(temp_model.from_map(k1))

        return self

class DescribeOnceTaskResponseBodyTaskManageResponseList(DaraModel):
    def __init__(
        self,
        detail_data: str = None,
        fail_count: int = None,
        progress: str = None,
        result_info: str = None,
        success_count: int = None,
        task_end_time: int = None,
        task_id: str = None,
        task_name: str = None,
        task_start_time: int = None,
        task_status: int = None,
        task_status_text: str = None,
        task_type: str = None,
    ):
        # The task execution details. This parameter is in JSON format.
        # 
        # - **causeCode**: the return code of the troubleshooting cause.
        # - **causeMsg**: the return message of the troubleshooting cause.
        # - **resCode**: the troubleshooting return code.
        # - **resMsg**: the troubleshooting return message.
        # - **problemType**: the problem type.
        # - **dispatchType**: the task dispatch method.
        # - **uuid**: the server UUID.
        # - **instanceId**: the ID of the server instance.
        # - **internetIp**: the public IP address of the server.
        # - **intranetIp**: the private IP address of the server.
        # - **instanceName**: the name of the server instance.
        # - **url**: the download URL of the troubleshooting log.
        self.detail_data = detail_data
        # The number of tasks that failed to be executed.
        self.fail_count = fail_count
        # The task progress, in percentage.
        self.progress = progress
        # The task execution result.
        self.result_info = result_info
        # The number of tasks that are executed successfully.
        self.success_count = success_count
        # The timestamp when the task actually ends. Unit: milliseconds.
        self.task_end_time = task_end_time
        # The task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The timestamp when the task actually starts. Unit: milliseconds.
        self.task_start_time = task_start_time
        # The task status. Valid values:
        # - **1**: Started.
        # - **2**: Completed.
        # - **3**: Failed.
        # - **4**: Timed out.
        self.task_status = task_status
        # The text representation of the task status. Valid values:
        # - **INIT**: Pending.
        # - **START**: Started.
        # - **DISPATCH**: Self-check command dispatched.
        # - **SUCCESS**: Self-check completed.
        # - **FAIL**: Execution failed.
        # - **TIMEOUT**: Timed out.
        self.task_status_text = task_status_text
        # The task type. Valid values:
        # - **CLIENT_PROBLEM_CHECK**: client task
        # - **CLIENT_DEV_OPS**: cloud O&M task
        # - **ASSET_SECURITY_CHECK**: asset information collection task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_data is not None:
            result['DetailData'] = self.detail_data

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.result_info is not None:
            result['ResultInfo'] = self.result_info

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_text is not None:
            result['TaskStatusText'] = self.task_status_text

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailData') is not None:
            self.detail_data = m.get('DetailData')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ResultInfo') is not None:
            self.result_info = m.get('ResultInfo')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusText') is not None:
            self.task_status_text = m.get('TaskStatusText')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class DescribeOnceTaskResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of client tasks displayed on the current page in a paged query.
        self.count = count
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # The number of client tasks per page in a paged query. Default value: **20**.
        self.page_size = page_size
        # The total number of client tasks returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

