# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeRplInspectionTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeRplInspectionTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Data') is not None:
            temp_model = main_models.DescribeRplInspectionTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeRplInspectionTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        inspection_task_list: List[main_models.DescribeRplInspectionTaskResponseBodyDataInspectionTaskList] = None,
        slink_stage: str = None,
    ):
        self.inspection_task_list = inspection_task_list
        self.slink_stage = slink_stage

    def validate(self):
        if self.inspection_task_list:
            for v1 in self.inspection_task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InspectionTaskList'] = []
        if self.inspection_task_list is not None:
            for k1 in self.inspection_task_list:
                result['InspectionTaskList'].append(k1.to_map() if k1 else None)

        if self.slink_stage is not None:
            result['SlinkStage'] = self.slink_stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_task_list = []
        if m.get('InspectionTaskList') is not None:
            for k1 in m.get('InspectionTaskList'):
                temp_model = main_models.DescribeRplInspectionTaskResponseBodyDataInspectionTaskList()
                self.inspection_task_list.append(temp_model.from_map(k1))

        if m.get('SlinkStage') is not None:
            self.slink_stage = m.get('SlinkStage')

        return self

class DescribeRplInspectionTaskResponseBodyDataInspectionTaskList(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        id: int = None,
        slink_task_id: str = None,
        stage: str = None,
        status: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.id = id
        # slinktaskid。
        self.slink_task_id = slink_task_id
        self.stage = stage
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.slink_task_id is not None:
            result['SlinkTaskId'] = self.slink_task_id

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SlinkTaskId') is not None:
            self.slink_task_id = m.get('SlinkTaskId')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

