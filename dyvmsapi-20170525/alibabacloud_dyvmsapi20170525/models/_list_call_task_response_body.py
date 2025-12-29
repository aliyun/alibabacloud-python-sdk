# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class ListCallTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListCallTaskResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response code.
        self.code = code
        # The task information.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of tasks.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCallTaskResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListCallTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        complete_time: str = None,
        completed_count: int = None,
        completed_rate: int = None,
        data: str = None,
        data_type: str = None,
        fire_time: str = None,
        id: int = None,
        resource: str = None,
        status: str = None,
        stop_time: str = None,
        task_name: str = None,
        template_code: str = None,
        template_name: str = None,
        total_count: int = None,
    ):
        # The type of the task template. Valid values:
        # 
        # *   **VMS_VOICE_TTS**: the TTS notification template.
        # *   **VMS_VOICE_CODE**: the voice notification template.
        # *   **VMS_TTS**: the voice verification code template.
        self.biz_type = biz_type
        # The time when the task was completed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.complete_time = complete_time
        # The number of tasks that were complete.
        self.completed_count = completed_count
        # The task progress.
        self.completed_rate = completed_rate
        # This parameter is unavailable.
        self.data = data
        # The type of the called number.
        self.data_type = data_type
        # The time when the scheduled task was started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.fire_time = fire_time
        # The task ID.
        self.id = id
        # The calling number.
        self.resource = resource
        # The task state. Valid values:
        # 
        # *   **INIT**: The task was in the initial state.
        # *   **RELEASE**: The task was being parsed.
        # *   **RUNNING**: The task was running.
        # *   **STOP**: The task was manually suspended.
        # *   **SYSTEM_STOP**: The task was suspended by the system.
        # *   **CANCEL**: The task was manually canceled.
        # *   **SYSTEM_CANCEL**: The task was canceled by the system.
        # *   **DONE**: The task was complete.
        self.status = status
        # This parameter is unavailable.
        self.stop_time = stop_time
        # The task name.
        self.task_name = task_name
        # The ID of the voice template.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name
        # The total number of called numbers.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.completed_count is not None:
            result['CompletedCount'] = self.completed_count

        if self.completed_rate is not None:
            result['CompletedRate'] = self.completed_rate

        if self.data is not None:
            result['Data'] = self.data

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.fire_time is not None:
            result['FireTime'] = self.fire_time

        if self.id is not None:
            result['Id'] = self.id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CompletedCount') is not None:
            self.completed_count = m.get('CompletedCount')

        if m.get('CompletedRate') is not None:
            self.completed_rate = m.get('CompletedRate')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

