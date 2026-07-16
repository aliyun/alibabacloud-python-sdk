# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class CreateTaskGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.CreateTaskGroupResponseBodyResultObject = None,
    ):
        # The response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.CreateTaskGroupResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class CreateTaskGroupResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator_user_id: int = None,
        group_status: str = None,
        sample_names: List[str] = None,
        sub_task_count: int = None,
        sub_task_list: List[main_models.CreateTaskGroupResponseBodyResultObjectSubTaskList] = None,
        tab: str = None,
        task_group_id: int = None,
        task_group_name: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The creator user ID.
        self.creator_user_id = creator_user_id
        # The group status.
        self.group_status = group_status
        # The task group name.
        self.sample_names = sample_names
        # The number of subtasks generated from task parsing and splitting.
        self.sub_task_count = sub_task_count
        # The subtask list.
        self.sub_task_list = sub_task_list
        # The scenario.
        self.tab = tab
        # The task group ID.
        # 
        # > This parameter is in invitational preview. When this parameter is used, other query conditions become invalid.
        self.task_group_id = task_group_id
        # The task group name.
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
                temp_model = main_models.CreateTaskGroupResponseBodyResultObjectSubTaskList()
                self.sub_task_list.append(temp_model.from_map(k1))

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')

        if m.get('TaskGroupName') is not None:
            self.task_group_name = m.get('TaskGroupName')

        return self

class CreateTaskGroupResponseBodyResultObjectSubTaskList(DaraModel):
    def __init__(
        self,
        checker: str = None,
        file_name: str = None,
        file_rows: str = None,
        finish_time: str = None,
        group_name: str = None,
        is_charge: str = None,
        model_scene: str = None,
        sample_id: str = None,
        sample_name: str = None,
        service_code: str = None,
        service_name: str = None,
        sub_task_id: int = None,
        tab: str = None,
        task_group_id: str = None,
        task_name: str = None,
        task_status: str = None,
    ):
        # The reviewer.
        self.checker = checker
        # The file name.
        self.file_name = file_name
        # The number of rows in the file.
        self.file_rows = file_rows
        # The task end time.
        self.finish_time = finish_time
        # The user group name.
        self.group_name = group_name
        # Indicates whether the task is billed.
        self.is_charge = is_charge
        # The model scenario.
        self.model_scene = model_scene
        # The sample IDs.
        self.sample_id = sample_id
        # The sample name.
        self.sample_name = sample_name
        # The service code.
        self.service_code = service_code
        # The service name.
        self.service_name = service_name
        # The subtask ID.
        self.sub_task_id = sub_task_id
        # The scenario.
        self.tab = tab
        # The task group ID.
        self.task_group_id = task_group_id
        # The task name.
        self.task_name = task_name
        # The execution status of the import task. Valid values:
        # - DOING: Running.
        # - FINISH: Completed.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checker is not None:
            result['Checker'] = self.checker

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_rows is not None:
            result['FileRows'] = self.file_rows

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.group_name is not None:
            result['GroupName'] = self.group_name

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

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checker') is not None:
            self.checker = m.get('Checker')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileRows') is not None:
            self.file_rows = m.get('FileRows')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

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

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

