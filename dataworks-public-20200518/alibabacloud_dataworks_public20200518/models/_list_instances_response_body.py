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
        # The ID of the node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the ID of the node.
        self.data = data
        # The HTTP status code returned.
        self.error_code = error_code
        # The page number of the returned page.
        self.error_message = error_message
        # The error message that is returned for the instance.
        # 
        # This parameter is deprecated. You can call the [GetInstanceLog](https://help.aliyun.com/document_detail/173983.html) operation to query the error information related to the node.
        self.http_status_code = http_status_code
        # The name of the node.
        self.request_id = request_id
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
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
        # The name of the node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the name of the node.
        self.instances = instances
        # The time when the node was scheduled to run.
        self.page_number = page_number
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        self.page_size = page_size
        # The priority of the instance. Valid values: 1, 3, 5, 7, and 8.
        # 
        # A greater value indicates a higher priority. Default value: 1.
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
        # The type of the workflow. Valid values:
        # 
        # *   DAILY: The workflow is used to run auto triggered nodes.
        # *   MANUAL: The workflow is used to run manually triggered nodes.
        # *   SMOKE_TEST: The workflow is used to perform smoke testing.
        # *   SUPPLY_DATA: The workflow is used to backfill data.
        self.baseline_id = baseline_id
        # The time when the instance started to run.
        self.begin_running_time = begin_running_time
        # The time when the node stopped running.
        self.begin_wait_res_time = begin_wait_res_time
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.begin_wait_time_time = begin_wait_time_time
        # The number of entries to return on each page. Default value: 10. Maximum value: 100.
        # 
        # You cannot specify the sorting method for the instances to be returned by this operation. By default, the instances are sorted in descending order of the time when the instances were created.
        self.bizdate = bizdate
        # The ID of the workflow to which the node belongs.
        self.business_id = business_id
        # The number of times the node can be rerun. The value of this parameter can be empty or an integer that is greater than or equal to 0.
        # 
        # *   If the value of this parameter is empty, the number of times that the node can be rerun is not specified.
        # *   If the value of this parameter is 0, the node cannot be rerun.
        # *   If the value of this parameter is a positive integer such as n, the node can be rerun n times. For example, if the value of this parameter is 1, the node can be rerun once. If the value of this parameter is 2, the node can be rerun twice.
        self.connection = connection
        # The interval at which the node is rerun after the node fails to run. Unit: milliseconds.
        self.create_time = create_time
        # The ID of the node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the ID of the node.
        self.create_user = create_user
        # The error message returned.
        self.cyc_time = cyc_time
        # The time when the instance started to wait for resources.
        self.dag_id = dag_id
        # The data timestamp of the instance. In most cases, the value is one day before the time when the instance was run.
        self.dag_type = dag_type
        # The operation that you want to perform.
        self.dqc_description = dqc_description
        # The status of the node. Valid values:
        # 
        # *   NOT_RUN: The node is not run.
        # *   WAIT_TIME: The node is waiting for the scheduling time to arrive.
        # *   WAIT_RESOURCE: The node is waiting for resources.
        # *   RUNNING: The node is running.
        # *   CHECKING: Data quality is being checked for the node.
        # *   CHECKING_CONDITION: Branch conditions are being checked for the node.
        # *   FAILURE: The node fails to run.
        # *   SUCCESS: The node is successfully run.
        self.dqc_type = dqc_type
        # The name of the account that is used to run the instance. For example, if an account named Test was used to run the instance to backfill data, the value of this parameter is Test.
        self.error_message = error_message
        # The ID of the Alibaba Cloud account used by the workspace administrator. You can log on to the Alibaba Cloud Management Console and view the ID on the Security Settings page of the Account Center console.
        self.finish_time = finish_time
        # The number of the page to return. Minimum value:1. Maximum value: 100.
        self.instance_id = instance_id
        # The name of the workflow. You can call the [ListBusiness](https://help.aliyun.com/document_detail/173945.html) operation to query the name of the workflow.
        self.modify_time = modify_time
        # The environment of the workspace. Valid values: PROD and DEV. The value PROD indicates the production environment. The value DEV indicates the development environment.
        self.node_id = node_id
        # The ID of the workflow.
        self.node_name = node_name
        # The table and partition filter expression in Data Quality that are associated with the node.
        self.param_values = param_values
        # The total number of instances.
        self.priority = priority
        # The type of the node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the type of the node.
        self.related_flow_id = related_flow_id
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL(0): The node is an auto triggered node. The scheduling system regularly runs the node.
        # 
        # *   MANUAL(1): The node is a manually triggered node. The scheduling system does not regularly run the node.
        # 
        # *   PAUSE(2): The node is a frozen node. The scheduling system regularly runs the node but sets the status of the node to failed when the scheduling system starts to run the node.
        # 
        # *   SKIP(3): The node is a dry-run node. The scheduling system regularly runs the node but sets the status of the node to succeeded when the scheduling system starts to run the node.
        # 
        # *   SKIP_UNCHOOSE(4): The node is an unselected node in a temporary workflow. This type of node exists only in temporary workflows. The scheduling system sets the status of the node to succeeded when the scheduling system starts to run the node.
        # 
        # *   SKIP_CYCLE(5): The node is a node that is scheduled by week or month and is waiting for the scheduling time to arrive. The scheduling system regularly runs the node but sets the status of the node to succeeded when the scheduling system starts to run the node.
        # 
        # *   CONDITION_UNCHOOSE(6): The node is not selected by its ancestor branch node and is run as a dry-run node.
        # 
        #     REALTIME_DEPRECATED(7): The node has instances that are generated in real time but deprecated. The scheduling system sets the status of the node to succeeded.
        self.repeat_interval = repeat_interval
        # The status of the node. Valid values:
        # 
        # *   NOT_RUN: The node is not run.
        # *   WAIT_TIME: The node is waiting for the scheduling time to arrive.
        # *   WAIT_RESOURCE: The node is waiting for resources.
        # *   RUNNING: The node is running.
        # *   CHECKING: Data quality is being checked for the node.
        # *   CHECKING_CONDITION: Branch conditions are being checked for the node.
        # *   FAILURE: The node fails to run.
        # *   SUCCESS: The node is successfully run.
        self.repeatability = repeatability
        # The data timestamp of the instances that you want to query. Specify the timestamp in the yyyy-MM-dd HH:mm:ss format.
        self.status = status
        # The ID of the workspace. You can call the [ListProjects](https://help.aliyun.com/document_detail/178393.html) operation to query the ID of the workspace.
        self.task_rerun_time = task_rerun_time
        # The information about the instances.
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

