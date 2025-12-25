# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTaskFlowInstanceResponseBody(DaraModel):
    def __init__(
        self,
        daginstance_list: main_models.ListTaskFlowInstanceResponseBodyDAGInstanceList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The information about the execution records returned.
        self.daginstance_list = daginstance_list
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success
        # The total number of execution records returned.
        self.total_count = total_count

    def validate(self):
        if self.daginstance_list:
            self.daginstance_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daginstance_list is not None:
            result['DAGInstanceList'] = self.daginstance_list.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DAGInstanceList') is not None:
            temp_model = main_models.ListTaskFlowInstanceResponseBodyDAGInstanceList()
            self.daginstance_list = temp_model.from_map(m.get('DAGInstanceList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTaskFlowInstanceResponseBodyDAGInstanceList(DaraModel):
    def __init__(
        self,
        daginstance: List[main_models.ListTaskFlowInstanceResponseBodyDAGInstanceListDAGInstance] = None,
    ):
        self.daginstance = daginstance

    def validate(self):
        if self.daginstance:
            for v1 in self.daginstance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DAGInstance'] = []
        if self.daginstance is not None:
            for k1 in self.daginstance:
                result['DAGInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daginstance = []
        if m.get('DAGInstance') is not None:
            for k1 in m.get('DAGInstance'):
                temp_model = main_models.ListTaskFlowInstanceResponseBodyDAGInstanceListDAGInstance()
                self.daginstance.append(temp_model.from_map(k1))

        return self

class ListTaskFlowInstanceResponseBodyDAGInstanceListDAGInstance(DaraModel):
    def __init__(
        self,
        business_time: str = None,
        dag_id: str = None,
        dag_name: str = None,
        dag_version: str = None,
        end_time: str = None,
        history_dag_id: int = None,
        id: int = None,
        message: str = None,
        owner_name: str = None,
        status: int = None,
        trigger_type: int = None,
        start_time: str = None,
    ):
        # The business time of the task flow. The time is displayed in the yyyy-MM-DD HH:mm:ss format.
        self.business_time = business_time
        # The ID of the task flow.
        self.dag_id = dag_id
        # The name of the task flow.
        self.dag_name = dag_name
        # The version of the task flow.
        self.dag_version = dag_version
        # The time when the execution of the task flow was complete. The time is displayed in the yyyy-MM-DD HH:mm:ss format.
        self.end_time = end_time
        # The ID of the previously published version of the task flow.
        self.history_dag_id = history_dag_id
        # The ID of the execution record.
        self.id = id
        # The description of the task.
        self.message = message
        # The name of the task flow owner.
        self.owner_name = owner_name
        # The status of the task flow. Valid values:
        # 
        # *   **0**: The task flow is waiting to be scheduled.
        # *   **1**: The task flow is being executed.
        # *   **2**: The task flow is paused.
        # *   **3**: The task flow failed.
        # *   **4**: The task flow is executed.
        # *   **5**: The task flow is complete.
        self.status = status
        # The mode in which the task flow is triggered. Valid values:
        # 
        # *   **0**: The task flow is automatically triggered based on periodic scheduling.
        # *   **1**: The task flow is manually triggered.
        self.trigger_type = trigger_type
        # The time when the execution of the task flow was start. The time is displayed in the yyyy-MM-DD HH:mm:ss format.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_time is not None:
            result['BusinessTime'] = self.business_time

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.dag_version is not None:
            result['DagVersion'] = self.dag_version

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.history_dag_id is not None:
            result['HistoryDagId'] = self.history_dag_id

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.status is not None:
            result['Status'] = self.status

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('DagVersion') is not None:
            self.dag_version = m.get('DagVersion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HistoryDagId') is not None:
            self.history_dag_id = m.get('HistoryDagId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

