# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListInstancesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of instances.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. You can use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true: The request was successful.
        # - false: The request failed.
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
            temp_model = main_models.ListInstancesResponseBodyData()
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

class ListInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyDataInstances] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The instance information.
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of instances.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyDataInstances(DaraModel):
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
        error_message: str = None,
        finish_time: int = None,
        instance_id: int = None,
        modify_time: int = None,
        node_id: int = None,
        node_name: str = None,
        param_values: str = None,
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
        # The time when the instance started running.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.begin_running_time = begin_running_time
        # The time when the instance started waiting for resources.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.begin_wait_res_time = begin_wait_res_time
        # The time when the instance started waiting for scheduling.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.begin_wait_time_time = begin_wait_time_time
        # The data timestamp of the scheduled node. This is typically the day before the node runs.
        # 
        # The value is a 13-digit number, such as `1590336000000`.
        self.bizdate = bizdate
        # The business process ID.
        self.business_id = business_id
        # The connection string.
        self.connection = connection
        # The time when the instance was created.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.create_time = create_time
        # The user who triggered the instance to run. For example, if user Test triggered a data backfill instance, the CreateUser is Test.
        self.create_user = create_user
        # The scheduled runtime of the node.
        # 
        # The value is a 13-digit number, such as `1590422400000`.
        self.cyc_time = cyc_time
        # The workflow ID.
        self.dag_id = dag_id
        # The type of the workflow. Valid values:
        # 
        # - DAILY(0): daily scheduling workflow.
        # - MANUAL(1): manual task workflow.
        # - SMOKE_TEST(2): smoke testing workflow.
        # - SUPPLY_DATA(3): data backfill workflow.
        # - MANUAL_FLOW(4): manually triggered dataflow PAI workflow (such as running a workflow in the IDE).
        # - BUSINESS_PROCESS_DAG(5): manual business process workflow.
        self.dag_type = dag_type
        # The DQC partitioning rule string.
        self.dqc_description = dqc_description
        # The DQC type. Valid values:
        # - 0: associated with DQC.
        # - 1: not associated with DQC.
        self.dqc_type = dqc_type
        # **[Deprecated]** The error message of the instance run. You can call [GetInstanceLog](https://help.aliyun.com/document_detail/173983.html) to obtain the error information of the executed task.
        self.error_message = error_message
        # The time when the scheduled node finished running.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.finish_time = finish_time
        # The instance ID.
        self.instance_id = instance_id
        # The time when the scheduled node was last modified.
        # 
        # The value is a 13-digit number, such as `1590416703313`.
        self.modify_time = modify_time
        # The node ID.
        self.node_id = node_id
        # The node name.
        self.node_name = node_name
        # The parameter information.
        self.param_values = param_values
        # The priority of the instance. Valid values: 1, 3, 5, 7, and 8.
        # 
        # A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The ID of the associated business process.
        self.related_flow_id = related_flow_id
        # The interval at which the node is rescheduled after a failure. Unit: milliseconds.
        self.repeat_interval = repeat_interval
        # Indicates whether the instance task can be rerun.
        self.repeatability = repeatability
        # The status of the node. Valid values:
        # 
        # - NOT_RUN(1): The node is not run.
        # - WAIT_TIME(2): The node is waiting for the scheduled time to arrive.
        # - WAIT_RESOURCE(3): The node has been sent to the execution engine and is waiting for resources to be scheduled.
        # - RUNNING(4): The node is running.
        # - CHECKING(7): The node has finished running and has been sent to Data Quality for data verification.
        # - CHECKING_CONDITION(8): The node has finished running and is undergoing branch condition verification.
        # - WAIT_TRIGGER(9): The node is waiting to be triggered. A trigger-based node enters this state after the waiting time elapses.
        # - FAILURE(5): The node failed to run.
        # - SUCCESS(6): The node ran successfully.
        self.status = status
        # The number of remaining reruns for the instance. The value can be empty or an integer greater than or equal to 0.
        # - Empty: The node corresponding to this instance does not have automatic rerun configured.
        # - 0: The instance cannot be rerun.
        # - An integer greater than 0 (n): The instance can be rerun n times. For example, if the value is 1, the remaining rerun count is 1. If the value is 2, the remaining rerun count is 2, and so on. The initial value is the automatic rerun count defined for the corresponding node plus 1.
        self.task_rerun_time = task_rerun_time
        # The scheduling type of the task instance. Valid values:
        # - NORMAL(0): The node is a normal scheduled node that is triggered by daily scheduling.
        # - MANUAL(1): The node is a manual node that is not triggered by daily scheduling.
        # - PAUSE(2): The node is a frozen node that is triggered by daily scheduling but is set to failed when scheduling starts.
        # - SKIP(3): The node is a dry-run node that is triggered by daily scheduling but is set to successful when scheduling starts.
        # - SKIP_UNCHOOSE(4): The node is an unselected node in a temporary workflow. It exists only in temporary workflows and is set to successful when scheduling starts.
        # - SKIP_CYCLE(5): The node is a weekly or monthly node whose scheduling cycle has not arrived. It is triggered by daily scheduling but is set to successful when scheduling starts.
        # - CONDITION_UNCHOOSE(6): The upstream instance contains a branch (IF) node, but this downstream node is not selected by the branch node and is set to a dry-run node.
        # - REALTIME_DEPRECATED(7): The node is an expired periodic instance generated in real time. This type of node is set to successful.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

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

