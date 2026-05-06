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
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        tab: str = None,
        task_group_id: int = None,
        task_group_name: str = None,
    ):
        self.create_time = create_time
        self.creator_user_id = creator_user_id
        self.group_status = group_status
        self.sample_names = sample_names
        self.sub_task_count = sub_task_count
        self.tab = tab
        self.task_group_id = task_group_id
        self.task_group_name = task_group_name

    def validate(self):
        pass

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

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')

        if m.get('TaskGroupName') is not None:
            self.task_group_name = m.get('TaskGroupName')

        return self

