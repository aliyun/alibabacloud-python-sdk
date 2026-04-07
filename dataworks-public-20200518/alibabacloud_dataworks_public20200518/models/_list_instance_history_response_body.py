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
        # The instances.
        self.instances = instances
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        # The time when the instance started to be run. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.begin_running_time = begin_running_time
        # The time when the instance started to wait for resources.
        self.begin_wait_res_time = begin_wait_res_time
        # The time when the instance started to wait to be scheduled.
        self.begin_wait_time_time = begin_wait_time_time
        # The data timestamp of the instance. In most cases, the value is one day before the time when the instance was run.
        self.bizdate = bizdate
        # The time when the instance was generated.
        self.create_time = create_time
        # The time when the node started to be run. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.cyc_time = cyc_time
        # The workflow ID.
        self.dag_id = dag_id
        # Indicates whether the instance is associated with a monitoring rule in Data Quality. Valid values:
        # 
        # *   0: The instance is associated with a monitoring rule in Data Quality.
        # *   1: The instance is not associated with a monitoring rule in Data Quality.
        self.dag_type = dag_type
        # The error message. This parameter is deprecated. You can call the GetInstanceLog operation to query the error information related to the node.
        self.error_message = error_message
        # The time when the running of the node was complete. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.finish_time = finish_time
        # The historical record number of the instance.
        self.instance_history_id = instance_history_id
        # The instance ID.
        self.instance_id = instance_id
        # The time when the node was last modified.
        self.modify_time = modify_time
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The status of the node that generates the instance. Valid values:
        # 
        # *   NOT_RUN: The node is not run.
        # *   WAIT_TIME: The node is waiting for the scheduling time to arrive.
        # *   WAIT_RESOURCE: The node is waiting for resources.
        # *   RUNNING: The node is running.
        # *   CHECKING: Data quality is being checked for the node.
        # *   CHECKING_CONDITION: Branch conditions are being checked for the node.
        # *   FAILURE: The node fails to be run.
        # *   SUCCESS: The node is successfully run.
        self.status = status
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL(0): The node is an auto triggered node. The scheduling system regularly runs the node.
        # *   MANUAL(1): The node is a manually triggered node. The scheduling system does not regularly run the node.
        # *   PAUSE(2): The node is a frozen node. The scheduling system regularly runs the node but sets the status of the node to failed when the scheduling system starts to run the node.
        # *   SKIP(3): The node is a dry-run node. The scheduling system regularly runs the node but sets the status of the node to successful when the scheduling system starts to run the node.
        # *   SKIP_UNCHOOSE(4): The node is an unselected node in a temporary workflow. This type of node exists only in temporary workflows. The scheduling system sets the status of the node to successful when the scheduling system starts to run the node.
        # *   SKIP_CYCLE(5): The node is a node that is scheduled by the week or month and is waiting for the scheduling time to arrive. The scheduling system regularly runs the node but sets the status of the node to successful when the scheduling system starts to run the node.
        # *   CONDITION_UNCHOOSE(6): The node is not selected by its ancestor branch node and is run as a dry-run node.
        # *   REALTIME_DEPRECATED(7): The node has instances that are generated in real time but deprecated. The scheduling system sets the status of the node to successful.
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

