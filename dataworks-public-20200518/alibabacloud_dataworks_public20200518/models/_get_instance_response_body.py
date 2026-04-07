# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetInstanceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the instance.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned when the instance fails to be scheduled.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        begin_running_time: int = None,
        begin_wait_res_time: int = None,
        begin_wait_time_time: int = None,
        bizdate: int = None,
        business_id: int = None,
        connection: str = None,
        create_time: int = None,
        create_user: str = None,
        cyc_time: int = None,
        dag_id: int = None,
        dag_type: str = None,
        dqc_description: str = None,
        dqc_type: int = None,
        finish_time: int = None,
        instance_id: int = None,
        modify_time: int = None,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        param_values: str = None,
        period_number: int = None,
        priority: int = None,
        related_flow_id: int = None,
        repeat_interval: int = None,
        repeatability: bool = None,
        status: str = None,
        task_rerun_time: int = None,
        task_type: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The time when the instance started to run.
        self.begin_running_time = begin_running_time
        # The time when the instance started to wait for resources.
        self.begin_wait_res_time = begin_wait_res_time
        # The time when the instance started to wait to be scheduled.
        self.begin_wait_time_time = begin_wait_time_time
        # The data timestamp of the instance. In most cases, the value is one day before the time when the instance was run.
        self.bizdate = bizdate
        # The workflow ID.
        self.business_id = business_id
        # The connection string.
        self.connection = connection
        # The time when the instance was generated.
        self.create_time = create_time
        # The creator of the instance.
        self.create_user = create_user
        # The scheduling time of the instance.
        self.cyc_time = cyc_time
        # The workflow ID.
        self.dag_id = dag_id
        # The type of the workflow. Valid values:
        # 
        # *   DAILY: The workflow is used to run auto triggered nodes.
        # *   MANUAL: The workflow is used to run manually triggered nodes.
        # *   SMOKE_TEST: The workflow is used to perform smoke testing.
        # *   SUPPLY_DATA: The workflow is used to backfill data.
        self.dag_type = dag_type
        # The table and partition filter expression in Data Quality that are associated with the node.
        self.dqc_description = dqc_description
        # Indicates whether the instance is associated with a monitoring rule in Data Quality. Valid values:
        # 
        # *   0: The instance is associated with a monitoring rule in Data Quality.
        # *   1: The instance is not associated with a monitoring rule in Data Quality.
        self.dqc_type = dqc_type
        # The time when the running of the instance was complete.
        self.finish_time = finish_time
        # The instance ID.
        self.instance_id = instance_id
        # The time when the instance was last modified.
        self.modify_time = modify_time
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The owner of the instance.
        self.owner = owner
        # The parameters related to the node.
        self.param_values = param_values
        # The sequence number of the cycle. This parameter indicates the sequence number of the cycle of the instance on the current day.
        self.period_number = period_number
        # The priority of the instance. Valid values: 1, 3, 5, 7, and 8. A greater value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The ID of the workflow to which the node belongs.
        self.related_flow_id = related_flow_id
        # The interval at which the node is rerun after the node fails to run. Unit: milliseconds.
        self.repeat_interval = repeat_interval
        # Indicates whether the node that generates the instance can be rerun.
        self.repeatability = repeatability
        # The status of the node that generates the instance. Valid values:
        # 
        # *   NOT_RUN: The node is not run.
        # *   WAIT_TIME: The node is waiting for its scheduling time to arrive.
        # *   WAIT_RESOURCE: The node is waiting for resources.
        # *   RUNNING: The node is running.
        # *   CHECKING: Data quality is being checked for the node.
        # *   CHECKING_CONDITION: Branch conditions are being checked for the node.
        # *   FAILURE: The node fails to run.
        # *   SUCCESS: The node is successfully run.
        self.status = status
        # The number of times the node can be rerun. The value of this parameter can be empty or an integer that is greater than or equal to 0.
        # 
        # *   If the value of this parameter is empty, the number of times that the node can be rerun is not specified.
        # *   If the value of this parameter is 0, the node cannot be rerun.
        # *   If the value of this parameter is a positive integer such as n, the node can still be rerun n times. For example, if the value of this parameter is 1, the node can still be rerun once. If the value of this parameter is 2, the node can still be rerun twice.
        self.task_rerun_time = task_rerun_time
        # The scheduling type of the node that generates the instance. Valid values:
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
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.begin_running_time is not None:
            result['BeginRunningTime'] = self.begin_running_time

        if self.begin_wait_res_time is not None:
            result['BeginWaitResTime'] = self.begin_wait_res_time

        if self.begin_wait_time_time is not None:
            result['BeginWaitTimeTime'] = self.begin_wait_time_time

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.connection is not None:
            result['Connection'] = self.connection

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

        if self.dqc_description is not None:
            result['DqcDescription'] = self.dqc_description

        if self.dqc_type is not None:
            result['DqcType'] = self.dqc_type

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

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.param_values is not None:
            result['ParamValues'] = self.param_values

        if self.period_number is not None:
            result['PeriodNumber'] = self.period_number

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.related_flow_id is not None:
            result['RelatedFlowId'] = self.related_flow_id

        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval

        if self.repeatability is not None:
            result['Repeatability'] = self.repeatability

        if self.status is not None:
            result['Status'] = self.status

        if self.task_rerun_time is not None:
            result['TaskRerunTime'] = self.task_rerun_time

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BeginRunningTime') is not None:
            self.begin_running_time = m.get('BeginRunningTime')

        if m.get('BeginWaitResTime') is not None:
            self.begin_wait_res_time = m.get('BeginWaitResTime')

        if m.get('BeginWaitTimeTime') is not None:
            self.begin_wait_time_time = m.get('BeginWaitTimeTime')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('Connection') is not None:
            self.connection = m.get('Connection')

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

        if m.get('DqcDescription') is not None:
            self.dqc_description = m.get('DqcDescription')

        if m.get('DqcType') is not None:
            self.dqc_type = m.get('DqcType')

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

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParamValues') is not None:
            self.param_values = m.get('ParamValues')

        if m.get('PeriodNumber') is not None:
            self.period_number = m.get('PeriodNumber')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RelatedFlowId') is not None:
            self.related_flow_id = m.get('RelatedFlowId')

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        if m.get('Repeatability') is not None:
            self.repeatability = m.get('Repeatability')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskRerunTime') is not None:
            self.task_rerun_time = m.get('TaskRerunTime')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

