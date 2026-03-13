# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarRecordsRequest(DaraModel):
    def __init__(
        self,
        completed_begin_time: int = None,
        completed_end_time: int = None,
        end_millis: int = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        playbook_uuid: str = None,
        query_value: str = None,
        request_uuid: str = None,
        start_millis: int = None,
        task_status: str = None,
        taskflow_md_5: str = None,
        trigger_type: str = None,
        trigger_user: str = None,
    ):
        self.completed_begin_time = completed_begin_time
        self.completed_end_time = completed_end_time
        # The end time of the task execution, in 13-digit timestamp format.
        self.end_millis = end_millis
        # Set the language type for requests and received messages. The default is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Set which page to start displaying the query results from. The default value is 1, indicating the first page.
        self.page_number = page_number
        # Specify the maximum number of data entries per page when performing a paginated query. The default number of entries per page is 20. If the PageSize parameter is empty, it will return 10 entries by default.
        # > It is recommended not to leave the PageSize value empty.
        self.page_size = page_size
        # The UUID of the playbook.
        # > You can obtain this parameter by calling the [DescribePlaybooks](~~DescribePlaybooks~~) interface.
        self.playbook_uuid = playbook_uuid
        self.query_value = query_value
        # UUID of the playbook task execution.
        # > You can obtain this parameter by calling the [DescribeSoarRecords](https://help.aliyun.com/document_detail/2627455.html) interface.
        self.request_uuid = request_uuid
        # The start time of the task execution, in 13-digit timestamp format.
        self.start_millis = start_millis
        # The status of the task execution. Values:
        # 
        # - **success**: Successful task.
        # - **failed**: Failed task.
        # - **inprogress**: Task in progress
        self.task_status = task_status
        # The MD5 value of the playbook configuration.
        self.taskflow_md_5 = taskflow_md_5
        self.trigger_type = trigger_type
        # The Alibaba Cloud account ID that executed the playbook task.
        self.trigger_user = trigger_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_begin_time is not None:
            result['CompletedBeginTime'] = self.completed_begin_time

        if self.completed_end_time is not None:
            result['CompletedEndTime'] = self.completed_end_time

        if self.end_millis is not None:
            result['EndMillis'] = self.end_millis

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.query_value is not None:
            result['QueryValue'] = self.query_value

        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid

        if self.start_millis is not None:
            result['StartMillis'] = self.start_millis

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedBeginTime') is not None:
            self.completed_begin_time = m.get('CompletedBeginTime')

        if m.get('CompletedEndTime') is not None:
            self.completed_end_time = m.get('CompletedEndTime')

        if m.get('EndMillis') is not None:
            self.end_millis = m.get('EndMillis')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('QueryValue') is not None:
            self.query_value = m.get('QueryValue')

        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')

        if m.get('StartMillis') is not None:
            self.start_millis = m.get('StartMillis')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')

        return self

