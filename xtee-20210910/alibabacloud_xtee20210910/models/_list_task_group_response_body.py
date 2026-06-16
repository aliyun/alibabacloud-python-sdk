# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class ListTaskGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        http_status_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.ListTaskGroupResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Status code.
        self.code = code
        # Current page number.
        self.current_page = current_page
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Page size.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Request result.
        self.result_object = result_object
        # Total number of returned items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.ListTaskGroupResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListTaskGroupResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator_user_id: int = None,
        group_status: str = None,
        sample_names: List[str] = None,
        sub_task_count: int = None,
        sub_task_list: List[main_models.ListTaskGroupResponseBodyResultObjectSubTaskList] = None,
        tab: str = None,
        task_group_id: int = None,
        task_group_name: str = None,
    ):
        # Creation Time.
        self.create_time = create_time
        # Creator.
        self.creator_user_id = creator_user_id
        # Audience group status.
        self.group_status = group_status
        # Task group name.
        self.sample_names = sample_names
        # Number of subtasks parsed and split from the task.
        self.sub_task_count = sub_task_count
        # Subtask.
        self.sub_task_list = sub_task_list
        # Scenario.
        self.tab = tab
        # Task group ID.
        self.task_group_id = task_group_id
        # Task group name.
        self.task_group_name = task_group_name

    def validate(self):
        if self.sub_task_list:
            for v1 in self.sub_task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_user_id is not None:
            result['CreatorUserId'] = self.creator_user_id

        if self.group_status is not None:
            result['GroupStatus'] = self.group_status

        if self.sample_names is not None:
            result['SampleNames'] = self.sample_names

        if self.sub_task_count is not None:
            result['SubTaskCount'] = self.sub_task_count

        result['SubTaskList'] = []
        if self.sub_task_list is not None:
            for k1 in self.sub_task_list:
                result['SubTaskList'].append(k1.to_map() if k1 else None)

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id

        if self.task_group_name is not None:
            result['TaskGroupName'] = self.task_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorUserId') is not None:
            self.creator_user_id = m.get('CreatorUserId')

        if m.get('GroupStatus') is not None:
            self.group_status = m.get('GroupStatus')

        if m.get('SampleNames') is not None:
            self.sample_names = m.get('SampleNames')

        if m.get('SubTaskCount') is not None:
            self.sub_task_count = m.get('SubTaskCount')

        self.sub_task_list = []
        if m.get('SubTaskList') is not None:
            for k1 in m.get('SubTaskList'):
                temp_model = main_models.ListTaskGroupResponseBodyResultObjectSubTaskList()
                self.sub_task_list.append(temp_model.from_map(k1))

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')

        if m.get('TaskGroupName') is not None:
            self.task_group_name = m.get('TaskGroupName')

        return self

class ListTaskGroupResponseBodyResultObjectSubTaskList(DaraModel):
    def __init__(
        self,
        finish_time: int = None,
        group_name: str = None,
        hide_view_result_button: bool = None,
        is_charge: bool = None,
        model_scene: str = None,
        sample_id: int = None,
        sample_name: str = None,
        service_code: str = None,
        service_name: str = None,
        sub_task_id: int = None,
        support_cancel: bool = None,
        support_download: bool = None,
        support_merge_select: bool = None,
        support_view: bool = None,
        tab: str = None,
        task_group_id: int = None,
        task_status: str = None,
    ):
        # Job end time.
        self.finish_time = finish_time
        # Group name.
        self.group_name = group_name
        # Indicates whether to hide.
        self.hide_view_result_button = hide_view_result_button
        # Indicates whether the subtask is charged.
        self.is_charge = is_charge
        # Model scenario.
        self.model_scene = model_scene
        # Sample ID.
        self.sample_id = sample_id
        # Sample name.
        self.sample_name = sample_name
        # Service code.
        self.service_code = service_code
        # Service name.
        self.service_name = service_name
        # Subtask ID.
        self.sub_task_id = sub_task_id
        # Indicates whether the job can be canceled. Valid values:  
        # - true: The job can be canceled.  
        # - false: The job cannot be canceled.
        self.support_cancel = support_cancel
        # Supports download.
        self.support_download = support_download
        # Indicates whether merge download is supported.
        self.support_merge_select = support_merge_select
        # Indicates whether viewing is supported.
        self.support_view = support_view
        # Scenario.
        self.tab = tab
        # Task group ID.
        self.task_group_id = task_group_id
        # The execution status of the import job:  
        # - DOING: running  
        # - FINISH: execution completed.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.hide_view_result_button is not None:
            result['HideViewResultButton'] = self.hide_view_result_button

        if self.is_charge is not None:
            result['IsCharge'] = self.is_charge

        if self.model_scene is not None:
            result['ModelScene'] = self.model_scene

        if self.sample_id is not None:
            result['SampleId'] = self.sample_id

        if self.sample_name is not None:
            result['SampleName'] = self.sample_name

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.sub_task_id is not None:
            result['SubTaskId'] = self.sub_task_id

        if self.support_cancel is not None:
            result['SupportCancel'] = self.support_cancel

        if self.support_download is not None:
            result['SupportDownload'] = self.support_download

        if self.support_merge_select is not None:
            result['SupportMergeSelect'] = self.support_merge_select

        if self.support_view is not None:
            result['SupportView'] = self.support_view

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HideViewResultButton') is not None:
            self.hide_view_result_button = m.get('HideViewResultButton')

        if m.get('IsCharge') is not None:
            self.is_charge = m.get('IsCharge')

        if m.get('ModelScene') is not None:
            self.model_scene = m.get('ModelScene')

        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')

        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SubTaskId') is not None:
            self.sub_task_id = m.get('SubTaskId')

        if m.get('SupportCancel') is not None:
            self.support_cancel = m.get('SupportCancel')

        if m.get('SupportDownload') is not None:
            self.support_download = m.get('SupportDownload')

        if m.get('SupportMergeSelect') is not None:
            self.support_merge_select = m.get('SupportMergeSelect')

        if m.get('SupportView') is not None:
            self.support_view = m.get('SupportView')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

