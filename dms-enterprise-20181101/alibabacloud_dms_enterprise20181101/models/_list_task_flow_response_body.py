# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTaskFlowResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task_flow_list: main_models.ListTaskFlowResponseBodyTaskFlowList = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The information about the task flows returned.
        self.task_flow_list = task_flow_list

    def validate(self):
        if self.task_flow_list:
            self.task_flow_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_flow_list is not None:
            result['TaskFlowList'] = self.task_flow_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskFlowList') is not None:
            temp_model = main_models.ListTaskFlowResponseBodyTaskFlowList()
            self.task_flow_list = temp_model.from_map(m.get('TaskFlowList'))

        return self

class ListTaskFlowResponseBodyTaskFlowList(DaraModel):
    def __init__(
        self,
        task_flow: List[main_models.ListTaskFlowResponseBodyTaskFlowListTaskFlow] = None,
    ):
        self.task_flow = task_flow

    def validate(self):
        if self.task_flow:
            for v1 in self.task_flow:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskFlow'] = []
        if self.task_flow is not None:
            for k1 in self.task_flow:
                result['TaskFlow'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_flow = []
        if m.get('TaskFlow') is not None:
            for k1 in m.get('TaskFlow'):
                temp_model = main_models.ListTaskFlowResponseBodyTaskFlowListTaskFlow()
                self.task_flow.append(temp_model.from_map(k1))

        return self

class ListTaskFlowResponseBodyTaskFlowListTaskFlow(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        creator_nick_name: str = None,
        dag_owner_nick_name: str = None,
        deploy_id: int = None,
        id: int = None,
        latest_instance_status: int = None,
        latest_instance_time: str = None,
        status: int = None,
    ):
        # The ID of the user who creates the task flow.
        self.creator_id = creator_id
        # The name of the user who creates the task flow.
        self.creator_nick_name = creator_nick_name
        # The name of the task flow owner.
        self.dag_owner_nick_name = dag_owner_nick_name
        # The ID of the latest deployment record.
        self.deploy_id = deploy_id
        # The ID of the task flow.
        self.id = id
        # The status of the latest execution. Valid values:
        # 
        # *   **0**: invalid.
        # *   **1**: scheduling disabled.
        # *   **2**: waiting to be scheduled.
        self.latest_instance_status = latest_instance_status
        # The time when the latest execution record was generated.
        self.latest_instance_time = latest_instance_time
        # The status of the task flow. Valid values:
        # 
        # *   **0**: The task flow is invalid.
        # *   **1**: Scheduling is disabled for the task flow.
        # *   **2**: The task flow is waiting to be scheduled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name

        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name

        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id

        if self.id is not None:
            result['Id'] = self.id

        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status

        if self.latest_instance_time is not None:
            result['LatestInstanceTime'] = self.latest_instance_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')

        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')

        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')

        if m.get('LatestInstanceTime') is not None:
            self.latest_instance_time = m.get('LatestInstanceTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

