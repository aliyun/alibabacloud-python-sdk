# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetManualDagInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.GetManualDagInstancesResponseBodyInstances] = None,
        request_id: str = None,
    ):
        # The list of internal instances of the manual workflow.
        self.instances = instances
        # The unique ID of the request.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.GetManualDagInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetManualDagInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        begin_running_time: int = None,
        begin_wait_res_time: int = None,
        begin_wait_time_time: int = None,
        biz_date: int = None,
        create_time: int = None,
        create_user: str = None,
        cyc_time: int = None,
        dag_id: int = None,
        dag_type: str = None,
        finish_time: int = None,
        instance_id: int = None,
        modify_time: int = None,
        node_id: int = None,
        node_name: str = None,
        param_values: str = None,
        status: str = None,
        task_type: str = None,
    ):
        # The time when the instance node started to run.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.begin_running_time = begin_running_time
        # The time when the instance node started to wait for resources.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.begin_wait_res_time = begin_wait_res_time
        # The time when the instance node started to wait for scheduling.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.begin_wait_time_time = begin_wait_time_time
        # The business date. This is typically the day before the node runs.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.biz_date = biz_date
        # The time when the instance node was created.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.create_time = create_time
        # The operator.
        self.create_user = create_user
        # The scheduled time of the instance node.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.cyc_time = cyc_time
        # The DAG ID of the manual workflow instance.
        self.dag_id = dag_id
        # The type of the manual workflow.
        self.dag_type = dag_type
        # The time when the instance node finished running.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.finish_time = finish_time
        # The internal instance ID.
        self.instance_id = instance_id
        # The most recent modification time of the instance node.
        # 
        # The value is a 13-digit number, for example, `1605178414676`.
        self.modify_time = modify_time
        # The internal node ID of the workflow.
        self.node_id = node_id
        # The node name.
        self.node_name = node_name
        # The parameter information of the instance.
        self.param_values = param_values
        # The status of the instance node. Valid values:
        # - NOT_RUN: The instance is not run.
        # - WAIT_TIME: The instance is waiting for the scheduled dueTime or cycleTime.
        # - WAIT_RESOURCE: The instance is waiting for resources.
        # - RUNNING: The instance is running.
        # - CHECKING: The instance is submitted to Data Quality for data verification.
        # - CHECKING_CONDITION: The instance is performing branch condition verification.
        # - FAILURE: The instance failed to run.
        # - SUCCESS: The instance is run successfully.
        self.status = status
        # The scheduling type of the instance node. Valid values:
        # - NORMAL(0): a normal scheduling node. The node is scheduled on a daily basis.
        # - MANUAL(1): a manual node. The node is not scheduled on a daily basis.
        # - PAUSE(2): a paused node. The node is scheduled on a daily basis, but is set to failed when scheduling starts.
        # - SKIP(3): a dry-run node. The node is scheduled on a daily basis, but is set to successful when scheduling starts.
        # - SKIP_UNCHOOSE(4): a node that is not selected in a temporary workflow. This type of node exists only in temporary workflows and is set to successful when scheduling starts.
        # - SKIP_CYCLE(5): a weekly or monthly node that has not reached its run cycle. The node is scheduled on a daily basis, but is set to successful when scheduling starts.
        # - CONDITION_UNCHOOSE(6): a downstream node that is not selected by an upstream branch (IF) node. The node is directly set to dry-run.
        # - REALTIME_DEPRECATED(7): an expired periodic instance generated in real time. This type of node is directly set to successful.
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

        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.cyc_time is not None:
            result['CycTime'] = self.cyc_time

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.dag_type is not None:
            result['DagType'] = self.dag_type

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.param_values is not None:
            result['ParamValues'] = self.param_values

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

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CycTime') is not None:
            self.cyc_time = m.get('CycTime')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DagType') is not None:
            self.dag_type = m.get('DagType')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('ParamValues') is not None:
            self.param_values = m.get('ParamValues')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

