# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class CreateJobRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_name: str = None,
        job_spec: main_models.CreateJobRequestJobSpec = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The job name.
        self.job_name = job_name
        # The job configurations.
        self.job_spec = job_spec

    def validate(self):
        if self.job_spec:
            self.job_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_spec is not None:
            result['JobSpec'] = self.job_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSpec') is not None:
            temp_model = main_models.CreateJobRequestJobSpec()
            self.job_spec = temp_model.from_map(m.get('JobSpec'))

        return self

class CreateJobRequestJobSpec(DaraModel):
    def __init__(
        self,
        array_request: str = None,
        command_line: str = None,
        job_queue: str = None,
        post_cmd_line: str = None,
        priority: str = None,
        resources: main_models.CreateJobRequestJobSpecResources = None,
        runas_user: str = None,
        runas_user_password: str = None,
        stderr_path: str = None,
        stdout_path: str = None,
        variables: str = None,
        wall_time: str = None,
    ):
        # The jobs in the queue.
        # 
        # Format: X-Y:Z. X is the minimum index value. Y is the maximum index value. Z is the step size. For example, 2-7:2 indicates that three jobs need to be run and their index values are 2, 4, and 6.
        self.array_request = array_request
        # The command or script that is used to run the job. If you want to use a command, you must specify the full path of the command, for example, /bin/ping.
        # 
        # If you want to use a script, you must make sure that you have the execution permissions on it. By default, the user root directory ~/ is used as the default script path on the cluster side. If your script is not in that directory, you must specify the full path in this parameter, such as /home/xxx/job.sh Note that in this mode, if requirements on resources such as CPU and memory are specified in the script, the job will be run based on the resource requirements specified in the script. In this case, do not specify resource requirements in the Resource parameter. Otherwise, the job may fail to run.
        # 
        # If you want to run the job directly by using the CLI, you must specify the absolute path of the command and add two hyphens and a space (-- ) before the path, such as -- /bin/ping -c 10 localhost.
        # 
        # This parameter is required.
        self.command_line = command_line
        # The queue to which the job belongs.
        self.job_queue = job_queue
        # The post-processing command of the job.
        self.post_cmd_line = post_cmd_line
        # The job priority.
        self.priority = priority
        # The resource configurations of the job.
        self.resources = resources
        # The cluster-side user as which you want to submit the job.
        self.runas_user = runas_user
        # The password of the user specified by the RunasUser parameter.
        self.runas_user_password = runas_user_password
        # The path of the standard error output file of the job. You need to specify the full path.
        self.stderr_path = stderr_path
        # The path of the standard output file of the job. You need to specify the full path.
        self.stdout_path = stdout_path
        # The environment variables of the job. The value is a string in the JSON array format. Each array member is a JSON object that contains two members: Name and Value. Name indicates the name of the environment variable, and Value indicates the value of the environment variable.
        self.variables = variables
        # The maximum duration for which the job can be run. Format: `hour: minute: second`. For example, `01:00:00` indicates 1 hour.
        self.wall_time = wall_time

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request

        if self.command_line is not None:
            result['CommandLine'] = self.command_line

        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue

        if self.post_cmd_line is not None:
            result['PostCmdLine'] = self.post_cmd_line

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user

        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password

        if self.stderr_path is not None:
            result['StderrPath'] = self.stderr_path

        if self.stdout_path is not None:
            result['StdoutPath'] = self.stdout_path

        if self.variables is not None:
            result['Variables'] = self.variables

        if self.wall_time is not None:
            result['WallTime'] = self.wall_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')

        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')

        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')

        if m.get('PostCmdLine') is not None:
            self.post_cmd_line = m.get('PostCmdLine')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Resources') is not None:
            temp_model = main_models.CreateJobRequestJobSpecResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')

        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')

        if m.get('StderrPath') is not None:
            self.stderr_path = m.get('StderrPath')

        if m.get('StdoutPath') is not None:
            self.stdout_path = m.get('StdoutPath')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        if m.get('WallTime') is not None:
            self.wall_time = m.get('WallTime')

        return self

class CreateJobRequestJobSpecResources(DaraModel):
    def __init__(
        self,
        cores: int = None,
        gpus: int = None,
        memory: str = None,
        nodes: int = None,
    ):
        # The number of vCPUs to be allocated to each compute node.
        self.cores = cores
        # The number of GPUs to be allocated to each compute node.
        self.gpus = gpus
        # The memory size to be allocated to each compute node. The memory size is in string format. Unit: MB or GB.
        self.memory = memory
        # The number of compute nodes to be allocated to the job.
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

