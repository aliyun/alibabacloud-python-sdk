# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AIMasterMessage(TeaModel):
    def __init__(
        self,
        extended: str = None,
        job_restart_count: int = None,
        message_content: str = None,
        message_event: str = None,
        message_version: int = None,
        restart_type: str = None,
    ):
        self.extended = extended
        self.job_restart_count = job_restart_count
        self.message_content = message_content
        self.message_event = message_event
        self.message_version = message_version
        self.restart_type = restart_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended is not None:
            result['Extended'] = self.extended
        if self.job_restart_count is not None:
            result['JobRestartCount'] = self.job_restart_count
        if self.message_content is not None:
            result['MessageContent'] = self.message_content
        if self.message_event is not None:
            result['MessageEvent'] = self.message_event
        if self.message_version is not None:
            result['MessageVersion'] = self.message_version
        if self.restart_type is not None:
            result['RestartType'] = self.restart_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extended') is not None:
            self.extended = m.get('Extended')
        if m.get('JobRestartCount') is not None:
            self.job_restart_count = m.get('JobRestartCount')
        if m.get('MessageContent') is not None:
            self.message_content = m.get('MessageContent')
        if m.get('MessageEvent') is not None:
            self.message_event = m.get('MessageEvent')
        if m.get('MessageVersion') is not None:
            self.message_version = m.get('MessageVersion')
        if m.get('RestartType') is not None:
            self.restart_type = m.get('RestartType')
        return self


class AliyunAccounts(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        employee_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.employee_id = employee_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.employee_id is not None:
            result['EmployeeId'] = self.employee_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('EmployeeId') is not None:
            self.employee_id = m.get('EmployeeId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        return self


class AssignNodeSpec(TeaModel):
    def __init__(
        self,
        anti_affinity_node_names: str = None,
        enable_assign_node: bool = None,
        node_names: str = None,
    ):
        self.anti_affinity_node_names = anti_affinity_node_names
        self.enable_assign_node = enable_assign_node
        self.node_names = node_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_affinity_node_names is not None:
            result['AntiAffinityNodeNames'] = self.anti_affinity_node_names
        if self.enable_assign_node is not None:
            result['EnableAssignNode'] = self.enable_assign_node
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiAffinityNodeNames') is not None:
            self.anti_affinity_node_names = m.get('AntiAffinityNodeNames')
        if m.get('EnableAssignNode') is not None:
            self.enable_assign_node = m.get('EnableAssignNode')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        return self


class AssumeUserInfo(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        id: str = None,
        security_token: str = None,
        type: str = None,
    ):
        self.access_key_id = access_key_id
        self.id = id
        self.security_token = security_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.id is not None:
            result['Id'] = self.id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CodeSourceItem(TeaModel):
    def __init__(
        self,
        code_branch: str = None,
        code_commit: str = None,
        code_repo: str = None,
        code_repo_access_token: str = None,
        code_repo_user_name: str = None,
        code_source_id: str = None,
        description: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        user_id: str = None,
    ):
        self.code_branch = code_branch
        self.code_commit = code_commit
        self.code_repo = code_repo
        self.code_repo_access_token = code_repo_access_token
        self.code_repo_user_name = code_repo_user_name
        self.code_source_id = code_source_id
        self.description = description
        self.display_name = display_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_branch is not None:
            result['CodeBranch'] = self.code_branch
        if self.code_commit is not None:
            result['CodeCommit'] = self.code_commit
        if self.code_repo is not None:
            result['CodeRepo'] = self.code_repo
        if self.code_repo_access_token is not None:
            result['CodeRepoAccessToken'] = self.code_repo_access_token
        if self.code_repo_user_name is not None:
            result['CodeRepoUserName'] = self.code_repo_user_name
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeBranch') is not None:
            self.code_branch = m.get('CodeBranch')
        if m.get('CodeCommit') is not None:
            self.code_commit = m.get('CodeCommit')
        if m.get('CodeRepo') is not None:
            self.code_repo = m.get('CodeRepo')
        if m.get('CodeRepoAccessToken') is not None:
            self.code_repo_access_token = m.get('CodeRepoAccessToken')
        if m.get('CodeRepoUserName') is not None:
            self.code_repo_user_name = m.get('CodeRepoUserName')
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class EnvVar(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ResourceRequirements(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        self.limits = limits
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['Limits'] = self.limits
        if self.requests is not None:
            result['Requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limits') is not None:
            self.limits = m.get('Limits')
        if m.get('Requests') is not None:
            self.requests = m.get('Requests')
        return self


class ContainerSpec(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        env: List[EnvVar] = None,
        image: str = None,
        name: str = None,
        resources: ResourceRequirements = None,
        working_dir: str = None,
    ):
        self.args = args
        self.command = command
        self.env = env
        self.image = image
        self.name = name
        self.resources = resources
        self.working_dir = working_dir

    def validate(self):
        if self.env:
            for k in self.env:
                if k:
                    k.validate()
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.command is not None:
            result['Command'] = self.command
        result['Env'] = []
        if self.env is not None:
            for k in self.env:
                result['Env'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        self.env = []
        if m.get('Env') is not None:
            for k in m.get('Env'):
                temp_model = EnvVar()
                self.env.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Resources') is not None:
            temp_model = ResourceRequirements()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CredentialRole(TeaModel):
    def __init__(
        self,
        assume_role_for: str = None,
        assume_user_info: AssumeUserInfo = None,
        policy: str = None,
        role_arn: str = None,
        role_type: str = None,
    ):
        self.assume_role_for = assume_role_for
        self.assume_user_info = assume_user_info
        self.policy = policy
        self.role_arn = role_arn
        self.role_type = role_type

    def validate(self):
        if self.assume_user_info:
            self.assume_user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        if self.assume_user_info is not None:
            result['AssumeUserInfo'] = self.assume_user_info.to_map()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        if m.get('AssumeUserInfo') is not None:
            temp_model = AssumeUserInfo()
            self.assume_user_info = temp_model.from_map(m['AssumeUserInfo'])
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class CredentialConfigItem(TeaModel):
    def __init__(
        self,
        key: str = None,
        roles: List[CredentialRole] = None,
        type: str = None,
    ):
        self.key = key
        self.roles = roles
        self.type = type

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = CredentialRole()
                self.roles.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CredentialConfig(TeaModel):
    def __init__(
        self,
        aliyun_env_role_key: str = None,
        credential_config_items: List[CredentialConfigItem] = None,
        enable_credential_inject: bool = None,
    ):
        self.aliyun_env_role_key = aliyun_env_role_key
        self.credential_config_items = credential_config_items
        self.enable_credential_inject = enable_credential_inject

    def validate(self):
        if self.credential_config_items:
            for k in self.credential_config_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_env_role_key is not None:
            result['AliyunEnvRoleKey'] = self.aliyun_env_role_key
        result['CredentialConfigItems'] = []
        if self.credential_config_items is not None:
            for k in self.credential_config_items:
                result['CredentialConfigItems'].append(k.to_map() if k else None)
        if self.enable_credential_inject is not None:
            result['EnableCredentialInject'] = self.enable_credential_inject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunEnvRoleKey') is not None:
            self.aliyun_env_role_key = m.get('AliyunEnvRoleKey')
        self.credential_config_items = []
        if m.get('CredentialConfigItems') is not None:
            for k in m.get('CredentialConfigItems'):
                temp_model = CredentialConfigItem()
                self.credential_config_items.append(temp_model.from_map(k))
        if m.get('EnableCredentialInject') is not None:
            self.enable_credential_inject = m.get('EnableCredentialInject')
        return self


class DataSourceItem(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_type: str = None,
        description: str = None,
        display_name: str = None,
        endpoint: str = None,
        file_system_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        mount_path: str = None,
        options: str = None,
        path: str = None,
        user_id: str = None,
    ):
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.description = description
        self.display_name = display_name
        self.endpoint = endpoint
        self.file_system_id = file_system_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.mount_path = mount_path
        self.options = options
        self.path = path
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.options is not None:
            result['Options'] = self.options
        if self.path is not None:
            result['Path'] = self.path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DebuggerConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        debugger_config_id: str = None,
        description: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
    ):
        self.content = content
        self.debugger_config_id = debugger_config_id
        self.description = description
        self.display_name = display_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.debugger_config_id is not None:
            result['DebuggerConfigId'] = self.debugger_config_id
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DebuggerConfigId') is not None:
            self.debugger_config_id = m.get('DebuggerConfigId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        return self


class DebuggerJob(TeaModel):
    def __init__(
        self,
        debugger_job_id: str = None,
        display_name: str = None,
        duration: str = None,
        gmt_create_time: str = None,
        gmt_failed_time: str = None,
        gmt_finish_time: str = None,
        gmt_running_time: str = None,
        gmt_stopped_time: str = None,
        gmt_submitted_time: str = None,
        gmt_succeed_time: str = None,
        status: str = None,
        user_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.debugger_job_id = debugger_job_id
        self.display_name = display_name
        self.duration = duration
        self.gmt_create_time = gmt_create_time
        self.gmt_failed_time = gmt_failed_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_running_time = gmt_running_time
        self.gmt_stopped_time = gmt_stopped_time
        self.gmt_submitted_time = gmt_submitted_time
        self.gmt_succeed_time = gmt_succeed_time
        self.status = status
        self.user_id = user_id
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_job_id is not None:
            result['DebuggerJobId'] = self.debugger_job_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
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
        if self.gmt_succeed_time is not None:
            result['GmtSucceedTime'] = self.gmt_succeed_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerJobId') is not None:
            self.debugger_job_id = m.get('DebuggerJobId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
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
        if m.get('GmtSucceedTime') is not None:
            self.gmt_succeed_time = m.get('GmtSucceedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class DebuggerJobIssue(TeaModel):
    def __init__(
        self,
        debugger_job_issue: str = None,
        gmt_create_time: str = None,
        job_debugger_issue_id: str = None,
        job_id: str = None,
        reason_code: str = None,
        reason_message: str = None,
        rule_name: str = None,
    ):
        self.debugger_job_issue = debugger_job_issue
        self.gmt_create_time = gmt_create_time
        self.job_debugger_issue_id = job_debugger_issue_id
        self.job_id = job_id
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_job_issue is not None:
            result['DebuggerJobIssue'] = self.debugger_job_issue
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.job_debugger_issue_id is not None:
            result['JobDebuggerIssueId'] = self.job_debugger_issue_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerJobIssue') is not None:
            self.debugger_job_issue = m.get('DebuggerJobIssue')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JobDebuggerIssueId') is not None:
            self.job_debugger_issue_id = m.get('JobDebuggerIssueId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DebuggerResult(TeaModel):
    def __init__(
        self,
        debugger_config_content: str = None,
        debugger_job_issues: str = None,
        debugger_job_status: str = None,
        debugger_report_url: str = None,
        job_display_name: str = None,
        job_id: str = None,
        job_user_id: str = None,
    ):
        self.debugger_config_content = debugger_config_content
        self.debugger_job_issues = debugger_job_issues
        self.debugger_job_status = debugger_job_status
        self.debugger_report_url = debugger_report_url
        self.job_display_name = job_display_name
        self.job_id = job_id
        self.job_user_id = job_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content
        if self.debugger_job_issues is not None:
            result['DebuggerJobIssues'] = self.debugger_job_issues
        if self.debugger_job_status is not None:
            result['DebuggerJobStatus'] = self.debugger_job_status
        if self.debugger_report_url is not None:
            result['DebuggerReportURL'] = self.debugger_report_url
        if self.job_display_name is not None:
            result['JobDisplayName'] = self.job_display_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_user_id is not None:
            result['JobUserId'] = self.job_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')
        if m.get('DebuggerJobIssues') is not None:
            self.debugger_job_issues = m.get('DebuggerJobIssues')
        if m.get('DebuggerJobStatus') is not None:
            self.debugger_job_status = m.get('DebuggerJobStatus')
        if m.get('DebuggerReportURL') is not None:
            self.debugger_report_url = m.get('DebuggerReportURL')
        if m.get('JobDisplayName') is not None:
            self.job_display_name = m.get('JobDisplayName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobUserId') is not None:
            self.job_user_id = m.get('JobUserId')
        return self


class EcsSpec(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        cpu: int = None,
        default_gpudriver: str = None,
        gpu: int = None,
        gpu_memory: int = None,
        gpu_type: str = None,
        instance_type: str = None,
        is_available: bool = None,
        memory: int = None,
        non_protect_spot_discount: float = None,
        payment_types: List[str] = None,
        resource_type: str = None,
        spot_stock_status: str = None,
        supported_gpudrivers: List[str] = None,
    ):
        self.accelerator_type = accelerator_type
        self.cpu = cpu
        self.default_gpudriver = default_gpudriver
        self.gpu = gpu
        self.gpu_memory = gpu_memory
        self.gpu_type = gpu_type
        self.instance_type = instance_type
        self.is_available = is_available
        self.memory = memory
        self.non_protect_spot_discount = non_protect_spot_discount
        self.payment_types = payment_types
        self.resource_type = resource_type
        self.spot_stock_status = spot_stock_status
        self.supported_gpudrivers = supported_gpudrivers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.default_gpudriver is not None:
            result['DefaultGPUDriver'] = self.default_gpudriver
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_available is not None:
            result['IsAvailable'] = self.is_available
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.non_protect_spot_discount is not None:
            result['NonProtectSpotDiscount'] = self.non_protect_spot_discount
        if self.payment_types is not None:
            result['PaymentTypes'] = self.payment_types
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spot_stock_status is not None:
            result['SpotStockStatus'] = self.spot_stock_status
        if self.supported_gpudrivers is not None:
            result['SupportedGPUDrivers'] = self.supported_gpudrivers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DefaultGPUDriver') is not None:
            self.default_gpudriver = m.get('DefaultGPUDriver')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NonProtectSpotDiscount') is not None:
            self.non_protect_spot_discount = m.get('NonProtectSpotDiscount')
        if m.get('PaymentTypes') is not None:
            self.payment_types = m.get('PaymentTypes')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SpotStockStatus') is not None:
            self.spot_stock_status = m.get('SpotStockStatus')
        if m.get('SupportedGPUDrivers') is not None:
            self.supported_gpudrivers = m.get('SupportedGPUDrivers')
        return self


class EventInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        pod_id: str = None,
        pod_uid: str = None,
        time: str = None,
    ):
        self.content = content
        self.id = id
        self.pod_id = pod_id
        self.pod_uid = pod_uid
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class LifecyclePostStartExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class LifecyclePostStart(TeaModel):
    def __init__(
        self,
        exec: LifecyclePostStartExec = None,
    ):
        self.exec = exec

    def validate(self):
        if self.exec:
            self.exec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = LifecyclePostStartExec()
            self.exec = temp_model.from_map(m['Exec'])
        return self


class LifecyclePreStopExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class LifecyclePreStop(TeaModel):
    def __init__(
        self,
        exec: LifecyclePreStopExec = None,
    ):
        self.exec = exec

    def validate(self):
        if self.exec:
            self.exec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = LifecyclePreStopExec()
            self.exec = temp_model.from_map(m['Exec'])
        return self


class Lifecycle(TeaModel):
    def __init__(
        self,
        post_start: LifecyclePostStart = None,
        pre_stop: LifecyclePreStop = None,
    ):
        self.post_start = post_start
        self.pre_stop = pre_stop

    def validate(self):
        if self.post_start:
            self.post_start.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_start is not None:
            result['PostStart'] = self.post_start.to_map()
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostStart') is not None:
            temp_model = LifecyclePostStart()
            self.post_start = temp_model.from_map(m['PostStart'])
        if m.get('PreStop') is not None:
            temp_model = LifecyclePreStop()
            self.pre_stop = temp_model.from_map(m['PreStop'])
        return self


class ExtraPodSpec(TeaModel):
    def __init__(
        self,
        init_containers: List[ContainerSpec] = None,
        lifecycle: Lifecycle = None,
        pod_annotations: Dict[str, str] = None,
        pod_labels: Dict[str, str] = None,
        shared_volume_mount_paths: List[str] = None,
        side_car_containers: List[ContainerSpec] = None,
    ):
        self.init_containers = init_containers
        self.lifecycle = lifecycle
        self.pod_annotations = pod_annotations
        self.pod_labels = pod_labels
        self.shared_volume_mount_paths = shared_volume_mount_paths
        self.side_car_containers = side_car_containers

    def validate(self):
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.lifecycle:
            self.lifecycle.validate()
        if self.side_car_containers:
            for k in self.side_car_containers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle.to_map()
        if self.pod_annotations is not None:
            result['PodAnnotations'] = self.pod_annotations
        if self.pod_labels is not None:
            result['PodLabels'] = self.pod_labels
        if self.shared_volume_mount_paths is not None:
            result['SharedVolumeMountPaths'] = self.shared_volume_mount_paths
        result['SideCarContainers'] = []
        if self.side_car_containers is not None:
            for k in self.side_car_containers:
                result['SideCarContainers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = ContainerSpec()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('Lifecycle') is not None:
            temp_model = Lifecycle()
            self.lifecycle = temp_model.from_map(m['Lifecycle'])
        if m.get('PodAnnotations') is not None:
            self.pod_annotations = m.get('PodAnnotations')
        if m.get('PodLabels') is not None:
            self.pod_labels = m.get('PodLabels')
        if m.get('SharedVolumeMountPaths') is not None:
            self.shared_volume_mount_paths = m.get('SharedVolumeMountPaths')
        self.side_car_containers = []
        if m.get('SideCarContainers') is not None:
            for k in m.get('SideCarContainers'):
                temp_model = ContainerSpec()
                self.side_car_containers.append(temp_model.from_map(k))
        return self


class FreeResourceClusterControlItem(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cross_clusters: bool = None,
        enable_free_resource: bool = None,
        free_resource_cluster_control_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cross_clusters = cross_clusters
        self.enable_free_resource = enable_free_resource
        self.free_resource_cluster_control_id = free_resource_cluster_control_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cross_clusters is not None:
            result['CrossClusters'] = self.cross_clusters
        if self.enable_free_resource is not None:
            result['EnableFreeResource'] = self.enable_free_resource
        if self.free_resource_cluster_control_id is not None:
            result['FreeResourceClusterControlId'] = self.free_resource_cluster_control_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CrossClusters') is not None:
            self.cross_clusters = m.get('CrossClusters')
        if m.get('EnableFreeResource') is not None:
            self.enable_free_resource = m.get('EnableFreeResource')
        if m.get('FreeResourceClusterControlId') is not None:
            self.free_resource_cluster_control_id = m.get('FreeResourceClusterControlId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        return self


class FreeResourceDetail(TeaModel):
    def __init__(
        self,
        amount: int = None,
        resource_type: str = None,
    ):
        self.amount = amount
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class FreeResourceItem(TeaModel):
    def __init__(
        self,
        available_number: int = None,
        cluster_id: str = None,
        cluster_name: str = None,
        free_resource_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        self.available_number = available_number
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.free_resource_id = free_resource_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.region_id = region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_number is not None:
            result['AvailableNumber'] = self.available_number
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.free_resource_id is not None:
            result['FreeResourceId'] = self.free_resource_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableNumber') is not None:
            self.available_number = m.get('AvailableNumber')
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('FreeResourceId') is not None:
            self.free_resource_id = m.get('FreeResourceId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GPUDetail(TeaModel):
    def __init__(
        self,
        gpu: str = None,
        gputype: str = None,
        gputype_full_name: str = None,
    ):
        self.gpu = gpu
        self.gputype = gputype
        self.gputype_full_name = gputype_full_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.gputype_full_name is not None:
            result['GPUTypeFullName'] = self.gputype_full_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('GPUTypeFullName') is not None:
            self.gputype_full_name = m.get('GPUTypeFullName')
        return self


class ImageConfig(TeaModel):
    def __init__(
        self,
        auth: str = None,
        docker_registry: str = None,
        password: str = None,
        username: str = None,
    ):
        self.auth = auth
        self.docker_registry = docker_registry
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.docker_registry is not None:
            result['DockerRegistry'] = self.docker_registry
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('DockerRegistry') is not None:
            self.docker_registry = m.get('DockerRegistry')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ImageItem(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        author_id: str = None,
        framework: str = None,
        image_provider_type: str = None,
        image_tag: str = None,
        image_url: str = None,
        image_url_vpc: str = None,
    ):
        self.accelerator_type = accelerator_type
        self.author_id = author_id
        self.framework = framework
        self.image_provider_type = image_provider_type
        self.image_tag = image_tag
        self.image_url = image_url
        self.image_url_vpc = image_url_vpc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.author_id is not None:
            result['AuthorId'] = self.author_id
        if self.framework is not None:
            result['Framework'] = self.framework
        if self.image_provider_type is not None:
            result['ImageProviderType'] = self.image_provider_type
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.image_url_vpc is not None:
            result['ImageUrlVpc'] = self.image_url_vpc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('AuthorId') is not None:
            self.author_id = m.get('AuthorId')
        if m.get('Framework') is not None:
            self.framework = m.get('Framework')
        if m.get('ImageProviderType') is not None:
            self.image_provider_type = m.get('ImageProviderType')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ImageUrlVpc') is not None:
            self.image_url_vpc = m.get('ImageUrlVpc')
        return self


class JobDebuggerConfig(TeaModel):
    def __init__(
        self,
        debugger_config_content: str = None,
        debugger_config_id: str = None,
        gmt_create_time: str = None,
        job_id: str = None,
    ):
        self.debugger_config_content = debugger_config_content
        self.debugger_config_id = debugger_config_id
        self.gmt_create_time = gmt_create_time
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content
        if self.debugger_config_id is not None:
            result['DebuggerConfigId'] = self.debugger_config_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')
        if m.get('DebuggerConfigId') is not None:
            self.debugger_config_id = m.get('DebuggerConfigId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class JobElasticSpec(TeaModel):
    def __init__(
        self,
        aimaster_docker_image: str = None,
        aimaster_type: str = None,
        edpmax_parallelism: int = None,
        edpmin_parallelism: int = None,
        elastic_strategy: str = None,
        enable_aimaster: bool = None,
        enable_edp: bool = None,
        enable_elastic_training: bool = None,
        enable_ps_job_elastic_ps: bool = None,
        enable_ps_job_elastic_worker: bool = None,
        enable_ps_resource_estimate: bool = None,
        max_parallelism: int = None,
        min_parallelism: int = None,
        psmax_parallelism: int = None,
        psmin_parallelism: int = None,
    ):
        self.aimaster_docker_image = aimaster_docker_image
        self.aimaster_type = aimaster_type
        self.edpmax_parallelism = edpmax_parallelism
        self.edpmin_parallelism = edpmin_parallelism
        self.elastic_strategy = elastic_strategy
        self.enable_aimaster = enable_aimaster
        self.enable_edp = enable_edp
        self.enable_elastic_training = enable_elastic_training
        self.enable_ps_job_elastic_ps = enable_ps_job_elastic_ps
        self.enable_ps_job_elastic_worker = enable_ps_job_elastic_worker
        self.enable_ps_resource_estimate = enable_ps_resource_estimate
        self.max_parallelism = max_parallelism
        self.min_parallelism = min_parallelism
        self.psmax_parallelism = psmax_parallelism
        self.psmin_parallelism = psmin_parallelism

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aimaster_docker_image is not None:
            result['AIMasterDockerImage'] = self.aimaster_docker_image
        if self.aimaster_type is not None:
            result['AIMasterType'] = self.aimaster_type
        if self.edpmax_parallelism is not None:
            result['EDPMaxParallelism'] = self.edpmax_parallelism
        if self.edpmin_parallelism is not None:
            result['EDPMinParallelism'] = self.edpmin_parallelism
        if self.elastic_strategy is not None:
            result['ElasticStrategy'] = self.elastic_strategy
        if self.enable_aimaster is not None:
            result['EnableAIMaster'] = self.enable_aimaster
        if self.enable_edp is not None:
            result['EnableEDP'] = self.enable_edp
        if self.enable_elastic_training is not None:
            result['EnableElasticTraining'] = self.enable_elastic_training
        if self.enable_ps_job_elastic_ps is not None:
            result['EnablePsJobElasticPS'] = self.enable_ps_job_elastic_ps
        if self.enable_ps_job_elastic_worker is not None:
            result['EnablePsJobElasticWorker'] = self.enable_ps_job_elastic_worker
        if self.enable_ps_resource_estimate is not None:
            result['EnablePsResourceEstimate'] = self.enable_ps_resource_estimate
        if self.max_parallelism is not None:
            result['MaxParallelism'] = self.max_parallelism
        if self.min_parallelism is not None:
            result['MinParallelism'] = self.min_parallelism
        if self.psmax_parallelism is not None:
            result['PSMaxParallelism'] = self.psmax_parallelism
        if self.psmin_parallelism is not None:
            result['PSMinParallelism'] = self.psmin_parallelism
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIMasterDockerImage') is not None:
            self.aimaster_docker_image = m.get('AIMasterDockerImage')
        if m.get('AIMasterType') is not None:
            self.aimaster_type = m.get('AIMasterType')
        if m.get('EDPMaxParallelism') is not None:
            self.edpmax_parallelism = m.get('EDPMaxParallelism')
        if m.get('EDPMinParallelism') is not None:
            self.edpmin_parallelism = m.get('EDPMinParallelism')
        if m.get('ElasticStrategy') is not None:
            self.elastic_strategy = m.get('ElasticStrategy')
        if m.get('EnableAIMaster') is not None:
            self.enable_aimaster = m.get('EnableAIMaster')
        if m.get('EnableEDP') is not None:
            self.enable_edp = m.get('EnableEDP')
        if m.get('EnableElasticTraining') is not None:
            self.enable_elastic_training = m.get('EnableElasticTraining')
        if m.get('EnablePsJobElasticPS') is not None:
            self.enable_ps_job_elastic_ps = m.get('EnablePsJobElasticPS')
        if m.get('EnablePsJobElasticWorker') is not None:
            self.enable_ps_job_elastic_worker = m.get('EnablePsJobElasticWorker')
        if m.get('EnablePsResourceEstimate') is not None:
            self.enable_ps_resource_estimate = m.get('EnablePsResourceEstimate')
        if m.get('MaxParallelism') is not None:
            self.max_parallelism = m.get('MaxParallelism')
        if m.get('MinParallelism') is not None:
            self.min_parallelism = m.get('MinParallelism')
        if m.get('PSMaxParallelism') is not None:
            self.psmax_parallelism = m.get('PSMaxParallelism')
        if m.get('PSMinParallelism') is not None:
            self.psmin_parallelism = m.get('PSMinParallelism')
        return self


class JobItemCodeSource(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class JobItemDataSources(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class JobItemUserVpc(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ResourceConfig(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.gputype = gputype
        self.memory = memory
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')
        return self


class SpotSpec(TeaModel):
    def __init__(
        self,
        spot_discount_limit: float = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
    ):
        self.spot_discount_limit = spot_discount_limit
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spot_discount_limit is not None:
            result['SpotDiscountLimit'] = self.spot_discount_limit
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpotDiscountLimit') is not None:
            self.spot_discount_limit = m.get('SpotDiscountLimit')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        return self


class JobSpec(TeaModel):
    def __init__(
        self,
        assign_node_spec: AssignNodeSpec = None,
        ecs_spec: str = None,
        extra_pod_spec: ExtraPodSpec = None,
        image: str = None,
        image_config: ImageConfig = None,
        pod_count: int = None,
        resource_config: ResourceConfig = None,
        spot_spec: SpotSpec = None,
        type: str = None,
        use_spot_instance: bool = None,
    ):
        self.assign_node_spec = assign_node_spec
        self.ecs_spec = ecs_spec
        self.extra_pod_spec = extra_pod_spec
        self.image = image
        self.image_config = image_config
        self.pod_count = pod_count
        self.resource_config = resource_config
        self.spot_spec = spot_spec
        self.type = type
        self.use_spot_instance = use_spot_instance

    def validate(self):
        if self.assign_node_spec:
            self.assign_node_spec.validate()
        if self.extra_pod_spec:
            self.extra_pod_spec.validate()
        if self.image_config:
            self.image_config.validate()
        if self.resource_config:
            self.resource_config.validate()
        if self.spot_spec:
            self.spot_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_node_spec is not None:
            result['AssignNodeSpec'] = self.assign_node_spec.to_map()
        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec
        if self.extra_pod_spec is not None:
            result['ExtraPodSpec'] = self.extra_pod_spec.to_map()
        if self.image is not None:
            result['Image'] = self.image
        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()
        if self.pod_count is not None:
            result['PodCount'] = self.pod_count
        if self.resource_config is not None:
            result['ResourceConfig'] = self.resource_config.to_map()
        if self.spot_spec is not None:
            result['SpotSpec'] = self.spot_spec.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.use_spot_instance is not None:
            result['UseSpotInstance'] = self.use_spot_instance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignNodeSpec') is not None:
            temp_model = AssignNodeSpec()
            self.assign_node_spec = temp_model.from_map(m['AssignNodeSpec'])
        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')
        if m.get('ExtraPodSpec') is not None:
            temp_model = ExtraPodSpec()
            self.extra_pod_spec = temp_model.from_map(m['ExtraPodSpec'])
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageConfig') is not None:
            temp_model = ImageConfig()
            self.image_config = temp_model.from_map(m['ImageConfig'])
        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')
        if m.get('ResourceConfig') is not None:
            temp_model = ResourceConfig()
            self.resource_config = temp_model.from_map(m['ResourceConfig'])
        if m.get('SpotSpec') is not None:
            temp_model = SpotSpec()
            self.spot_spec = temp_model.from_map(m['SpotSpec'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UseSpotInstance') is not None:
            self.use_spot_instance = m.get('UseSpotInstance')
        return self


class PodItem(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_start_time: str = None,
        history_pods: List['PodItem'] = None,
        ip: str = None,
        node_name: str = None,
        pod_id: str = None,
        pod_uid: str = None,
        status: str = None,
        sub_status: str = None,
        type: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_start_time = gmt_start_time
        self.history_pods = history_pods
        self.ip = ip
        self.node_name = node_name
        self.pod_id = pod_id
        self.pod_uid = pod_uid
        self.status = status
        self.sub_status = sub_status
        self.type = type

    def validate(self):
        if self.history_pods:
            for k in self.history_pods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        result['HistoryPods'] = []
        if self.history_pods is not None:
            for k in self.history_pods:
                result['HistoryPods'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        self.history_pods = []
        if m.get('HistoryPods') is not None:
            for k in m.get('HistoryPods'):
                temp_model = PodItem()
                self.history_pods.append(temp_model.from_map(k))
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class JobSettings(TeaModel):
    def __init__(
        self,
        advanced_settings: Dict[str, Any] = None,
        business_user_id: str = None,
        caller: str = None,
        disable_ecs_stock_check: bool = None,
        driver: str = None,
        enable_cpuaffinity: bool = None,
        enable_error_monitoring_in_aimaster: bool = None,
        enable_oss_append: bool = None,
        enable_rdma: bool = None,
        enable_sanity_check: bool = None,
        enable_tide_resource: bool = None,
        error_monitoring_args: str = None,
        job_reserved_minutes: int = None,
        job_reserved_policy: str = None,
        oversold_type: str = None,
        pipeline_id: str = None,
        sanity_check_args: str = None,
        tags: Dict[str, str] = None,
    ):
        self.advanced_settings = advanced_settings
        self.business_user_id = business_user_id
        self.caller = caller
        self.disable_ecs_stock_check = disable_ecs_stock_check
        self.driver = driver
        self.enable_cpuaffinity = enable_cpuaffinity
        self.enable_error_monitoring_in_aimaster = enable_error_monitoring_in_aimaster
        self.enable_oss_append = enable_oss_append
        self.enable_rdma = enable_rdma
        self.enable_sanity_check = enable_sanity_check
        self.enable_tide_resource = enable_tide_resource
        self.error_monitoring_args = error_monitoring_args
        self.job_reserved_minutes = job_reserved_minutes
        self.job_reserved_policy = job_reserved_policy
        self.oversold_type = oversold_type
        self.pipeline_id = pipeline_id
        self.sanity_check_args = sanity_check_args
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_settings is not None:
            result['AdvancedSettings'] = self.advanced_settings
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.disable_ecs_stock_check is not None:
            result['DisableEcsStockCheck'] = self.disable_ecs_stock_check
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.enable_cpuaffinity is not None:
            result['EnableCPUAffinity'] = self.enable_cpuaffinity
        if self.enable_error_monitoring_in_aimaster is not None:
            result['EnableErrorMonitoringInAIMaster'] = self.enable_error_monitoring_in_aimaster
        if self.enable_oss_append is not None:
            result['EnableOssAppend'] = self.enable_oss_append
        if self.enable_rdma is not None:
            result['EnableRDMA'] = self.enable_rdma
        if self.enable_sanity_check is not None:
            result['EnableSanityCheck'] = self.enable_sanity_check
        if self.enable_tide_resource is not None:
            result['EnableTideResource'] = self.enable_tide_resource
        if self.error_monitoring_args is not None:
            result['ErrorMonitoringArgs'] = self.error_monitoring_args
        if self.job_reserved_minutes is not None:
            result['JobReservedMinutes'] = self.job_reserved_minutes
        if self.job_reserved_policy is not None:
            result['JobReservedPolicy'] = self.job_reserved_policy
        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.sanity_check_args is not None:
            result['SanityCheckArgs'] = self.sanity_check_args
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedSettings') is not None:
            self.advanced_settings = m.get('AdvancedSettings')
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DisableEcsStockCheck') is not None:
            self.disable_ecs_stock_check = m.get('DisableEcsStockCheck')
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('EnableCPUAffinity') is not None:
            self.enable_cpuaffinity = m.get('EnableCPUAffinity')
        if m.get('EnableErrorMonitoringInAIMaster') is not None:
            self.enable_error_monitoring_in_aimaster = m.get('EnableErrorMonitoringInAIMaster')
        if m.get('EnableOssAppend') is not None:
            self.enable_oss_append = m.get('EnableOssAppend')
        if m.get('EnableRDMA') is not None:
            self.enable_rdma = m.get('EnableRDMA')
        if m.get('EnableSanityCheck') is not None:
            self.enable_sanity_check = m.get('EnableSanityCheck')
        if m.get('EnableTideResource') is not None:
            self.enable_tide_resource = m.get('EnableTideResource')
        if m.get('ErrorMonitoringArgs') is not None:
            self.error_monitoring_args = m.get('ErrorMonitoringArgs')
        if m.get('JobReservedMinutes') is not None:
            self.job_reserved_minutes = m.get('JobReservedMinutes')
        if m.get('JobReservedPolicy') is not None:
            self.job_reserved_policy = m.get('JobReservedPolicy')
        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('SanityCheckArgs') is not None:
            self.sanity_check_args = m.get('SanityCheckArgs')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class StatusTransitionItem(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        reason_code: str = None,
        reason_message: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class JobItem(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        cluster_id: str = None,
        code_source: JobItemCodeSource = None,
        credential_config: CredentialConfig = None,
        data_sources: List[JobItemDataSources] = None,
        display_name: str = None,
        duration: int = None,
        elastic_spec: JobElasticSpec = None,
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
        job_specs: List[JobSpec] = None,
        job_type: str = None,
        node_count: str = None,
        node_names: List[str] = None,
        pods: List[PodItem] = None,
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
        settings: JobSettings = None,
        status: str = None,
        status_history: List[StatusTransitionItem] = None,
        sub_status: str = None,
        system_envs: Dict[str, str] = None,
        tenant_id: str = None,
        thirdparty_lib_dir: str = None,
        thirdparty_libs: List[str] = None,
        use_oversold_resource: bool = None,
        user_command: str = None,
        user_id: str = None,
        user_script: str = None,
        user_vpc: JobItemUserVpc = None,
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
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.pods:
            for k in self.pods:
                if k:
                    k.validate()
        if self.settings:
            self.settings.validate()
        if self.status_history:
            for k in self.status_history:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
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
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_names is not None:
            result['NodeNames'] = self.node_names
        result['Pods'] = []
        if self.pods is not None:
            for k in self.pods:
                result['Pods'].append(k.to_map() if k else None)
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
            for k in self.status_history:
                result['StatusHistory'].append(k.to_map() if k else None)
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
            temp_model = JobItemCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = JobItemDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ElasticSpec') is not None:
            temp_model = JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m['ElasticSpec'])
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
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')
        self.pods = []
        if m.get('Pods') is not None:
            for k in m.get('Pods'):
                temp_model = PodItem()
                self.pods.append(temp_model.from_map(k))
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
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.status_history = []
        if m.get('StatusHistory') is not None:
            for k in m.get('StatusHistory'):
                temp_model = StatusTransitionItem()
                self.status_history.append(temp_model.from_map(k))
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
            temp_model = JobItemUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class LogInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        is_truncated: bool = None,
        pod_id: str = None,
        pod_uid: str = None,
        source: str = None,
        time: str = None,
    ):
        self.content = content
        self.id = id
        self.is_truncated = is_truncated
        self.pod_id = pod_id
        self.pod_uid = pod_uid
        self.source = source
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.source is not None:
            result['Source'] = self.source
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class Member(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        return self


class Metric(TeaModel):
    def __init__(
        self,
        time: int = None,
        value: float = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class NodeMetric(TeaModel):
    def __init__(
        self,
        metrics: List[Metric] = None,
        node_name: str = None,
    ):
        self.metrics = metrics
        self.node_name = node_name

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class PodMetric(TeaModel):
    def __init__(
        self,
        metrics: List[Metric] = None,
        pod_id: str = None,
    ):
        self.metrics = metrics
        self.pod_id = pod_id

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class QuotaConfig(TeaModel):
    def __init__(
        self,
        allowed_max_priority: int = None,
        enable_dlc: bool = None,
        enable_dsw: bool = None,
        enable_tide_resource: bool = None,
        resource_level: str = None,
    ):
        self.allowed_max_priority = allowed_max_priority
        self.enable_dlc = enable_dlc
        self.enable_dsw = enable_dsw
        self.enable_tide_resource = enable_tide_resource
        self.resource_level = resource_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_max_priority is not None:
            result['AllowedMaxPriority'] = self.allowed_max_priority
        if self.enable_dlc is not None:
            result['EnableDLC'] = self.enable_dlc
        if self.enable_dsw is not None:
            result['EnableDSW'] = self.enable_dsw
        if self.enable_tide_resource is not None:
            result['EnableTideResource'] = self.enable_tide_resource
        if self.resource_level is not None:
            result['ResourceLevel'] = self.resource_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedMaxPriority') is not None:
            self.allowed_max_priority = m.get('AllowedMaxPriority')
        if m.get('EnableDLC') is not None:
            self.enable_dlc = m.get('EnableDLC')
        if m.get('EnableDSW') is not None:
            self.enable_dsw = m.get('EnableDSW')
        if m.get('EnableTideResource') is not None:
            self.enable_tide_resource = m.get('EnableTideResource')
        if m.get('ResourceLevel') is not None:
            self.resource_level = m.get('ResourceLevel')
        return self


class QuotaDetail(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpudetails: List[GPUDetail] = None,
        gputype: str = None,
        gputype_full_name: str = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.gpudetails = gpudetails
        self.gputype = gputype
        self.gputype_full_name = gputype_full_name
        self.memory = memory

    def validate(self):
        if self.gpudetails:
            for k in self.gpudetails:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        result['GPUDetails'] = []
        if self.gpudetails is not None:
            for k in self.gpudetails:
                result['GPUDetails'].append(k.to_map() if k else None)
        if self.gputype is not None:
            result['GPUType'] = self.gputype
        if self.gputype_full_name is not None:
            result['GPUTypeFullName'] = self.gputype_full_name
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        self.gpudetails = []
        if m.get('GPUDetails') is not None:
            for k in m.get('GPUDetails'):
                temp_model = GPUDetail()
                self.gpudetails.append(temp_model.from_map(k))
        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')
        if m.get('GPUTypeFullName') is not None:
            self.gputype_full_name = m.get('GPUTypeFullName')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class Quota(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        quota_config: QuotaConfig = None,
        quota_id: str = None,
        quota_name: str = None,
        quota_type: str = None,
        total_quota: QuotaDetail = None,
        total_tide_quota: QuotaDetail = None,
        used_quota: QuotaDetail = None,
        used_tide_quota: QuotaDetail = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.quota_config = quota_config
        self.quota_id = quota_id
        self.quota_name = quota_name
        self.quota_type = quota_type
        self.total_quota = total_quota
        self.total_tide_quota = total_tide_quota
        self.used_quota = used_quota
        self.used_tide_quota = used_tide_quota

    def validate(self):
        if self.quota_config:
            self.quota_config.validate()
        if self.total_quota:
            self.total_quota.validate()
        if self.total_tide_quota:
            self.total_tide_quota.validate()
        if self.used_quota:
            self.used_quota.validate()
        if self.used_tide_quota:
            self.used_tide_quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota.to_map()
        if self.total_tide_quota is not None:
            result['TotalTideQuota'] = self.total_tide_quota.to_map()
        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()
        if self.used_tide_quota is not None:
            result['UsedTideQuota'] = self.used_tide_quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('QuotaConfig') is not None:
            temp_model = QuotaConfig()
            self.quota_config = temp_model.from_map(m['QuotaConfig'])
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('TotalQuota') is not None:
            temp_model = QuotaDetail()
            self.total_quota = temp_model.from_map(m['TotalQuota'])
        if m.get('TotalTideQuota') is not None:
            temp_model = QuotaDetail()
            self.total_tide_quota = temp_model.from_map(m['TotalTideQuota'])
        if m.get('UsedQuota') is not None:
            temp_model = QuotaDetail()
            self.used_quota = temp_model.from_map(m['UsedQuota'])
        if m.get('UsedTideQuota') is not None:
            temp_model = QuotaDetail()
            self.used_tide_quota = temp_model.from_map(m['UsedTideQuota'])
        return self


class Resources(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.gpu is not None:
            result['GPU'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class SanityCheckResultItem(TeaModel):
    def __init__(
        self,
        check_number: int = None,
        finished_at: str = None,
        message: str = None,
        phase: str = None,
        started_at: str = None,
        status: str = None,
    ):
        self.check_number = check_number
        self.finished_at = finished_at
        self.message = message
        self.phase = phase
        self.started_at = started_at
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_number is not None:
            result['CheckNumber'] = self.check_number
        if self.finished_at is not None:
            result['FinishedAt'] = self.finished_at
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.started_at is not None:
            result['StartedAt'] = self.started_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckNumber') is not None:
            self.check_number = m.get('CheckNumber')
        if m.get('FinishedAt') is not None:
            self.finished_at = m.get('FinishedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('StartedAt') is not None:
            self.started_at = m.get('StartedAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SeccompProfile(TeaModel):
    def __init__(
        self,
        localhost_profile: str = None,
        type: str = None,
    ):
        self.localhost_profile = localhost_profile
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.localhost_profile is not None:
            result['LocalhostProfile'] = self.localhost_profile
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalhostProfile') is not None:
            self.localhost_profile = m.get('LocalhostProfile')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SecurityContext(TeaModel):
    def __init__(
        self,
        run_as_group: int = None,
        run_as_user: int = None,
        seccomp_profile: SeccompProfile = None,
    ):
        self.run_as_group = run_as_group
        self.run_as_user = run_as_user
        self.seccomp_profile = seccomp_profile

    def validate(self):
        if self.seccomp_profile:
            self.seccomp_profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_as_group is not None:
            result['RunAsGroup'] = self.run_as_group
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        if self.seccomp_profile is not None:
            result['SeccompProfile'] = self.seccomp_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunAsGroup') is not None:
            self.run_as_group = m.get('RunAsGroup')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        if m.get('SeccompProfile') is not None:
            temp_model = SeccompProfile()
            self.seccomp_profile = temp_model.from_map(m['SeccompProfile'])
        return self


class SmartCache(TeaModel):
    def __init__(
        self,
        cache_worker_num: int = None,
        cache_worker_size: int = None,
        description: str = None,
        display_name: str = None,
        duration: str = None,
        endpoint: str = None,
        file_system_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        mount_path: str = None,
        options: str = None,
        path: str = None,
        smart_cache_id: str = None,
        status: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.cache_worker_num = cache_worker_num
        self.cache_worker_size = cache_worker_size
        self.description = description
        self.display_name = display_name
        self.duration = duration
        self.endpoint = endpoint
        self.file_system_id = file_system_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.mount_path = mount_path
        self.options = options
        self.path = path
        self.smart_cache_id = smart_cache_id
        self.status = status
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_worker_num is not None:
            result['CacheWorkerNum'] = self.cache_worker_num
        if self.cache_worker_size is not None:
            result['CacheWorkerSize'] = self.cache_worker_size
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.options is not None:
            result['Options'] = self.options
        if self.path is not None:
            result['Path'] = self.path
        if self.smart_cache_id is not None:
            result['SmartCacheId'] = self.smart_cache_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheWorkerNum') is not None:
            self.cache_worker_num = m.get('CacheWorkerNum')
        if m.get('CacheWorkerSize') is not None:
            self.cache_worker_size = m.get('CacheWorkerSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SmartCacheId') is not None:
            self.smart_cache_id = m.get('SmartCacheId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class TensorboardDataSourceSpec(TeaModel):
    def __init__(
        self,
        data_source_type: str = None,
        directory_name: str = None,
        full_summary_path: str = None,
        id: str = None,
        name: str = None,
        source_type: str = None,
        summary_path: str = None,
        uri: str = None,
    ):
        self.data_source_type = data_source_type
        self.directory_name = directory_name
        self.full_summary_path = full_summary_path
        self.id = id
        self.name = name
        self.source_type = source_type
        self.summary_path = summary_path
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.full_summary_path is not None:
            result['FullSummaryPath'] = self.full_summary_path
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('FullSummaryPath') is not None:
            self.full_summary_path = m.get('FullSummaryPath')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class TensorboardSpec(TeaModel):
    def __init__(
        self,
        ecs_type: str = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        self.ecs_type = ecs_type
        self.security_group_id = security_group_id
        self.switch_id = switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_type is not None:
            result['EcsType'] = self.ecs_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsType') is not None:
            self.ecs_type = m.get('EcsType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class Tensorboard(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        cpu: int = None,
        data_source_id: str = None,
        data_source_type: str = None,
        display_name: str = None,
        duration: str = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_modify_time: str = None,
        job_id: str = None,
        max_running_time_minutes: int = None,
        memory: int = None,
        options: str = None,
        priority: str = None,
        quota_id: str = None,
        quota_name: str = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        status: str = None,
        summary_path: str = None,
        summary_relative_path: str = None,
        tensorboard_data_sources: List[TensorboardDataSourceSpec] = None,
        tensorboard_id: str = None,
        tensorboard_spec: TensorboardSpec = None,
        tensorboard_url: str = None,
        token: str = None,
        user_id: str = None,
        username: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.cpu = cpu
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.display_name = display_name
        self.duration = duration
        self.gmt_create_time = gmt_create_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_modify_time = gmt_modify_time
        self.job_id = job_id
        self.max_running_time_minutes = max_running_time_minutes
        self.memory = memory
        self.options = options
        self.priority = priority
        self.quota_id = quota_id
        self.quota_name = quota_name
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.request_id = request_id
        self.status = status
        self.summary_path = summary_path
        self.summary_relative_path = summary_relative_path
        self.tensorboard_data_sources = tensorboard_data_sources
        self.tensorboard_id = tensorboard_id
        self.tensorboard_spec = tensorboard_spec
        self.tensorboard_url = tensorboard_url
        self.token = token
        self.user_id = user_id
        self.username = username
        self.workspace_id = workspace_id

    def validate(self):
        if self.tensorboard_data_sources:
            for k in self.tensorboard_data_sources:
                if k:
                    k.validate()
        if self.tensorboard_spec:
            self.tensorboard_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.options is not None:
            result['Options'] = self.options
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path
        if self.summary_relative_path is not None:
            result['SummaryRelativePath'] = self.summary_relative_path
        result['TensorboardDataSources'] = []
        if self.tensorboard_data_sources is not None:
            for k in self.tensorboard_data_sources:
                result['TensorboardDataSources'].append(k.to_map() if k else None)
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.tensorboard_spec is not None:
            result['TensorboardSpec'] = self.tensorboard_spec.to_map()
        if self.tensorboard_url is not None:
            result['TensorboardUrl'] = self.tensorboard_url
        if self.token is not None:
            result['Token'] = self.token
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')
        if m.get('SummaryRelativePath') is not None:
            self.summary_relative_path = m.get('SummaryRelativePath')
        self.tensorboard_data_sources = []
        if m.get('TensorboardDataSources') is not None:
            for k in m.get('TensorboardDataSources'):
                temp_model = TensorboardDataSourceSpec()
                self.tensorboard_data_sources.append(temp_model.from_map(k))
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('TensorboardSpec') is not None:
            temp_model = TensorboardSpec()
            self.tensorboard_spec = temp_model.from_map(m['TensorboardSpec'])
        if m.get('TensorboardUrl') is not None:
            self.tensorboard_url = m.get('TensorboardUrl')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class Workspace(TeaModel):
    def __init__(
        self,
        creator: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        members: List[Member] = None,
        quotas: List[Quota] = None,
        total_resources: Resources = None,
        workspace_admins: List[Member] = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.creator = creator
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.members = members
        self.quotas = quotas
        self.total_resources = total_resources
        self.workspace_admins = workspace_admins
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.workspace_admins:
            for k in self.workspace_admins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        result['WorkspaceAdmins'] = []
        if self.workspace_admins is not None:
            for k in self.workspace_admins:
                result['WorkspaceAdmins'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = Member()
                self.members.append(temp_model.from_map(k))
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = Quota()
                self.quotas.append(temp_model.from_map(k))
        if m.get('TotalResources') is not None:
            temp_model = Resources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        self.workspace_admins = []
        if m.get('WorkspaceAdmins') is not None:
            for k in m.get('WorkspaceAdmins'):
                temp_model = Member()
                self.workspace_admins.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class CreateJobRequestCodeSource(TeaModel):
    def __init__(
        self,
        branch: str = None,
        code_source_id: str = None,
        commit: str = None,
        mount_path: str = None,
    ):
        # The branch of the referenced code repository. By default, the branch configured in the code source is used. This parameter is optional.
        self.branch = branch
        # The ID of the code source.
        self.code_source_id = code_source_id
        # The commit ID of the code to be downloaded. By default, the commit ID configured in the code source is used. This parameter is optional.
        self.commit = commit
        # The path to which the job is mounted. By default, the mount path configured in the data source is used. This parameter is optional.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateJobRequestDataSources(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_version: str = None,
        mount_access: str = None,
        mount_path: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The data source ID.
        self.data_source_id = data_source_id
        self.data_source_version = data_source_version
        self.mount_access = mount_access
        # The path to which the job is mounted. By default, the mount path in the data source configuration is used. This parameter is optional.
        self.mount_path = mount_path
        # The mount attribute of the custom dataset. Set the value to OSS.
        self.options = options
        # The data source path.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_version is not None:
            result['DataSourceVersion'] = self.data_source_version
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.options is not None:
            result['Options'] = self.options
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceVersion') is not None:
            self.data_source_version = m.get('DataSourceVersion')
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateJobRequestUserVpc(TeaModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        # The default route. Default value: false. Valid values:
        # 
        # *   eth0: The default network interface is used to access the Internet through the public gateway.
        # *   eth1: The user\\"s Elastic Network Interface is used to access the Internet through the private gateway. For more information about the configuration method, see [Enable Internet access for a DSW instance by using a private Internet NAT gateway](https://help.aliyun.com/document_detail/2525343.html).
        self.default_route = default_route
        # The extended CIDR block.
        # 
        # *   If you leave the SwitchId and ExtendedCIDRs parameters empty, the system automatically obtains all CIDR blocks in a VPC.
        # *   If you configure the SwitchId and ExtendedCIDRs parameters, we recommend that you specify all CIDR blocks in a VPC.
        self.extended_cidrs = extended_cidrs
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The vSwitch ID. This parameter is optional.
        # 
        # *   If you leave this parameter empty, the system automatically selects a vSwitch based on the inventory status.
        # *   You can also specify a vSwitch ID.
        self.switch_id = switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route
        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs
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
        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        code_source: CreateJobRequestCodeSource = None,
        credential_config: CredentialConfig = None,
        data_sources: List[CreateJobRequestDataSources] = None,
        debugger_config_content: str = None,
        display_name: str = None,
        elastic_spec: JobElasticSpec = None,
        envs: Dict[str, str] = None,
        job_max_running_time_minutes: int = None,
        job_specs: List[JobSpec] = None,
        job_type: str = None,
        options: str = None,
        priority: int = None,
        resource_id: str = None,
        settings: JobSettings = None,
        success_policy: str = None,
        thirdparty_lib_dir: str = None,
        thirdparty_libs: List[str] = None,
        user_command: str = None,
        user_vpc: CreateJobRequestUserVpc = None,
        workspace_id: str = None,
    ):
        # The job visibility. Valid values:
        # 
        # *   PUBLIC: The job is visible to all members in the workspace.
        # *   PRIVATE: The job is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The code source of the job. Before the node of the job runs, DLC automatically downloads the configured code from the code source and mounts the code to the local path of the container.
        self.code_source = code_source
        # The access credential configuration.
        self.credential_config = credential_config
        # The data sources for job running.
        self.data_sources = data_sources
        # This parameter is not supported.
        self.debugger_config_content = debugger_config_content
        # The job name. The name must be in the following format:
        # 
        # *   The name must be 1 to 256 characters in length.
        # *   The name can contain digits, letters, underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.display_name = display_name
        # This parameter is not supported.
        self.elastic_spec = elastic_spec
        # The environment variables.
        self.envs = envs
        # The maximum running duration of the job. Unit: minutes.
        self.job_max_running_time_minutes = job_max_running_time_minutes
        # The configurations for job running, such as the image address, startup command, node resource declaration, and number of replicas.****\
        # 
        # A DLC job consists of different types of nodes. If nodes of the same type have exactly the same configuration, the configuration is called JobSpec. **JobSpecs** specifies the configurations of all types of nodes. The value is of the array type.
        # 
        # This parameter is required.
        self.job_specs = job_specs
        # The job type. The value is case-sensitive. The following job types are supported:
        # 
        # *   TFJob
        # *   PyTorchJob
        # *   MPIJob
        # *   XGBoostJob
        # *   OneFlowJob
        # *   ElasticBatchJob
        # *   SlurmJob
        # *   RayJob
        # 
        # Valid values for each job type:
        # 
        # *   OneFlowJob: OneFlow.
        # *   PyTorchJob: PyTorch.
        # *   SlurmJob: Slurm.
        # *   XGBoostJob: XGBoost.
        # *   ElasticBatchJob: ElasticBatch.
        # *   MPIJob: MPIJob.
        # *   TFJob: Tensorflow.
        # *   RayJob: Ray.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The additional configuration of the job. You can use this parameter to adjust the behavior of the attached data source. For example, if the attached data source of the job is of the OSS type, you can use this parameter to add the following configurations to override the default parameters of JindoFS: `fs.oss.download.thread.concurrency=4,fs.oss.download.queue.size=16`.
        self.options = options
        # The priority of the job. Default value: 1. Valid values: 1 to 9.
        # 
        # *   1: the lowest priority.
        # *   9: the highest priority.
        self.priority = priority
        # The ID of the resource group. This parameter is optional.
        # 
        # *   If you leave this parameter empty, the job is submitted to a public resource group.
        # *   If a resource quota is bound to the current workspace, you can specify the resource quota ID. For more information about how to query the resource quota ID, see [Manage resource quotas](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        # The additional parameter configurations of the job.
        self.settings = settings
        # The policy that is used to check whether a distributed multi-node job is successful. Only TensorFlow distributed multi-node jobs are supported.
        # 
        # *   ChiefWorker: If you use this policy, the job is considered successful when the pod on the chief node completes operations.
        # *   AllWorkers (default): If you use this policy, the job is considered successful when all worker nodes complete operations.
        self.success_policy = success_policy
        # The folder in which the third-party Python library file requirements.txt is stored. Before the startup command specified by the UserCommand parameter is run on each node, DLC fetches the requirements.txt file from the folder and runs `pip install -r` to install the required package and library.
        self.thirdparty_lib_dir = thirdparty_lib_dir
        # The third-party Python libraries to be installed.
        self.thirdparty_libs = thirdparty_libs
        # The startup command for all nodes of the job.
        # 
        # This parameter is required.
        self.user_command = user_command
        # The VPC settings.
        self.user_vpc = user_vpc
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.settings:
            self.settings.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.job_max_running_time_minutes is not None:
            result['JobMaxRunningTimeMinutes'] = self.job_max_running_time_minutes
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.options is not None:
            result['Options'] = self.options
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.success_policy is not None:
            result['SuccessPolicy'] = self.success_policy
        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir
        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs
        if self.user_command is not None:
            result['UserCommand'] = self.user_command
        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('CodeSource') is not None:
            temp_model = CreateJobRequestCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = CreateJobRequestDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ElasticSpec') is not None:
            temp_model = JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m['ElasticSpec'])
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('JobMaxRunningTimeMinutes') is not None:
            self.job_max_running_time_minutes = m.get('JobMaxRunningTimeMinutes')
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('SuccessPolicy') is not None:
            self.success_policy = m.get('SuccessPolicy')
        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')
        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')
        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')
        if m.get('UserVpc') is not None:
            temp_model = CreateJobRequestUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID used to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTensorboardRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        cpu: int = None,
        data_source_id: str = None,
        data_source_type: str = None,
        data_sources: List[DataSourceItem] = None,
        display_name: str = None,
        job_id: str = None,
        max_running_time_minutes: int = None,
        memory: int = None,
        options: str = None,
        priority: str = None,
        quota_id: str = None,
        source_id: str = None,
        source_type: str = None,
        summary_path: str = None,
        summary_relative_path: str = None,
        tensorboard_data_sources: List[TensorboardDataSourceSpec] = None,
        tensorboard_spec: TensorboardSpec = None,
        uri: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the job. Valid values:
        # 
        # *   PUBLIC: The configuration is public in the workspace.
        # *   PRIVATE: The configuration is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The number of vCPU cores.
        self.cpu = cpu
        # The dataset ID. 
        # <props="china">Call [ListDatasets](https://help.aliyun.com/document_detail/457222.html) to get the dataset ID.
        self.data_source_id = data_source_id
        # The dataset type. Valid values:
        # 
        # *   OSS
        # *   NAS
        self.data_source_type = data_source_type
        # The configurations of the data source.
        self.data_sources = data_sources
        # The TensorBoard name
        self.display_name = display_name
        # The job ID. Call [ListJobs](https://help.aliyun.com/document_detail/459676.html) to get the job ID.
        self.job_id = job_id
        # The maximum running duration. Unit: minutes.
        self.max_running_time_minutes = max_running_time_minutes
        # The memory size. Unit: GB.
        self.memory = memory
        # The extended fields of the dataset are in the JSON format. MountPath: the path to mount the dataset.
        self.options = options
        # The priority of the job. Default value: 1. Valid values: 1 to 9.
        # 
        # *   1 is the lowest priority.
        # *   9 is the highest priority.
        self.priority = priority
        # The resource quota ID. This parameter is required when you create a TensorBoard job by using a resource quota. <props="china">Call [ListQuotas](https://help.aliyun.com/document_detail/2628071.html) to get the quota ID. 
        # This feature is currently limited to whitelisted users. If you need to use this feature, contact us.
        self.quota_id = quota_id
        # The source ID.
        self.source_id = source_id
        # The source type.
        self.source_type = source_type
        # The directory of summary.
        self.summary_path = summary_path
        # The relative path of summary.
        self.summary_relative_path = summary_relative_path
        # The configurations of datasets mounted with the TensorBoard job.
        self.tensorboard_data_sources = tensorboard_data_sources
        # The pay-as-you-go configuration of TensorBoard, which is used to create TensorBoard jobs that use pay-as-you-go resources.
        self.tensorboard_spec = tensorboard_spec
        # The dataset URI.
        # 
        # *   Value format when DataSourceType is set to OSS: `oss://[oss-bucket].[endpoint]/[path]`.
        # *   Value format when DataSourceType is set to NAS:`nas://[nas-filesystem-id].[region]/[path]`.
        self.uri = uri
        # The workspace ID. 
        # <props="china">Call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.tensorboard_data_sources:
            for k in self.tensorboard_data_sources:
                if k:
                    k.validate()
        if self.tensorboard_spec:
            self.tensorboard_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.options is not None:
            result['Options'] = self.options
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path
        if self.summary_relative_path is not None:
            result['SummaryRelativePath'] = self.summary_relative_path
        result['TensorboardDataSources'] = []
        if self.tensorboard_data_sources is not None:
            for k in self.tensorboard_data_sources:
                result['TensorboardDataSources'].append(k.to_map() if k else None)
        if self.tensorboard_spec is not None:
            result['TensorboardSpec'] = self.tensorboard_spec.to_map()
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = DataSourceItem()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')
        if m.get('SummaryRelativePath') is not None:
            self.summary_relative_path = m.get('SummaryRelativePath')
        self.tensorboard_data_sources = []
        if m.get('TensorboardDataSources') is not None:
            for k in m.get('TensorboardDataSources'):
                temp_model = TensorboardDataSourceSpec()
                self.tensorboard_data_sources.append(temp_model.from_map(k))
        if m.get('TensorboardSpec') is not None:
            temp_model = TensorboardSpec()
            self.tensorboard_spec = temp_model.from_map(m['TensorboardSpec'])
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateTensorboardResponseBody(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        job_id: str = None,
        request_id: str = None,
        tensorboard_id: str = None,
    ):
        # The dataset ID.
        self.data_source_id = data_source_id
        # The job ID.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # TensorBoard ID
        self.tensorboard_id = tensorboard_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class CreateTensorboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTensorboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID. You can troubleshoot issues based on the request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTensorboardRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # The workspace ID. 
        # <props="china">For more information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteTensorboardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboard_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The TensorBoard ID.
        self.tensorboard_id = tensorboard_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class DeleteTensorboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTensorboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        need_detail: bool = None,
    ):
        # Specifies whether to return the job details. Default value: true.
        self.need_detail = need_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_detail is not None:
            result['NeedDetail'] = self.need_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedDetail') is not None:
            self.need_detail = m.get('NeedDetail')
        return self


class GetJobResponseBodyCodeSource(TeaModel):
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
        # The code commit ID
        self.commit = commit
        # The local mount path.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetJobResponseBodyDataSources(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        mount_path: str = None,
        uri: str = None,
    ):
        # The data source ID.
        self.data_source_id = data_source_id
        # The local mount path. This parameter is optional. The default value is empty, which specifies that the mount path in the data source is used.
        self.mount_path = mount_path
        # The data source URL.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetJobResponseBodyPodsHistoryPods(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_start_time: str = None,
        ip: str = None,
        pod_id: str = None,
        pod_uid: str = None,
        resource_type: str = None,
        status: str = None,
        sub_status: str = None,
        type: str = None,
    ):
        # The time when the node was created (UTC).
        self.gmt_create_time = gmt_create_time
        # The end time of the node (UTC).
        self.gmt_finish_time = gmt_finish_time
        # The start time of the node (UTC).
        self.gmt_start_time = gmt_start_time
        # The IP address of the node.
        self.ip = ip
        # The ID of the node.
        self.pod_id = pod_id
        # The UID of the node.
        self.pod_uid = pod_uid
        # The resource type of the node.
        self.resource_type = resource_type
        # The status of the node.
        self.status = status
        # The sub-status of the node, such as its preemption status. Valid values:
        # 
        # *   Normal
        # *   Evicted
        self.sub_status = sub_status
        # The type of the node.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
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
        return self


class GetJobResponseBodyPods(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_start_time: str = None,
        history_pods: List[GetJobResponseBodyPodsHistoryPods] = None,
        ip: str = None,
        pod_id: str = None,
        pod_uid: str = None,
        resource_type: str = None,
        status: str = None,
        sub_status: str = None,
        type: str = None,
    ):
        # The time when the node was created (UTC).
        self.gmt_create_time = gmt_create_time
        # The end time of the node (UTC).
        self.gmt_finish_time = gmt_finish_time
        # The start time of the node (UTC).
        self.gmt_start_time = gmt_start_time
        # The historical nodes.
        self.history_pods = history_pods
        # The IP address of the node.
        self.ip = ip
        # The node ID. It can be used in the GetPodLogs and GetPodEvents operations to obtain the detailed logs and events of the node.
        self.pod_id = pod_id
        # The UID of the node.
        self.pod_uid = pod_uid
        # The resource type of the node.
        self.resource_type = resource_type
        # The status of the node. Valid values:
        # 
        # *   Pending
        # *   Running
        # *   Succeeded
        # *   Failed
        # *   Unknown
        self.status = status
        # The sub-status of the node, such as its preemption status. Valid values:
        # 
        # *   Normal
        # *   Evicted
        self.sub_status = sub_status
        # The node type, which corresponds to a specific JobSpec in JobSpecs of the CreateJob operation.
        self.type = type

    def validate(self):
        if self.history_pods:
            for k in self.history_pods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        result['HistoryPods'] = []
        if self.history_pods is not None:
            for k in self.history_pods:
                result['HistoryPods'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        self.history_pods = []
        if m.get('HistoryPods') is not None:
            for k in m.get('HistoryPods'):
                temp_model = GetJobResponseBodyPodsHistoryPods()
                self.history_pods.append(temp_model.from_map(k))
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
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
        return self


class GetJobResponseBodyUserVpc(TeaModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        # The default router. This parameter is valid only for general-purpose computing resources. Valid values:
        # 
        # eth0: The default network interface is used to access the Internet through the public gateway. eth1: The user\\"s Elastic Network Interface is used to access the Internet through the private gateway.
        self.default_route = default_route
        # The extended CIDR block. Example: 192.168.0.1/24.
        self.extended_cidrs = extended_cidrs
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.switch_id = switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        cluster_id: str = None,
        code_source: GetJobResponseBodyCodeSource = None,
        credential_config: CredentialConfig = None,
        data_sources: List[GetJobResponseBodyDataSources] = None,
        display_name: str = None,
        duration: int = None,
        elastic_spec: JobElasticSpec = None,
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
        job_specs: List[JobSpec] = None,
        job_type: str = None,
        pods: List[GetJobResponseBodyPods] = None,
        priority: int = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_level: str = None,
        resource_type: str = None,
        restart_times: str = None,
        settings: JobSettings = None,
        status: str = None,
        status_history: List[StatusTransitionItem] = None,
        sub_status: str = None,
        tenant_id: str = None,
        thirdparty_lib_dir: str = None,
        thirdparty_libs: List[str] = None,
        user_command: str = None,
        user_id: str = None,
        user_vpc: GetJobResponseBodyUserVpc = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The visibility of the job. Valid values:
        # 
        # *   PUBLIC: The code is public in the workspace.
        # *   PRIVATE: The workspace is visible only to you and the administrator of the workspace. This is the default value.
        self.accessibility = accessibility
        # The cluster ID.
        self.cluster_id = cluster_id
        # The code source.
        self.code_source = code_source
        # The access credential configurations.
        self.credential_config = credential_config
        # The data sources.
        self.data_sources = data_sources
        # The job name.
        self.display_name = display_name
        # The duration of the job (seconds).
        self.duration = duration
        # The elastic job parameters.
        self.elastic_spec = elastic_spec
        # Specifies whether to enable the debugger job.
        self.enabled_debugger = enabled_debugger
        # The configurations of environment variables.
        self.envs = envs
        # The time when the job was created (UTC).
        self.gmt_create_time = gmt_create_time
        # The time of the job failed (UTC).
        self.gmt_failed_time = gmt_failed_time
        # The time when the job ended (UTC).
        self.gmt_finish_time = gmt_finish_time
        # The start time of the job (UTC).
        self.gmt_running_time = gmt_running_time
        # The time when the job stopped (UTC).
        self.gmt_stopped_time = gmt_stopped_time
        # The time when the job was submitted to the cluster (UTC).
        self.gmt_submitted_time = gmt_submitted_time
        # The time when the job succeeded (UTC).
        self.gmt_successed_time = gmt_successed_time
        # The job ID.
        self.job_id = job_id
        # The node configurations of the job, which is **JobSpecs** in the CreateJob operation.
        self.job_specs = job_specs
        # The job type. Specified by the JobType parameter of the [CreateJob](https://help.aliyun.com/document_detail/459672.html) operation.
        self.job_type = job_type
        # All running nodes of the job.
        self.pods = pods
        # The priority of the job. Valid values: 1 to 9.
        self.priority = priority
        # The status detail code, which is a sub-status under the current status.
        self.reason_code = reason_code
        # The description of the status detail code.
        self.reason_message = reason_message
        # The request ID, which can be used for troubleshooting.
        self.request_id = request_id
        # The ID of the resource group to which the job belongs.
        self.resource_id = resource_id
        # The resource level that the job uses.
        self.resource_level = resource_level
        # The resource type. Valid values: ECS, Lingjun, and ACS.
        self.resource_type = resource_type
        # The number of retries and the maximum number of retries used by the job.
        self.restart_times = restart_times
        # The settings of the additional parameters of the job.
        self.settings = settings
        # The status of the job. Valid values:
        # 
        # *   Creating
        # *   Queuing
        # *   Bidding (Only for Lingjun preemptible jobs)
        # *   EnvPreparing
        # *   SanityChecking
        # *   Running
        # *   Restarting
        # *   Stopping
        # *   SucceededReserving
        # *   FailedReserving
        # *   Succeeded
        # *   Failed
        # *   Stopped
        self.status = status
        # The status history.
        self.status_history = status_history
        # The sub-status of the job, such as its preemption status.
        self.sub_status = sub_status
        # The tenant ID.
        self.tenant_id = tenant_id
        # The directory that contains requirements.txt.
        self.thirdparty_lib_dir = thirdparty_lib_dir
        # The third-party Python libraries to be installed.
        self.thirdparty_libs = thirdparty_libs
        # The command that is run to start each node.
        self.user_command = user_command
        # The UID of the Alibaba Cloud account who submitted the job.
        self.user_id = user_id
        # The VPC of the user.
        self.user_vpc = user_vpc
        # The ID of the workspace to which the job belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the job belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()
        if self.job_specs:
            for k in self.job_specs:
                if k:
                    k.validate()
        if self.pods:
            for k in self.pods:
                if k:
                    k.validate()
        if self.settings:
            self.settings.validate()
        if self.status_history:
            for k in self.status_history:
                if k:
                    k.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
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
        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k in self.job_specs:
                result['JobSpecs'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['JobType'] = self.job_type
        result['Pods'] = []
        if self.pods is not None:
            for k in self.pods:
                result['Pods'].append(k.to_map() if k else None)
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
        if self.restart_times is not None:
            result['RestartTimes'] = self.restart_times
        if self.settings is not None:
            result['Settings'] = self.settings.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['StatusHistory'] = []
        if self.status_history is not None:
            for k in self.status_history:
                result['StatusHistory'].append(k.to_map() if k else None)
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CodeSource') is not None:
            temp_model = GetJobResponseBodyCodeSource()
            self.code_source = temp_model.from_map(m['CodeSource'])
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = GetJobResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ElasticSpec') is not None:
            temp_model = JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m['ElasticSpec'])
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
        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k in m.get('JobSpecs'):
                temp_model = JobSpec()
                self.job_specs.append(temp_model.from_map(k))
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        self.pods = []
        if m.get('Pods') is not None:
            for k in m.get('Pods'):
                temp_model = GetJobResponseBodyPods()
                self.pods.append(temp_model.from_map(k))
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
        if m.get('RestartTimes') is not None:
            self.restart_times = m.get('RestartTimes')
        if m.get('Settings') is not None:
            temp_model = JobSettings()
            self.settings = temp_model.from_map(m['Settings'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.status_history = []
        if m.get('StatusHistory') is not None:
            for k in m.get('StatusHistory'):
                temp_model = StatusTransitionItem()
                self.status_history.append(temp_model.from_map(k))
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
            temp_model = GetJobResponseBodyUserVpc()
            self.user_vpc = temp_model.from_map(m['UserVpc'])
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_events_num: int = None,
        start_time: str = None,
    ):
        # The end time (UTC) of the time range for querying events. The default value is the current time.
        self.end_time = end_time
        # The maximum number of events that can be returned. Default value: 2000.
        self.max_events_num = max_events_num
        # The start time (UTC) of the time range for querying events. The default value is 7 days ago.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetJobEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[str] = None,
        job_id: str = None,
        request_id: str = None,
    ):
        # The events.
        self.events = events
        # The job ID.
        self.job_id = job_id
        # The request ID, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['Events'] = self.events
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobMetricsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        metric_type: str = None,
        start_time: str = None,
        time_step: str = None,
        token: str = None,
    ):
        # The end time of the time range to query monitoring data. The time is displayed in UTC. The default value is the current time.
        self.end_time = end_time
        # The type of the monitoring metrics. Valid values:
        # 
        # *   GpuCoreUsage: GPU utilization
        # *   GpuMemoryUsage: GPU memory utilization
        # *   CpuCoreUsage: CPU utilization
        # *   MemoryUsage: memory utilization
        # *   NetworkInputRate: the network write in rate.
        # *   NetworkOutputRate: the network write out rate
        # *   DiskReadRate: the disk read rate
        # *   DiskWriteRate: the disk write rate
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The beginning of the time range to query monitoring data. The time is displayed in UTC. The default value is the time 1 hour before the current time.
        self.start_time = start_time
        # The interval at which monitoring data is returned. Default value: 5. Unit: minutes.
        self.time_step = time_step
        # The temporary token used for authentication.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetJobMetricsResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        pod_metrics: List[PodMetric] = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The monitoring metrics of the job.
        self.pod_metrics = pod_metrics
        # The request ID. You can troubleshoot issues based on the request ID.
        self.request_id = request_id

    def validate(self):
        if self.pod_metrics:
            for k in self.pod_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['PodMetrics'] = []
        if self.pod_metrics is not None:
            for k in self.pod_metrics:
                result['PodMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.pod_metrics = []
        if m.get('PodMetrics') is not None:
            for k in m.get('PodMetrics'):
                temp_model = PodMetric()
                self.pod_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobSanityCheckResultRequest(TeaModel):
    def __init__(
        self,
        sanity_check_number: int = None,
        sanity_check_phase: str = None,
        token: str = None,
    ):
        # The nth time for which the job sanity check is performed.
        # 
        # This parameter is required.
        self.sanity_check_number = sanity_check_number
        # The phase in which the job sanity check is performed.
        # 
        # *   CheckInit
        # *   DeviceCheck
        # *   SingleNodeCommCheck
        # *   TwoNodeCommCheck
        # *   AllNodeCommCheck
        self.sanity_check_phase = sanity_check_phase
        # The token information for job sharing. For more information about how to obtain the token information, see [GetToken](https://help.aliyun.com/document_detail/2557812.html).
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sanity_check_number is not None:
            result['SanityCheckNumber'] = self.sanity_check_number
        if self.sanity_check_phase is not None:
            result['SanityCheckPhase'] = self.sanity_check_phase
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SanityCheckNumber') is not None:
            self.sanity_check_number = m.get('SanityCheckNumber')
        if m.get('SanityCheckPhase') is not None:
            self.sanity_check_phase = m.get('SanityCheckPhase')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetJobSanityCheckResultResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        sanity_check_result: List[SanityCheckResultItem] = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id
        # The job sanity check result.
        self.sanity_check_result = sanity_check_result

    def validate(self):
        if self.sanity_check_result:
            for k in self.sanity_check_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        result['SanityCheckResult'] = []
        if self.sanity_check_result is not None:
            for k in self.sanity_check_result:
                result['SanityCheckResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        self.sanity_check_result = []
        if m.get('SanityCheckResult') is not None:
            for k in m.get('SanityCheckResult'):
                temp_model = SanityCheckResultItem()
                self.sanity_check_result.append(temp_model.from_map(k))
        return self


class GetJobSanityCheckResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobSanityCheckResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobSanityCheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPodEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_events_num: int = None,
        pod_uid: str = None,
        start_time: str = None,
    ):
        # The end time (UTC).
        self.end_time = end_time
        # The maximum number of events that can be returned.
        self.max_events_num = max_events_num
        # The node UID. Call [GetJob](https://help.aliyun.com/document_detail/459677.html) to get the node UID.
        self.pod_uid = pod_uid
        # The start time (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetPodEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[str] = None,
        job_id: str = None,
        pod_id: str = None,
        pod_uid: str = None,
        request_id: str = None,
    ):
        # The events returned.
        self.events = events
        # The job ID.
        self.job_id = job_id
        # The node ID.
        # 
        # This parameter is required.
        self.pod_id = pod_id
        # The node UID.
        self.pod_uid = pod_uid
        # The request ID, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['Events'] = self.events
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPodEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPodEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPodEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPodLogsRequest(TeaModel):
    def __init__(
        self,
        download_to_file: bool = None,
        end_time: str = None,
        max_lines: int = None,
        pod_uid: str = None,
        start_time: str = None,
    ):
        # Specifies whether to download the log file. Default value: false. Valid values:
        # 
        # *   false
        # *   true
        self.download_to_file = download_to_file
        # The end time of the query. Default value: current time.
        self.end_time = end_time
        # The maximum number of log entries. Default value: 2000.
        self.max_lines = max_lines
        # The node UID. For more information about how to obtain a node UID, see [GetJob](https://help.aliyun.com/document_detail/459677.html).
        self.pod_uid = pod_uid
        # The start time of the query. Default value: 7 days ago.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_to_file is not None:
            result['DownloadToFile'] = self.download_to_file
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_lines is not None:
            result['MaxLines'] = self.max_lines
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadToFile') is not None:
            self.download_to_file = m.get('DownloadToFile')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxLines') is not None:
            self.max_lines = m.get('MaxLines')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetPodLogsResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        logs: List[str] = None,
        pod_id: str = None,
        pod_uid: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The logs.
        self.logs = logs
        # The node ID.
        self.pod_id = pod_id
        # The instance UID.
        self.pod_uid = pod_uid
        # The request ID which is used for diagnostics and Q\\&A.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPodLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPodLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPodLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRayDashboardRequest(TeaModel):
    def __init__(
        self,
        is_shared: bool = None,
        token: str = None,
    ):
        # Specifies whether the link is a sharing link. If yes, a token is required.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.is_shared = is_shared
        # The token obtained from GetToken
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_shared is not None:
            result['isShared'] = self.is_shared
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isShared') is not None:
            self.is_shared = m.get('isShared')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetRayDashboardResponseBody(TeaModel):
    def __init__(
        self,
        metrics_enabled: str = None,
        url: str = None,
    ):
        # Indicates whether the dashboard has been integrated with CloudMonitor and supports ray metrics
        self.metrics_enabled = metrics_enabled
        # The Ray Dashboard URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metrics_enabled is not None:
            result['metricsEnabled'] = self.metrics_enabled
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricsEnabled') is not None:
            self.metrics_enabled = m.get('metricsEnabled')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetRayDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRayDashboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRayDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTensorboardRequest(TeaModel):
    def __init__(
        self,
        jod_id: str = None,
        token: str = None,
        workspace_id: str = None,
    ):
        # The job ID. For more information about how to query the job ID, see [ListJob](https://help.aliyun.com/document_detail/459676.html).
        self.jod_id = jod_id
        # The information about the shared token. You can specify this parameter to obtain the permission to view a TensorBoard job based on the shared token information. You can execute [GetTensorboardSharedUrl](https://help.aliyun.com/document_detail/2557813.html) and extract the shared token from the obtained information.
        self.token = token
        # The workspace ID. 
        # <props="china">For more information about how to query the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jod_id is not None:
            result['JodId'] = self.jod_id
        if self.token is not None:
            result['Token'] = self.token
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JodId') is not None:
            self.jod_id = m.get('JodId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetTensorboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Tensorboard = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Tensorboard()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTensorboardSharedUrlRequest(TeaModel):
    def __init__(
        self,
        expire_time_seconds: str = None,
    ):
        # The validity period of the shareable link. Unit: seconds. Maximum value: 604800.
        self.expire_time_seconds = expire_time_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time_seconds is not None:
            result['ExpireTimeSeconds'] = self.expire_time_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTimeSeconds') is not None:
            self.expire_time_seconds = m.get('ExpireTimeSeconds')
        return self


class GetTensorboardSharedUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboard_shared_url: str = None,
    ):
        # The request ID which is used for troubleshooting.
        self.request_id = request_id
        # The shareable link of the TensorBoard task.
        self.tensorboard_shared_url = tensorboard_shared_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_shared_url is not None:
            result['TensorboardSharedUrl'] = self.tensorboard_shared_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardSharedUrl') is not None:
            self.tensorboard_shared_url = m.get('TensorboardSharedUrl')
        return self


class GetTensorboardSharedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTensorboardSharedUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTensorboardSharedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The time when the share link expires. Default value: 604800. Minimum value: 0. Unit: seconds.
        self.expire_time = expire_time
        # The ID of the job to be shared.
        self.target_id = target_id
        # The type of the job that you want to share. Valid values: job and tensorboard.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
    ):
        # The request ID, which is used to troubleshoot issues.
        self.request_id = request_id
        # The sharing token, used to view the information about the shared job.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebTerminalRequest(TeaModel):
    def __init__(
        self,
        is_shared: bool = None,
        pod_uid: str = None,
    ):
        # Specifies whether to create a shareable link to access the container. Valid values:
        # 
        # *   true: returns a shareable link to access the container. The link will expire after 30 seconds and can only be used once. After you access the container by using the link, other requests that use this link to access the container become invalid.
        # *   false: returns a common shareable link to access the container. If you use a common shareable link to access a container, Alibaba Cloud identity authentication is required. The link will expire after 30 seconds.
        self.is_shared = is_shared
        # The pod UID.
        self.pod_uid = pod_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared
        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')
        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')
        return self


class GetWebTerminalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        web_terminal_url: str = None,
    ):
        # The request ID which is used for diagnostics and Q\\&A.
        self.request_id = request_id
        # The WebSocket URI for accessing the container. You must build a WebSocket client. For more information about the communication format, see the following code:
        # 
        #     ws = new WebSocket(
        #       `wss://xxxxx`,
        #     );
        #     ws.onopen = function open() {
        #       console.warn(\\"connected\\");
        #       term.write(\\"\\r\\");
        #     };
        # 
        #     ws.onclose = function close() {
        #       console.warn(\\"disconnected\\");
        #       term.write(\\"Connection closed\\");
        #     };
        # 
        #     // Return the following information in the backend.
        #     ws.onmessage = function incoming(event) {
        #       const msg = JSON.parse(event.data);
        #       console.warn(msg);
        #       if (msg.operation === \\"stdout\\") {
        #         term.write(msg.data);
        #       } else {
        #         console.warn(\\"invalid msg operation: \\" + msg);
        #       }
        #     };
        # 
        #     // Enter the following code in the console.
        #     term.onData(data => {
        #       const msg = { operation: \\"stdin\\", data: data };
        #       ws.send(JSON.stringify(msg));
        #     });
        # 
        #     term.onResize(size => {
        #       const msg = { operation: \\"resize\\", cols: size.cols, rows: size.rows };
        #       ws.send(JSON.stringify(msg));
        #     });
        # 
        #     fitAddon.fit();
        #     };
        self.web_terminal_url = web_terminal_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.web_terminal_url is not None:
            result['WebTerminalUrl'] = self.web_terminal_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebTerminalUrl') is not None:
            self.web_terminal_url = m.get('WebTerminalUrl')
        return self


class GetWebTerminalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebTerminalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWebTerminalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsSpecsRequest(TeaModel):
    def __init__(
        self,
        accelerator_type: str = None,
        instance_types: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_type: str = None,
        sort_by: str = None,
    ):
        # Filter by accelerator type. Valid values:
        # 
        # *   CPU
        # *   GPU
        self.accelerator_type = accelerator_type
        # The instance types to query. Separate the types with commas (,).
        self.instance_types = instance_types
        # The sorting order. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.order = order
        # The number of the page to query. The start value is 1.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The type of the resource. Valid values:
        # 
        # *   ECS
        # *   Lingjun
        self.resource_type = resource_type
        # The field based on which the results are sorted. Valid values:
        # 
        # *   CPU
        # *   GPU
        # *   Memory
        # *   GmtCreateTime
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListEcsSpecsResponseBody(TeaModel):
    def __init__(
        self,
        ecs_specs: List[EcsSpec] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of ECS specifications.
        self.ecs_specs = ecs_specs
        # The request ID.
        self.request_id = request_id
        # The number of types that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.ecs_specs:
            for k in self.ecs_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k in self.ecs_specs:
                result['EcsSpecs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k in m.get('EcsSpecs'):
                temp_model = EcsSpec()
                self.ecs_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEcsSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEcsSpecsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEcsSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobSanityCheckResultsRequest(TeaModel):
    def __init__(
        self,
        order: str = None,
    ):
        # The sorting order:
        # 
        # *   desc: descending order
        # *   asc: ascending order
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListJobSanityCheckResultsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sanity_check_results: List[List[SanityCheckResultItem]] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The sanity check results.
        self.sanity_check_results = sanity_check_results
        # The total number of results that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.sanity_check_results:
            for k in self.sanity_check_results:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        result['SanityCheckResults'] = []
        if self.sanity_check_results is not None:
            for k in self.sanity_check_results:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['SanityCheckResults'].append(l1)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        self.sanity_check_results = []
        if m.get('SanityCheckResults') is not None:
            for k in m.get('SanityCheckResults'):
                l1 = []
                for k1 in k:
                    temp_model = SanityCheckResultItem()
                    l1.append(temp_model.from_map(k1))
                self.sanity_check_results.append(l1)
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobSanityCheckResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobSanityCheckResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobSanityCheckResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        business_user_id: str = None,
        caller: str = None,
        display_name: str = None,
        end_time: str = None,
        from_all_workspaces: bool = None,
        job_id: str = None,
        job_ids: str = None,
        job_type: str = None,
        order: str = None,
        oversold_info: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        pipeline_id: str = None,
        resource_id: str = None,
        resource_quota_name: str = None,
        show_own: bool = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, str] = None,
        user_id_for_filter: str = None,
        username: str = None,
        workspace_id: str = None,
    ):
        # The job visibility. Valid values:
        # 
        # *   PUBLIC: The job is visible to all members in the workspace.
        # *   PRIVATE: The job is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The ID of the user associated with the job.
        self.business_user_id = business_user_id
        # The caller.
        self.caller = caller
        # The job name. Fuzzy query is supported. The name is case-insensitive. Wildcards are not supported. For example, if you enter test, test-job1, job-test, job-test2, or job-test can be matched, and job-t1 cannot be matched. The default value null indicates any job name.
        self.display_name = display_name
        # The end time of the query. Use the job creation time to filter data. The default value is the current time.
        self.end_time = end_time
        # Specifies whether to query a list of jobs across workspaces. This parameter must be used together with `ShowOwn=true`. You can use this parameter to query a list of jobs recently submitted by the current user.
        self.from_all_workspaces = from_all_workspaces
        # The job ID. Fuzzy query is supported. The name is case-insensitive. Wildcards are not supported. The default value null indicates any job ID.
        self.job_id = job_id
        self.job_ids = job_ids
        # The job type. The default value null indicates any type. Valid values:
        # 
        # *   TFJob
        # *   PyTorchJob
        # *   XGBoostJob
        # *   OneFlowJob
        # *   ElasticBatchJob
        self.job_type = job_type
        # The sorting order. Valid values:
        # 
        # *   desc (default)
        # *   asc
        self.order = order
        # The Idle resource information. Valid values:
        # 
        # *   ForbiddenQuotaOverSold
        # *   ForceQuotaOverSold
        # *   AcceptQuotaOverSold-true (true indicates that the job uses idle resources.)
        # *   AcceptQuotaOverSold-false (false indicates that the job uses guaranteed resources.)
        self.oversold_info = oversold_info
        # The number of the page to return for the current query. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of jobs per page.
        self.page_size = page_size
        # The type of the resource. Valid values:
        # 
        # *   PrePaid: Resource quota
        # *   Spot: Preemptible resources
        # *   PostPaid: Public resources
        self.payment_type = payment_type
        # The specific pipeline ID used to filter jobs.
        self.pipeline_id = pipeline_id
        # The resource group ID. For information about how to obtain the ID of a dedicated resource group, see [Manage resource quota](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        # The resource quota name used to filter jobs. Fuzzy search is supported. Wildcards are not supported. The default value null indicates that jobs are not filtered by resource quota name.
        self.resource_quota_name = resource_quota_name
        # Specifies whether to query only the jobs submitted by the current user.
        self.show_own = show_own
        # The sorting field. Valid values:
        # 
        # *   DisplayName
        # *   JobType
        # *   Status
        # *   GmtCreateTime
        # *   GmtFinishTime
        self.sort_by = sort_by
        # The start time of the query. Use the job creation time to filter data. The default value is the current time minus seven days. In other words, if you do not configure the StartTime and EndTime parameters, the system queries the job list in the last seven days.
        self.start_time = start_time
        # The job status. Valid values:
        # 
        # *   Creating
        # *   Queuing
        # *   Bidding (only available for spot jobs that use Lingjun resources)
        # *   EnvPreparing
        # *   SanityChecking
        # *   Running
        # *   Restarting
        # *   Stopping
        # *   SucceededReserving
        # *   FailedReserving
        # *   Succeeded
        # *   Failed
        # *   Stopped
        self.status = status
        # The tags.
        self.tags = tags
        # The user ID used to filter jobs.
        self.user_id_for_filter = user_id_for_filter
        # The username used to filter jobs. Fuzzy search is supported. Wildcards are not supported. The default value null indicates that jobs are not filtered by username.
        self.username = username
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.from_all_workspaces is not None:
            result['FromAllWorkspaces'] = self.from_all_workspaces
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.order is not None:
            result['Order'] = self.order
        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_quota_name is not None:
            result['ResourceQuotaName'] = self.resource_quota_name
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_id_for_filter is not None:
            result['UserIdForFilter'] = self.user_id_for_filter
        if self.username is not None:
            result['Username'] = self.username
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FromAllWorkspaces') is not None:
            self.from_all_workspaces = m.get('FromAllWorkspaces')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceQuotaName') is not None:
            self.resource_quota_name = m.get('ResourceQuotaName')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserIdForFilter') is not None:
            self.user_id_for_filter = m.get('UserIdForFilter')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        business_user_id: str = None,
        caller: str = None,
        display_name: str = None,
        end_time: str = None,
        from_all_workspaces: bool = None,
        job_id: str = None,
        job_ids: str = None,
        job_type: str = None,
        order: str = None,
        oversold_info: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        pipeline_id: str = None,
        resource_id: str = None,
        resource_quota_name: str = None,
        show_own: bool = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        tags_shrink: str = None,
        user_id_for_filter: str = None,
        username: str = None,
        workspace_id: str = None,
    ):
        # The job visibility. Valid values:
        # 
        # *   PUBLIC: The job is visible to all members in the workspace.
        # *   PRIVATE: The job is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The ID of the user associated with the job.
        self.business_user_id = business_user_id
        # The caller.
        self.caller = caller
        # The job name. Fuzzy query is supported. The name is case-insensitive. Wildcards are not supported. For example, if you enter test, test-job1, job-test, job-test2, or job-test can be matched, and job-t1 cannot be matched. The default value null indicates any job name.
        self.display_name = display_name
        # The end time of the query. Use the job creation time to filter data. The default value is the current time.
        self.end_time = end_time
        # Specifies whether to query a list of jobs across workspaces. This parameter must be used together with `ShowOwn=true`. You can use this parameter to query a list of jobs recently submitted by the current user.
        self.from_all_workspaces = from_all_workspaces
        # The job ID. Fuzzy query is supported. The name is case-insensitive. Wildcards are not supported. The default value null indicates any job ID.
        self.job_id = job_id
        self.job_ids = job_ids
        # The job type. The default value null indicates any type. Valid values:
        # 
        # *   TFJob
        # *   PyTorchJob
        # *   XGBoostJob
        # *   OneFlowJob
        # *   ElasticBatchJob
        self.job_type = job_type
        # The sorting order. Valid values:
        # 
        # *   desc (default)
        # *   asc
        self.order = order
        # The Idle resource information. Valid values:
        # 
        # *   ForbiddenQuotaOverSold
        # *   ForceQuotaOverSold
        # *   AcceptQuotaOverSold-true (true indicates that the job uses idle resources.)
        # *   AcceptQuotaOverSold-false (false indicates that the job uses guaranteed resources.)
        self.oversold_info = oversold_info
        # The number of the page to return for the current query. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of jobs per page.
        self.page_size = page_size
        # The type of the resource. Valid values:
        # 
        # *   PrePaid: Resource quota
        # *   Spot: Preemptible resources
        # *   PostPaid: Public resources
        self.payment_type = payment_type
        # The specific pipeline ID used to filter jobs.
        self.pipeline_id = pipeline_id
        # The resource group ID. For information about how to obtain the ID of a dedicated resource group, see [Manage resource quota](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        # The resource quota name used to filter jobs. Fuzzy search is supported. Wildcards are not supported. The default value null indicates that jobs are not filtered by resource quota name.
        self.resource_quota_name = resource_quota_name
        # Specifies whether to query only the jobs submitted by the current user.
        self.show_own = show_own
        # The sorting field. Valid values:
        # 
        # *   DisplayName
        # *   JobType
        # *   Status
        # *   GmtCreateTime
        # *   GmtFinishTime
        self.sort_by = sort_by
        # The start time of the query. Use the job creation time to filter data. The default value is the current time minus seven days. In other words, if you do not configure the StartTime and EndTime parameters, the system queries the job list in the last seven days.
        self.start_time = start_time
        # The job status. Valid values:
        # 
        # *   Creating
        # *   Queuing
        # *   Bidding (only available for spot jobs that use Lingjun resources)
        # *   EnvPreparing
        # *   SanityChecking
        # *   Running
        # *   Restarting
        # *   Stopping
        # *   SucceededReserving
        # *   FailedReserving
        # *   Succeeded
        # *   Failed
        # *   Stopped
        self.status = status
        # The tags.
        self.tags_shrink = tags_shrink
        # The user ID used to filter jobs.
        self.user_id_for_filter = user_id_for_filter
        # The username used to filter jobs. Fuzzy search is supported. Wildcards are not supported. The default value null indicates that jobs are not filtered by username.
        self.username = username
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.from_all_workspaces is not None:
            result['FromAllWorkspaces'] = self.from_all_workspaces
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.order is not None:
            result['Order'] = self.order
        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_quota_name is not None:
            result['ResourceQuotaName'] = self.resource_quota_name
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_id_for_filter is not None:
            result['UserIdForFilter'] = self.user_id_for_filter
        if self.username is not None:
            result['Username'] = self.username
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FromAllWorkspaces') is not None:
            self.from_all_workspaces = m.get('FromAllWorkspaces')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceQuotaName') is not None:
            self.resource_quota_name = m.get('ResourceQuotaName')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserIdForFilter') is not None:
            self.user_id_for_filter = m.get('UserIdForFilter')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[JobItem] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The jobs.
        self.jobs = jobs
        # The request ID used to troubleshoot issues.
        self.request_id = request_id
        # The total number of jobs that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = JobItem()
                self.jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTensorboardsRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        display_name: str = None,
        end_time: str = None,
        job_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        quota_id: str = None,
        show_own: bool = None,
        sort_by: str = None,
        source_id: str = None,
        source_type: str = None,
        start_time: str = None,
        status: str = None,
        tensorboard_id: str = None,
        user_id: str = None,
        username: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The instance visibility.
        # 
        # *   PUBLIC: TensorBoard instances are visible to all members in the workspace.
        # *   PRIVATE: TensorBoard instances are visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The TensorBoard instance name.
        self.display_name = display_name
        # The end time of the query. Use the UTC time when the TensorBoard instance is created to filter data. If you leave this parameter empty, the default value is the current time.
        self.end_time = end_time
        # The job ID used to filter TensorBoard instances. For more information about how to obtain the ID of a job, see [ListJobs](https://help.aliyun.com/document_detail/459676.html).
        self.job_id = job_id
        # The sorting order.
        # 
        # *   desc
        # *   asc
        self.order = order
        # The page number. Minimum value: 1.
        self.page_number = page_number
        # The number of TensorBoard instances per page.
        self.page_size = page_size
        # The billing method of TensorBoard instances.
        # 
        # *   Free: the TensorBoard instance that uses free resources.
        # *   Postpaid: the TensorBoard instance that uses pay-as-you-go resources.
        self.payment_type = payment_type
        # The resource quota ID.
        # 
        # > 
        # 
        # *   Only whitelisted users can use resource quotas to create TensorBoard instances. If you want to use this feature, contact us.
        # 
        # *   This parameter takes effect only when TensorBoard instances use resource quotas.
        self.quota_id = quota_id
        # Specifies whether to return only the TensorBoard instances created by the current logon account.
        self.show_own = show_own
        # The returned field used to sort TensorBoard instances.
        # 
        # *   DisplayName: the name of the TensorBoard instance.
        # *   GmtCreateTime: the time when the TensorBoard instance is created.
        self.sort_by = sort_by
        # The data source ID. For more information about how to obtain the ID of a job, see [ListJobs](https://help.aliyun.com/document_detail/459676.html).
        self.source_id = source_id
        # The data source associated with the TensorBoard instance. This parameter is no longer used. Only Deep Learning Containers (DLC) training jobs are supported.
        self.source_type = source_type
        # The start time of the query. Use the UTC time when the TensorBoard instance is created to filter data. If you leave this parameter empty, the default value is seven days before the current time.
        self.start_time = start_time
        # The TensorBoard instance status. Valid values:
        # 
        # *   Creating
        # *   Running
        # *   Stopped
        # *   Succeeded
        # *   Failed
        self.status = status
        # The TensorBoard instance ID used to filter TensorBoard instances.
        self.tensorboard_id = tensorboard_id
        # The user ID.
        self.user_id = user_id
        # The username.
        self.username = username
        # Specifies whether to return the information about the TensorBoard instance.
        # 
        # *   true
        # *   false
        self.verbose = verbose
        # The workspace ID. Obtain a list of TensorBoard instances based on the workspace ID. 
        # <props="china">For more information, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.show_own is not None:
            result['ShowOwn'] = self.show_own
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTensorboardsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboards: List[Tensorboard] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The TensorBoard instances.
        self.tensorboards = tensorboards
        # The total number of data sources that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.tensorboards:
            for k in self.tensorboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tensorboards'] = []
        if self.tensorboards is not None:
            for k in self.tensorboards:
                result['Tensorboards'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tensorboards = []
        if m.get('Tensorboards') is not None:
            for k in m.get('Tensorboards'):
                temp_model = Tensorboard()
                self.tensorboards.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTensorboardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTensorboardsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTensorboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTensorboardRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class StartTensorboardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboard_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The TensorBoard instance ID.
        self.tensorboard_id = tensorboard_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class StartTensorboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTensorboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID. You can troubleshoot issues based on the request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTensorboardRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # The workspace ID. 
        # <props="china">For more information about how to query the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class StopTensorboardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboard_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the TensorBoard instance.
        self.tensorboard_id = tensorboard_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class StopTensorboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopTensorboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        priority: int = None,
    ):
        # The job visibility. Valid values:
        # 
        # *   PUBLIC: The job is visible to all members in the workspace.
        # *   PRIVATE: The job is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The job priority. Valid values: 1 to 9.
        # 
        # *   1: the lowest priority.
        # *   9: the highest priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class UpdateJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID, which is used for diagnostics and Q\\&A.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTensorboardRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        max_running_time_minutes: int = None,
        priority: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the jobs. Valid values:
        # 
        # *   PUBLIC: The jobs are public in the workspace.
        # *   PRIVATE: The jobs are visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The maximum running time. Unit: minutes.
        self.max_running_time_minutes = max_running_time_minutes
        self.priority = priority
        # The workspace ID. 
        # <props="china">For more information about how to query the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateTensorboardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboard_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the TensorBoard instance.
        self.tensorboard_id = tensorboard_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')
        return self


class UpdateTensorboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTensorboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTensorboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


