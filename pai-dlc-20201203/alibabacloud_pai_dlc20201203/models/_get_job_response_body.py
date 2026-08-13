# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class GetJobResponseBody(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        cluster_id: str = None,
        code_source: main_models.GetJobResponseBodyCodeSource = None,
        credential_config: main_models.CredentialConfig = None,
        custom_envs: List[main_models.GetJobResponseBodyCustomEnvs] = None,
        data_sources: List[main_models.GetJobResponseBodyDataSources] = None,
        description: str = None,
        display_name: str = None,
        duration: int = None,
        elastic_spec: main_models.JobElasticSpec = None,
        enabled_debugger: bool = None,
        envs: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_failed_time: str = None,
        gmt_finish_time: str = None,
        gmt_running_time: str = None,
        gmt_stopped_time: str = None,
        gmt_submitted_time: str = None,
        gmt_successed_time: str = None,
        job_id: str = None,
        job_replica_statuses: List[main_models.JobReplicaStatus] = None,
        job_specs: List[main_models.JobSpec] = None,
        job_type: str = None,
        pods: List[main_models.GetJobResponseBodyPods] = None,
        priority: int = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_level: str = None,
        resource_type: str = None,
        restart_record: List[main_models.GetJobResponseBodyRestartRecord] = None,
        restart_times: str = None,
        role_system_envs: Dict[str, dict] = None,
        scheduling_strategy: str = None,
        settings: main_models.JobSettings = None,
        status: str = None,
        status_history: List[main_models.StatusTransitionItem] = None,
        sub_status: str = None,
        tenant_id: str = None,
        thirdparty_lib_dir: str = None,
        thirdparty_libs: List[str] = None,
        user_command: str = None,
        user_id: str = None,
        user_vpc: main_models.GetJobResponseBodyUserVpc = None,
        workspace_id: str = None,
        workspace_name: str = None,
        supported_profiling_types: str = None,
    ):
        # The visibility of the task. Valid values:
        self.accessibility = accessibility
        # The cluster ID.
        self.cluster_id = cluster_id
        # The code source.
        self.code_source = code_source
        # The access credential configuration.
        self.credential_config = credential_config
        self.custom_envs = custom_envs
        # The list of data sources.
        self.data_sources = data_sources
        self.description = description
        # The job name.
        self.display_name = display_name
        # The job duration, in seconds.
        self.duration = duration
        # The elastic job parameters.
        self.elastic_spec = elastic_spec
        # Specifies whether the debugger job is enabled.
        self.enabled_debugger = enabled_debugger
        # The environment variable configuration.
        self.envs = envs
        # The time when the job was created (UTC).
        self.gmt_create_time = gmt_create_time
        # The time when the job failed (UTC).
        self.gmt_failed_time = gmt_failed_time
        # The time when the task finished (UTC).
        self.gmt_finish_time = gmt_finish_time
        # The time when the job started running (UTC).
        self.gmt_running_time = gmt_running_time
        # The time when the job was stopped (UTC).
        self.gmt_stopped_time = gmt_stopped_time
        # The time when the job was submitted to the cluster (UTC).
        self.gmt_submitted_time = gmt_submitted_time
        # The time when the job completed successfully (UTC).
        self.gmt_successed_time = gmt_successed_time
        # The job ID.
        self.job_id = job_id
        # The job replica statuses.
        self.job_replica_statuses = job_replica_statuses
        # The node configurations in the job. Refer to **JobSpecs** in the CreateJob API.
        self.job_specs = job_specs
        # The job type. Specified by the JobType parameter in the [CreateJob](https://help.aliyun.com/document_detail/459672.html) API.
        self.job_type = job_type
        # All pods running in the job.
        self.pods = pods
        # The priority of the job. Valid values: 1 to 9.
        self.priority = priority
        # The status detail code, which categorizes the sub-status under the current status (Status).
        self.reason_code = reason_code
        # The detailed description of the status.
        self.reason_message = reason_message
        # The request ID, used for diagnostics and troubleshooting.
        self.request_id = request_id
        # The ID of the resource group in which the job runs.
        self.resource_id = resource_id
        # The resource level used when the job runs.
        self.resource_level = resource_level
        # The resource type. Valid values: ECS, Lingjun, ACS.
        self.resource_type = resource_type
        # The job restart records.
        self.restart_record = restart_record
        # The number of restarts used and the maximum number of restarts for the job.
        self.restart_times = restart_times
        self.role_system_envs = role_system_envs
        self.scheduling_strategy = scheduling_strategy
        # The additional parameter settings for the job.
        self.settings = settings
        # The job running status. Valid values:
        self.status = status
        # The status history.
        self.status_history = status_history
        # The job sub-status, such as preemption retry status.
        self.sub_status = sub_status
        # The tenant ID.
        self.tenant_id = tenant_id
        # The folder where the third-party library (requirements.txt) file is located.
        self.thirdparty_lib_dir = thirdparty_lib_dir
        # The list of third-party Python libraries to install.
        self.thirdparty_libs = thirdparty_libs
        # The startup command for each node.
        self.user_command = user_command
        # The Alibaba Cloud UID of the job submitter.
        self.user_id = user_id
        # The user VPC.
        self.user_vpc = user_vpc
        # The ID of the workspace to which the job belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the job belongs.
        self.workspace_name = workspace_name
        self.supported_profiling_types = supported_profiling_types

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.custom_envs:
            for v1 in self.custom_envs:
                 if v1:
                    v1.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()
        if self.job_replica_statuses:
            for v1 in self.job_replica_statuses:
                 if v1:
                    v1.validate()
        if self.job_specs:
            for v1 in self.job_specs:
                 if v1:
                    v1.validate()
        if self.pods:
            for v1 in self.pods:
                 if v1:
                    v1.validate()
        if self.restart_record:
            for v1 in self.restart_record:
                 if v1:
                    v1.validate()
        if self.settings:
            self.settings.validate()
        if self.status_history:
            for v1 in self.status_history:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        result['CustomEnvs'] = []
        if self.custom_envs is not None:
            for k1 in self.custom_envs:
                result['CustomEnvs'].append(k1.to_map() if k1 else None)

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()

        if self.enabled_debugger is not None:
            result['EnabledDebugger'] = self.enabled_debugger

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_failed_time is not None:
            result['GmtFailedTime'] = self.gmt_failed_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_running_time is not None:
            result['GmtRunningTime'] = self.gmt_running_time

        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time

        if self.gmt_submitted_time is not None:
            result['GmtSubmittedTime'] = self.gmt_submitted_time

        if self.gmt_successed_time is not None:
            result['GmtSuccessedTime'] = self.gmt_successed_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['JobReplicaStatuses'] = []
        if self.job_replica_statuses is not None:
            for k1 in self.job_replica_statuses:
                result['JobReplicaStatuses'].append(k1.to_map() if k1 else None)

        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k1 in self.job_specs:
                result['JobSpecs'].append(k1.to_map() if k1 else None)

        if self.job_type is not None:
            result['JobType'] = self.job_type

        result['Pods'] = []
        if self.pods is not None:
            for k1 in self.pods:
                result['Pods'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['RestartRecord'] = []
        if self.restart_record is not None:
            for k1 in self.restart_record:
                result['RestartRecord'].append(k1.to_map() if k1 else None)

        if self.restart_times is not None:
            result['RestartTimes'] = self.restart_times

        if self.role_system_envs is not None:
            result['RoleSystemEnvs'] = self.role_system_envs

        if self.scheduling_strategy is not None:
            result['SchedulingStrategy'] = self.scheduling_strategy

        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        if self.status is not None:
            result['Status'] = self.status

        result['StatusHistory'] = []
        if self.status_history is not None:
            for k1 in self.status_history:
                result['StatusHistory'].append(k1.to_map() if k1 else None)

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir

        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs

        if self.user_command is not None:
            result['UserCommand'] = self.user_command

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        if self.supported_profiling_types is not None:
            result['supportedProfilingTypes'] = self.supported_profiling_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CodeSource') is not None:
            temp_model = main_models.GetJobResponseBodyCodeSource()
            self.code_source = temp_model.from_map(m.get('CodeSource'))

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        self.custom_envs = []
        if m.get('CustomEnvs') is not None:
            for k1 in m.get('CustomEnvs'):
                temp_model = main_models.GetJobResponseBodyCustomEnvs()
                self.custom_envs.append(temp_model.from_map(k1))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.GetJobResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ElasticSpec') is not None:
            temp_model = main_models.JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m.get('ElasticSpec'))

        if m.get('EnabledDebugger') is not None:
            self.enabled_debugger = m.get('EnabledDebugger')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFailedTime') is not None:
            self.gmt_failed_time = m.get('GmtFailedTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtRunningTime') is not None:
            self.gmt_running_time = m.get('GmtRunningTime')

        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')

        if m.get('GmtSubmittedTime') is not None:
            self.gmt_submitted_time = m.get('GmtSubmittedTime')

        if m.get('GmtSuccessedTime') is not None:
            self.gmt_successed_time = m.get('GmtSuccessedTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.job_replica_statuses = []
        if m.get('JobReplicaStatuses') is not None:
            for k1 in m.get('JobReplicaStatuses'):
                temp_model = main_models.JobReplicaStatus()
                self.job_replica_statuses.append(temp_model.from_map(k1))

        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k1 in m.get('JobSpecs'):
                temp_model = main_models.JobSpec()
                self.job_specs.append(temp_model.from_map(k1))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        self.pods = []
        if m.get('Pods') is not None:
            for k1 in m.get('Pods'):
                temp_model = main_models.GetJobResponseBodyPods()
                self.pods.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.restart_record = []
        if m.get('RestartRecord') is not None:
            for k1 in m.get('RestartRecord'):
                temp_model = main_models.GetJobResponseBodyRestartRecord()
                self.restart_record.append(temp_model.from_map(k1))

        if m.get('RestartTimes') is not None:
            self.restart_times = m.get('RestartTimes')

        if m.get('RoleSystemEnvs') is not None:
            self.role_system_envs = m.get('RoleSystemEnvs')

        if m.get('SchedulingStrategy') is not None:
            self.scheduling_strategy = m.get('SchedulingStrategy')

        if m.get('Settings') is not None:
            temp_model = main_models.JobSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.status_history = []
        if m.get('StatusHistory') is not None:
            for k1 in m.get('StatusHistory'):
                temp_model = main_models.StatusTransitionItem()
                self.status_history.append(temp_model.from_map(k1))

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')

        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')

        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserVpc') is not None:
            temp_model = main_models.GetJobResponseBodyUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        if m.get('supportedProfilingTypes') is not None:
            self.supported_profiling_types = m.get('supportedProfilingTypes')

        return self

class GetJobResponseBodyUserVpc(DaraModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        # The default routing. This parameter is valid only for general computing resources. Valid values:
        self.default_route = default_route
        # The extended CIDR blocks. Example: 192.168.0.1/24.
        self.extended_cidrs = extended_cidrs
        # The ID of the user security group.
        self.security_group_id = security_group_id
        # The ID of the user vSwitch.
        self.switch_id = switch_id
        # The ID of the user VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route

        if self.extended_cidrs is not None:
            result['ExtendedCidrs'] = self.extended_cidrs

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')

        if m.get('ExtendedCidrs') is not None:
            self.extended_cidrs = m.get('ExtendedCidrs')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetJobResponseBodyRestartRecord(DaraModel):
    def __init__(
        self,
        detail_error_info_list: List[main_models.GetJobResponseBodyRestartRecordDetailErrorInfoList] = None,
        job_restart_count: int = None,
        occur_phase: str = None,
        occur_time: str = None,
        reason: str = None,
        restart_duration_in_sec: int = None,
        restart_fail_reason: str = None,
        restart_level_type: str = None,
        restart_status: str = None,
        trigger_id: str = None,
    ):
        # The list of fault error messages.
        self.detail_error_info_list = detail_error_info_list
        # The number of job restarts.
        self.job_restart_count = job_restart_count
        # The phase in which the event occurred.
        self.occur_phase = occur_phase
        # The time when the event occurred.
        self.occur_time = occur_time
        # The reason for the restart.
        self.reason = reason
        # The restart duration, in seconds.
        self.restart_duration_in_sec = restart_duration_in_sec
        # The reason for the restart failure.
        self.restart_fail_reason = restart_fail_reason
        self.restart_level_type = restart_level_type
        # The restart status.
        self.restart_status = restart_status
        # TriggerID
        self.trigger_id = trigger_id

    def validate(self):
        if self.detail_error_info_list:
            for v1 in self.detail_error_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetailErrorInfoList'] = []
        if self.detail_error_info_list is not None:
            for k1 in self.detail_error_info_list:
                result['DetailErrorInfoList'].append(k1.to_map() if k1 else None)

        if self.job_restart_count is not None:
            result['JobRestartCount'] = self.job_restart_count

        if self.occur_phase is not None:
            result['OccurPhase'] = self.occur_phase

        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.restart_duration_in_sec is not None:
            result['RestartDurationInSec'] = self.restart_duration_in_sec

        if self.restart_fail_reason is not None:
            result['RestartFailReason'] = self.restart_fail_reason

        if self.restart_level_type is not None:
            result['RestartLevelType'] = self.restart_level_type

        if self.restart_status is not None:
            result['RestartStatus'] = self.restart_status

        if self.trigger_id is not None:
            result['TriggerID'] = self.trigger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_error_info_list = []
        if m.get('DetailErrorInfoList') is not None:
            for k1 in m.get('DetailErrorInfoList'):
                temp_model = main_models.GetJobResponseBodyRestartRecordDetailErrorInfoList()
                self.detail_error_info_list.append(temp_model.from_map(k1))

        if m.get('JobRestartCount') is not None:
            self.job_restart_count = m.get('JobRestartCount')

        if m.get('OccurPhase') is not None:
            self.occur_phase = m.get('OccurPhase')

        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RestartDurationInSec') is not None:
            self.restart_duration_in_sec = m.get('RestartDurationInSec')

        if m.get('RestartFailReason') is not None:
            self.restart_fail_reason = m.get('RestartFailReason')

        if m.get('RestartLevelType') is not None:
            self.restart_level_type = m.get('RestartLevelType')

        if m.get('RestartStatus') is not None:
            self.restart_status = m.get('RestartStatus')

        if m.get('TriggerID') is not None:
            self.trigger_id = m.get('TriggerID')

        return self

class GetJobResponseBodyRestartRecordDetailErrorInfoList(DaraModel):
    def __init__(
        self,
        add_job_level_blacklist: bool = None,
        add_node_to_blacklist: bool = None,
        detail_error_msg: str = None,
        error_code: str = None,
        error_msg: str = None,
        error_source: str = None,
        node: str = None,
        pod: str = None,
        trigger_restart: bool = None,
    ):
        # The job blacklist.
        self.add_job_level_blacklist = add_job_level_blacklist
        # The node blacklist.
        self.add_node_to_blacklist = add_node_to_blacklist
        # The detailed error message.
        self.detail_error_msg = detail_error_msg
        # The error code.
        self.error_code = error_code
        # The fault error message.
        self.error_msg = error_msg
        # The error source.
        self.error_source = error_source
        # The node.
        self.node = node
        # The pod.
        self.pod = pod
        # Indicates whether a restart is triggered.
        self.trigger_restart = trigger_restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_job_level_blacklist is not None:
            result['AddJobLevelBlacklist'] = self.add_job_level_blacklist

        if self.add_node_to_blacklist is not None:
            result['AddNodeToBlacklist'] = self.add_node_to_blacklist

        if self.detail_error_msg is not None:
            result['DetailErrorMsg'] = self.detail_error_msg

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.error_source is not None:
            result['ErrorSource'] = self.error_source

        if self.node is not None:
            result['Node'] = self.node

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.trigger_restart is not None:
            result['TriggerRestart'] = self.trigger_restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddJobLevelBlacklist') is not None:
            self.add_job_level_blacklist = m.get('AddJobLevelBlacklist')

        if m.get('AddNodeToBlacklist') is not None:
            self.add_node_to_blacklist = m.get('AddNodeToBlacklist')

        if m.get('DetailErrorMsg') is not None:
            self.detail_error_msg = m.get('DetailErrorMsg')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ErrorSource') is not None:
            self.error_source = m.get('ErrorSource')

        if m.get('Node') is not None:
            self.node = m.get('Node')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('TriggerRestart') is not None:
            self.trigger_restart = m.get('TriggerRestart')

        return self

class GetJobResponseBodyPods(DaraModel):
    def __init__(
        self,
        duration: float = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_start_time: str = None,
        history_pods: List[main_models.GetJobResponseBodyPodsHistoryPods] = None,
        ip: str = None,
        node_name: str = None,
        pod_id: str = None,
        pod_ips: List[main_models.PodNetworkInterface] = None,
        pod_uid: str = None,
        resource_type: str = None,
        status: str = None,
        sub_status: str = None,
        type: str = None,
        supported_profiling_types: str = None,
    ):
        # The pod duration.
        self.duration = duration
        # The pod creation time (UTC).
        self.gmt_create_time = gmt_create_time
        # The pod finish time (UTC).
        self.gmt_finish_time = gmt_finish_time
        # The pod start time (UTC).
        self.gmt_start_time = gmt_start_time
        # The historical pods.
        self.history_pods = history_pods
        # The network IP address of the pod.
        self.ip = ip
        # The node name.
        self.node_name = node_name
        # The pod ID. You can use this ID with the GetPodLogs and GetPodEvents APIs to retrieve detailed logs and events for the pod.
        self.pod_id = pod_id
        # The pod IP addresses.
        self.pod_ips = pod_ips
        # Pod UID。
        self.pod_uid = pod_uid
        # The pod resource usage type.
        self.resource_type = resource_type
        # The pod status. Valid values:
        self.status = status
        # The pod sub-status, such as preemption status. Valid values:
        self.sub_status = sub_status
        # The pod type, which corresponds to a JobSpec in the JobSpecs parameter of CreateJob.
        self.type = type
        self.supported_profiling_types = supported_profiling_types

    def validate(self):
        if self.history_pods:
            for v1 in self.history_pods:
                 if v1:
                    v1.validate()
        if self.pod_ips:
            for v1 in self.pod_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        result['HistoryPods'] = []
        if self.history_pods is not None:
            for k1 in self.history_pods:
                result['HistoryPods'].append(k1.to_map() if k1 else None)

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        result['PodIps'] = []
        if self.pod_ips is not None:
            for k1 in self.pod_ips:
                result['PodIps'].append(k1.to_map() if k1 else None)

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.type is not None:
            result['Type'] = self.type

        if self.supported_profiling_types is not None:
            result['supportedProfilingTypes'] = self.supported_profiling_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        self.history_pods = []
        if m.get('HistoryPods') is not None:
            for k1 in m.get('HistoryPods'):
                temp_model = main_models.GetJobResponseBodyPodsHistoryPods()
                self.history_pods.append(temp_model.from_map(k1))

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        self.pod_ips = []
        if m.get('PodIps') is not None:
            for k1 in m.get('PodIps'):
                temp_model = main_models.PodNetworkInterface()
                self.pod_ips.append(temp_model.from_map(k1))

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('supportedProfilingTypes') is not None:
            self.supported_profiling_types = m.get('supportedProfilingTypes')

        return self

class GetJobResponseBodyPodsHistoryPods(DaraModel):
    def __init__(
        self,
        duration: float = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_start_time: str = None,
        ip: str = None,
        node_name: str = None,
        pod_id: str = None,
        pod_ips: List[main_models.PodNetworkInterface] = None,
        pod_uid: str = None,
        resource_type: str = None,
        status: str = None,
        sub_status: str = None,
        type: str = None,
        supported_profiling_types: str = None,
    ):
        # The pod duration.
        self.duration = duration
        # The pod creation time (UTC).
        self.gmt_create_time = gmt_create_time
        # The pod finish time (UTC).
        self.gmt_finish_time = gmt_finish_time
        # The pod start time (UTC).
        self.gmt_start_time = gmt_start_time
        # Pod IP。
        self.ip = ip
        # The node name.
        self.node_name = node_name
        # Pod ID。
        self.pod_id = pod_id
        # The pod IP addresses.
        self.pod_ips = pod_ips
        # Pod UID。
        self.pod_uid = pod_uid
        # The pod resource usage type.
        self.resource_type = resource_type
        # The pod status.
        self.status = status
        # The pod sub-status, such as preemption status. Valid values:
        self.sub_status = sub_status
        # The pod type.
        self.type = type
        self.supported_profiling_types = supported_profiling_types

    def validate(self):
        if self.pod_ips:
            for v1 in self.pod_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        result['PodIps'] = []
        if self.pod_ips is not None:
            for k1 in self.pod_ips:
                result['PodIps'].append(k1.to_map() if k1 else None)

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.type is not None:
            result['Type'] = self.type

        if self.supported_profiling_types is not None:
            result['supportedProfilingTypes'] = self.supported_profiling_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        self.pod_ips = []
        if m.get('PodIps') is not None:
            for k1 in m.get('PodIps'):
                temp_model = main_models.PodNetworkInterface()
                self.pod_ips.append(temp_model.from_map(k1))

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('supportedProfilingTypes') is not None:
            self.supported_profiling_types = m.get('supportedProfilingTypes')

        return self

class GetJobResponseBodyDataSources(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        mount_path: str = None,
        uri: str = None,
    ):
        # The data source ID.
        self.data_source_id = data_source_id
        # The local mount path. This is an optional parameter. If left empty, the mount path specified in the data source is used.
        self.mount_path = mount_path
        # The data source path.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class GetJobResponseBodyCustomEnvs(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        visible: str = None,
    ):
        self.key = key
        self.value = value
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        if self.visible is not None:
            result['Visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

class GetJobResponseBodyCodeSource(DaraModel):
    def __init__(
        self,
        branch: str = None,
        code_source_id: str = None,
        commit: str = None,
        mount_path: str = None,
    ):
        # The code branch.
        self.branch = branch
        # The code source ID.
        self.code_source_id = code_source_id
        # The code commit ID.
        self.commit = commit
        # The local mount path.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch is not None:
            result['Branch'] = self.branch

        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id

        if self.commit is not None:
            result['Commit'] = self.commit

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')

        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')

        if m.get('Commit') is not None:
            self.commit = m.get('Commit')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

