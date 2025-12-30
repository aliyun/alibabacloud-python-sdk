# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class GetJobResponseBody(DaraModel):
    def __init__(
        self,
        job_info: main_models.GetJobResponseBodyJobInfo = None,
        request_id: str = None,
        success: str = None,
    ):
        # The job details.
        self.job_info = job_info
        # The request ID.
        self.request_id = request_id
        # The request result. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.job_info:
            self.job_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_info is not None:
            result['JobInfo'] = self.job_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInfo') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfo()
            self.job_info = temp_model.from_map(m.get('JobInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetJobResponseBodyJobInfo(DaraModel):
    def __init__(
        self,
        array_job_id: str = None,
        array_job_sub_id: str = None,
        array_request: str = None,
        command_line: str = None,
        create_time: str = None,
        error_log: str = None,
        extra_info: str = None,
        job_id: str = None,
        job_name: str = None,
        job_queue: str = None,
        last_modify_time: str = None,
        node_list: str = None,
        output_log: str = None,
        priority: str = None,
        resources: main_models.GetJobResponseBodyJobInfoResources = None,
        resources_used: main_models.GetJobResponseBodyJobInfoResourcesUsed = None,
        runas_user: str = None,
        start_time: str = None,
        state: str = None,
        variables: List[main_models.GetJobResponseBodyJobInfoVariables] = None,
    ):
        # The parent job ID. If the return value is a non-empty string, the job is an array job.
        self.array_job_id = array_job_id
        # The sub-job ID. This parameter is valid when the ArrayJobId parameter is a non-empty string.
        self.array_job_sub_id = array_job_sub_id
        # The job queue. If the job is not in a queue, the output is empty.
        # 
        # The format is X-Y:Z. X indicates the first index, Y indicates the final index, and Z indicates the step size. For example, 2-7:2 indicates three sub-jobs numbered 2, 4, and 6.
        self.array_request = array_request
        # The command that is used to run the job.
        self.command_line = command_line
        # The time when the job was submitted.
        self.create_time = create_time
        # The error log file of the job.
        self.error_log = error_log
        # Additional information.
        self.extra_info = extra_info
        # The job ID.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        # The queue to which the job belongs.
        self.job_queue = job_queue
        # The time when the job was last modified.
        self.last_modify_time = last_modify_time
        # The compute nodes that are used to run the job.
        self.node_list = node_list
        # The standard output log file of the job.
        self.output_log = output_log
        # The priority of the job.
        self.priority = priority
        # The resources that were requested when the job was submitted.
        self.resources = resources
        # The resources that are actually used by the job.
        self.resources_used = resources_used
        # The user to which the job belongs or that is used to submit the job. This user is a cluster-side user.
        self.runas_user = runas_user
        # The time when the job was started.
        self.start_time = start_time
        # The job state.
        self.state = state
        # The variables of the job.
        self.variables = variables

    def validate(self):
        if self.resources:
            self.resources.validate()
        if self.resources_used:
            self.resources_used.validate()
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_job_id is not None:
            result['ArrayJobId'] = self.array_job_id

        if self.array_job_sub_id is not None:
            result['ArrayJobSubId'] = self.array_job_sub_id

        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request

        if self.command_line is not None:
            result['CommandLine'] = self.command_line

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_log is not None:
            result['ErrorLog'] = self.error_log

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.node_list is not None:
            result['NodeList'] = self.node_list

        if self.output_log is not None:
            result['OutputLog'] = self.output_log

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.resources_used is not None:
            result['ResourcesUsed'] = self.resources_used.to_map()

        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayJobId') is not None:
            self.array_job_id = m.get('ArrayJobId')

        if m.get('ArrayJobSubId') is not None:
            self.array_job_sub_id = m.get('ArrayJobSubId')

        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')

        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorLog') is not None:
            self.error_log = m.get('ErrorLog')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('NodeList') is not None:
            self.node_list = m.get('NodeList')

        if m.get('OutputLog') is not None:
            self.output_log = m.get('OutputLog')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Resources') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('ResourcesUsed') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoResourcesUsed()
            self.resources_used = temp_model.from_map(m.get('ResourcesUsed'))

        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.GetJobResponseBodyJobInfoVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class GetJobResponseBodyJobInfoVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable.
        self.name = name
        # The value of the environment variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetJobResponseBodyJobInfoResourcesUsed(DaraModel):
    def __init__(
        self,
        cores: str = None,
        memory: str = None,
        nodes: str = None,
    ):
        # The number of vCPUs used by the job on each node.
        self.cores = cores
        # The memory size used by the job on each node.
        self.memory = memory
        # The number of nodes that are used to run the job.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        return self

class GetJobResponseBodyJobInfoResources(DaraModel):
    def __init__(
        self,
        cores: str = None,
        gpus: str = None,
        memory: str = None,
        nodes: str = None,
    ):
        # The number of vCPUs used by the job on each node.
        self.cores = cores
        # The number of GPUs used by the job on each node.
        self.gpus = gpus
        # The memory size used by the job on each node.
        self.memory = memory
        # The number of nodes that are used to run the job.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.gpus is not None:
            result['Gpus'] = self.gpus

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Gpus') is not None:
            self.gpus = m.get('Gpus')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        return self

