# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListInstanceHistoryResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstanceHistoryResponseBodyInstances] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of instances.
        self.instances = instances
        # The request ID. Used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstanceHistoryResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstanceHistoryResponseBodyInstances(DaraModel):
    def __init__(
        self,
        begin_running_time: int = None,
        begin_wait_res_time: int = None,
        begin_wait_time_time: int = None,
        bizdate: int = None,
        create_time: int = None,
        cyc_time: int = None,
        dag_id: int = None,
        dag_type: str = None,
        error_message: str = None,
        finish_time: int = None,
        instance_history_id: int = None,
        instance_id: int = None,
        modify_time: int = None,
        node_id: int = None,
        node_name: str = None,
        status: str = None,
        task_type: str = None,
    ):
        # The time when the instance started running, in timestamp format.
        self.begin_running_time = begin_running_time
        # The time when the instance started waiting for resources.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.begin_wait_res_time = begin_wait_res_time
        # The time when the instance started waiting for scheduling.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.begin_wait_time_time = begin_wait_time_time
        # The business date on which the scheduled node was run. This value is typically one day before the run time of the node.
        # 
        # The value is a 13-digit number, such as `1590336000000`.
        self.bizdate = bizdate
        # The time when the instance was created.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.create_time = create_time
        # The scheduled run time of the node, in timestamp format.
        self.cyc_time = cyc_time
        # The ID of the workflow.
        self.dag_id = dag_id
        # The Data Quality Check (DQC) type. Valid values:
        # 
        # - 0: associated with DQC.
        # - 1: not associated with DQC.
        self.dag_type = dag_type
        # **[Deprecated]** The error message returned when the instance failed to run. This field is deprecated. You can call the GetInstanceLog operation to obtain the error information of the node.
        self.error_message = error_message
        # The time when the scheduled node finished running, in timestamp format.
        self.finish_time = finish_time
        # The history archive ID of the instance.
        self.instance_history_id = instance_history_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The time when the scheduled node was last modified.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.modify_time = modify_time
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The status of the node. Valid values:
        # 
        # - NOT_RUN: The node is not run.
        # - WAIT_TIME: The node is waiting for the scheduled time (DueTime or CycTime) to arrive.
        # - WAIT_RESOURCE: The node is waiting for resources.
        # - RUNNING: The node is running.
        # - CHECKING: The node is sent to Data Quality for data verification.
        # - CHECKING_CONDITION: The node is undergoing branch condition verification.
        # - FAILURE: The node failed to run.
        # - SUCCESS: The node ran successfully.
        self.status = status
        # The scheduling type of the node instance. Valid values:
        # 
        # - NORMAL(0): A normal scheduling node. The node is scheduled on a daily basis.
        # - MANUAL(1): A manual node. The node is not scheduled on a daily basis.
        # - PAUSE(2): A frozen node. The node is scheduled on a daily basis, but is set to failed when scheduling starts.
        # - SKIP(3): A dry-run node. The node is scheduled on a daily basis, but is set to successful when scheduling starts.
        # - SKIP_UNCHOOSE(4): A node that is not selected in a temporary workflow. This type of node exists only in temporary workflows and is set to successful when scheduling starts.
        # - SKIP_CYCLE(5): A weekly or monthly node that has not reached its run cycle. The node is scheduled on a daily basis, but is set to successful when scheduling starts.
        # - CONDITION_UNCHOOSE(6): A downstream node that is not selected by an upstream branch (IF) node. The node is directly set to dry-run.
        # - REALTIME_DEPRECATED(7): An expired periodic instance generated in real time. This type of node is directly set to successful.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_running_time is not None:
            result['BeginRunningTime'] = self.begin_running_time

        if self.begin_wait_res_time is not None:
            result['BeginWaitResTime'] = self.begin_wait_res_time

        if self.begin_wait_time_time is not None:
            result['BeginWaitTimeTime'] = self.begin_wait_time_time

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cyc_time is not None:
            result['CycTime'] = self.cyc_time

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.dag_type is not None:
            result['DagType'] = self.dag_type

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_history_id is not None:
            result['InstanceHistoryId'] = self.instance_history_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginRunningTime') is not None:
            self.begin_running_time = m.get('BeginRunningTime')

        if m.get('BeginWaitResTime') is not None:
            self.begin_wait_res_time = m.get('BeginWaitResTime')

        if m.get('BeginWaitTimeTime') is not None:
            self.begin_wait_time_time = m.get('BeginWaitTimeTime')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CycTime') is not None:
            self.cyc_time = m.get('CycTime')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DagType') is not None:
            self.dag_type = m.get('DagType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceHistoryId') is not None:
            self.instance_history_id = m.get('InstanceHistoryId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

