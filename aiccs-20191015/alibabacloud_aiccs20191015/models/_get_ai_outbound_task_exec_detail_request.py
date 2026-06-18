# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiOutboundTaskExecDetailRequest(DaraModel):
    def __init__(
        self,
        batch_version: int = None,
        case_id: int = None,
        case_status: int = None,
        create_time_end: int = None,
        create_time_start: int = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
        phone_num: str = None,
        task_id: int = None,
    ):
        # The job batch version.
        self.batch_version = batch_version
        # Activity ID associated with this outbound call.
        self.case_id = case_id
        # Job execution status for a single phone number. Valid values:
        # 
        # - **1**: Pending call.
        # - **2**: Calling.
        # - **3**: Completed.
        # - **4**: Stopped.
        # - **5**: Pending retry.
        self.case_status = case_status
        # End time of phone number import. Format: UNIX timestamp in milliseconds.
        self.create_time_end = create_time_end
        # Start time of phone number import. Format: UNIX timestamp in milliseconds.
        self.create_time_start = create_time_start
        # Page size. The value must be greater than **0**. Default Value: **20**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID.
        # 
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries per page. The value must be greater than **0**. Default value: **20**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The outbound phone number.
        self.phone_num = phone_num
        # The job ID.
        # 
        # You can invoke the [CreateAiOutboundTask](https://help.aliyun.com/document_detail/312260.html) API and check the **Data** field in the response, or invoke the [GetAiOutboundTaskList](https://help.aliyun.com/document_detail/2718026.html) API and check the **TaskId** field in the response.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_version is not None:
            result['BatchVersion'] = self.batch_version

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.case_status is not None:
            result['CaseStatus'] = self.case_status

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchVersion') is not None:
            self.batch_version = m.get('BatchVersion')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

