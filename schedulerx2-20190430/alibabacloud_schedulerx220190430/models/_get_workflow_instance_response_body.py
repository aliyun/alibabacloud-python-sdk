# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class GetWorkflowInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetWorkflowInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The details of the workflow instance.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.GetWorkflowInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWorkflowInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        wf_instance_dag: main_models.GetWorkflowInstanceResponseBodyDataWfInstanceDag = None,
        wf_instance_info: main_models.GetWorkflowInstanceResponseBodyDataWfInstanceInfo = None,
    ):
        # The directed acyclic graph (DAG) of the workflow instance, including nodes and dependencies.
        self.wf_instance_dag = wf_instance_dag
        # The details of the workflow instance, including the state of the workflow instance, the time when the workflow instance started to run, the time when the workflow instance stopped running, the state of each job instance, and the dependencies between job instances.
        self.wf_instance_info = wf_instance_info

    def validate(self):
        if self.wf_instance_dag:
            self.wf_instance_dag.validate()
        if self.wf_instance_info:
            self.wf_instance_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.wf_instance_dag is not None:
            result['WfInstanceDag'] = self.wf_instance_dag.to_map()

        if self.wf_instance_info is not None:
            result['WfInstanceInfo'] = self.wf_instance_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WfInstanceDag') is not None:
            temp_model = main_models.GetWorkflowInstanceResponseBodyDataWfInstanceDag()
            self.wf_instance_dag = temp_model.from_map(m.get('WfInstanceDag'))

        if m.get('WfInstanceInfo') is not None:
            temp_model = main_models.GetWorkflowInstanceResponseBodyDataWfInstanceInfo()
            self.wf_instance_info = temp_model.from_map(m.get('WfInstanceInfo'))

        return self

class GetWorkflowInstanceResponseBodyDataWfInstanceInfo(DaraModel):
    def __init__(
        self,
        data_time: str = None,
        end_time: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: int = None,
    ):
        # The data timestamp of the workflow instance.
        self.data_time = data_time
        # The time when the workflow instance stopped running.
        self.end_time = end_time
        # The time when the workflow instance was scheduled to run.
        self.schedule_time = schedule_time
        # The time when the workflow instance started to run.
        self.start_time = start_time
        # The state of the workflow instance. Valid values:
        # 
        # *   1: pending
        # *   2: preparing
        # *   3: running
        # *   4: successful
        # *   5: failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetWorkflowInstanceResponseBodyDataWfInstanceDag(DaraModel):
    def __init__(
        self,
        edges: List[main_models.GetWorkflowInstanceResponseBodyDataWfInstanceDagEdges] = None,
        nodes: List[main_models.GetWorkflowInstanceResponseBodyDataWfInstanceDagNodes] = None,
    ):
        # The dependencies between job instances.
        self.edges = edges
        # The job instances.
        self.nodes = nodes

    def validate(self):
        if self.edges:
            for v1 in self.edges:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Edges'] = []
        if self.edges is not None:
            for k1 in self.edges:
                result['Edges'].append(k1.to_map() if k1 else None)

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k1 in m.get('Edges'):
                temp_model = main_models.GetWorkflowInstanceResponseBodyDataWfInstanceDagEdges()
                self.edges.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetWorkflowInstanceResponseBodyDataWfInstanceDagNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class GetWorkflowInstanceResponseBodyDataWfInstanceDagNodes(DaraModel):
    def __init__(
        self,
        attempt: int = None,
        data_time: str = None,
        end_time: str = None,
        job_id: int = None,
        job_instance_id: int = None,
        job_name: str = None,
        result: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: int = None,
        work_addr: str = None,
    ):
        # The number of retries when the job failed.
        self.attempt = attempt
        # The data timestamp of the job.
        self.data_time = data_time
        # The time when the job stopped running.
        self.end_time = end_time
        # The job ID.
        self.job_id = job_id
        # The ID of the job instance.
        self.job_instance_id = job_instance_id
        # The job name.
        self.job_name = job_name
        # The execution result of the job.
        self.result = result
        # The time when the job was scheduled.
        self.schedule_time = schedule_time
        # The time when the job started to run.
        self.start_time = start_time
        # The state of the job instance. Valid values: 1: The job instance is waiting for execution. 3: The job instance is running. 4: The job instance is run. 5: The job instance failed to run. 9: The job instance is rejected. Enumeration class: com.alibaba.schedulerx.common.domain.InstanceStatus.
        self.status = status
        # The worker on which the job instance run.
        self.work_addr = work_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt is not None:
            result['Attempt'] = self.attempt

        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.result is not None:
            result['Result'] = self.result

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempt') is not None:
            self.attempt = m.get('Attempt')

        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')

        return self

class GetWorkflowInstanceResponseBodyDataWfInstanceDagEdges(DaraModel):
    def __init__(
        self,
        source: int = None,
        target: int = None,
    ):
        # The upstream job instance of the current job instance. A value of 0 indicates that the upstream job instance is the root node.
        self.source = source
        # The downstream job instance of the current job instance.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

