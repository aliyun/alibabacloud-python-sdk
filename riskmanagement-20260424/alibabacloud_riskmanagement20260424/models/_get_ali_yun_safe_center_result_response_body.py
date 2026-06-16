# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetAliYunSafeCenterResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAliYunSafeCenterResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            temp_model = main_models.GetAliYunSafeCenterResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAliYunSafeCenterResultResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_status: bool = None,
        ecs_instance_status: bool = None,
        instance_ids: List[int] = None,
        request_id: str = None,
        swas_instance_status: bool = None,
        task_id: int = None,
        task_status: bool = None,
    ):
        self.agent_status = agent_status
        self.ecs_instance_status = ecs_instance_status
        self.instance_ids = instance_ids
        self.request_id = request_id
        self.swas_instance_status = swas_instance_status
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.ecs_instance_status is not None:
            result['EcsInstanceStatus'] = self.ecs_instance_status

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.swas_instance_status is not None:
            result['SwasInstanceStatus'] = self.swas_instance_status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('EcsInstanceStatus') is not None:
            self.ecs_instance_status = m.get('EcsInstanceStatus')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SwasInstanceStatus') is not None:
            self.swas_instance_status = m.get('SwasInstanceStatus')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

