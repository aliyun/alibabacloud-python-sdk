# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class JobItem(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        cluster_id: str = None,
        code_source: main_models.JobItemCodeSource = None,
        credential_config: main_models.CredentialConfig = None,
        data_sources: List[main_models.JobItemDataSources] = None,
        display_name: str = None,
        duration: int = None,
        elastic_spec: main_models.JobElasticSpec = None,
        enable_preemptible_job: bool = None,
        enabled_debugger: bool = None,
        envs: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_failed_time: str = None,
        gmt_finish_time: str = None,
        gmt_modified_time: str = None,
        gmt_running_time: str = None,
        gmt_stopped_time: str = None,
        gmt_submitted_time: str = None,
        gmt_successed_time: str = None,
        is_deleted: bool = None,
        job_id: str = None,
        job_max_running_time_minutes: int = None,
        job_replica_statuses: List[main_models.JobReplicaStatus] = None,
        job_specs: List[main_models.JobSpec] = None,
        job_type: str = None,
        node_count: str = None,
        node_names: List[str] = None,
        pods: List[main_models.PodItem] = None,
        priority: int = None,
        reason_code: str = None,
        reason_message: str = None,
        request_cpu: int = None,
        request_gpu: str = None,
        request_memory: str = None,
        resource_id: str = None,
        resource_level: str = None,
        resource_name: str = None,
        resource_quota_name: str = None,
        resource_type: str = None,
        restart_times: str = None,
        settings: main_models.JobSettings = None,
        status: str = None,
        status_history: List[main_models.StatusTransitionItem] = None,
        sub_status: str = None,
        system_envs: Dict[str, str] = None,
        tenant_id: str = None,
        thirdparty_lib_dir: str = None,
        thirdparty_libs: List[str] = None,
        use_oversold_resource: bool = None,
        user_command: str = None,
        user_id: str = None,
        user_script: str = None,
        user_vpc: main_models.JobItemUserVpc = None,
        username: str = None,
        working_dir: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.accessibility = accessibility
        self.cluster_id = cluster_id
        self.code_source = code_source
        self.credential_config = credential_config
        self.data_sources = data_sources
        self.display_name = display_name
        self.duration = duration
        self.elastic_spec = elastic_spec
        self.enable_preemptible_job = enable_preemptible_job
        self.enabled_debugger = enabled_debugger
        self.envs = envs
        self.gmt_create_time = gmt_create_time
        self.gmt_failed_time = gmt_failed_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_running_time = gmt_running_time
        self.gmt_stopped_time = gmt_stopped_time
        self.gmt_submitted_time = gmt_submitted_time
        self.gmt_successed_time = gmt_successed_time
        self.is_deleted = is_deleted
        self.job_id = job_id
        self.job_max_running_time_minutes = job_max_running_time_minutes
        self.job_replica_statuses = job_replica_statuses
        self.job_specs = job_specs
        self.job_type = job_type
        self.node_count = node_count
        self.node_names = node_names
        self.pods = pods
        self.priority = priority
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.request_cpu = request_cpu
        self.request_gpu = request_gpu
        self.request_memory = request_memory
        self.resource_id = resource_id
        self.resource_level = resource_level
        self.resource_name = resource_name
        self.resource_quota_name = resource_quota_name
        self.resource_type = resource_type
        self.restart_times = restart_times
        self.settings = settings
        self.status = status
        self.status_history = status_history
        self.sub_status = sub_status
        self.system_envs = system_envs
        self.tenant_id = tenant_id
        self.thirdparty_lib_dir = thirdparty_lib_dir
        self.thirdparty_libs = thirdparty_libs
        self.use_oversold_resource = use_oversold_resource
        self.user_command = user_command
        self.user_id = user_id
        self.user_script = user_script
        self.user_vpc = user_vpc
        self.username = username
        self.working_dir = working_dir
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.credential_config:
            self.credential_config.validate()
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

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()

        if self.enable_preemptible_job is not None:
            result['EnablePreemptibleJob'] = self.enable_preemptible_job

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

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_running_time is not None:
            result['GmtRunningTime'] = self.gmt_running_time

        if self.gmt_stopped_time is not None:
            result['GmtStoppedTime'] = self.gmt_stopped_time

        if self.gmt_submitted_time is not None:
            result['GmtSubmittedTime'] = self.gmt_submitted_time

        if self.gmt_successed_time is not None:
            result['GmtSuccessedTime'] = self.gmt_successed_time

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_max_running_time_minutes is not None:
            result['JobMaxRunningTimeMinutes'] = self.job_max_running_time_minutes

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

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

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

        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu

        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu

        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_quota_name is not None:
            result['ResourceQuotaName'] = self.resource_quota_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.restart_times is not None:
            result['RestartTimes'] = self.restart_times

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

        if self.system_envs is not None:
            result['SystemEnvs'] = self.system_envs

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir

        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs

        if self.use_oversold_resource is not None:
            result['UseOversoldResource'] = self.use_oversold_resource

        if self.user_command is not None:
            result['UserCommand'] = self.user_command

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_script is not None:
            result['UserScript'] = self.user_script

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.username is not None:
            result['Username'] = self.username

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CodeSource') is not None:
            temp_model = main_models.JobItemCodeSource()
            self.code_source = temp_model.from_map(m.get('CodeSource'))

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.JobItemDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ElasticSpec') is not None:
            temp_model = main_models.JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m.get('ElasticSpec'))

        if m.get('EnablePreemptibleJob') is not None:
            self.enable_preemptible_job = m.get('EnablePreemptibleJob')

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

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtRunningTime') is not None:
            self.gmt_running_time = m.get('GmtRunningTime')

        if m.get('GmtStoppedTime') is not None:
            self.gmt_stopped_time = m.get('GmtStoppedTime')

        if m.get('GmtSubmittedTime') is not None:
            self.gmt_submitted_time = m.get('GmtSubmittedTime')

        if m.get('GmtSuccessedTime') is not None:
            self.gmt_successed_time = m.get('GmtSuccessedTime')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobMaxRunningTimeMinutes') is not None:
            self.job_max_running_time_minutes = m.get('JobMaxRunningTimeMinutes')

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

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        self.pods = []
        if m.get('Pods') is not None:
            for k1 in m.get('Pods'):
                temp_model = main_models.PodItem()
                self.pods.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')

        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')

        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceQuotaName') is not None:
            self.resource_quota_name = m.get('ResourceQuotaName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RestartTimes') is not None:
            self.restart_times = m.get('RestartTimes')

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

        if m.get('SystemEnvs') is not None:
            self.system_envs = m.get('SystemEnvs')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')

        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')

        if m.get('UseOversoldResource') is not None:
            self.use_oversold_resource = m.get('UseOversoldResource')

        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserScript') is not None:
            self.user_script = m.get('UserScript')

        if m.get('UserVpc') is not None:
            temp_model = main_models.JobItemUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class JobItemUserVpc(DaraModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        self.default_route = default_route
        self.extended_cidrs = extended_cidrs
        self.security_group_id = security_group_id
        self.switch_id = switch_id
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

class JobItemDataSources(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        mount_path: str = None,
    ):
        self.data_source_id = data_source_id
        self.mount_path = mount_path

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self



class JobItemCodeSource(DaraModel):
    def __init__(
        self,
        branch: str = None,
        code_source_id: str = None,
        commit: str = None,
        mount_path: str = None,
    ):
        self.branch = branch
        self.code_source_id = code_source_id
        self.commit = commit
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

