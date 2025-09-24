# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CodeSourceItem(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
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
        mount_path: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
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
        self.mount_path = mount_path
        self.user_id = user_id
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
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
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
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class Collection(TeaModel):
    def __init__(
        self,
        collection_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        owner_id: str = None,
        user_id: str = None,
    ):
        self.collection_name = collection_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.owner_id = owner_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ConnectionModels(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        model: str = None,
        model_type: str = None,
        tool_call: bool = None,
    ):
        self.display_name = display_name
        self.model = model
        self.model_type = model_type
        self.tool_call = tool_call

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.model is not None:
            result['Model'] = self.model
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')
        return self


class ConnectionResourceMeta(TeaModel):
    def __init__(
        self,
        extra: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.extra = extra
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class Connection(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        configs: Dict[str, str] = None,
        connection_id: str = None,
        connection_name: str = None,
        connection_type: str = None,
        creator: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        models: List[ConnectionModels] = None,
        resource_meta: ConnectionResourceMeta = None,
        secrets: Dict[str, str] = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.configs = configs
        self.connection_id = connection_id
        self.connection_name = connection_name
        self.connection_type = connection_type
        self.creator = creator
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.models = models
        self.resource_meta = resource_meta
        self.secrets = secrets
        self.workspace_id = workspace_id

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()
        if self.resource_meta:
            self.resource_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.resource_meta is not None:
            result['ResourceMeta'] = self.resource_meta.to_map()
        if self.secrets is not None:
            result['Secrets'] = self.secrets
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = ConnectionModels()
                self.models.append(temp_model.from_map(k))
        if m.get('ResourceMeta') is not None:
            temp_model = ConnectionResourceMeta()
            self.resource_meta = temp_model.from_map(m['ResourceMeta'])
        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DatasetShareRelationship(TeaModel):
    def __init__(
        self,
        allowed_mount_access_levels: List[str] = None,
        expires_at: str = None,
        is_secure_mode: bool = None,
        shared_at: str = None,
        source_tenant_id: str = None,
        source_workspace_id: str = None,
        status: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.allowed_mount_access_levels = allowed_mount_access_levels
        self.expires_at = expires_at
        self.is_secure_mode = is_secure_mode
        self.shared_at = shared_at
        self.source_tenant_id = source_tenant_id
        self.source_workspace_id = source_workspace_id
        self.status = status
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_mount_access_levels is not None:
            result['AllowedMountAccessLevels'] = self.allowed_mount_access_levels
        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at
        if self.is_secure_mode is not None:
            result['IsSecureMode'] = self.is_secure_mode
        if self.shared_at is not None:
            result['SharedAt'] = self.shared_at
        if self.source_tenant_id is not None:
            result['SourceTenantId'] = self.source_tenant_id
        if self.source_workspace_id is not None:
            result['SourceWorkspaceId'] = self.source_workspace_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedMountAccessLevels') is not None:
            self.allowed_mount_access_levels = m.get('AllowedMountAccessLevels')
        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')
        if m.get('IsSecureMode') is not None:
            self.is_secure_mode = m.get('IsSecureMode')
        if m.get('SharedAt') is not None:
            self.shared_at = m.get('SharedAt')
        if m.get('SourceTenantId') is not None:
            self.source_tenant_id = m.get('SourceTenantId')
        if m.get('SourceWorkspaceId') is not None:
            self.source_workspace_id = m.get('SourceWorkspaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DatasetSharingConfig(TeaModel):
    def __init__(
        self,
        shared_to: List[DatasetShareRelationship] = None,
    ):
        self.shared_to = shared_to

    def validate(self):
        if self.shared_to:
            for k in self.shared_to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SharedTo'] = []
        if self.shared_to is not None:
            for k in self.shared_to:
                result['SharedTo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shared_to = []
        if m.get('SharedTo') is not None:
            for k in m.get('SharedTo'):
                temp_model = DatasetShareRelationship()
                self.shared_to.append(temp_model.from_map(k))
        return self


class Label(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DatasetVersion(TeaModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        import_info: str = None,
        labels: List[Label] = None,
        mount_access: str = None,
        options: str = None,
        property: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
        version_name: str = None,
    ):
        self.data_count = data_count
        self.data_size = data_size
        self.data_source_type = data_source_type
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.import_info = import_info
        self.labels = labels
        self.mount_access = mount_access
        self.options = options
        self.property = property
        self.source_id = source_id
        self.source_type = source_type
        self.uri = uri
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_count is not None:
            result['DataCount'] = self.data_count
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.import_info is not None:
            result['ImportInfo'] = self.import_info
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.options is not None:
            result['Options'] = self.options
        if self.property is not None:
            result['Property'] = self.property
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class Dataset(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        data_source_type: str = None,
        data_type: str = None,
        dataset_id: str = None,
        description: str = None,
        edition: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        import_info: str = None,
        is_shared: bool = None,
        labels: List[Label] = None,
        latest_version: DatasetVersion = None,
        mount_access: str = None,
        mount_access_read_write_role_id_list: List[str] = None,
        name: str = None,
        options: str = None,
        owner_id: str = None,
        property: str = None,
        provider_type: str = None,
        shared_from: DatasetShareRelationship = None,
        sharing_config: DatasetSharingConfig = None,
        source_dataset_id: str = None,
        source_dataset_version: str = None,
        source_id: str = None,
        source_type: str = None,
        tag_template_type: str = None,
        uri: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.data_source_type = data_source_type
        self.data_type = data_type
        self.dataset_id = dataset_id
        self.description = description
        self.edition = edition
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.import_info = import_info
        self.is_shared = is_shared
        self.labels = labels
        self.latest_version = latest_version
        self.mount_access = mount_access
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        self.name = name
        self.options = options
        self.owner_id = owner_id
        self.property = property
        self.provider_type = provider_type
        self.shared_from = shared_from
        self.sharing_config = sharing_config
        self.source_dataset_id = source_dataset_id
        self.source_dataset_version = source_dataset_version
        self.source_id = source_id
        self.source_type = source_type
        self.tag_template_type = tag_template_type
        self.uri = uri
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_version:
            self.latest_version.validate()
        if self.shared_from:
            self.shared_from.validate()
        if self.sharing_config:
            self.sharing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.description is not None:
            result['Description'] = self.description
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.import_info is not None:
            result['ImportInfo'] = self.import_info
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.mount_access_read_write_role_id_list is not None:
            result['MountAccessReadWriteRoleIdList'] = self.mount_access_read_write_role_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.property is not None:
            result['Property'] = self.property
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.shared_from is not None:
            result['SharedFrom'] = self.shared_from.to_map()
        if self.sharing_config is not None:
            result['SharingConfig'] = self.sharing_config.to_map()
        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id
        if self.source_dataset_version is not None:
            result['SourceDatasetVersion'] = self.source_dataset_version
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.tag_template_type is not None:
            result['TagTemplateType'] = self.tag_template_type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestVersion') is not None:
            temp_model = DatasetVersion()
            self.latest_version = temp_model.from_map(m['LatestVersion'])
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('MountAccessReadWriteRoleIdList') is not None:
            self.mount_access_read_write_role_id_list = m.get('MountAccessReadWriteRoleIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('SharedFrom') is not None:
            temp_model = DatasetShareRelationship()
            self.shared_from = temp_model.from_map(m['SharedFrom'])
        if m.get('SharingConfig') is not None:
            temp_model = DatasetSharingConfig()
            self.sharing_config = temp_model.from_map(m['SharingConfig'])
        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')
        if m.get('SourceDatasetVersion') is not None:
            self.source_dataset_version = m.get('SourceDatasetVersion')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TagTemplateType') is not None:
            self.tag_template_type = m.get('TagTemplateType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DatasetFileMeta(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        data_size: int = None,
        dataset_file_meta_id: str = None,
        download_url: str = None,
        file_create_time: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        score: float = None,
        semantic_index_job_id: str = None,
        semantic_index_update_time: str = None,
        tags: str = None,
        thumbnail_url: str = None,
        uri: str = None,
    ):
        self.content_type = content_type
        self.data_size = data_size
        self.dataset_file_meta_id = dataset_file_meta_id
        self.download_url = download_url
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        self.file_finger_print = file_finger_print
        self.file_name = file_name
        self.file_type = file_type
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        self.meta_attributes = meta_attributes
        self.score = score
        self.semantic_index_job_id = semantic_index_job_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.semantic_index_update_time = semantic_index_update_time
        self.tags = tags
        self.thumbnail_url = thumbnail_url
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_finger_print is not None:
            result['FileFingerPrint'] = self.file_finger_print
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_update_time is not None:
            result['FileUpdateTime'] = self.file_update_time
        if self.meta_attributes is not None:
            result['MetaAttributes'] = self.meta_attributes
        if self.score is not None:
            result['Score'] = self.score
        if self.semantic_index_job_id is not None:
            result['SemanticIndexJobId'] = self.semantic_index_job_id
        if self.semantic_index_update_time is not None:
            result['SemanticIndexUpdateTime'] = self.semantic_index_update_time
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileFingerPrint') is not None:
            self.file_finger_print = m.get('FileFingerPrint')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUpdateTime') is not None:
            self.file_update_time = m.get('FileUpdateTime')
        if m.get('MetaAttributes') is not None:
            self.meta_attributes = m.get('MetaAttributes')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SemanticIndexJobId') is not None:
            self.semantic_index_job_id = m.get('SemanticIndexJobId')
        if m.get('SemanticIndexUpdateTime') is not None:
            self.semantic_index_update_time = m.get('SemanticIndexUpdateTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DatasetFileMetaConentUpdate(TeaModel):
    def __init__(
        self,
        comment: str = None,
        content_type: str = None,
        data_size: int = None,
        dataset_file_meta_id: str = None,
        file_create_time: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        semantic_index_job_id: str = None,
        semantic_index_update_time: str = None,
        tags: str = None,
    ):
        self.comment = comment
        self.content_type = content_type
        self.data_size = data_size
        # This parameter is required.
        self.dataset_file_meta_id = dataset_file_meta_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        self.file_finger_print = file_finger_print
        self.file_name = file_name
        self.file_type = file_type
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        self.meta_attributes = meta_attributes
        self.semantic_index_job_id = semantic_index_job_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.semantic_index_update_time = semantic_index_update_time
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_finger_print is not None:
            result['FileFingerPrint'] = self.file_finger_print
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_update_time is not None:
            result['FileUpdateTime'] = self.file_update_time
        if self.meta_attributes is not None:
            result['MetaAttributes'] = self.meta_attributes
        if self.semantic_index_job_id is not None:
            result['SemanticIndexJobId'] = self.semantic_index_job_id
        if self.semantic_index_update_time is not None:
            result['SemanticIndexUpdateTime'] = self.semantic_index_update_time
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileFingerPrint') is not None:
            self.file_finger_print = m.get('FileFingerPrint')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUpdateTime') is not None:
            self.file_update_time = m.get('FileUpdateTime')
        if m.get('MetaAttributes') is not None:
            self.meta_attributes = m.get('MetaAttributes')
        if m.get('SemanticIndexJobId') is not None:
            self.semantic_index_job_id = m.get('SemanticIndexJobId')
        if m.get('SemanticIndexUpdateTime') is not None:
            self.semantic_index_update_time = m.get('SemanticIndexUpdateTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DatasetFileMetaContentCreate(TeaModel):
    def __init__(
        self,
        comment: str = None,
        content_type: str = None,
        data_size: int = None,
        file_create_time: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        tags: str = None,
        uri: str = None,
    ):
        self.comment = comment
        # This parameter is required.
        self.content_type = content_type
        self.data_size = data_size
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        # This parameter is required.
        self.file_finger_print = file_finger_print
        self.file_name = file_name
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        self.meta_attributes = meta_attributes
        self.tags = tags
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_finger_print is not None:
            result['FileFingerPrint'] = self.file_finger_print
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_update_time is not None:
            result['FileUpdateTime'] = self.file_update_time
        if self.meta_attributes is not None:
            result['MetaAttributes'] = self.meta_attributes
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileFingerPrint') is not None:
            self.file_finger_print = m.get('FileFingerPrint')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUpdateTime') is not None:
            self.file_update_time = m.get('FileUpdateTime')
        if m.get('MetaAttributes') is not None:
            self.meta_attributes = m.get('MetaAttributes')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DatasetFileMetaContentGet(TeaModel):
    def __init__(
        self,
        comment: str = None,
        content_type: str = None,
        data_size: int = None,
        dataset_file_meta_id: str = None,
        file_create_time: str = None,
        file_dir: str = None,
        file_finger_print: str = None,
        file_name: str = None,
        file_type: str = None,
        file_update_time: str = None,
        meta_attributes: str = None,
        semantic_index_job_id: str = None,
        semantic_index_update_time: str = None,
        tag_update_time: str = None,
        tags: str = None,
        uri: str = None,
    ):
        self.comment = comment
        self.content_type = content_type
        self.data_size = data_size
        self.dataset_file_meta_id = dataset_file_meta_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_create_time = file_create_time
        self.file_dir = file_dir
        self.file_finger_print = file_finger_print
        self.file_name = file_name
        self.file_type = file_type
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.file_update_time = file_update_time
        self.meta_attributes = meta_attributes
        self.semantic_index_job_id = semantic_index_job_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.semantic_index_update_time = semantic_index_update_time
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.tag_update_time = tag_update_time
        self.tags = tags
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_dir is not None:
            result['FileDir'] = self.file_dir
        if self.file_finger_print is not None:
            result['FileFingerPrint'] = self.file_finger_print
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_update_time is not None:
            result['FileUpdateTime'] = self.file_update_time
        if self.meta_attributes is not None:
            result['MetaAttributes'] = self.meta_attributes
        if self.semantic_index_job_id is not None:
            result['SemanticIndexJobId'] = self.semantic_index_job_id
        if self.semantic_index_update_time is not None:
            result['SemanticIndexUpdateTime'] = self.semantic_index_update_time
        if self.tag_update_time is not None:
            result['TagUpdateTime'] = self.tag_update_time
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')
        if m.get('FileFingerPrint') is not None:
            self.file_finger_print = m.get('FileFingerPrint')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUpdateTime') is not None:
            self.file_update_time = m.get('FileUpdateTime')
        if m.get('MetaAttributes') is not None:
            self.meta_attributes = m.get('MetaAttributes')
        if m.get('SemanticIndexJobId') is not None:
            self.semantic_index_job_id = m.get('SemanticIndexJobId')
        if m.get('SemanticIndexUpdateTime') is not None:
            self.semantic_index_update_time = m.get('SemanticIndexUpdateTime')
        if m.get('TagUpdateTime') is not None:
            self.tag_update_time = m.get('TagUpdateTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DatasetFileMetaResponse(TeaModel):
    def __init__(
        self,
        dataset_file_meta_id: str = None,
        result: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.dataset_file_meta_id = dataset_file_meta_id
        # This parameter is required.
        self.result = result
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id
        if self.result is not None:
            result['Result'] = self.result
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DatasetFileMetasStat(TeaModel):
    def __init__(
        self,
        count: int = None,
        key: str = None,
    ):
        self.count = count
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class DatasetJob(TeaModel):
    def __init__(
        self,
        completed_file_count: int = None,
        create_time: str = None,
        dataset_job_id: str = None,
        dataset_version: str = None,
        description: str = None,
        failed_file_count: int = None,
        finish_time: str = None,
        job_action: str = None,
        job_mode: str = None,
        job_spec: str = None,
        logs: List[str] = None,
        status: str = None,
        total_file_count: int = None,
        workspace_id: str = None,
    ):
        self.completed_file_count = completed_file_count
        self.create_time = create_time
        self.dataset_job_id = dataset_job_id
        self.dataset_version = dataset_version
        self.description = description
        self.failed_file_count = failed_file_count
        self.finish_time = finish_time
        self.job_action = job_action
        self.job_mode = job_mode
        self.job_spec = job_spec
        self.logs = logs
        self.status = status
        self.total_file_count = total_file_count
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_file_count is not None:
            result['CompletedFileCount'] = self.completed_file_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_job_id is not None:
            result['DatasetJobId'] = self.dataset_job_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.description is not None:
            result['Description'] = self.description
        if self.failed_file_count is not None:
            result['FailedFileCount'] = self.failed_file_count
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.job_action is not None:
            result['JobAction'] = self.job_action
        if self.job_mode is not None:
            result['JobMode'] = self.job_mode
        if self.job_spec is not None:
            result['JobSpec'] = self.job_spec
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.status is not None:
            result['Status'] = self.status
        if self.total_file_count is not None:
            result['TotalFileCount'] = self.total_file_count
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedFileCount') is not None:
            self.completed_file_count = m.get('CompletedFileCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetJobId') is not None:
            self.dataset_job_id = m.get('DatasetJobId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailedFileCount') is not None:
            self.failed_file_count = m.get('FailedFileCount')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')
        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')
        if m.get('JobSpec') is not None:
            self.job_spec = m.get('JobSpec')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalFileCount') is not None:
            self.total_file_count = m.get('TotalFileCount')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DatasetJobConfig(TeaModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        create_time: str = None,
        dataset_job_config_id: str = None,
        dataset_version: str = None,
        modify_time: str = None,
        workspace_id: str = None,
    ):
        self.config = config
        self.config_type = config_type
        self.create_time = create_time
        self.dataset_job_config_id = dataset_job_config_id
        self.dataset_version = dataset_version
        self.modify_time = modify_time
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_job_config_id is not None:
            result['DatasetJobConfigId'] = self.dataset_job_config_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetJobConfigId') is not None:
            self.dataset_job_config_id = m.get('DatasetJobConfigId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DatasetLabel(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ExperimentLabel(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        key: str = None,
        value: str = None,
    ):
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RunLabel(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        key: str = None,
        run_id: str = None,
        value: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        # This parameter is required.
        self.key = key
        self.run_id = run_id
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.key is not None:
            result['Key'] = self.key
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RunMetric(TeaModel):
    def __init__(
        self,
        key: str = None,
        step: int = None,
        timestamp: int = None,
        value: float = None,
    ):
        # This parameter is required.
        self.key = key
        self.step = step
        self.timestamp = timestamp
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.step is not None:
            result['Step'] = self.step
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RunParam(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class Run(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[RunLabel] = None,
        metrics: List[RunMetric] = None,
        name: str = None,
        owner_id: str = None,
        params: List[RunParam] = None,
        request_id: str = None,
        run_id: str = None,
        source_id: str = None,
        source_type: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.metrics = metrics
        self.name = name
        self.owner_id = owner_id
        self.params = params
        self.request_id = request_id
        self.run_id = run_id
        self.source_id = source_id
        self.source_type = source_type
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = RunLabel()
                self.labels.append(temp_model.from_map(k))
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = RunMetric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = RunParam()
                self.params.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class Experiment(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        artifact_uri: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[ExperimentLabel] = None,
        latest_run: Run = None,
        name: str = None,
        owner_id: str = None,
        request_id: str = None,
        tensorboard_log_uri: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.artifact_uri = artifact_uri
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.latest_run = latest_run
        self.name = name
        self.owner_id = owner_id
        self.request_id = request_id
        self.tensorboard_log_uri = tensorboard_log_uri
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_run:
            self.latest_run.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.artifact_uri is not None:
            result['ArtifactUri'] = self.artifact_uri
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_run is not None:
            result['LatestRun'] = self.latest_run.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tensorboard_log_uri is not None:
            result['TensorboardLogUri'] = self.tensorboard_log_uri
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('ArtifactUri') is not None:
            self.artifact_uri = m.get('ArtifactUri')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ExperimentLabel()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestRun') is not None:
            temp_model = Run()
            self.latest_run = temp_model.from_map(m['LatestRun'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TensorboardLogUri') is not None:
            self.tensorboard_log_uri = m.get('TensorboardLogUri')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class LabelInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class LineageEntity(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        entity_type: str = None,
        name: str = None,
        qualified_name: str = None,
    ):
        self.attributes = attributes
        self.entity_type = entity_type
        self.name = name
        self.qualified_name = qualified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.name is not None:
            result['Name'] = self.name
        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')
        return self


class LineageRelation(TeaModel):
    def __init__(
        self,
        dest_entity_qualified_name: str = None,
        relationship_guid: str = None,
        src_entity_qualified_name: str = None,
    ):
        self.dest_entity_qualified_name = dest_entity_qualified_name
        self.relationship_guid = relationship_guid
        self.src_entity_qualified_name = src_entity_qualified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_entity_qualified_name is not None:
            result['DestEntityQualifiedName'] = self.dest_entity_qualified_name
        if self.relationship_guid is not None:
            result['RelationshipGuid'] = self.relationship_guid
        if self.src_entity_qualified_name is not None:
            result['SrcEntityQualifiedName'] = self.src_entity_qualified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestEntityQualifiedName') is not None:
            self.dest_entity_qualified_name = m.get('DestEntityQualifiedName')
        if m.get('RelationshipGuid') is not None:
            self.relationship_guid = m.get('RelationshipGuid')
        if m.get('SrcEntityQualifiedName') is not None:
            self.src_entity_qualified_name = m.get('SrcEntityQualifiedName')
        return self


class ModelVersionLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModelVersion(TeaModel):
    def __init__(
        self,
        approval_status: str = None,
        compression_spec: Dict[str, Any] = None,
        distillation_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        extra_info: Dict[str, Any] = None,
        format_type: str = None,
        framework_type: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        inference_spec: Dict[str, Any] = None,
        labels: List[ModelVersionLabels] = None,
        metrics: Dict[str, Any] = None,
        options: str = None,
        owner_id: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        uri: str = None,
        user_id: str = None,
        version_description: str = None,
        version_name: str = None,
    ):
        self.approval_status = approval_status
        self.compression_spec = compression_spec
        self.distillation_spec = distillation_spec
        self.evaluation_spec = evaluation_spec
        self.extra_info = extra_info
        self.format_type = format_type
        self.framework_type = framework_type
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.inference_spec = inference_spec
        self.labels = labels
        self.metrics = metrics
        self.options = options
        self.owner_id = owner_id
        self.source_id = source_id
        self.source_type = source_type
        self.training_spec = training_spec
        self.uri = uri
        self.user_id = user_id
        self.version_description = version_description
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status
        if self.compression_spec is not None:
            result['CompressionSpec'] = self.compression_spec
        if self.distillation_spec is not None:
            result['DistillationSpec'] = self.distillation_spec
        if self.evaluation_spec is not None:
            result['EvaluationSpec'] = self.evaluation_spec
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.inference_spec is not None:
            result['InferenceSpec'] = self.inference_spec
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.options is not None:
            result['Options'] = self.options
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.training_spec is not None:
            result['TrainingSpec'] = self.training_spec
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')
        if m.get('CompressionSpec') is not None:
            self.compression_spec = m.get('CompressionSpec')
        if m.get('DistillationSpec') is not None:
            self.distillation_spec = m.get('DistillationSpec')
        if m.get('EvaluationSpec') is not None:
            self.evaluation_spec = m.get('EvaluationSpec')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ModelVersionLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TrainingSpec') is not None:
            self.training_spec = m.get('TrainingSpec')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class Model(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_latest_version_modified_time: str = None,
        gmt_modified_time: str = None,
        labels: List[Label] = None,
        latest_version: ModelVersion = None,
        model_description: str = None,
        model_doc: str = None,
        model_id: str = None,
        model_name: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        owner_id: str = None,
        parameter_size: int = None,
        provider: str = None,
        tags: List[Label] = None,
        task: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.domain = domain
        self.extra_info = extra_info
        self.gmt_create_time = gmt_create_time
        self.gmt_latest_version_modified_time = gmt_latest_version_modified_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.latest_version = latest_version
        self.model_description = model_description
        self.model_doc = model_doc
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.order_number = order_number
        self.origin = origin
        self.owner_id = owner_id
        self.parameter_size = parameter_size
        self.provider = provider
        self.tags = tags
        self.task = task
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_version:
            self.latest_version.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_latest_version_modified_time is not None:
            result['GmtLatestVersionModifiedTime'] = self.gmt_latest_version_modified_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()
        if self.model_description is not None:
            result['ModelDescription'] = self.model_description
        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.order_number is not None:
            result['OrderNumber'] = self.order_number
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_size is not None:
            result['ParameterSize'] = self.parameter_size
        if self.provider is not None:
            result['Provider'] = self.provider
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.task is not None:
            result['Task'] = self.task
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtLatestVersionModifiedTime') is not None:
            self.gmt_latest_version_modified_time = m.get('GmtLatestVersionModifiedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestVersion') is not None:
            temp_model = ModelVersion()
            self.latest_version = temp_model.from_map(m['LatestVersion'])
        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')
        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParameterSize') is not None:
            self.parameter_size = m.get('ParameterSize')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = Label()
                self.tags.append(temp_model.from_map(k))
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class Prompt(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        create_time: str = None,
        description: str = None,
        framework_content: str = None,
        framework_type: str = None,
        modify_time: str = None,
        prompt_id: str = None,
        prompt_name: str = None,
    ):
        self.accessibility = accessibility
        self.create_time = create_time
        self.description = description
        self.framework_content = framework_content
        self.framework_type = framework_type
        self.modify_time = modify_time
        self.prompt_id = prompt_id
        self.prompt_name = prompt_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.framework_content is not None:
            result['FrameworkContent'] = self.framework_content
        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.prompt_id is not None:
            result['PromptId'] = self.prompt_id
        if self.prompt_name is not None:
            result['PromptName'] = self.prompt_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FrameworkContent') is not None:
            self.framework_content = m.get('FrameworkContent')
        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PromptId') is not None:
            self.prompt_id = m.get('PromptId')
        if m.get('PromptName') is not None:
            self.prompt_name = m.get('PromptName')
        return self


class Relation(TeaModel):
    def __init__(
        self,
        err_msg: str = None,
        lineage_relation: LineageRelation = None,
        result: bool = None,
    ):
        self.err_msg = err_msg
        self.lineage_relation = lineage_relation
        self.result = result

    def validate(self):
        if self.lineage_relation:
            self.lineage_relation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.lineage_relation is not None:
            result['LineageRelation'] = self.lineage_relation.to_map()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('LineageRelation') is not None:
            temp_model = LineageRelation()
            self.lineage_relation = temp_model.from_map(m['LineageRelation'])
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class Relationship(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        data_channel: str = None,
        relationship_guid: str = None,
        relationship_type: str = None,
    ):
        self.attributes = attributes
        self.data_channel = data_channel
        self.relationship_guid = relationship_guid
        self.relationship_type = relationship_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.data_channel is not None:
            result['DataChannel'] = self.data_channel
        if self.relationship_guid is not None:
            result['RelationshipGuid'] = self.relationship_guid
        if self.relationship_type is not None:
            result['RelationshipType'] = self.relationship_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DataChannel') is not None:
            self.data_channel = m.get('DataChannel')
        if m.get('RelationshipGuid') is not None:
            self.relationship_guid = m.get('RelationshipGuid')
        if m.get('RelationshipType') is not None:
            self.relationship_type = m.get('RelationshipType')
        return self


class Trial(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        experiment_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[Dict[str, Any]] = None,
        name: str = None,
        owner_id: str = None,
        source_id: str = None,
        source_type: str = None,
        trial_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.experiment_id = experiment_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.name = name
        self.owner_id = owner_id
        self.source_id = source_id
        self.source_type = source_type
        self.trial_id = trial_id
        self.user_id = user_id
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
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.trial_id is not None:
            result['TrialId'] = self.trial_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TrialId') is not None:
            self.trial_id = m.get('TrialId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class TrialLabel(TeaModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        key: str = None,
        trial_id: str = None,
        value: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.key = key
        self.trial_id = trial_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.key is not None:
            result['Key'] = self.key
        if self.trial_id is not None:
            result['TrialId'] = self.trial_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('TrialId') is not None:
            self.trial_id = m.get('TrialId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AcceptDataworksEventRequest(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        message_id: str = None,
    ):
        # The event content in the message.
        self.data = data
        # The message ID. You can obtain the ID from the message received when an extension point event is triggered. For more information about the message format, see [Message formats](https://help.aliyun.com/document_detail/436911.html).
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class AcceptDataworksEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AcceptDataworksEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptDataworksEventResponseBody = None,
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
            temp_model = AcceptDataworksEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddImageRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        image_id: str = None,
        image_uri: str = None,
        labels: List[AddImageRequestLabels] = None,
        name: str = None,
        size: int = None,
        source_id: str = None,
        source_type: str = None,
        workspace_id: str = None,
    ):
        # The accessibility of the image. Valid values:
        # 
        # *   PUBLIC: The image is accessible to all members in the workspace.
        # *   PRIVATE: The image is accessible only to the image creator.
        self.accessibility = accessibility
        # The image description.
        self.description = description
        # The image ID. If you do not specify this parameter, the system automatically generates an image ID. The image ID must start with image- followed by 18 characters in letters or digits.
        self.image_id = image_id
        # The URL of the image, which can be repeated. You can call [ListImage](https://help.aliyun.com/document_detail/449118.html) to view the image URL.
        # 
        # This parameter is required.
        self.image_uri = image_uri
        # The image tag, which is an array. Each element in the array contains a key-value pair. Alibaba Cloud images have the system.official=true tag. You can add the following keys to an image:
        # 
        # *   system.chipType
        # *   system.dsw.cudaVersion
        # *   system.dsw.fromImageId
        # *   system.dsw.fromInstanceId
        # *   system.dsw.id
        # *   system.dsw.os
        # *   system.dsw.osVersion
        # *   system.dsw.resourceType
        # *   system.dsw.rootImageId
        # *   system.dsw.stage
        # *   system.dsw.tag
        # *   system.dsw.type
        # *   system.framework
        # *   system.origin
        # *   system.pythonVersion
        # *   system.source
        # *   system.supported.dlc
        # *   system.supported.dsw
        self.labels = labels
        # The image name. The name must meet the following requirements:
        # 
        # *   The name must be 1 to 50 characters in length.
        # *   The name can contain lowercase letters, digits, and hyphens (-). The name must start with a lowercase letter.
        # *   The name must be unique in a workspace.
        # 
        # This parameter is required.
        self.name = name
        # The size of the image. Unit: GB.
        self.size = size
        self.source_id = source_id
        self.source_type = source_type
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AddImageRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageResponseBody = None,
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
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageLabelsRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The following keys can be added:
        # 
        # *   system.chipType
        # *   system.dsw.cudaVersion
        # *   system.dsw.fromImageId
        # *   system.dsw.fromInstanceId
        # *   system.dsw.id
        # *   system.dsw.os
        # *   system.dsw.osVersion
        # *   system.dsw.resourceType
        # *   system.dsw.rootImageId
        # *   system.dsw.stage
        # *   system.dsw.tag
        # *   system.dsw.type
        # *   system.framework
        # *   system.origin
        # *   system.pythonVersion
        # *   system.source
        # *   system.supported.dlc
        # *   system.supported.dsw
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddImageLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[AddImageLabelsRequestLabels] = None,
    ):
        # The list of image tags.
        # 
        # This parameter is required.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = AddImageLabelsRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class AddImageLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageLabelsResponseBody = None,
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
            temp_model = AddImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMemberRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddMemberRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMemberRoleResponseBody = None,
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
            temp_model = AddMemberRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the target resource group. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.new_resource_group_id = new_resource_group_id
        # The resource ID, which is the workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.resource_id = resource_id
        # The resource group type, which must be set to workspace.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCodeSourceRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        code_branch: str = None,
        code_commit: str = None,
        code_repo: str = None,
        code_repo_access_token: str = None,
        code_repo_user_name: str = None,
        description: str = None,
        display_name: str = None,
        mount_path: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the code build. Valid values:
        # 
        # *   PUBLIC: The code build is visible to all members in the workspace.
        # *   PRIVATE: The code build is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The code branch.
        self.code_branch = code_branch
        self.code_commit = code_commit
        # The URL of the code repository.
        self.code_repo = code_repo
        # The token used to access the code repository.
        self.code_repo_access_token = code_repo_access_token
        # The username of the code repository.
        self.code_repo_user_name = code_repo_user_name
        # The description of the code build, which helps you distinguish between code builds.
        self.description = description
        # The name of the code build.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The local mount path of the code. By default, the code is mounted to the /root/code/ path.
        self.mount_path = mount_path
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
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
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateCodeSourceResponseBody(TeaModel):
    def __init__(
        self,
        code_source_id: str = None,
        request_id: str = None,
    ):
        # The ID of the created code build.
        self.code_source_id = code_source_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCodeSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCodeSourceResponseBody = None,
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
            temp_model = CreateCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionRequestModels(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        model: str = None,
        model_type: str = None,
        tool_call: bool = None,
    ):
        # The display name of the model.
        self.display_name = display_name
        # The model identifier.
        self.model = model
        # The model type. Valid values:
        # 
        # *   LLM
        # *   Embedding
        # *   ReRank
        self.model_type = model_type
        # Specifies whether a tool can be called by using ToolCall. Valid values:
        # 
        # *   true
        # *   false
        self.tool_call = tool_call

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.model is not None:
            result['Model'] = self.model
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')
        return self


class CreateConnectionRequestResourceMeta(TeaModel):
    def __init__(
        self,
        extra: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.extra = extra
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class CreateConnectionRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        configs: Dict[str, str] = None,
        connection_name: str = None,
        connection_type: str = None,
        description: str = None,
        models: List[CreateConnectionRequestModels] = None,
        resource_meta: CreateConnectionRequestResourceMeta = None,
        secrets: Dict[str, str] = None,
        workspace_id: str = None,
    ):
        # The accessibility of the workspace. Valid values:
        # 
        # *   PRIVATE: The workspace is accessible only to you and the administrator of the workspace. This is the default value.
        # *   PUBLIC: The workspace is accessible to all users in the workspace.
        self.accessibility = accessibility
        # The connection configurations, in key-value pairs. The key varies based on the connection type. For more information, see the supplementary notes below the request parameters.
        # 
        # This parameter is required.
        self.configs = configs
        # The connection name.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The connection type. Valid values:
        # 
        # *   DashScopeConnection: Alibaba Cloud Model Studio connection
        # *   OpenLLMConnection: open source model connection
        # *   MilvusConnection: Milvus connection
        # *   OpenSearchConnection: OpenSearch connection
        # *   LindormConnection: Lindorm connection
        # *   ElasticsearchConnection: Elasticsearch connection
        # *   HologresConnection: Hologres connection
        # *   RDSConnection: RDS connection
        # *   CustomConnection: custom connection
        self.connection_type = connection_type
        # The connection description.
        self.description = description
        # The models, which apply to model service connections.
        self.models = models
        # The instance resource information of the connection, which applies to database connections.
        self.resource_meta = resource_meta
        # The configuration to be encrypted. Examples: the database logon account and password and the key of the model service.
        self.secrets = secrets
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()
        if self.resource_meta:
            self.resource_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.description is not None:
            result['Description'] = self.description
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.resource_meta is not None:
            result['ResourceMeta'] = self.resource_meta.to_map()
        if self.secrets is not None:
            result['Secrets'] = self.secrets
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = CreateConnectionRequestModels()
                self.models.append(temp_model.from_map(k))
        if m.get('ResourceMeta') is not None:
            temp_model = CreateConnectionRequestResourceMeta()
            self.resource_meta = temp_model.from_map(m['ResourceMeta'])
        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateConnectionResponseBody(TeaModel):
    def __init__(
        self,
        connection_id: str = None,
        request_id: str = None,
    ):
        # The connection ID.
        self.connection_id = connection_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConnectionResponseBody = None,
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
            temp_model = CreateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        data_type: str = None,
        description: str = None,
        edition: str = None,
        import_info: str = None,
        labels: List[Label] = None,
        mount_access_read_write_role_id_list: List[str] = None,
        name: str = None,
        options: str = None,
        property: str = None,
        provider: str = None,
        provider_type: str = None,
        source_dataset_id: str = None,
        source_dataset_version: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
        user_id: str = None,
        version_description: str = None,
        version_labels: List[Label] = None,
        workspace_id: str = None,
    ):
        # The workspace accessibility. Valid values:
        # 
        # *   PRIVATE: The workspace is accessible only to you and the administrator of the workspace. This is the default value.
        # *   PUBLIC: The workspace is accessible to all users.
        self.accessibility = accessibility
        # The number of dataset files.
        self.data_count = data_count
        # The size of the dataset file. Unit: bytes.
        self.data_size = data_size
        # The data source type. Valid values:
        # 
        # *   OSS: Object Storage Service (OSS).
        # *   NAS: File Storage NAS (NAS).
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The type of the dataset. Default value: COMMON. Valid values:
        # 
        # *   COMMON: common
        # *   PIC: picture
        # *   TEXT: text
        # *   Video: video
        # *   AUDIO: audio
        self.data_type = data_type
        # The description of the dataset. Descriptions are used to differentiate datasets.
        self.description = description
        self.edition = edition
        # The dataset configurations to be imported to a storage, such as OSS, NAS, or Cloud Parallel File Storage (CPFS).
        # 
        # **OSS**\
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "bucket": "${bucket}",//The bucket name.\\
        # "path": "${path}" // The file path.\\
        # }\\
        # 
        # 
        # **NAS**\
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "fileSystemId": "${file_system_id}", // The file system ID.\\
        # "path": "${path}", // The file system path.\\
        # "mountTarget": "${mount_target}" // The mount point of the file system.\\
        # }\\
        # 
        # 
        # **CPFS**\
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "fileSystemId": "${file_system_id}", // The file system ID.\\
        # "protocolServiceId":"${protocol_service_id}", // The file system protocol service.\\
        # "exportId": "${export_id}", // The file system export directory.\\
        # "path": "${path}", // The file system path.\\
        # }\\
        # 
        # 
        # **CPFS for Lingjun**\
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "fileSystemId": "${file_system_id}", // The file system ID.\\
        # "path": "${path}", // The file system path.\\
        # "mountTarget": "${mount_target}" // The mount point of the file system, CPFS for Lingjun only.\\
        # "isVpcMount": boolean, // Whether the mount point is a virtual private cloud (VPC) mount point, CPFS for Lingjun only.\\
        # }\\
        self.import_info = import_info
        # The tags.
        self.labels = labels
        # The list of role names in the workspace that have read and write permissions on the mounted database. The names start with PAI are basic role names and the names start with role- are custom role names. If the list contains asterisks (\\*), all roles have read and write permissions.
        # 
        # *   If you set the value to ["PAI.AlgoOperator", "role-hiuwpd01ncrokkgp21"], the account of the specified role is granted the read and write permissions.
        # *   If you set the value to ["\\*"], all accounts are granted the read and write permissions.
        # *   If you set the value to [], only the creator of the dataset has the read and write permissions.
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        # The dataset name. The name must meet the following requirements:
        # 
        # *   The name must start with a letter, digit, or Chinese character.
        # *   The name can contain underscores (_) and hyphens (-).
        # *   The name must be 1 to 127 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The extended field, which is a JSON string. When you use the dataset in Deep Learning Containers (DLC), you can configure the mountPath field to specify the default mount path of the dataset.
        self.options = options
        # The property of the dataset. Valid values:
        # 
        # *   FILE
        # *   DIRECTORY
        # 
        # This parameter is required.
        self.property = property
        # The dataset provider. The value cannot be set to pai.
        self.provider = provider
        # The source type of the dataset. Valid values:
        # 
        # *   Ecs (default)
        # *   Lingjun
        self.provider_type = provider_type
        # The ID of the source dataset for the labeled dataset.
        self.source_dataset_id = source_dataset_id
        # The version of the source dataset for the labeled dataset.
        self.source_dataset_version = source_dataset_version
        # The data source ID.
        # 
        # *   If SourceType is set to USER, the value of SourceId is a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The type of the data source. Default value: USER.
        # 
        # Valid values:
        # 
        # *   PAI_PUBLIC_DATASET: a public dataset of PAI.
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
        self.source_type = source_type
        # The URI of the data source.
        # 
        # *   Value format if DataSourceType is set to OSS: `oss://bucket.endpoint/object`.
        # *   Value formats if DataSourceType is set to NAS: General-purpose NAS: `nas://<nasfisid>.region/subpath/to/dir/`. CPFS 1.0: `nas://<cpfs-fsid>.region/subpath/to/dir/`. CPFS 2.0: `nas://<cpfs-fsid>.region/<protocolserviceid>/`. You can distinguish CPFS 1.0 and CPFS 2.0 file systems based on the format of the file system ID: The ID for CPFS 1.0 is in the cpfs-<8-bit ASCII characters> format. The ID for CPFS 2.0 is in the cpfs-<16-bit ASCII characters> format.
        # 
        # This parameter is required.
        self.uri = uri
        # The ID of the Alibaba Cloud account to which the dataset belongs. The workspace owner and administrator have permissions to create datasets for specified members in the workspace.
        self.user_id = user_id
        # The description of the dataset of the initial version.
        self.version_description = version_description
        # The list of tags to be added to the dataset of the initial version.
        self.version_labels = version_labels
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID. If you do not specify this parameter, the default workspace is used. If the default workspace does not exist, an error is reported.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.version_labels:
            for k in self.version_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.data_count is not None:
            result['DataCount'] = self.data_count
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.import_info is not None:
            result['ImportInfo'] = self.import_info
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.mount_access_read_write_role_id_list is not None:
            result['MountAccessReadWriteRoleIdList'] = self.mount_access_read_write_role_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        if self.property is not None:
            result['Property'] = self.property
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id
        if self.source_dataset_version is not None:
            result['SourceDatasetVersion'] = self.source_dataset_version
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        result['VersionLabels'] = []
        if self.version_labels is not None:
            for k in self.version_labels:
                result['VersionLabels'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('MountAccessReadWriteRoleIdList') is not None:
            self.mount_access_read_write_role_id_list = m.get('MountAccessReadWriteRoleIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')
        if m.get('SourceDatasetVersion') is not None:
            self.source_dataset_version = m.get('SourceDatasetVersion')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        self.version_labels = []
        if m.get('VersionLabels') is not None:
            for k in m.get('VersionLabels'):
                temp_model = Label()
                self.version_labels.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        request_id: str = None,
    ):
        # The dataset ID.
        self.dataset_id = dataset_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetResponseBody = None,
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
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetFileMetasRequest(TeaModel):
    def __init__(
        self,
        dataset_file_metas: List[DatasetFileMetaContentCreate] = None,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The metadata of the file.
        # 
        # This parameter is required.
        self.dataset_file_metas = dataset_file_metas
        # The dataset version name.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_file_metas:
            for k in self.dataset_file_metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetFileMetas'] = []
        if self.dataset_file_metas is not None:
            for k in self.dataset_file_metas:
                result['DatasetFileMetas'].append(k.to_map() if k else None)
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_file_metas = []
        if m.get('DatasetFileMetas') is not None:
            for k in m.get('DatasetFileMetas'):
                temp_model = DatasetFileMetaContentCreate()
                self.dataset_file_metas.append(temp_model.from_map(k))
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDatasetFileMetasResponseBody(TeaModel):
    def __init__(
        self,
        failed_details: List[DatasetFileMetaResponse] = None,
        request_id: str = None,
        status: bool = None,
        succeed_details: List[DatasetFileMetaResponse] = None,
    ):
        # The metadata that failed to be created.
        self.failed_details = failed_details
        # The request ID.
        self.request_id = request_id
        # Indicates whether the metadata records of all dataset files were created. The value true indicates that the metadata records of all dataset files are created. If the value is false, view the failure details specified by FailedDetails.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.status = status
        # The metadata that is created.
        self.succeed_details = succeed_details

    def validate(self):
        if self.failed_details:
            for k in self.failed_details:
                if k:
                    k.validate()
        if self.succeed_details:
            for k in self.succeed_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedDetails'] = []
        if self.failed_details is not None:
            for k in self.failed_details:
                result['FailedDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        result['SucceedDetails'] = []
        if self.succeed_details is not None:
            for k in self.succeed_details:
                result['SucceedDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_details = []
        if m.get('FailedDetails') is not None:
            for k in m.get('FailedDetails'):
                temp_model = DatasetFileMetaResponse()
                self.failed_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.succeed_details = []
        if m.get('SucceedDetails') is not None:
            for k in m.get('SucceedDetails'):
                temp_model = DatasetFileMetaResponse()
                self.succeed_details.append(temp_model.from_map(k))
        return self


class CreateDatasetFileMetasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetFileMetasResponseBody = None,
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
            temp_model = CreateDatasetFileMetasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetJobRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        description: str = None,
        job_action: str = None,
        job_mode: str = None,
        job_spec: str = None,
        workspace_id: str = None,
    ):
        # The dataset version.
        self.dataset_version = dataset_version
        # The job description.
        self.description = description
        # The job action.
        # 
        # Valid values:
        # 
        # *   SemanticIndex
        # *   IntelligentTag
        # *   FileMetaExport
        # 
        # This parameter is required.
        self.job_action = job_action
        # The job mode.
        # 
        # Valid values:
        # 
        # *   Full: full mode.
        self.job_mode = job_mode
        # The job configuration.
        # 
        # This parameter is required.
        self.job_spec = job_spec
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.description is not None:
            result['Description'] = self.description
        if self.job_action is not None:
            result['JobAction'] = self.job_action
        if self.job_mode is not None:
            result['JobMode'] = self.job_mode
        if self.job_spec is not None:
            result['JobSpec'] = self.job_spec
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')
        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')
        if m.get('JobSpec') is not None:
            self.job_spec = m.get('JobSpec')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDatasetJobResponseBody(TeaModel):
    def __init__(
        self,
        dataset_job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the dataset job.
        self.dataset_job_id = dataset_job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_job_id is not None:
            result['DatasetJobId'] = self.dataset_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetJobId') is not None:
            self.dataset_job_id = m.get('DatasetJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetJobResponseBody = None,
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
            temp_model = CreateDatasetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetJobConfigRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The configuration content. Format:
        # 
        # *   MultimodalIntelligentTag
        # 
        # { "apiKey":"sk-xxxxxxxxxxxxxxxxxxxxx" }
        # 
        # *   MultimodalSemanticIndex
        # 
        # { "defaultModelId": "xxx" "defaultModelVersion":"1.0.0" }
        # 
        # This parameter is required.
        self.config = config
        # The configuration type.
        # 
        # Valid values:
        # 
        # *   MultimodalIntelligentTag
        # *   MultimodalSemanticIndex
        # 
        # This parameter is required.
        self.config_type = config_type
        self.dataset_version = dataset_version
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDatasetJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        dataset_job_config_id: str = None,
        request_id: str = None,
    ):
        # The configuration ID.
        self.dataset_job_config_id = dataset_job_config_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_job_config_id is not None:
            result['DatasetJobConfigId'] = self.dataset_job_config_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetJobConfigId') is not None:
            self.dataset_job_config_id = m.get('DatasetJobConfigId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetJobConfigResponseBody = None,
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
            temp_model = CreateDatasetJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[Label] = None,
    ):
        # The tags.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        return self


class CreateDatasetLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetLabelsResponseBody = None,
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
            temp_model = CreateDatasetLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetVersionRequest(TeaModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        description: str = None,
        import_info: str = None,
        labels: List[Label] = None,
        options: str = None,
        property: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
    ):
        # The number of dataset files.
        self.data_count = data_count
        # The size of the dataset file. Unit: bytes.
        self.data_size = data_size
        # The type of the data source. Separate multiple types with commas (,). Valid values:
        # 
        # *   NAS: File Storage NAS (NAS).
        # *   OSS: Object Storage Service (OSS).
        # *   CPFS
        # 
        # Note: The DataSourceType value of a dataset version must be the same as that of the dataset. When you create a dataset version, the system checks whether the values are the same.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The description of the dataset. Descriptions are used to differentiate datasets.
        self.description = description
        # The dataset storage import configurations, such as OSS, NAS, and CPFS.
        # 
        # **OSS**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "bucket": "${bucket}",//The bucket name\\
        # "path": "${path}" // The file path\\
        # }\\
        # 
        # 
        # **NAS**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "path": "${path}", // The file system path\\
        # "mountTarget": "${mount_target}" // The mount point of the file system\\
        # }\\
        # 
        # 
        # **CPFS**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "protocolServiceId":"${protocol_service_id}", // The file system protocol service\\
        # "exportId": "${export_id}", // The file system export directory\\
        # "path": "${path}", // The file system path\\
        # }\\
        # 
        # 
        # **CPFS for Lingjun**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "path": "${path}", // The ile system path\\
        # "mountTarget": "${mount_target}" // The mount point of the file system, CPFS for Lingjun only\\
        # "isVpcMount": boolean, // Whether the mount point is a VPC mount point, CPFS for Lingjun only\\
        # }\\
        self.import_info = import_info
        # The tags of the dataset version.
        self.labels = labels
        # The extended field, which is of the JsonString type. When you use the dataset in Deep Learning Containers (DLC), you can use the mountPath field to specify the default mount path of the dataset.
        self.options = options
        # The property of the dataset. Valid values:
        # 
        # *   FILE
        # *   DIRECTORY
        # 
        # This parameter is required.
        self.property = property
        # The ID of the data source.
        # 
        # *   If SourceType is set to USER, the value of SourceId can be a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The type of the data source. Default value: USER. Valid values:
        # 
        # *   PAI-PUBLIC-DATASET: a public dataset of Platform for AI (PAI).
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
        # 
        # For each job type:
        # 
        # *   PAI_PUBLIC_DATASET: PAI_PUBLIC_DATASET.
        # *   ITAG: ITAG.
        # *   USER: USER.
        self.source_type = source_type
        # Example format:
        # 
        # *   Value format when DataSourceType is set to OSS: `oss://bucket.endpoint/object`.
        # *   Value formats when DataSourceType is set to NAS: General-purpose NAS: `nas://<nasfisid>.region/subpath/to/dir/`. CPFS 1.0: `nas://<cpfs-fsid>.region/subpath/to/dir/`. CPFS 2.0: `nas://<cpfs-fsid>.region/<protocolserviceid>/`. You can distinguish CPFS 1.0 and CPFS 2.0 file systems based on the format of the file system ID: The ID for CPFS 1.0 is in the cpfs-<8-bit ASCII characters> format. The ID for CPFS 2.0 is in the cpfs-<16-bit ASCII characters> format.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_count is not None:
            result['DataCount'] = self.data_count
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.description is not None:
            result['Description'] = self.description
        if self.import_info is not None:
            result['ImportInfo'] = self.import_info
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.options is not None:
            result['Options'] = self.options
        if self.property is not None:
            result['Property'] = self.property
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateDatasetVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_name: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The dataset version name.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateDatasetVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetVersionResponseBody = None,
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
            temp_model = CreateDatasetVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetVersionLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[Label] = None,
    ):
        # The tags.
        # 
        # This parameter is required.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        return self


class CreateDatasetVersionLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetVersionLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasetVersionLabelsResponseBody = None,
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
            temp_model = CreateDatasetVersionLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        artifact_uri: str = None,
        labels: List[LabelInfo] = None,
        name: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the experiment. Valid values: PRIVATE (the experiment is visible only to the creator and the Alibaba Cloud account) and PUBLIC (the experiment is visible to all users). This parameter is optional and the default value is PRIVATE.
        self.accessibility = accessibility
        # The default artifact output path of all jobs that are associated with the experiment. Only Object Storage Service (OSS) paths are supported.
        self.artifact_uri = artifact_uri
        # The tags.
        self.labels = labels
        # The experiment name. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be 1 to 63 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.artifact_uri is not None:
            result['ArtifactUri'] = self.artifact_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('ArtifactUri') is not None:
            self.artifact_uri = m.get('ArtifactUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = LabelInfo()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        request_id: str = None,
    ):
        # The returned data. If the operation is asynchronously implemented, the job ID is returned.
        self.experiment_id = experiment_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentResponseBody = None,
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
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMemberRequestMembers(TeaModel):
    def __init__(
        self,
        roles: List[str] = None,
        user_id: str = None,
    ):
        # The list of roles.
        # 
        # This parameter is required.
        self.roles = roles
        # The member IDs. Multiple member IDs are separated by commas (,). You can call [ListMembers](https://help.aliyun.com/document_detail/449135.html) to obtain the member IDs.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateMemberRequest(TeaModel):
    def __init__(
        self,
        members: List[CreateMemberRequestMembers] = None,
    ):
        # The members.
        # 
        # This parameter is required.
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = CreateMemberRequestMembers()
                self.members.append(temp_model.from_map(k))
        return self


class CreateMemberResponseBodyMembers(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        member_id: str = None,
        roles: List[str] = None,
        user_id: str = None,
    ):
        # The display name.
        self.display_name = display_name
        # The member ID.
        self.member_id = member_id
        # The list of roles.
        self.roles = roles
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateMemberResponseBody(TeaModel):
    def __init__(
        self,
        members: List[CreateMemberResponseBodyMembers] = None,
        request_id: str = None,
    ):
        # The returned members.
        self.members = members
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = CreateMemberResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMemberResponseBody = None,
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
            temp_model = CreateMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        labels: List[Label] = None,
        model_description: str = None,
        model_doc: str = None,
        model_name: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        parameter_size: int = None,
        tag: List[Label] = None,
        task: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the model in the workspace. Valid values:
        # 
        # *   PRIVATE (default): Visible only to you and the administrator of the workspace.
        # *   PUBLIC: Vvisible to all users in the workspace.
        self.accessibility = accessibility
        # The domain of the model. Describes the domain in which the model is for. Example: nlp (natural language processing), cv (computer vision), and others.
        self.domain = domain
        # Other information about the model.
        self.extra_info = extra_info
        # The tags. This parameter will be deprecated and replaced by Tag.
        self.labels = labels
        # The model description, used to distinguish different models.
        self.model_description = model_description
        # The documentation of the model.
        self.model_doc = model_doc
        # The name of the model. The name must be 1 to 127 characters in length.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The model type. Example: Checkpoint or LoRA.
        self.model_type = model_type
        # The sequence number of the model. Can be used for custom sorting.
        self.order_number = order_number
        # The source of the model. The community or organization to which the source model belongs, such as ModelScope or HuggingFace.
        self.origin = origin
        self.parameter_size = parameter_size
        # The tags.
        self.tag = tag
        # The task of the model. Describes the specific problem that the model solves. Example: text-classification.
        self.task = task
        # The workspace ID. Call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.model_description is not None:
            result['ModelDescription'] = self.model_description
        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.order_number is not None:
            result['OrderNumber'] = self.order_number
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.parameter_size is not None:
            result['ParameterSize'] = self.parameter_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.task is not None:
            result['Task'] = self.task
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')
        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('ParameterSize') is not None:
            self.parameter_size = m.get('ParameterSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = Label()
                self.tag.append(temp_model.from_map(k))
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(
        self,
        model_id: str = None,
        request_id: str = None,
    ):
        # The model ID.
        self.model_id = model_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelResponseBody = None,
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
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[Label] = None,
    ):
        # The tags.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        return self


class CreateModelLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelLabelsResponseBody = None,
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
            temp_model = CreateModelLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelVersionRequest(TeaModel):
    def __init__(
        self,
        approval_status: str = None,
        compression_spec: Dict[str, Any] = None,
        distillation_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        extra_info: Dict[str, Any] = None,
        format_type: str = None,
        framework_type: str = None,
        inference_spec: Dict[str, Any] = None,
        labels: List[Label] = None,
        metrics: Dict[str, Any] = None,
        options: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        uri: str = None,
        version_description: str = None,
        version_name: str = None,
    ):
        # The approval status. Valid values:
        # 
        # *   Pending
        # *   Approved
        # *   Rejected
        self.approval_status = approval_status
        # The compression configuration.
        self.compression_spec = compression_spec
        self.distillation_spec = distillation_spec
        # The evaluation configuration.
        self.evaluation_spec = evaluation_spec
        # The additional information.
        self.extra_info = extra_info
        # The model format. Valid values:
        # 
        # *   OfflineModel
        # *   SavedModel
        # *   Keras H5
        # *   Frozen Pb
        # *   Caffe Prototxt
        # *   TorchScript
        # *   XGBoost
        # *   PMML
        # *   AlinkModel
        # *   ONNX
        self.format_type = format_type
        # The model framework. Valid values:
        # 
        # *   Pytorch
        # *   XGBoost
        # *   Keras
        # *   Caffe
        # *   Alink
        # *   Xflow
        # *   TensorFlow
        self.framework_type = framework_type
        # Describes how to apply to downstream inference services. For example, describe the processor and container of EAS. Example: `{ "processor": "tensorflow_gpu_1.12" }`
        self.inference_spec = inference_spec
        # The labels.
        self.labels = labels
        # The metrics for the model. The length after serialization is limited to 8,192.
        self.metrics = metrics
        # The extended field. This is a JSON string.
        self.options = options
        # The ID of the model source.
        # 
        # *   If SourceType is set to Custom, this parameter is not limited.
        # *   If SourceType is set to PAIFlow or TrainingService, the ID of the model source is in the following format:
        # 
        # <!---->
        # 
        #     region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # 
        # Take note of the following parameters:
        # 
        # *   region indicates the region ID.
        # *   workspaceId indicates the workspace ID.
        # *   kind indicates the type. Valid values: PipelineRun (PAIFlow) and ServiceJob (training service).
        # *   id indicates the unique identifier.
        self.source_id = source_id
        # The type of the model source. Valid values:
        # 
        # *   Custom (default)
        # *   PAIFlow
        # *   TrainingService: the Platform for AI (PAI) training service.
        self.source_type = source_type
        # The training configurations, which is used for fine-tuning and incremental training.
        self.training_spec = training_spec
        # The URI of the model version, which is the location where the model is stored. Valid values:
        # 
        # *   The HTTP(S) address of the model. Example: `https://myweb.com/mymodel.tar.gz`.
        # *   The OSS path of the model, in the format of `oss://<bucket>.<endpoint>/object`. For information about endpoints, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html). Example: `oss://mybucket.oss-cn-beijing.aliyuncs.com/mypath/`.
        # 
        # This parameter is required.
        self.uri = uri
        # The version description.
        self.version_description = version_description
        # The model version, which is unique for each model. If you leave this parameter empty, the first version is **0.1.0** by default. After that, the minor version number is increased by 1 in sequence. For example, the second version number is **0.2.0**. A version number consists of a major version number, a minor version number, and a stage version number, separated by periods (.). The major version number and minor version number are numeric. The stage version number begins with a digit and can include numbers, underscores, and letters. For example, the version number is 1.1.0 or 2.3.4_beta.
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status
        if self.compression_spec is not None:
            result['CompressionSpec'] = self.compression_spec
        if self.distillation_spec is not None:
            result['DistillationSpec'] = self.distillation_spec
        if self.evaluation_spec is not None:
            result['EvaluationSpec'] = self.evaluation_spec
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type
        if self.inference_spec is not None:
            result['InferenceSpec'] = self.inference_spec
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.options is not None:
            result['Options'] = self.options
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.training_spec is not None:
            result['TrainingSpec'] = self.training_spec
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')
        if m.get('CompressionSpec') is not None:
            self.compression_spec = m.get('CompressionSpec')
        if m.get('DistillationSpec') is not None:
            self.distillation_spec = m.get('DistillationSpec')
        if m.get('EvaluationSpec') is not None:
            self.evaluation_spec = m.get('EvaluationSpec')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')
        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TrainingSpec') is not None:
            self.training_spec = m.get('TrainingSpec')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_name: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The version of the model.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelVersionResponseBody = None,
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
            temp_model = CreateModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelVersionLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[Label] = None,
    ):
        # The tags.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        return self


class CreateModelVersionLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelVersionLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelVersionLabelsResponseBody = None,
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
            temp_model = CreateModelVersionLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductOrdersRequestProductsInstanceProperties(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property name.
        self.name = name
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateProductOrdersRequestProducts(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        instance_properties: List[CreateProductOrdersRequestProductsInstanceProperties] = None,
        order_type: str = None,
        pricing_cycle: str = None,
        product_code: str = None,
    ):
        # Specifies whether to automatically renew the product.
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # The billing method. Only POSTPAY is supported.
        self.charge_type = charge_type
        # The purchase duration. You can use this parameter together with pricingCycle. Only 1 is supported.
        self.duration = duration
        # The properties of the instance.
        # 
        # *   DataWorks_share: [ { "Code": "region", "Value": "cn-shanghai" } ]
        # *   OSS_share: [ { "Code": "commodity_type", "Value": "oss", "Name": "Object Storage Service" }, { "Code": "ord_time", "Value": "1:Hour", "Name": "1 Hour" } ]
        # *   PAI_share: None
        # *   China bid MaxCompute_share: [ { "Code": "region", "Value": "cn-hangzhou" }, { "Code": "odps_specification_type", "Value": "OdpsStandard" }, { "Code": "ord_time", "Value": "1:Hour" } ]
        # *   International bid MaxCompute_share: [ { "Code": "region", "Value": "cn-hangzhou" }, { "Code": "ord_time", "Value": "1:Hour" } ]
        self.instance_properties = instance_properties
        # The type of the order. Only BUY is supported.
        self.order_type = order_type
        # The billing cycle. Valid values:
        # 
        # *   Month: The price is calculated every month. DataWorks_share only supports Month.
        # *   Hour: The price is calculated every hour. OSS_share and MaxCompute_share only support Hour.
        self.pricing_cycle = pricing_cycle
        # The product code. Valid values:
        # 
        # *   DataWorks_share: pay-as-you-go DataWorks
        # *   MaxCompute_share: pay-as-you-go MaxCompute
        # *   PAI_share: pay-as-you-go PAI.
        # *   OSS_share: pay-as-you-go OSS
        self.product_code = product_code

    def validate(self):
        if self.instance_properties:
            for k in self.instance_properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.duration is not None:
            result['Duration'] = self.duration
        result['InstanceProperties'] = []
        if self.instance_properties is not None:
            for k in self.instance_properties:
                result['InstanceProperties'].append(k.to_map() if k else None)
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.instance_properties = []
        if m.get('InstanceProperties') is not None:
            for k in m.get('InstanceProperties'):
                temp_model = CreateProductOrdersRequestProductsInstanceProperties()
                self.instance_properties.append(temp_model.from_map(k))
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class CreateProductOrdersRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        products: List[CreateProductOrdersRequestProducts] = None,
    ):
        # Specifies whether to automatically pay for the provided products.
        # 
        # *   true
        # *   false
        self.auto_pay = auto_pay
        # The list of products to be purchased. Separate them with commas (,).
        self.products = products

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        result['Products'] = []
        if self.products is not None:
            for k in self.products:
                result['Products'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        self.products = []
        if m.get('Products') is not None:
            for k in m.get('Products'):
                temp_model = CreateProductOrdersRequestProducts()
                self.products.append(temp_model.from_map(k))
        return self


class CreateProductOrdersResponseBody(TeaModel):
    def __init__(
        self,
        buy_product_request_id: str = None,
        message: str = None,
        order_id: str = None,
        product_ids: List[str] = None,
        request_id: str = None,
    ):
        # The ID of the product purchase request.
        self.buy_product_request_id = buy_product_request_id
        # The returned message.
        self.message = message
        # The purchase order ID.
        self.order_id = order_id
        self.product_ids = product_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_product_request_id is not None:
            result['BuyProductRequestId'] = self.buy_product_request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyProductRequestId') is not None:
            self.buy_product_request_id = m.get('BuyProductRequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProductOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductOrdersResponseBody = None,
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
            temp_model = CreateProductOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRunRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        labels: List[Label] = None,
        name: str = None,
        params: List[RunParam] = None,
        source_id: str = None,
        source_type: str = None,
    ):
        # The ID of the experiment that corresponds to the run.
        # 
        # This parameter is required.
        self.experiment_id = experiment_id
        # The list of tags added to the run.
        self.labels = labels
        # The name of the run. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be 1 to 63 characters in length.
        # 
        # If the name is left empty when you create a run, a random run ID generated by the server is used as the name.
        self.name = name
        # The parameters of the run.
        self.params = params
        # The ID of the workload associated with the run.
        self.source_id = source_id
        # The type of the workload source that is associated with the run. Valid values: TrainingService and DLC. You can also leave this parameter empty. This parameter is optional and left empty by default.
        self.source_type = source_type

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = RunParam()
                self.params.append(temp_model.from_map(k))
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class CreateRunResponseBody(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        request_id: str = None,
    ):
        # The run ID.
        self.run_id = run_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRunResponseBody = None,
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
            temp_model = CreateRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        env_types: List[str] = None,
        resource_group_id: str = None,
        workspace_name: str = None,
    ):
        # The description of the workspace. The description can be up to 80 characters in length.
        # 
        # This parameter is required.
        self.description = description
        # The display name of the workspace. You can set it based on the purpose of the workspace. If left empty, the name of the workspace is used.
        self.display_name = display_name
        # The environment of the workspace.
        # 
        # *   Workspaces in basic mode can run only in the production environment (prod).
        # *   Workspaces in standard mode can run in both the development and production environments (dev and prod).
        # 
        # This parameter is required.
        self.env_types = env_types
        self.resource_group_id = resource_group_id
        # The name of the workspace. Format:
        # 
        # *   The name must be 3 to 23 characters in length, and can contain letters, underscores (_), and digits.
        # *   The name must start with a letter.
        # *   It must be unique in the current region.
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env_types is not None:
            result['EnvTypes'] = self.env_types
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkspaceResponseBody = None,
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
            temp_model = CreateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceResourceRequestResourcesLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key.
        self.key = key
        # The label value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateWorkspaceResourceRequestResourcesQuotas(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The quota ID. You can call [ListQuotas](https://help.aliyun.com/document_detail/449144.html) to obtain the quota ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateWorkspaceResourceRequestResources(TeaModel):
    def __init__(
        self,
        env_type: str = None,
        group_name: str = None,
        is_default: bool = None,
        labels: List[CreateWorkspaceResourceRequestResourcesLabels] = None,
        name: str = None,
        product_type: str = None,
        quotas: List[CreateWorkspaceResourceRequestResourcesQuotas] = None,
        resource_type: str = None,
        spec: Dict[str, Any] = None,
        workspace_id: str = None,
    ):
        # The environment type. Valid values:
        # 
        # *   dev: development environment
        # *   prod: production environment
        # 
        # This parameter is required.
        self.env_type = env_type
        # The name of the resource group, which is unique within your Alibaba Cloud account. This parameter is required for MaxCompute, Elastic Compute Service (ECS), Lingjun, Alibaba Cloud Container Compute Service (ACS), and Realtime Compute for Apache Flink resources.
        self.group_name = group_name
        # Specifies whether the resource is the default resource. Each type of resources has a default resource. Valid values:
        # 
        # *   false (default)
        # *   true
        self.is_default = is_default
        # The labels added to the resource.
        self.labels = labels
        # The resource name. The name must meet the following requirements:
        # 
        # *   The name must be 3 to 28 characters in length, and can contain only letters, digits, and underscores (_). The name must start with a letter.
        # *   The name must be unique in the region.
        # 
        # This parameter is required.
        self.name = name
        # **This parameter is no longer used and will be removed. Use the ResourceType parameter instead.
        self.product_type = product_type
        # The quotas. Only MaxCompute quotas are available.
        self.quotas = quotas
        # The resource types. Valid values:
        # 
        # *   MaxCompute
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        self.resource_type = resource_type
        # The resource specifications in the JSON format.
        self.spec = spec
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateWorkspaceResourceRequestResourcesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = CreateWorkspaceResourceRequestResourcesQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWorkspaceResourceRequest(TeaModel):
    def __init__(
        self,
        option: str = None,
        resources: List[CreateWorkspaceResourceRequestResources] = None,
    ):
        # The operation to perform. Valid values:
        # 
        # *   CreateAndAttach: creates resources and associates the resources with a workspace.
        # *   Attach: associates resources with a workspace.
        # 
        # >  MaxCompute supports only the Attach operation.
        self.option = option
        # The resources.
        # 
        # This parameter is required.
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option is not None:
            result['Option'] = self.option
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            self.option = m.get('Option')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = CreateWorkspaceResourceRequestResources()
                self.resources.append(temp_model.from_map(k))
        return self


class CreateWorkspaceResourceResponseBodyResources(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The resource ID.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateWorkspaceResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[CreateWorkspaceResourceResponseBodyResources] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources
        # The total number of resources.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = CreateWorkspaceResourceResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateWorkspaceResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkspaceResourceResponseBody = None,
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
            temp_model = CreateWorkspaceResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCodeSourceResponseBody(TeaModel):
    def __init__(
        self,
        code_source_id: str = None,
        request_id: str = None,
    ):
        # The ID of the deleted code source.
        self.code_source_id = code_source_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCodeSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCodeSourceResponseBody = None,
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
            temp_model = DeleteCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        labels: str = None,
    ):
        # The category of the configuration item. Valid values:
        # 
        # *   CommonResourceConfig
        # *   DLCAutoRecycle - DLCPriorityConfig
        # *   DSWPriorityConfig
        # *   QuotaMaximumDuration
        # *   CommonTagConfig
        self.category_name = category_name
        # The filter conditions. Separate multiple conditions with commas (,). The conditions have an AND relationship.
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class DeleteConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConfigResponseBody = None,
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
            temp_model = DeleteConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConnectionResponseBody = None,
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
            temp_model = DeleteConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetResponseBody = None,
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
            temp_model = DeleteDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetFileMetasRequest(TeaModel):
    def __init__(
        self,
        dataset_file_meta_ids: str = None,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The metadata ID of the dataset file.
        # 
        # This parameter is required.
        self.dataset_file_meta_ids = dataset_file_meta_ids
        # The dataset version.
        self.dataset_version = dataset_version
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_file_meta_ids is not None:
            result['DatasetFileMetaIds'] = self.dataset_file_meta_ids
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetFileMetaIds') is not None:
            self.dataset_file_meta_ids = m.get('DatasetFileMetaIds')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteDatasetFileMetasResponseBody(TeaModel):
    def __init__(
        self,
        failed_details: List[DatasetFileMetaResponse] = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The metadata records that fail to be deleted for the dataset files.
        self.failed_details = failed_details
        # The request ID.
        self.request_id = request_id
        # Indicates whether the metadata records of all dataset files were deleted. The value true indicates that the metadata records of all dataset files are deleted. If the value is false, view the failure details specified by FailedDetails.
        self.status = status

    def validate(self):
        if self.failed_details:
            for k in self.failed_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedDetails'] = []
        if self.failed_details is not None:
            for k in self.failed_details:
                result['FailedDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_details = []
        if m.get('FailedDetails') is not None:
            for k in m.get('FailedDetails'):
                temp_model = DatasetFileMetaResponse()
                self.failed_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDatasetFileMetasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetFileMetasResponseBody = None,
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
            temp_model = DeleteDatasetFileMetasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetJobResponseBody = None,
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
            temp_model = DeleteDatasetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetJobConfigRequest(TeaModel):
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


class DeleteDatasetJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetJobConfigResponseBody = None,
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
            temp_model = DeleteDatasetJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetLabelsRequest(TeaModel):
    def __init__(
        self,
        label_keys: str = None,
    ):
        # The tag key. You can call [GetDataset](https://help.aliyun.com/document_detail/457218.html) to obtain the tag key. Multiple tag keys are separated by commas (,).
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        return self


class DeleteDatasetLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetLabelsResponseBody = None,
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
            temp_model = DeleteDatasetLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetVersionResponseBody = None,
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
            temp_model = DeleteDatasetVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetVersionLabelsRequest(TeaModel):
    def __init__(
        self,
        keys: str = None,
    ):
        # The tag keys. Multiple tags are separated by commas (,).
        # 
        # This parameter is required.
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class DeleteDatasetVersionLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatasetVersionLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatasetVersionLabelsResponseBody = None,
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
            temp_model = DeleteDatasetVersionLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentResponseBody = None,
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
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteExperimentLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentLabelResponseBody = None,
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
            temp_model = DeleteExperimentLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMembersRequest(TeaModel):
    def __init__(
        self,
        member_ids: str = None,
    ):
        # The list of member IDs. Separate multiple member IDs with commas (,). You can call [ListMembers](https://help.aliyun.com/document_detail/449135.html) to obtain the member ID.
        # 
        # This parameter is required.
        self.member_ids = member_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_ids is not None:
            result['MemberIds'] = self.member_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberIds') is not None:
            self.member_ids = m.get('MemberIds')
        return self


class DeleteMembersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code returned if the call failed.
        self.code = code
        # The error message returned if the call failed.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMembersResponseBody = None,
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
            temp_model = DeleteMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModelResponseBody = None,
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
            temp_model = DeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelLabelsRequest(TeaModel):
    def __init__(
        self,
        label_keys: str = None,
    ):
        # The label key to be deleted. To delete multiple label keys, separate them with commas (,).
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        return self


class DeleteModelLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModelLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModelLabelsResponseBody = None,
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
            temp_model = DeleteModelLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModelVersionResponseBody = None,
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
            temp_model = DeleteModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelVersionLabelsRequest(TeaModel):
    def __init__(
        self,
        label_keys: str = None,
    ):
        # The key of the tag to be deleted. Separate multiple tag keys with commas (,).
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        return self


class DeleteModelVersionLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteModelVersionLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModelVersionLabelsResponseBody = None,
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
            temp_model = DeleteModelVersionLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRunResponseBody = None,
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
            temp_model = DeleteRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRunLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRunLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRunLabelResponseBody = None,
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
            temp_model = DeleteRunLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserConfigRequest(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        scope: str = None,
    ):
        # The configuration item keys. Currently, only customizePAIAssumedRole.
        self.config_key = config_key
        # The scope. Valid values: subUser and owner.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class DeleteUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserConfigResponseBody = None,
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
            temp_model = DeleteUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkspaceResponseBody = None,
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
            temp_model = DeleteWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceResourceRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        labels: str = None,
        option: str = None,
        product_type: str = None,
        resource_ids: str = None,
        resource_type: str = None,
    ):
        # The name of the resource group. You can call [ListResources](https://help.aliyun.com/document_detail/449143.html) to obtain the name of the resource group.
        self.group_name = group_name
        # The tags. Multiple tags are separated by commas (,).
        self.labels = labels
        # The operation to perform. Valid values:
        # 
        # *   DetachAndDelete: disassociates a resource from a workspace and deletes the resource in the workspace. This is the default value.
        # *   Detach: disassociates a resource group from a workspace.
        self.option = option
        # **This field is no longer used and will be removed. Use the ResourceType field instead.
        self.product_type = product_type
        # The resource IDs. Multiple resource IDs are separated by commas (,). The GroupName values for the specified resources must be the same. You cannot leave both GroupName and ResourceIds empty. You can specify both parameters.
        self.resource_ids = resource_ids
        # The resource type. Valid values:
        # 
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        # *   MaxCompute (This resource type is valid only if Option is set to Detach.)
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.option is not None:
            result['Option'] = self.option
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DeleteWorkspaceResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_ids: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resource IDs.
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        return self


class DeleteWorkspaceResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkspaceResourceResponseBody = None,
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
            temp_model = DeleteWorkspaceResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeSourceResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
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
        mount_path: str = None,
        request_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the code source. Valid values:
        # 
        # *   PRIVATE: Visible only to you and the administrator of the workspace.
        # *   PUBLIC: Visible to all members in the workspace.
        self.accessibility = accessibility
        # The code repository branch.
        self.code_branch = code_branch
        # The code commit ID.
        self.code_commit = code_commit
        # The address of the code repository.
        self.code_repo = code_repo
        # The token used to access the code repository.
        self.code_repo_access_token = code_repo_access_token
        # The username of the code repository.
        self.code_repo_user_name = code_repo_user_name
        # The ID of the code source.
        self.code_source_id = code_source_id
        # The description of the code source.
        self.description = description
        # The name of the code source.
        self.display_name = display_name
        # The time when the code source was created, in the ISO8601 format.
        self.gmt_create_time = gmt_create_time
        # The time when the code source was modified, in the ISO8601 format.
        self.gmt_modify_time = gmt_modify_time
        # The local mount path of the code.
        self.mount_path = mount_path
        # The request ID.
        self.request_id = request_id
        # The ID of the creator.
        self.user_id = user_id
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
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
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
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetCodeSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCodeSourceResponseBody = None,
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
            temp_model = GetCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        verbose: str = None,
    ):
        # The category of the configuration item. Valid values:
        # 
        # *   CommonResourceConfig
        # *   DLCAutoRecycle
        # *   DLCPriorityConfig
        # *   DSWPriorityConfig
        # *   QuotaMaximumDuration
        # *   CommonTagConfig
        self.category_name = category_name
        # The key of the configuration item. Valid values:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   priorityConfig: Priority configuration. This key can be used only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: Predefined tags of the workspace. Created resources must include tags.
        self.config_key = config_key
        # The value of the configuration item.
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetConfigResponseBodyLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConfigResponseBody(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[GetConfigResponseBodyLabels] = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The category of the configuration item. Valid values:
        # 
        # *   CommonResourceConfig
        # *   DLCAutoRecycle
        # *   DLCPriorityConfig
        # *   DSWPriorityConfig
        # *   QuotaMaximumDuration
        # *   CommonTagConfig
        self.category_name = category_name
        # The key of the configuration item. Valid values:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   priorityConfig: Priority configuration. This key can be used only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: Predefined tags of the workspace. Created resources must include tags.
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        # The tags of the configuration item.
        self.labels = labels
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetConfigResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConfigResponseBody = None,
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
            temp_model = GetConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionRequest(TeaModel):
    def __init__(
        self,
        encrypt_option: str = None,
    ):
        # The encryption settings. Valid values:
        # 
        # *   PlainText
        # *   Secret
        self.encrypt_option = encrypt_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_option is not None:
            result['EncryptOption'] = self.encrypt_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptOption') is not None:
            self.encrypt_option = m.get('EncryptOption')
        return self


class GetConnectionResponseBodyModels(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        model: str = None,
        model_type: str = None,
        tool_call: bool = None,
    ):
        # The display name of the model.
        self.display_name = display_name
        # The model identifier.
        self.model = model
        # The model type. Valid values:
        # 
        # *   LLM
        # *   Embedding
        # *   ReRank
        self.model_type = model_type
        # Indicates whether a tool can be called by using ToolCall. Valid values:
        # 
        # *   true
        # *   false
        self.tool_call = tool_call

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.model is not None:
            result['Model'] = self.model
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')
        return self


class GetConnectionResponseBodyResourceMeta(TeaModel):
    def __init__(
        self,
        extra: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.extra = extra
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class GetConnectionResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        configs: Dict[str, str] = None,
        connection_id: str = None,
        connection_name: str = None,
        connection_type: str = None,
        creator: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        models: List[GetConnectionResponseBodyModels] = None,
        request_id: str = None,
        resource_meta: GetConnectionResponseBodyResourceMeta = None,
        secrets: Dict[str, str] = None,
        workspace_id: str = None,
    ):
        # The resource accessibility. Valid values:
        # 
        # *   PUBLIC: All members in the workspace can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        self.accessibility = accessibility
        # The connection configuration.
        self.configs = configs
        # The connection ID.
        self.connection_id = connection_id
        # The connection name.
        self.connection_name = connection_name
        # The type of the connection. Valid values:
        # 
        # *   DashScopeConnection: Alibaba Cloud Model Studio connection.
        # *   OpenLLMConnection: Open source model connection.
        # *   MilvusConnection: Milvus connection.
        # *   OpenSearchConnection: OpenSearch connection.
        # *   LindormConnection: Lindorm connection.
        # *   ElasticsearchConnection: Elasticsearch connection.
        # *   HologresConnection: Hologres connection.
        # *   RDSConnection: RDS connection.
        # *   CustomConnection: Custom connection.
        self.connection_type = connection_type
        # The creator of the connection.
        self.creator = creator
        # The connection description.
        self.description = description
        # The time when the connection is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the connection is modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The models, which apply to model service connections.
        self.models = models
        # The request ID.
        self.request_id = request_id
        # The instance resource information of the connection, which applies to database connections.
        self.resource_meta = resource_meta
        # The encrypted configuration, in key-value pairs. Examples: the database logon password and the key of the model connection.
        self.secrets = secrets
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()
        if self.resource_meta:
            self.resource_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_meta is not None:
            result['ResourceMeta'] = self.resource_meta.to_map()
        if self.secrets is not None:
            result['Secrets'] = self.secrets
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = GetConnectionResponseBodyModels()
                self.models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceMeta') is not None:
            temp_model = GetConnectionResponseBodyResourceMeta()
            self.resource_meta = temp_model.from_map(m['ResourceMeta'])
        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConnectionResponseBody = None,
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
            temp_model = GetConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetResponseBodySharingConfig(TeaModel):
    def __init__(
        self,
        shared_to: List[DatasetShareRelationship] = None,
    ):
        self.shared_to = shared_to

    def validate(self):
        if self.shared_to:
            for k in self.shared_to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SharedTo'] = []
        if self.shared_to is not None:
            for k in self.shared_to:
                result['SharedTo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shared_to = []
        if m.get('SharedTo') is not None:
            for k in m.get('SharedTo'):
                temp_model = DatasetShareRelationship()
                self.shared_to.append(temp_model.from_map(k))
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        data_source_type: str = None,
        data_type: str = None,
        dataset_id: str = None,
        description: str = None,
        edition: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        import_info: str = None,
        is_shared: bool = None,
        labels: List[Label] = None,
        latest_version: DatasetVersion = None,
        mount_access: str = None,
        mount_access_read_write_role_id_list: List[str] = None,
        name: str = None,
        options: str = None,
        owner_id: str = None,
        property: str = None,
        provider: str = None,
        provider_type: str = None,
        request_id: str = None,
        shared_from: DatasetShareRelationship = None,
        sharing_config: GetDatasetResponseBodySharingConfig = None,
        source_dataset_id: str = None,
        source_dataset_version: str = None,
        source_id: str = None,
        source_type: str = None,
        tag_template_type: str = None,
        uri: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the workspace. Valid values:
        # 
        # *   PRIVATE: The workspace is visible only to you and the administrator of the workspace.
        # *   PUBLIC: The workspace is visible to all users.
        self.accessibility = accessibility
        # The type of the data source. Valid values:
        # 
        # *   OSS: Object Storage Service (OSS)
        # *   NAS: File Storage NAS (NAS)
        self.data_source_type = data_source_type
        # The data type. Valid values:
        # 
        # *   COMMON: common
        # *   PIC: picture
        # *   TEXT: text
        # *   VIDEO: video
        # *   AUDIO: audio
        self.data_type = data_type
        # The dataset ID.
        self.dataset_id = dataset_id
        # The description.
        self.description = description
        self.edition = edition
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The update time.
        self.gmt_modified_time = gmt_modified_time
        # The dataset configurations to be imported to a storage, such as OSS, NAS, or CPFS.
        # 
        # **OSS**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "bucket": "${bucket}",// The bucket name\\
        # "path": "${path}" // The file path\\
        # }\\
        # 
        # 
        # **NAS**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "path": "${path}", // The file system path\\
        # "mountTarget": "${mount_target}" // The mount point of the file system\\
        # }\\
        # 
        # 
        # **CPFS**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "protocolServiceId":"${protocol_service_id}", // The file system protocol service\\
        # "exportId": "${export_id}", // The file system export directory\\
        # "path": "${path}", // The file system path\\
        # }\\
        # 
        # 
        # **CPFS for Lingjun**\
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "path": "${path}", // The file system path\\
        # "mountTarget": "${mount_target}" // The mount point of the file system, CPFS for Lingjun only\\
        # "isVpcMount": boolean, // Whether the mount point is a VPC mount point, CPFS for Lingjun only\\
        # }\\
        self.import_info = import_info
        self.is_shared = is_shared
        # The tags.
        self.labels = labels
        # The latest version of the dataset.
        self.latest_version = latest_version
        # The access permission on the dataset when the dataset is mounted. Valid values:
        # 
        # *   RO: read-only permissions
        # *   RW: read and write permissions
        self.mount_access = mount_access
        # The list of role names in the workspace that have read and write permissions on the mounted database. The names start with PAI are basic role names and the names start with role- are custom role names. If the list contains asterisks (\\*), all roles have read and write permissions.
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        # The dataset name.
        self.name = name
        # The extended fields of the dataset v1 (initial version). The value is a JSON string. When you use the dataset in Deep Learning Containers (DLC), you can use the mountPath field to specify the default mount path of the dataset.
        self.options = options
        # The ID of the Alibaba Could account.
        self.owner_id = owner_id
        # The property of the dataset of the initial version v1. Valid values:
        # 
        # *   FILE
        # *   DIRECTORY
        self.property = property
        # The dataset provider. If the value pai is returned, the dataset is a public dataset in PAI.
        self.provider = provider
        # The type of the data source for the dataset. Valid values:
        # 
        # *   Ecs (default)
        # *   Lingjun
        self.provider_type = provider_type
        # The request ID.
        self.request_id = request_id
        self.shared_from = shared_from
        self.sharing_config = sharing_config
        # The ID of the source dataset generated from a labeling job of iTAG.
        self.source_dataset_id = source_dataset_id
        # The version of the source dataset generated from a labeling job of iTAG.
        self.source_dataset_version = source_dataset_version
        # The ID of the source for the dataset v1 (initial version). Valid values:
        # 
        # *   If SourceType is set to USER, the value of SourceId can be a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The type of the source for the dataset v1 (initial version). Valid values:
        # 
        # *   PAI-PUBLIC-DATASET: a public dataset of Platform for AI (PAI).
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
        self.source_type = source_type
        # The labeling template for the source dataset generated from a labeling job of iTAG.
        self.tag_template_type = tag_template_type
        # The URI of the initial version v1.
        # 
        # *   Sample format for the OSS data source: `oss://bucket.endpoint/object`
        # *   Sample formats for the NAS data source: `nas://<nasfisid>.region/subpath/to/dir/`: General-purpose NAS. `nas://<cpfs-fsid>.region/subpath/to/dir/`: Cloud Parallel File Storage (CPFS) 1.0. `nas://<cpfs-fsid>.region/<protocolserviceid>/`: CPFS 2.0. You can distinguish CPFS 1.0 and CPFS 2.0 file systems based on the format of the file system ID. The ID for CPFS 1.0 is in the cpfs-<8-bit ASCII characters> format. The ID for CPFS 2.0 is in the cpfs-<16-bit ASCII characters> format.
        self.uri = uri
        # The ID of the user to which the dataset belongs.
        self.user_id = user_id
        # The ID of the workspace to which the dataset belongs.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_version:
            self.latest_version.validate()
        if self.shared_from:
            self.shared_from.validate()
        if self.sharing_config:
            self.sharing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.description is not None:
            result['Description'] = self.description
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.import_info is not None:
            result['ImportInfo'] = self.import_info
        if self.is_shared is not None:
            result['IsShared'] = self.is_shared
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.mount_access_read_write_role_id_list is not None:
            result['MountAccessReadWriteRoleIdList'] = self.mount_access_read_write_role_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.property is not None:
            result['Property'] = self.property
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.shared_from is not None:
            result['SharedFrom'] = self.shared_from.to_map()
        if self.sharing_config is not None:
            result['SharingConfig'] = self.sharing_config.to_map()
        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id
        if self.source_dataset_version is not None:
            result['SourceDatasetVersion'] = self.source_dataset_version
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.tag_template_type is not None:
            result['TagTemplateType'] = self.tag_template_type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')
        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestVersion') is not None:
            temp_model = DatasetVersion()
            self.latest_version = temp_model.from_map(m['LatestVersion'])
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('MountAccessReadWriteRoleIdList') is not None:
            self.mount_access_read_write_role_id_list = m.get('MountAccessReadWriteRoleIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SharedFrom') is not None:
            temp_model = DatasetShareRelationship()
            self.shared_from = temp_model.from_map(m['SharedFrom'])
        if m.get('SharingConfig') is not None:
            temp_model = GetDatasetResponseBodySharingConfig()
            self.sharing_config = temp_model.from_map(m['SharingConfig'])
        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')
        if m.get('SourceDatasetVersion') is not None:
            self.source_dataset_version = m.get('SourceDatasetVersion')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TagTemplateType') is not None:
            self.tag_template_type = m.get('TagTemplateType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetResponseBody = None,
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
            temp_model = GetDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetFileMetaRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The dataset version.
        self.dataset_version = dataset_version
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasetFileMetaResponseBody(TeaModel):
    def __init__(
        self,
        dataset_file_meta: DatasetFileMetaContentGet = None,
        dataset_id: str = None,
        dataset_version: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The queried metadata records of dataset files.
        self.dataset_file_meta = dataset_file_meta
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset version.
        self.dataset_version = dataset_version
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_file_meta:
            self.dataset_file_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_file_meta is not None:
            result['DatasetFileMeta'] = self.dataset_file_meta.to_map()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetFileMeta') is not None:
            temp_model = DatasetFileMetaContentGet()
            self.dataset_file_meta = temp_model.from_map(m['DatasetFileMeta'])
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasetFileMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetFileMetaResponseBody = None,
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
            temp_model = GetDatasetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetFileMetasStatisticsRequest(TeaModel):
    def __init__(
        self,
        aggregate_by: str = None,
        dataset_version: str = None,
        max_results: int = None,
        workspace_id: str = None,
    ):
        # Aggregates statistics based on the specified metadata field. The value is not case-sensitive. If not specified, the total number of dataset file metadata will be returned, instead of aggregation lists. Valid values:
        # 
        # *   filedir: the directory path of the file
        # *   file_type: the file type
        # *   tags.user: user-defined tag
        # *   tags.user-delete-ai-tags: algorithm tags deleted by the user
        # *   tags.ai: algorithm tags (aggregated by all tagging tasks)
        # *   tags.all: algorithm tags and user-defined tags (excluding alogorithm tags deleted by the user)
        self.aggregate_by = aggregate_by
        # The dataset version.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The maximum number of results to be returned from a single query when the NextToken parameter is used in the query. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate_by is not None:
            result['AggregateBy'] = self.aggregate_by
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateBy') is not None:
            self.aggregate_by = m.get('AggregateBy')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasetFileMetasStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        dataset_file_metas_stats: List[DatasetFileMetasStat] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        # The details of the returned aggregation list, including the number of each aggregate item. The list is by default sorted in descending order based on the count number.
        self.dataset_file_metas_stats = dataset_file_metas_stats
        # The returned number. Example: the number of metadata records or the number of user-defined tags.
        self.total_count = total_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dataset_file_metas_stats:
            for k in self.dataset_file_metas_stats:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetFileMetasStats'] = []
        if self.dataset_file_metas_stats is not None:
            for k in self.dataset_file_metas_stats:
                result['DatasetFileMetasStats'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_file_metas_stats = []
        if m.get('DatasetFileMetasStats') is not None:
            for k in m.get('DatasetFileMetasStats'):
                temp_model = DatasetFileMetasStat()
                self.dataset_file_metas_stats.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDatasetFileMetasStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetFileMetasStatisticsResponseBody = None,
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
            temp_model = GetDatasetFileMetasStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetJobRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The dataset version name.
        self.dataset_version = dataset_version
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasetJobResponseBody(TeaModel):
    def __init__(
        self,
        completed_file_count: int = None,
        create_time: str = None,
        description: str = None,
        failed_file_count: int = None,
        finish_time: str = None,
        job_action: str = None,
        job_mode: str = None,
        job_spec: str = None,
        logs: List[str] = None,
        request_id: str = None,
        status: str = None,
        total_file_count: int = None,
    ):
        # The total number of completed files.
        self.completed_file_count = completed_file_count
        # The time when the job is started.
        self.create_time = create_time
        # The job description.
        self.description = description
        # The total number of failed files.
        self.failed_file_count = failed_file_count
        # The time when the job ends.
        self.finish_time = finish_time
        # The action that is performed on the job.
        # 
        # Valid values:
        # 
        # *   SemanticIndex: semantic indexing
        # *   IntelligentTag: smart labeling
        # *   FileMetaExport: metadata export
        self.job_action = job_action
        # The job mode.
        # 
        # Valid value:
        # 
        # *   Full: full data mode.
        self.job_mode = job_mode
        # The job details.
        self.job_spec = job_spec
        # The job logs.
        self.logs = logs
        # The request ID.
        self.request_id = request_id
        # The job state.
        # 
        # Valid values:
        # 
        # *   Succeeded
        # *   Failed
        # *   Running
        # *   Pending
        # *   PartialFailed
        # *   Deleting
        # *   ManuallyStop
        self.status = status
        # The total number of job files.
        self.total_file_count = total_file_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_file_count is not None:
            result['CompletedFileCount'] = self.completed_file_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.failed_file_count is not None:
            result['FailedFileCount'] = self.failed_file_count
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.job_action is not None:
            result['JobAction'] = self.job_action
        if self.job_mode is not None:
            result['JobMode'] = self.job_mode
        if self.job_spec is not None:
            result['JobSpec'] = self.job_spec
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.total_file_count is not None:
            result['TotalFileCount'] = self.total_file_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedFileCount') is not None:
            self.completed_file_count = m.get('CompletedFileCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailedFileCount') is not None:
            self.failed_file_count = m.get('FailedFileCount')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')
        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')
        if m.get('JobSpec') is not None:
            self.job_spec = m.get('JobSpec')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalFileCount') is not None:
            self.total_file_count = m.get('TotalFileCount')
        return self


class GetDatasetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetJobResponseBody = None,
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
            temp_model = GetDatasetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetJobConfigRequest(TeaModel):
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


class GetDatasetJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        create_time: str = None,
        dataset_id: str = None,
        modify_time: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The configuration content. Configuration format for MultimodalIntelligentTag:
        # 
        # { "apiKey":"sk-xxxxxxxxxxxxxxxxxxxxx" }
        # 
        # MultimodalSemanticIndex
        # 
        # { "defaultModelId": "xxx" "defaultModelVersion":"1.0.0" }
        self.config = config
        # The configuration type. Valid values:
        # 
        # *   MultimodalIntelligentTag
        # *   MultimodalSemanticIndex
        self.config_type = config_type
        # The time when the configuration is created.
        self.create_time = create_time
        # The dataset ID.
        self.dataset_id = dataset_id
        # The time when the configuration is modified.
        self.modify_time = modify_time
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasetJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetJobConfigResponseBody = None,
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
            temp_model = GetDatasetJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetVersionResponseBody(TeaModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        dataset_id: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        import_info: str = None,
        labels: List[Label] = None,
        mount_access: str = None,
        options: str = None,
        property: str = None,
        request_id: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
        version_name: str = None,
    ):
        # The number of data records.
        self.data_count = data_count
        # The size of the dataset.
        self.data_size = data_size
        # The type of the data source.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The request ID.
        self.dataset_id = dataset_id
        # The version description.
        self.description = description
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The last modification time.
        self.gmt_modified_time = gmt_modified_time
        # The dataset configurations to be imported to a storage, such as Object Storage Service (OSS), File Storage NAS (NAS), or Cloud Parallel File Storage (CPFS).
        # 
        # **OSS**\
        # 
        # { "region": "${region}",// The region ID. $bucket = $options["bucket"]; // The bucket name. "path": "${path}" // The file path. }
        # 
        # **NAS**\
        # 
        # **CPFS**\
        # 
        # **CPFS for Lingjun**\
        self.import_info = import_info
        # The resource tags.
        self.labels = labels
        # The access permission on the dataset when the dataset is mounted. Valid values:
        # 
        # *   RO: read-only permissions
        # *   RW: read and write permissions
        self.mount_access = mount_access
        # The extended fields.
        self.options = options
        # The property of the dataset.
        # 
        # This parameter is required.
        self.property = property
        # Id of the request
        self.request_id = request_id
        # The ID of the source dataset.
        self.source_id = source_id
        # The type of the data source.
        self.source_type = source_type
        # The sample URI of the dataset.
        # 
        # This parameter is required.
        self.uri = uri
        # The version name of the dataset.
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_count is not None:
            result['DataCount'] = self.data_count
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.import_info is not None:
            result['ImportInfo'] = self.import_info
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access
        if self.options is not None:
            result['Options'] = self.options
        if self.property is not None:
            result['Property'] = self.property
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetDatasetVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatasetVersionResponseBody = None,
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
            temp_model = GetDatasetVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultWorkspaceRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to show the details of the default workspace. The details include the conditions of the workspace in different phases. Valid values:
        # 
        # *   false (default)
        # *   true
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetDefaultWorkspaceResponseBodyConditions(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        type: str = None,
    ):
        # The returned status code. HTTP status code 200 indicates that the request was successful. Other HTTP status codes indicate that the request failed.
        self.code = code
        # The error message. If the returned status code is 200, this parameter is empty.
        self.message = message
        # The task type. Valid values:
        # 
        # *   CREATING: The workspace is being created.
        # *   WORKSPACE_CREATED: The workspace is created.
        # *   MEMBERS_ADDED: The member is added.
        # *   ENABLED: The workspace is created and the member is added.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDefaultWorkspaceResponseBodyOwner(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_kp: str = None,
        user_name: str = None,
    ):
        # The user ID.
        self.user_id = user_id
        # The user ID.
        self.user_kp = user_kp
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetDefaultWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        conditions: List[GetDefaultWorkspaceResponseBodyConditions] = None,
        creator: str = None,
        description: str = None,
        display_name: str = None,
        env_types: List[str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        owner: GetDefaultWorkspaceResponseBodyOwner = None,
        request_id: str = None,
        status: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The conditions of the default workspace in the creation process.
        self.conditions = conditions
        # The UID of the Alibaba Cloud account.
        self.creator = creator
        # The workspace description.
        self.description = description
        # The display name of the workspace.
        self.display_name = display_name
        # The environments of the workspace. Valid values:
        # 
        # *   Workspaces in basic mode can run only in the production environment.
        # *   Workspaces in standard mode can run in both the development and production environments.
        self.env_types = env_types
        # The time when the workspace was created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the workspace was modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The UID of the Alibaba Cloud account.
        self.owner = owner
        # The request ID.
        self.request_id = request_id
        # The workspace status. Valid values:
        # 
        # *   ENABLED
        # *   INITIALIZING
        # *   FAILURE
        # *   DISABLED
        # *   FROZEN
        # *   UPDATING
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name, which is unique in a region.
        self.workspace_name = workspace_name

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env_types is not None:
            result['EnvTypes'] = self.env_types
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = GetDefaultWorkspaceResponseBodyConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Owner') is not None:
            temp_model = GetDefaultWorkspaceResponseBodyOwner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class GetDefaultWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDefaultWorkspaceResponseBody = None,
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
            temp_model = GetDefaultWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to obtain the latest run information associated with the experiment
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Experiment = None,
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
            temp_model = Experiment()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to display non-essential information, which contains tags. Valid values:
        # 
        # *   false (default)
        # *   true
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetImageResponseBodyLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_uri: str = None,
        labels: List[GetImageResponseBodyLabels] = None,
        name: str = None,
        parent_user_id: str = None,
        request_id: str = None,
        size: int = None,
        source_id: str = None,
        source_type: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The accessibility of the image. Valid values:
        # 
        # *   PUBLIC: All members can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        self.accessibility = accessibility
        # The image description.
        self.description = description
        # The time when the image is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the image is modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The image address, which contains the version number.
        self.image_uri = image_uri
        # The image tags, which are of the array data type. Each element in the array contains a key-value pair. The key of official tags is system.official and the tag value is true.
        self.labels = labels
        # The image name.
        self.name = name
        # The Alibaba Cloud account of the creator.
        self.parent_user_id = parent_user_id
        # The request ID.
        self.request_id = request_id
        # The size of the image. Unit: GB.
        self.size = size
        # 镜像来源 ID
        self.source_id = source_id
        # 镜像来源类型
        self.source_type = source_type
        # The user ID of the image.
        self.user_id = user_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetImageResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageResponseBody = None,
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMemberRequest(TeaModel):
    def __init__(
        self,
        member_id: str = None,
        user_id: str = None,
    ):
        # The member ID. You must specify only one of the following parameters: UserId and MemberId.
        self.member_id = member_id
        # The ID of the Alibaba Cloud account. You can call [ListWorkspaceUsers](https://help.aliyun.com/document_detail/449133.html) to obtain the ID of the Alibaba Cloud account. You must specify only one of the following parameters: UserId and MemberId.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetMemberResponseBody(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        member_id: str = None,
        member_name: str = None,
        request_id: str = None,
        roles: List[str] = None,
        user_id: str = None,
    ):
        self.account_type = account_type
        # The display name of the member.
        self.display_name = display_name
        # The time when the workspace is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The member ID.
        self.member_id = member_id
        # The username.
        self.member_name = member_name
        # The request ID.
        self.request_id = request_id
        # The list of roles.
        self.roles = roles
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMemberResponseBody = None,
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
            temp_model = GetMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelResponseBody(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_latest_version_modified_time: str = None,
        gmt_modified_time: str = None,
        labels: List[Label] = None,
        latest_version: ModelVersion = None,
        model_description: str = None,
        model_doc: str = None,
        model_id: str = None,
        model_name: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        owner_id: str = None,
        parameter_size: int = None,
        provider: str = None,
        request_id: str = None,
        task: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the workspace.
        # 
        # *   PRIVATE: The workspace is visible only to you and the administrator of the workspace.
        # *   PUBLIC: The workspace is visible to all users.
        self.accessibility = accessibility
        # The domain. This parameter specifies the domain for which the model is developed. Valid values: nlp and cv. nlp indicates natural language processing and cv indicates computer vision.
        self.domain = domain
        # Other information about the model.
        self.extra_info = extra_info
        # The time when the model is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        self.gmt_latest_version_modified_time = gmt_latest_version_modified_time
        # The time when the model is last modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The model tags.
        self.labels = labels
        # The latest version of the model.
        self.latest_version = latest_version
        # The model description.
        self.model_description = model_description
        # The documentation of the model.
        self.model_doc = model_doc
        # The model ID.
        self.model_id = model_id
        # The model name.
        self.model_name = model_name
        # The model type.
        self.model_type = model_type
        # The sequence number of the model.
        self.order_number = order_number
        # The source of the model. The community or organization to which the model belongs, such as ModelScope or HuggingFace.
        self.origin = origin
        # The ID of the Alibaba Cloud account.
        self.owner_id = owner_id
        self.parameter_size = parameter_size
        # The provider.
        self.provider = provider
        # The request ID.
        self.request_id = request_id
        # The task of the model. This parameter describes specific issues that the model solves, such as text-classification.
        self.task = task
        # The user ID.
        self.user_id = user_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.latest_version:
            self.latest_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_latest_version_modified_time is not None:
            result['GmtLatestVersionModifiedTime'] = self.gmt_latest_version_modified_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()
        if self.model_description is not None:
            result['ModelDescription'] = self.model_description
        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.order_number is not None:
            result['OrderNumber'] = self.order_number
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameter_size is not None:
            result['ParameterSize'] = self.parameter_size
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task is not None:
            result['Task'] = self.task
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtLatestVersionModifiedTime') is not None:
            self.gmt_latest_version_modified_time = m.get('GmtLatestVersionModifiedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestVersion') is not None:
            temp_model = ModelVersion()
            self.latest_version = temp_model.from_map(m['LatestVersion'])
        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')
        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParameterSize') is not None:
            self.parameter_size = m.get('ParameterSize')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelResponseBody = None,
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
            temp_model = GetModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        approval_status: str = None,
        compression_spec: Dict[str, Any] = None,
        distillation_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        extra_info: Dict[str, Any] = None,
        format_type: str = None,
        framework_type: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        inference_spec: Dict[str, Any] = None,
        labels: List[Label] = None,
        metrics: Dict[str, Any] = None,
        options: str = None,
        owner_id: str = None,
        request_id: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        uri: str = None,
        user_id: str = None,
        version_description: str = None,
        version_name: str = None,
    ):
        # The approval status. Valid values:
        # 
        # *   Pending
        # *   Approved
        # *   Rejected
        self.approval_status = approval_status
        # The compression configuration.
        self.compression_spec = compression_spec
        self.distillation_spec = distillation_spec
        # The evaluation configuration.
        self.evaluation_spec = evaluation_spec
        # The additional information.
        self.extra_info = extra_info
        # The model format. Valid values:
        # 
        # *   OfflineModel
        # *   SavedModel
        # *   Keras H5
        # *   Frozen Pb
        # *   Caffe Prototxt
        # *   TorchScript
        # *   XGBoost
        # *   PMML
        # *   AlinkModel
        # *   ONNX
        self.format_type = format_type
        # The model framework. Valid values:
        # 
        # *   Pytorch -XGBoost
        # *   Keras
        # *   Caffe
        # *   Alink
        # *   Xflow
        # *   TensorFlow
        self.framework_type = framework_type
        # The time when the model was created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the model was last modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # Describes how to apply to downstream inference services. For example, describes the processor and container of Elastic Algorithm Service (EAS).
        self.inference_spec = inference_spec
        # The labels.
        self.labels = labels
        # The metrics.
        self.metrics = metrics
        # The extended field. The value of this parameter is a JSON string.
        self.options = options
        # The ID of the Alibaba Cloud account.
        self.owner_id = owner_id
        # The request ID.
        self.request_id = request_id
        # The source ID.
        # 
        # *   If the source type is Custom, this field is not limited.
        # *   If the source type is PAIFlow or TrainingService, the format is:
        # 
        # <!---->
        # 
        #     region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # 
        # Take note of the following parameters:
        # 
        # *   region is the region ID.
        # *   workspaceId is the ID of the workspace.
        # *   kind is the type. Valid values: PipelineRun (PAIFlow) and ServiceJob (training service).
        # *   id is a unique identifier.
        self.source_id = source_id
        # The source type of the model. Valid values:
        # 
        # *   Custom
        # *   PAIFlow
        # *   TrainingService
        self.source_type = source_type
        # The training configurations used for fine-tuning and incremental training.
        self.training_spec = training_spec
        # The URI of the model version, which is the location where the model is stored. Valid values:
        # 
        # *   The HTTP(S) address of the model. Example: `https://myweb.com/mymodel.tar.gz`.
        # *   The Object Storage Service (OSS) path of the model, in the format of `oss://<bucket>.<endpoint>/object`. For endpoint, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html). Example: `oss://mybucket.oss-cn-beijing.aliyuncs.com/mypath/`.
        self.uri = uri
        # The user ID.
        self.user_id = user_id
        # The version description.
        self.version_description = version_description
        # The model version.
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status
        if self.compression_spec is not None:
            result['CompressionSpec'] = self.compression_spec
        if self.distillation_spec is not None:
            result['DistillationSpec'] = self.distillation_spec
        if self.evaluation_spec is not None:
            result['EvaluationSpec'] = self.evaluation_spec
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.inference_spec is not None:
            result['InferenceSpec'] = self.inference_spec
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.options is not None:
            result['Options'] = self.options
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.training_spec is not None:
            result['TrainingSpec'] = self.training_spec
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')
        if m.get('CompressionSpec') is not None:
            self.compression_spec = m.get('CompressionSpec')
        if m.get('DistillationSpec') is not None:
            self.distillation_spec = m.get('DistillationSpec')
        if m.get('EvaluationSpec') is not None:
            self.evaluation_spec = m.get('EvaluationSpec')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TrainingSpec') is not None:
            self.training_spec = m.get('TrainingSpec')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelVersionResponseBody = None,
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
            temp_model = GetModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermissionRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        labels: Dict[str, Any] = None,
        option: str = None,
        resource: str = None,
    ):
        # The accessibility. Valid values:
        # 
        # *   PUBLIC: All members in the workspace can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        self.accessibility = accessibility
        # The UID of the Alibaba Cloud account that is used to create the workspace.
        self.creator = creator
        self.labels = labels
        # The configuration. Separate multiple configurations with commas (,). Valid values:
        # 
        # *   ResourceEmpty: The Resource parameter is not configured.
        # *   DisableRam: The RAM check is not performed.
        self.option = option
        # The resource.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.option is not None:
            result['Option'] = self.option
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GetPermissionShrinkRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        labels_shrink: str = None,
        option: str = None,
        resource: str = None,
    ):
        # The accessibility. Valid values:
        # 
        # *   PUBLIC: All members in the workspace can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        self.accessibility = accessibility
        # The UID of the Alibaba Cloud account that is used to create the workspace.
        self.creator = creator
        self.labels_shrink = labels_shrink
        # The configuration. Separate multiple configurations with commas (,). Valid values:
        # 
        # *   ResourceEmpty: The Resource parameter is not configured.
        # *   DisableRam: The RAM check is not performed.
        self.option = option
        # The resource.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink
        if self.option is not None:
            result['Option'] = self.option
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GetPermissionResponseBodyPermissionRules(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        entity_access_type: str = None,
    ):
        # The accessibility. Valid values:
        # 
        # *   PUBLIC: All members can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        # *   ANY: All users can access the workspace.
        self.accessibility = accessibility
        # The access type. If you set Accessibility to PUBLIC, all users can access the workspace. This parameter is invalid. If you set Accessibility to PRIVATE, the value of this parameter can be:
        # 
        # *   PRIVATE: Only the creator can access the workspace.
        # *   ANY: All users can access the workspace.
        self.entity_access_type = entity_access_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.entity_access_type is not None:
            result['EntityAccessType'] = self.entity_access_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('EntityAccessType') is not None:
            self.entity_access_type = m.get('EntityAccessType')
        return self


class GetPermissionResponseBody(TeaModel):
    def __init__(
        self,
        permission_code: str = None,
        permission_rules: List[GetPermissionResponseBodyPermissionRules] = None,
        request_id: str = None,
    ):
        # The permission name, which is unique in a region. For more information about permissions, see [Appendix: Roles and permissions](https://help.aliyun.com/document_detail/2840449.html).
        self.permission_code = permission_code
        # The permission rules.
        self.permission_rules = permission_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.permission_rules:
            for k in self.permission_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code
        result['PermissionRules'] = []
        if self.permission_rules is not None:
            for k in self.permission_rules:
                result['PermissionRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')
        self.permission_rules = []
        if m.get('PermissionRules') is not None:
            for k in m.get('PermissionRules'):
                temp_model = GetPermissionResponseBodyPermissionRules()
                self.permission_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPermissionResponseBody = None,
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
            temp_model = GetPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to obtain the Metrics, Params, and Labels information. Default value: false.
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Run = None,
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
            temp_model = Run()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkspaceRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to display supplementary information such as the workspace owner. Valid values:
        # 
        # *   false (default)
        # *   true
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetWorkspaceResponseBodyOwner(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
        user_kp: str = None,
        user_name: str = None,
    ):
        # The display name.
        self.display_name = display_name
        # The user ID.
        self.user_id = user_id
        # The user ID.
        self.user_kp = user_kp
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        admin_names: List[str] = None,
        creator: str = None,
        description: str = None,
        display_name: str = None,
        env_types: List[str] = None,
        extra_infos: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        is_default: bool = None,
        owner: GetWorkspaceResponseBodyOwner = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The names of the administrator accounts.
        self.admin_names = admin_names
        # The ID of the user who creates the workspace.
        self.creator = creator
        # The description of the workspace.
        self.description = description
        # The display name of the workspace.
        self.display_name = display_name
        # The environment information of the workspace.
        # 
        # *   Workspaces in basic mode can run only in the production environment.
        # *   Workspaces in standard mode can run in both the development and production environments.
        self.env_types = env_types
        # The additional information, which only contains the TenantId field.
        self.extra_infos = extra_infos
        # The time when the workspace is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the workspace is modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # Indicates whether the workspace is the default workspace. Valid values:
        # 
        # *   false
        # *   true
        self.is_default = is_default
        # The information about the workspace owner. This parameter is valid only when Verbose is set to true.
        self.owner = owner
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The workspace state. Valid values:
        # 
        # *   ENABLED
        # *   INITIALIZING
        # *   FAILURE:
        # *   DISABLED
        # *   FROZEN
        # *   UPDATING
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_names is not None:
            result['AdminNames'] = self.admin_names
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env_types is not None:
            result['EnvTypes'] = self.env_types
        if self.extra_infos is not None:
            result['ExtraInfos'] = self.extra_infos
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminNames') is not None:
            self.admin_names = m.get('AdminNames')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')
        if m.get('ExtraInfos') is not None:
            self.extra_infos = m.get('ExtraInfos')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Owner') is not None:
            temp_model = GetWorkspaceResponseBodyOwner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class GetWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWorkspaceResponseBody = None,
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
            temp_model = GetWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCodeSourcesRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        # The display name of the code source. Fuzzy match is supported.
        self.display_name = display_name
        # The order in which the entries are sorted by the specific field on the returned page. Valid values:
        # 
        # *   ASC (default)
        # *   DESC
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The field used for sorting. Valid values:
        # 
        # *   GmtModifyTime: the time when the code source was modified.
        # *   DisplayName: the display name.
        # *   CodeSourceId: the code source ID.
        # *   GmtCreateTime: the time when the code source was created. This is the default value.
        self.sort_by = sort_by
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListCodeSourcesResponseBody(TeaModel):
    def __init__(
        self,
        code_sources: List[CodeSourceItem] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The code sources.
        self.code_sources = code_sources
        # The request ID.
        self.request_id = request_id
        # The total number of code sources that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.code_sources:
            for k in self.code_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CodeSources'] = []
        if self.code_sources is not None:
            for k in self.code_sources:
                result['CodeSources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_sources = []
        if m.get('CodeSources') is not None:
            for k in m.get('CodeSources'):
                temp_model = CodeSourceItem()
                self.code_sources.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCodeSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCodeSourcesResponseBody = None,
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
            temp_model = ListCodeSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigsRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        config_keys: str = None,
        labels: str = None,
        verbose: str = None,
    ):
        # The category of the configuration item. Supported categories:
        # 
        # *   CommonResourceConfig
        # *   DLCAutoRecycle
        # *   DLCPriorityConfig
        # *   DSWPriorityConfig
        # *   QuotaMaximumDuration
        # *   CommonTagConfig
        self.category_name = category_name
        # The key of the configuration item. Supported keys:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   priorityConfig: Priority configuration. This key can be used only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: The predefined tags of the workspace. All created resources must have tags
        self.config_keys = config_keys
        # The tags used as filter conditions. Separate multiple tags with commas (,). These conditions are in an AND relationship.
        self.labels = labels
        # Specifies whether to show the tag information.
        # 
        # *   true
        # *   false
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.config_keys is not None:
            result['ConfigKeys'] = self.config_keys
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ConfigKeys') is not None:
            self.config_keys = m.get('ConfigKeys')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ListConfigsResponseBodyConfigsLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[ListConfigsResponseBodyConfigsLabels] = None,
    ):
        # The key of the configuration item. Supported keys:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: The predefined tags of the workspace. All created resources must have tags
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        # The tags of the configuration item.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListConfigsResponseBodyConfigsLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class ListConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[ListConfigsResponseBodyConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configuration items.
        self.configs = configs
        # The request ID.
        self.request_id = request_id
        # The number of items returned.
        self.total_count = total_count

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = ListConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConfigsResponseBody = None,
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
            temp_model = ListConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionsRequest(TeaModel):
    def __init__(
        self,
        connection_ids: List[str] = None,
        connection_name: str = None,
        connection_types: List[str] = None,
        creator: str = None,
        encrypt_option: str = None,
        max_results: int = None,
        model: str = None,
        model_types: List[str] = None,
        next_token: str = None,
        order: str = None,
        sort_by: str = None,
        tool_call: bool = None,
        workspace_id: str = None,
    ):
        # The list of connection IDs.
        self.connection_ids = connection_ids
        # The connection name.
        self.connection_name = connection_name
        # The list of connection types.
        self.connection_types = connection_types
        self.creator = creator
        # The encryption settings. Valid values:
        # 
        # *   PlainText
        # *   Secret
        self.encrypt_option = encrypt_option
        # The maximum number of entries per page.
        self.max_results = max_results
        # The model identifier.
        self.model = model
        # The list of model types.
        self.model_types = model_types
        # The pagination token that indicates the start position from which to retrieve data on the next page.
        self.next_token = next_token
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy.
        # 
        # *   ASC: ascending order.
        # *   DESC: descending order. This is the default value.
        self.order = order
        # The field used to sort the results in queries by page. Default value: GmtCreateTime. Valid value:
        # 
        # *   GmtCreateTime: The results are sorted by creation time. This is the default value.
        self.sort_by = sort_by
        # Specifies whether a tool can be called by using ToolCall. Valid values:
        # 
        # *   true
        # *   false
        self.tool_call = tool_call
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_ids is not None:
            result['ConnectionIds'] = self.connection_ids
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connection_types is not None:
            result['ConnectionTypes'] = self.connection_types
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.encrypt_option is not None:
            result['EncryptOption'] = self.encrypt_option
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.model is not None:
            result['Model'] = self.model
        if self.model_types is not None:
            result['ModelTypes'] = self.model_types
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionIds') is not None:
            self.connection_ids = m.get('ConnectionIds')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('ConnectionTypes') is not None:
            self.connection_types = m.get('ConnectionTypes')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EncryptOption') is not None:
            self.encrypt_option = m.get('EncryptOption')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ModelTypes') is not None:
            self.model_types = m.get('ModelTypes')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListConnectionsShrinkRequest(TeaModel):
    def __init__(
        self,
        connection_ids_shrink: str = None,
        connection_name: str = None,
        connection_types_shrink: str = None,
        creator: str = None,
        encrypt_option: str = None,
        max_results: int = None,
        model: str = None,
        model_types_shrink: str = None,
        next_token: str = None,
        order: str = None,
        sort_by: str = None,
        tool_call: bool = None,
        workspace_id: str = None,
    ):
        # The list of connection IDs.
        self.connection_ids_shrink = connection_ids_shrink
        # The connection name.
        self.connection_name = connection_name
        # The list of connection types.
        self.connection_types_shrink = connection_types_shrink
        self.creator = creator
        # The encryption settings. Valid values:
        # 
        # *   PlainText
        # *   Secret
        self.encrypt_option = encrypt_option
        # The maximum number of entries per page.
        self.max_results = max_results
        # The model identifier.
        self.model = model
        # The list of model types.
        self.model_types_shrink = model_types_shrink
        # The pagination token that indicates the start position from which to retrieve data on the next page.
        self.next_token = next_token
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy.
        # 
        # *   ASC: ascending order.
        # *   DESC: descending order. This is the default value.
        self.order = order
        # The field used to sort the results in queries by page. Default value: GmtCreateTime. Valid value:
        # 
        # *   GmtCreateTime: The results are sorted by creation time. This is the default value.
        self.sort_by = sort_by
        # Specifies whether a tool can be called by using ToolCall. Valid values:
        # 
        # *   true
        # *   false
        self.tool_call = tool_call
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_ids_shrink is not None:
            result['ConnectionIds'] = self.connection_ids_shrink
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connection_types_shrink is not None:
            result['ConnectionTypes'] = self.connection_types_shrink
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.encrypt_option is not None:
            result['EncryptOption'] = self.encrypt_option
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.model is not None:
            result['Model'] = self.model
        if self.model_types_shrink is not None:
            result['ModelTypes'] = self.model_types_shrink
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionIds') is not None:
            self.connection_ids_shrink = m.get('ConnectionIds')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('ConnectionTypes') is not None:
            self.connection_types_shrink = m.get('ConnectionTypes')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EncryptOption') is not None:
            self.encrypt_option = m.get('EncryptOption')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ModelTypes') is not None:
            self.model_types_shrink = m.get('ModelTypes')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        connections: List[Connection] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The connection list.
        self.connections = connections
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token that indicates the start position from which to retrieve data on the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of connections that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = Connection()
                self.connections.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConnectionsResponseBody = None,
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
            temp_model = ListConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetFileMetasRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        end_file_update_time: str = None,
        end_tag_update_time: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_size: int = None,
        query_content_type_include_any: List[str] = None,
        query_expression: str = None,
        query_file_dir: str = None,
        query_file_name: str = None,
        query_file_type_include_any: List[str] = None,
        query_image: str = None,
        query_tags_exclude: List[str] = None,
        query_tags_include_all: List[str] = None,
        query_tags_include_any: List[str] = None,
        query_text: str = None,
        query_type: str = None,
        score_threshold: float = None,
        sort_by: str = None,
        start_file_update_time: str = None,
        start_tag_update_time: str = None,
        thumbnail_mode: str = None,
        top_k: int = None,
        workspace_id: str = None,
    ):
        # The dataset version.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The update time range to query. The end time. The time follows the ISO 8601 standard. This parameter is valid only when QueryType is set to TAG.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_file_update_time = end_file_update_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_tag_update_time = end_tag_update_time
        self.max_results = max_results
        # The pagination token.
        # 
        # >  If you do not configure this parameter, the data on the first page is returned. A return value other than Null of this parameter indicates that not all entries have been returned. You can use this value as an input parameter to obtain entries on the next page. The value Null indicates that all query results have been returned.
        self.next_token = next_token
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The number of entries per page. Default value: 10. Maximum value: 1000.
        self.page_size = page_size
        self.query_content_type_include_any = query_content_type_include_any
        self.query_expression = query_expression
        self.query_file_dir = query_file_dir
        self.query_file_name = query_file_name
        self.query_file_type_include_any = query_file_type_include_any
        self.query_image = query_image
        self.query_tags_exclude = query_tags_exclude
        self.query_tags_include_all = query_tags_include_all
        self.query_tags_include_any = query_tags_include_any
        # The text content to be queried.
        self.query_text = query_text
        # The retrieval type.
        # 
        # *   TAG (default)
        # *   VECTOR
        self.query_type = query_type
        # The similarity score. Only dataset files whose similarity score is greater than the value of ScoreThreshold are returned. This parameter is valid only when QueryType is set to VECTOR.
        self.score_threshold = score_threshold
        # The field used to sort the results. Default value: GmtCreateTime. Valid values:
        # 
        # *   FileCreateTime (default): The results are sorted by the time when the file is created.
        # *   FileUpdateTime: The results are sorted by the time when the file is last modified.
        self.sort_by = sort_by
        # The update time range to query. The start time. The time follows the ISO 8601 standard. This parameter is valid only when QueryType is set to TAG.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_file_update_time = start_file_update_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_tag_update_time = start_tag_update_time
        self.thumbnail_mode = thumbnail_mode
        # The number of search results to return. A maximum of Top K search results can be returned. This parameter is valid only when QueryType is set to VECTOR.
        self.top_k = top_k
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.end_file_update_time is not None:
            result['EndFileUpdateTime'] = self.end_file_update_time
        if self.end_tag_update_time is not None:
            result['EndTagUpdateTime'] = self.end_tag_update_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_content_type_include_any is not None:
            result['QueryContentTypeIncludeAny'] = self.query_content_type_include_any
        if self.query_expression is not None:
            result['QueryExpression'] = self.query_expression
        if self.query_file_dir is not None:
            result['QueryFileDir'] = self.query_file_dir
        if self.query_file_name is not None:
            result['QueryFileName'] = self.query_file_name
        if self.query_file_type_include_any is not None:
            result['QueryFileTypeIncludeAny'] = self.query_file_type_include_any
        if self.query_image is not None:
            result['QueryImage'] = self.query_image
        if self.query_tags_exclude is not None:
            result['QueryTagsExclude'] = self.query_tags_exclude
        if self.query_tags_include_all is not None:
            result['QueryTagsIncludeAll'] = self.query_tags_include_all
        if self.query_tags_include_any is not None:
            result['QueryTagsIncludeAny'] = self.query_tags_include_any
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_file_update_time is not None:
            result['StartFileUpdateTime'] = self.start_file_update_time
        if self.start_tag_update_time is not None:
            result['StartTagUpdateTime'] = self.start_tag_update_time
        if self.thumbnail_mode is not None:
            result['ThumbnailMode'] = self.thumbnail_mode
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('EndFileUpdateTime') is not None:
            self.end_file_update_time = m.get('EndFileUpdateTime')
        if m.get('EndTagUpdateTime') is not None:
            self.end_tag_update_time = m.get('EndTagUpdateTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryContentTypeIncludeAny') is not None:
            self.query_content_type_include_any = m.get('QueryContentTypeIncludeAny')
        if m.get('QueryExpression') is not None:
            self.query_expression = m.get('QueryExpression')
        if m.get('QueryFileDir') is not None:
            self.query_file_dir = m.get('QueryFileDir')
        if m.get('QueryFileName') is not None:
            self.query_file_name = m.get('QueryFileName')
        if m.get('QueryFileTypeIncludeAny') is not None:
            self.query_file_type_include_any = m.get('QueryFileTypeIncludeAny')
        if m.get('QueryImage') is not None:
            self.query_image = m.get('QueryImage')
        if m.get('QueryTagsExclude') is not None:
            self.query_tags_exclude = m.get('QueryTagsExclude')
        if m.get('QueryTagsIncludeAll') is not None:
            self.query_tags_include_all = m.get('QueryTagsIncludeAll')
        if m.get('QueryTagsIncludeAny') is not None:
            self.query_tags_include_any = m.get('QueryTagsIncludeAny')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartFileUpdateTime') is not None:
            self.start_file_update_time = m.get('StartFileUpdateTime')
        if m.get('StartTagUpdateTime') is not None:
            self.start_tag_update_time = m.get('StartTagUpdateTime')
        if m.get('ThumbnailMode') is not None:
            self.thumbnail_mode = m.get('ThumbnailMode')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasetFileMetasShrinkRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        end_file_update_time: str = None,
        end_tag_update_time: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_size: int = None,
        query_content_type_include_any_shrink: str = None,
        query_expression: str = None,
        query_file_dir: str = None,
        query_file_name: str = None,
        query_file_type_include_any_shrink: str = None,
        query_image: str = None,
        query_tags_exclude_shrink: str = None,
        query_tags_include_all_shrink: str = None,
        query_tags_include_any_shrink: str = None,
        query_text: str = None,
        query_type: str = None,
        score_threshold: float = None,
        sort_by: str = None,
        start_file_update_time: str = None,
        start_tag_update_time: str = None,
        thumbnail_mode: str = None,
        top_k: int = None,
        workspace_id: str = None,
    ):
        # The dataset version.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The update time range to query. The end time. The time follows the ISO 8601 standard. This parameter is valid only when QueryType is set to TAG.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_file_update_time = end_file_update_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.end_tag_update_time = end_tag_update_time
        self.max_results = max_results
        # The pagination token.
        # 
        # >  If you do not configure this parameter, the data on the first page is returned. A return value other than Null of this parameter indicates that not all entries have been returned. You can use this value as an input parameter to obtain entries on the next page. The value Null indicates that all query results have been returned.
        self.next_token = next_token
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The number of entries per page. Default value: 10. Maximum value: 1000.
        self.page_size = page_size
        self.query_content_type_include_any_shrink = query_content_type_include_any_shrink
        self.query_expression = query_expression
        self.query_file_dir = query_file_dir
        self.query_file_name = query_file_name
        self.query_file_type_include_any_shrink = query_file_type_include_any_shrink
        self.query_image = query_image
        self.query_tags_exclude_shrink = query_tags_exclude_shrink
        self.query_tags_include_all_shrink = query_tags_include_all_shrink
        self.query_tags_include_any_shrink = query_tags_include_any_shrink
        # The text content to be queried.
        self.query_text = query_text
        # The retrieval type.
        # 
        # *   TAG (default)
        # *   VECTOR
        self.query_type = query_type
        # The similarity score. Only dataset files whose similarity score is greater than the value of ScoreThreshold are returned. This parameter is valid only when QueryType is set to VECTOR.
        self.score_threshold = score_threshold
        # The field used to sort the results. Default value: GmtCreateTime. Valid values:
        # 
        # *   FileCreateTime (default): The results are sorted by the time when the file is created.
        # *   FileUpdateTime: The results are sorted by the time when the file is last modified.
        self.sort_by = sort_by
        # The update time range to query. The start time. The time follows the ISO 8601 standard. This parameter is valid only when QueryType is set to TAG.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_file_update_time = start_file_update_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_tag_update_time = start_tag_update_time
        self.thumbnail_mode = thumbnail_mode
        # The number of search results to return. A maximum of Top K search results can be returned. This parameter is valid only when QueryType is set to VECTOR.
        self.top_k = top_k
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.end_file_update_time is not None:
            result['EndFileUpdateTime'] = self.end_file_update_time
        if self.end_tag_update_time is not None:
            result['EndTagUpdateTime'] = self.end_tag_update_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_content_type_include_any_shrink is not None:
            result['QueryContentTypeIncludeAny'] = self.query_content_type_include_any_shrink
        if self.query_expression is not None:
            result['QueryExpression'] = self.query_expression
        if self.query_file_dir is not None:
            result['QueryFileDir'] = self.query_file_dir
        if self.query_file_name is not None:
            result['QueryFileName'] = self.query_file_name
        if self.query_file_type_include_any_shrink is not None:
            result['QueryFileTypeIncludeAny'] = self.query_file_type_include_any_shrink
        if self.query_image is not None:
            result['QueryImage'] = self.query_image
        if self.query_tags_exclude_shrink is not None:
            result['QueryTagsExclude'] = self.query_tags_exclude_shrink
        if self.query_tags_include_all_shrink is not None:
            result['QueryTagsIncludeAll'] = self.query_tags_include_all_shrink
        if self.query_tags_include_any_shrink is not None:
            result['QueryTagsIncludeAny'] = self.query_tags_include_any_shrink
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_file_update_time is not None:
            result['StartFileUpdateTime'] = self.start_file_update_time
        if self.start_tag_update_time is not None:
            result['StartTagUpdateTime'] = self.start_tag_update_time
        if self.thumbnail_mode is not None:
            result['ThumbnailMode'] = self.thumbnail_mode
        if self.top_k is not None:
            result['TopK'] = self.top_k
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('EndFileUpdateTime') is not None:
            self.end_file_update_time = m.get('EndFileUpdateTime')
        if m.get('EndTagUpdateTime') is not None:
            self.end_tag_update_time = m.get('EndTagUpdateTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryContentTypeIncludeAny') is not None:
            self.query_content_type_include_any_shrink = m.get('QueryContentTypeIncludeAny')
        if m.get('QueryExpression') is not None:
            self.query_expression = m.get('QueryExpression')
        if m.get('QueryFileDir') is not None:
            self.query_file_dir = m.get('QueryFileDir')
        if m.get('QueryFileName') is not None:
            self.query_file_name = m.get('QueryFileName')
        if m.get('QueryFileTypeIncludeAny') is not None:
            self.query_file_type_include_any_shrink = m.get('QueryFileTypeIncludeAny')
        if m.get('QueryImage') is not None:
            self.query_image = m.get('QueryImage')
        if m.get('QueryTagsExclude') is not None:
            self.query_tags_exclude_shrink = m.get('QueryTagsExclude')
        if m.get('QueryTagsIncludeAll') is not None:
            self.query_tags_include_all_shrink = m.get('QueryTagsIncludeAll')
        if m.get('QueryTagsIncludeAny') is not None:
            self.query_tags_include_any_shrink = m.get('QueryTagsIncludeAny')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartFileUpdateTime') is not None:
            self.start_file_update_time = m.get('StartFileUpdateTime')
        if m.get('StartTagUpdateTime') is not None:
            self.start_tag_update_time = m.get('StartTagUpdateTime')
        if m.get('ThumbnailMode') is not None:
            self.thumbnail_mode = m.get('ThumbnailMode')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasetFileMetasResponseBody(TeaModel):
    def __init__(
        self,
        dataset_file_metas: List[DatasetFileMeta] = None,
        dataset_id: str = None,
        dataset_version: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
        workspace_id: str = None,
    ):
        # The metadata records of the dataset files.
        self.dataset_file_metas = dataset_file_metas
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset version.
        self.dataset_version = dataset_version
        self.max_results = max_results
        # The pagination token. If the number of results exceeds the maximum number of entries allowed per page, a pagination token is returned. This token can be used as an input parameter to obtain the next page of results. If all results are obtained, no token is returned.
        self.next_token = next_token
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_file_metas:
            for k in self.dataset_file_metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetFileMetas'] = []
        if self.dataset_file_metas is not None:
            for k in self.dataset_file_metas:
                result['DatasetFileMetas'].append(k.to_map() if k else None)
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_file_metas = []
        if m.get('DatasetFileMetas') is not None:
            for k in m.get('DatasetFileMetas'):
                temp_model = DatasetFileMeta()
                self.dataset_file_metas.append(temp_model.from_map(k))
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasetFileMetasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetFileMetasResponseBody = None,
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
            temp_model = ListDatasetFileMetasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetJobConfigsRequest(TeaModel):
    def __init__(
        self,
        config_type: str = None,
        dataset_version: str = None,
        page_number: str = None,
        page_size: str = None,
        workspace_id: str = None,
    ):
        # The configuration type.
        # 
        # *   MultimodalIntelligentTag
        # *   MultimodalSemanticIndex
        self.config_type = config_type
        self.dataset_version = dataset_version
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasetJobConfigsResponseBody(TeaModel):
    def __init__(
        self,
        dataset_job_configs: List[DatasetJobConfig] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The dataset job configurations.
        self.dataset_job_configs = dataset_job_configs
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.dataset_job_configs:
            for k in self.dataset_job_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetJobConfigs'] = []
        if self.dataset_job_configs is not None:
            for k in self.dataset_job_configs:
                result['DatasetJobConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_job_configs = []
        if m.get('DatasetJobConfigs') is not None:
            for k in m.get('DatasetJobConfigs'):
                temp_model = DatasetJobConfig()
                self.dataset_job_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasetJobConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetJobConfigsResponseBody = None,
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
            temp_model = ListDatasetJobConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetJobsRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        job_action: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The dataset version name.
        self.dataset_version = dataset_version
        # The action to be performed on the job.
        self.job_action = job_action
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.sort_by = sort_by
        self.status = status
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.job_action is not None:
            result['JobAction'] = self.job_action
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasetJobsResponseBody(TeaModel):
    def __init__(
        self,
        dataset_jobs: List[DatasetJob] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The jobs in the dataset.
        self.dataset_jobs = dataset_jobs
        # The request ID.
        self.request_id = request_id
        # The total number of jobs.
        self.total_count = total_count

    def validate(self):
        if self.dataset_jobs:
            for k in self.dataset_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetJobs'] = []
        if self.dataset_jobs is not None:
            for k in self.dataset_jobs:
                result['DatasetJobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_jobs = []
        if m.get('DatasetJobs') is not None:
            for k in m.get('DatasetJobs'):
                temp_model = DatasetJob()
                self.dataset_jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasetJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetJobsResponseBody = None,
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
            temp_model = ListDatasetJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetVersionsRequest(TeaModel):
    def __init__(
        self,
        label_keys: str = None,
        label_values: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        properties: str = None,
        sort_by: str = None,
        source_id: str = None,
        source_types: str = None,
    ):
        # The dataset tag keys, which are used to filter datasets. Datasets whose tag keys or tag values contain a specified string are filtered.
        self.label_keys = label_keys
        # The dataset tag values, which are used to filter datasets. Datasets whose tag keys or tag values contain a specified string are filtered.
        self.label_values = label_values
        # The order in which the entries are sorted by the specific field on the returned page. Default value: ASC. Valid values:
        # 
        # *   ASC: ascending order
        # *   DESC: descending order.
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The dataset properties. Valid values:
        # 
        # *   DIRECTORY
        # *   FILE
        self.properties = properties
        # The field used to sort the results in queries by page. Default value: GmtCreateTime.
        # Valid values:
        # 
        # *   SourceType
        # *   DataSourceType
        # *   DataSize
        # *   DataCount
        # *   Property
        # *   GmtCreateTime: The results are sorted by creation time. This is the default value.
        # *   GmtModifiedTime: The results are sorted by modification time.
        # *   DatasetId
        self.sort_by = sort_by
        # The data source ID.
        # 
        # *   If SourceType is set to USER, the value of SourceId is a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The source type. Valid values:
        # 
        # *   PAI-PUBLIC-DATASET: a public dataset of Platform for AI (PAI).
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
        self.source_types = source_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        if self.label_values is not None:
            result['LabelValues'] = self.label_values
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_types is not None:
            result['SourceTypes'] = self.source_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        if m.get('LabelValues') is not None:
            self.label_values = m.get('LabelValues')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceTypes') is not None:
            self.source_types = m.get('SourceTypes')
        return self


class ListDatasetVersionsResponseBody(TeaModel):
    def __init__(
        self,
        dataset_versions: List[DatasetVersion] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The dataset versions.
        self.dataset_versions = dataset_versions
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of dataset versions that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.dataset_versions:
            for k in self.dataset_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetVersions'] = []
        if self.dataset_versions is not None:
            for k in self.dataset_versions:
                result['DatasetVersions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_versions = []
        if m.get('DatasetVersions') is not None:
            for k in m.get('DatasetVersions'):
                temp_model = DatasetVersion()
                self.dataset_versions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasetVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetVersionsResponseBody = None,
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
            temp_model = ListDatasetVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetsRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        data_source_types: str = None,
        data_types: str = None,
        edition: str = None,
        label: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        properties: str = None,
        provider: str = None,
        share_scope: str = None,
        sort_by: str = None,
        source_dataset_id: str = None,
        source_id: str = None,
        source_types: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        # The storage types of the data source. Multiple data source types are separated by commas (,). Valid values:
        # 
        # *   NAS: File Storage NAS (NAS).
        # *   OSS: Object Storage Service (OSS).
        self.data_source_types = data_source_types
        # The dataset types. Multiple dataset types are separated by commas (,). Valid values:
        # 
        # *   Video: video
        # *   COMMON: common
        # *   TEXT: text
        # *   PIC: picture
        # *   AUDIO: audio
        self.data_types = data_types
        self.edition = edition
        # The dataset tag, which is used to filter datasets. Datasets whose tag key or tag value contains a specified string are filtered.
        self.label = label
        # The dataset name. Fuzzy search based on the dataset name is supported.
        self.name = name
        # The order of specific fields of the entries on the returned page. Valid values: ASC and DESC. Default value: ASC.
        # 
        # *   ASC: The entries are sorted in ascending order.
        # *   DESC: The entries are sorted in descending order.
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The dataset properties. Multiple properties are separated by commas (,). Valid values:
        # 
        # *   DIRECTORY
        # *   FILE
        self.properties = properties
        # The dataset provider. If the value pai is returned, the dataset is a public dataset provided by PAI.
        self.provider = provider
        self.share_scope = share_scope
        # The field used for sorting.
        self.sort_by = sort_by
        # The ID of the iTAG labeled dataset that is used as the source dataset.
        self.source_dataset_id = source_dataset_id
        # The data source ID.
        # 
        # *   If SourceType is set to USER, the value of SourceId is a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The source types. Multiple source types are separated by commas (,). Valid values:
        # 
        # *   PAI-PUBLIC-DATASET: a public dataset of Platform for AI (PAI).
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
        self.source_types = source_types
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID. If you do not specify this parameter, the default workspace is used. If the default workspace does not exist, an error is reported.
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
        if self.data_source_types is not None:
            result['DataSourceTypes'] = self.data_source_types
        if self.data_types is not None:
            result['DataTypes'] = self.data_types
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.share_scope is not None:
            result['ShareScope'] = self.share_scope
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_types is not None:
            result['SourceTypes'] = self.source_types
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('DataSourceTypes') is not None:
            self.data_source_types = m.get('DataSourceTypes')
        if m.get('DataTypes') is not None:
            self.data_types = m.get('DataTypes')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('ShareScope') is not None:
            self.share_scope = m.get('ShareScope')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceTypes') is not None:
            self.source_types = m.get('SourceTypes')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasetsResponseBody(TeaModel):
    def __init__(
        self,
        datasets: List[Dataset] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The datasets.
        self.datasets = datasets
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = Dataset()
                self.datasets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasetsResponseBody = None,
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
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentRequestOptions(TeaModel):
    def __init__(
        self,
        match_name_exactly: str = None,
    ):
        # Specifies whether to exactly match the experiment by name. Valid values: true and false.
        self.match_name_exactly = match_name_exactly

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_name_exactly is not None:
            result['match_name_exactly'] = self.match_name_exactly
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match_name_exactly') is not None:
            self.match_name_exactly = m.get('match_name_exactly')
        return self


class ListExperimentRequest(TeaModel):
    def __init__(
        self,
        labels: str = None,
        max_results: int = None,
        name: str = None,
        options: ListExperimentRequestOptions = None,
        order: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        page_token: int = None,
        sort_by: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The tag filter conditions. Multiple conditions are separated by commas (,). The format of a single condition filter is `key=value`.
        self.labels = labels
        # The maximum number of entries in the request. Default value: 10.
        self.max_results = max_results
        # The experiment name.
        self.name = name
        # The optional parameters.
        self.options = options
        # The order of specific fields of results in a paged query (ascending or descending).
        # 
        # *   ASC: ascending order
        # *   DESC: descending order. This is the default value.
        self.order = order
        # The strings used for sorting. The following fields can be used for sorting: GmtCreateTime, Name, GmtModifiedTime, and ExperimentId. The sorting order can be ASC (default) and DESC.
        self.order_by = order_by
        # The page number. The value starts from 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The pagination token, which starts from 0. Default value: 0.
        self.page_token = page_token
        # The field used for sorting. The GmtCreateTime field is used.
        self.sort_by = sort_by
        # Specifies whether to obtain the LatestRun value that is related to the experiment.
        self.verbose = verbose
        # The ID of the workspace to which the experiment belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # >  If you do not specify a workspace ID, the system returns the experiments in the default workspace.
        self.workspace_id = workspace_id

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            temp_model = ListExperimentRequestOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListExperimentShrinkRequest(TeaModel):
    def __init__(
        self,
        labels: str = None,
        max_results: int = None,
        name: str = None,
        options_shrink: str = None,
        order: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        page_token: int = None,
        sort_by: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The tag filter conditions. Multiple conditions are separated by commas (,). The format of a single condition filter is `key=value`.
        self.labels = labels
        # The maximum number of entries in the request. Default value: 10.
        self.max_results = max_results
        # The experiment name.
        self.name = name
        # The optional parameters.
        self.options_shrink = options_shrink
        # The order of specific fields of results in a paged query (ascending or descending).
        # 
        # *   ASC: ascending order
        # *   DESC: descending order. This is the default value.
        self.order = order
        # The strings used for sorting. The following fields can be used for sorting: GmtCreateTime, Name, GmtModifiedTime, and ExperimentId. The sorting order can be ASC (default) and DESC.
        self.order_by = order_by
        # The page number. The value starts from 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The pagination token, which starts from 0. Default value: 0.
        self.page_token = page_token
        # The field used for sorting. The GmtCreateTime field is used.
        self.sort_by = sort_by
        # Specifies whether to obtain the LatestRun value that is related to the experiment.
        self.verbose = verbose
        # The ID of the workspace to which the experiment belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # >  If you do not specify a workspace ID, the system returns the experiments in the default workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.options_shrink is not None:
            result['Options'] = self.options_shrink
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiments: List[Experiment] = None,
        next_page_token: int = None,
        total_count: int = None,
        request_id: str = None,
    ):
        # The list of experiments.
        self.experiments = experiments
        # The pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The total number of entries.
        self.total_count = total_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = Experiment()
                self.experiments.append(temp_model.from_map(k))
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentResponseBody = None,
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
            temp_model = ListExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeaturesRequest(TeaModel):
    def __init__(
        self,
        names: str = None,
    ):
        self.names = names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        return self


class ListFeaturesResponseBody(TeaModel):
    def __init__(
        self,
        features: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.features = features
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.features is not None:
            result['Features'] = self.features
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFeaturesResponseBody = None,
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
            temp_model = ListFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageLabelsRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        label_filter: str = None,
        label_keys: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        # The image ID. You can call [ListImages](https://help.aliyun.com/document_detail/449118.html) to obtain the image ID.
        self.image_id = image_id
        # The tag filter conditions, separated with commas (,). The format of a single condition filter is `key=value`. Takes effect independently from LabelKeys.
        self.label_filter = label_filter
        # The tag keys, separated with commas (,). System tags start with system and take effect independently from LabelFilter.
        self.label_keys = label_keys
        # The region where the image resides.
        self.region = region
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.label_filter is not None:
            result['LabelFilter'] = self.label_filter
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys
        if self.region is not None:
            result['Region'] = self.region
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LabelFilter') is not None:
            self.label_filter = m.get('LabelFilter')
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListImageLabelsResponseBodyLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListImageLabelsResponseBody(TeaModel):
    def __init__(
        self,
        labels: List[ListImageLabelsResponseBodyLabels] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The image tags.
        self.labels = labels
        # The request ID.
        self.request_id = request_id
        # The total number of the images that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImageLabelsResponseBodyLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImageLabelsResponseBody = None,
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
            temp_model = ListImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        image_uri: str = None,
        labels: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        sort_by: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The visibility of the image. This parameter is valid only for custom images.
        # 
        # *   PUBLIC: The image is visible to all users.
        # *   PRIVATE: The image is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        self.image_uri = image_uri
        # The tag filter conditions. Multiple conditions are separated by commas (,). The format of a single condition filter is `key=value`. The following keys are supported:
        # 
        # *   system.chipType
        # *   system.dsw.cudaVersion
        # *   system.dsw.fromImageId
        # *   system.dsw.fromInstanceId
        # *   system.dsw.id
        # *   system.dsw.os
        # *   system.dsw.osVersion
        # *   system.dsw.resourceType
        # *   system.dsw.rootImageId
        # *   system.dsw.stage
        # *   system.dsw.tag
        # *   system.dsw.type
        # *   system.framework
        # *   system.origin
        # *   system.pythonVersion
        # *   system.source
        # *   system.supported.dlc
        # *   system.supported.dsw
        self.labels = labels
        # The image name. Fuzzy match is supported.
        self.name = name
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy. Default value: ASC. Valid values:
        # 
        # *   ASC: ascending order
        # *   DESC: descending order.
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The image name and description that are used for fuzzy search.
        self.query = query
        # The field used for sorting. The GmtCreateTime field is used.
        self.sort_by = sort_by
        # Specifies whether to display non-essential information, which contains tags. Valid values:
        # 
        # *   true
        # *   false
        self.verbose = verbose
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
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
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListImagesResponseBodyImagesLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        image_id: str = None,
        image_uri: str = None,
        labels: List[ListImagesResponseBodyImagesLabels] = None,
        name: str = None,
        parent_user_id: str = None,
        size: int = None,
        source_id: str = None,
        source_type: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The accessibility of the image. Valid values:
        # 
        # *   PUBLIC: All members can access the image.
        # *   PRIVATE: Only the creator can access the image.
        self.accessibility = accessibility
        # The image description.
        self.description = description
        # The time when the image is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the image is modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The image ID.
        self.image_id = image_id
        # The image address, which includes the version number.
        self.image_uri = image_uri
        # The image tags.
        self.labels = labels
        # The image name.
        self.name = name
        # The ID of the Alibaba Cloud account.
        self.parent_user_id = parent_user_id
        # The image size. Unit: GB.
        self.size = size
        # 镜像来源 ID
        self.source_id = source_id
        # 镜像来源类型
        self.source_type = source_type
        # The user ID.
        self.user_id = user_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id
        if self.size is not None:
            result['Size'] = self.size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListImagesResponseBodyImagesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[ListImagesResponseBodyImages] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The images.
        self.images = images
        # The request ID.
        self.request_id = request_id
        # The total number of returned images.
        self.total_count = total_count

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesResponseBody = None,
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMembersRequest(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        page_number: int = None,
        page_size: int = None,
        roles: str = None,
    ):
        # The member name. Fuzzy match is supported.
        self.member_name = member_name
        # The page number of the workspace list. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The roles that are used to filter members. Multiple roles are separated by commas (,). Valid values:
        # 
        # *   PAI.AlgoDeveloper: algorithm developer
        # *   PAI.AlgoOperator: algorithm O\\&M engineer
        # *   PAI.LabelManager: labeling administrator
        # *   PAI.MaxComputeDeveloper: MaxCompute developer
        # *   PAI.WorkspaceAdmin: administrator
        # *   PAI.WorkspaceGuest: guest
        # *   PAI.WorkspaceOwner: owner
        self.roles = roles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.roles is not None:
            result['Roles'] = self.roles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        return self


class ListMembersResponseBodyMembers(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        member_id: str = None,
        member_name: str = None,
        roles: List[str] = None,
        user_id: str = None,
    ):
        self.account_name = account_name
        self.account_type = account_type
        # The display name of the member.
        self.display_name = display_name
        # The time when the user is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The member ID.
        self.member_id = member_id
        # The username.
        self.member_name = member_name
        # The list of roles.
        self.roles = roles
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListMembersResponseBody(TeaModel):
    def __init__(
        self,
        members: List[ListMembersResponseBodyMembers] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The members.
        self.members = members
        # The request ID.
        self.request_id = request_id
        # The number of members that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = ListMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMembersResponseBody = None,
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
            temp_model = ListMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelVersionsRequest(TeaModel):
    def __init__(
        self,
        approval_status: str = None,
        format_type: str = None,
        framework_type: str = None,
        label: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        source_id: str = None,
        source_type: str = None,
        version_name: str = None,
    ):
        # The approval status based on which the model versions are queried. Valid values:
        # 
        # *   Pending
        # *   Approved
        # *   Rejected
        self.approval_status = approval_status
        # The model format used to filter model versions. Valid values:
        # 
        # *   OfflineModel
        # *   SavedModel
        # *   Keras H5
        # *   Frozen Pb
        # *   Caffe Prototxt
        # *   TorchScript
        # *   XGBoost
        # *   PMML
        # *   AlinkModel
        # *   ONNX
        self.format_type = format_type
        # The framework used to filter model versions.
        # 
        # *   Pytorch -XGBoost
        # *   Keras
        # *   Caffe
        # *   Alink
        # *   Xflow
        # *   TensorFlow
        self.framework_type = framework_type
        # The label. Model versions whose label key or label value contains a specific label are filtered.
        self.label = label
        # The order in which the entries are sorted by the specific field on the returned page. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The field used to sort the results. The GmtCreateTime field is used for sorting.
        self.sort_by = sort_by
        # The source ID.
        # 
        # *   If the source type is Custom, this field is not limited.
        # *   If the source type is PAIFlow or TrainingService, the format is:
        # 
        # <!---->
        # 
        #     region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # 
        # Take note of the following parameters:
        # 
        # *   region is the region ID.
        # *   workspaceId is the ID of the workspace.
        # *   kind is the type. Valid values: PipelineRun (PAIFlow) and ServiceJob (training service).
        # *   id is a unique identifier.
        self.source_id = source_id
        # The source type used to filter model versions. Valid values:
        # 
        # *   Custom (default)
        # *   PAIFlow
        # *   TrainingService
        self.source_type = source_type
        # The model version used to filter model versions.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type
        if self.label is not None:
            result['Label'] = self.label
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListModelVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        versions: List[ModelVersion] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of model versions.
        self.total_count = total_count
        # The model versions.
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ModelVersion()
                self.versions.append(temp_model.from_map(k))
        return self


class ListModelVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelVersionsResponseBody = None,
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
            temp_model = ListModelVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsRequestConditions(TeaModel):
    def __init__(
        self,
        column: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.column = column
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['Column'] = self.column
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListModelsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListModelsRequest(TeaModel):
    def __init__(
        self,
        collections: str = None,
        conditions: List[ListModelsRequestConditions] = None,
        domain: str = None,
        label: str = None,
        model_name: str = None,
        model_type: str = None,
        order: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        provider: str = None,
        query: str = None,
        sort_by: str = None,
        tag: List[ListModelsRequestTag] = None,
        task: str = None,
        workspace_id: str = None,
    ):
        # The collection where the model is located. You can specify multiple collections and separate them with commas (,).
        self.collections = collections
        self.conditions = conditions
        # The domain. Only models in the domain are returned. Valid values: nlp (Natural Language Processing) and cv (Computer Vision).
        self.domain = domain
        # The label. Models whose label key or label value contains a specific label are filtered.
        self.label = label
        # The model name used to filter the returned models.
        self.model_name = model_name
        # The model type.
        self.model_type = model_type
        # The order in which the entries are sorted by the specific field on the returned page. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The model source used to filter the models that belong to a community or organization, such as ModelScope and Hugging Face.
        self.origin = origin
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The provider. If you configure this parameter, only the models exposed by the provider are returned. If you leave this parameter empty, only models owned by the user are returned.
        self.provider = provider
        # The query condition. For example, if you set the value to nlp, all models that match ModelName, Domain, Task, LabelKey, and LabelValue are returned.
        self.query = query
        # The field used to sort the results. The GmtCreateTime field is used for sorting.
        self.sort_by = sort_by
        # The tags of the model.
        self.tag = tag
        # The task used to filter the models that belong to the task type. Example: text-classification.
        self.task = task
        # The workspace ID. Only models in this workspace are queried. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collections is not None:
            result['Collections'] = self.collections
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.label is not None:
            result['Label'] = self.label
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.order is not None:
            result['Order'] = self.order
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.query is not None:
            result['Query'] = self.query
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.task is not None:
            result['Task'] = self.task
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = ListModelsRequestConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListModelsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListModelsShrinkRequest(TeaModel):
    def __init__(
        self,
        collections: str = None,
        conditions_shrink: str = None,
        domain: str = None,
        label: str = None,
        model_name: str = None,
        model_type: str = None,
        order: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        provider: str = None,
        query: str = None,
        sort_by: str = None,
        tag_shrink: str = None,
        task: str = None,
        workspace_id: str = None,
    ):
        # The collection where the model is located. You can specify multiple collections and separate them with commas (,).
        self.collections = collections
        self.conditions_shrink = conditions_shrink
        # The domain. Only models in the domain are returned. Valid values: nlp (Natural Language Processing) and cv (Computer Vision).
        self.domain = domain
        # The label. Models whose label key or label value contains a specific label are filtered.
        self.label = label
        # The model name used to filter the returned models.
        self.model_name = model_name
        # The model type.
        self.model_type = model_type
        # The order in which the entries are sorted by the specific field on the returned page. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The model source used to filter the models that belong to a community or organization, such as ModelScope and Hugging Face.
        self.origin = origin
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The provider. If you configure this parameter, only the models exposed by the provider are returned. If you leave this parameter empty, only models owned by the user are returned.
        self.provider = provider
        # The query condition. For example, if you set the value to nlp, all models that match ModelName, Domain, Task, LabelKey, and LabelValue are returned.
        self.query = query
        # The field used to sort the results. The GmtCreateTime field is used for sorting.
        self.sort_by = sort_by
        # The tags of the model.
        self.tag_shrink = tag_shrink
        # The task used to filter the models that belong to the task type. Example: text-classification.
        self.task = task
        # The workspace ID. Only models in this workspace are queried. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collections is not None:
            result['Collections'] = self.collections
        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.label is not None:
            result['Label'] = self.label
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.order is not None:
            result['Order'] = self.order
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.query is not None:
            result['Query'] = self.query
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.task is not None:
            result['Task'] = self.task
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')
        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListModelsResponseBody(TeaModel):
    def __init__(
        self,
        models: List[Model] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The models.
        self.models = models
        # The request ID.
        self.request_id = request_id
        # The total number of models.
        self.total_count = total_count

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = Model()
                self.models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelsResponseBody = None,
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
            temp_model = ListModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionsResponseBodyPermissionsPermissionRules(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        entity_access_type: str = None,
    ):
        # The accessibility of the permission rule. Valid values:
        # 
        # *   PUBLIC: All members in the workspace can access the permission rule.
        # *   PRIVATE: Only the creator can access the permission rule.
        # *   ANY: All users can access the permission rule.
        self.accessibility = accessibility
        # The type of access. If you set Accessibility to PUBLIC, all users can access the workspace. This parameter is invalid. If you set Accessibility to PRIVATE, the permissions are determined based on the value of EntityAccessType. The value of EntityAccessType can be:
        # 
        # *   CREATOR: Only the creator can access the workspace.
        # *   ANY: All users can access the workspace.
        self.entity_access_type = entity_access_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.entity_access_type is not None:
            result['EntityAccessType'] = self.entity_access_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('EntityAccessType') is not None:
            self.entity_access_type = m.get('EntityAccessType')
        return self


class ListPermissionsResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        permission_code: str = None,
        permission_rules: List[ListPermissionsResponseBodyPermissionsPermissionRules] = None,
    ):
        # The permission name, which is unique in a region. For more information about permissions, see [Appendix: Roles and permissions](https://help.aliyun.com/document_detail/2840449.html). The example value PaiDLC:GetTensorboard indicates the permission to view details about a TensorBoard job on the Deep Learning Containers (DLC) page.
        self.permission_code = permission_code
        # The permission rules.
        self.permission_rules = permission_rules

    def validate(self):
        if self.permission_rules:
            for k in self.permission_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code
        result['PermissionRules'] = []
        if self.permission_rules is not None:
            for k in self.permission_rules:
                result['PermissionRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')
        self.permission_rules = []
        if m.get('PermissionRules') is not None:
            for k in m.get('PermissionRules'):
                temp_model = ListPermissionsResponseBodyPermissionsPermissionRules()
                self.permission_rules.append(temp_model.from_map(k))
        return self


class ListPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        permissions: List[ListPermissionsResponseBodyPermissions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The permissions.
        self.permissions = permissions
        # The request ID.
        self.request_id = request_id
        # The number of permissions that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = ListPermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPermissionsResponseBody = None,
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
            temp_model = ListPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        product_codes: str = None,
        service_codes: str = None,
        verbose: bool = None,
    ):
        self.product_codes = product_codes
        self.service_codes = service_codes
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_codes is not None:
            result['ProductCodes'] = self.product_codes
        if self.service_codes is not None:
            result['ServiceCodes'] = self.service_codes
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCodes') is not None:
            self.product_codes = m.get('ProductCodes')
        if m.get('ServiceCodes') is not None:
            self.service_codes = m.get('ServiceCodes')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class ListProductsResponseBodyProducts(TeaModel):
    def __init__(
        self,
        has_permission_to_purchase: bool = None,
        is_purchased: bool = None,
        product_code: str = None,
        product_id: str = None,
        purchase_url: str = None,
    ):
        self.has_permission_to_purchase = has_permission_to_purchase
        self.is_purchased = is_purchased
        self.product_code = product_code
        self.product_id = product_id
        self.purchase_url = purchase_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_permission_to_purchase is not None:
            result['HasPermissionToPurchase'] = self.has_permission_to_purchase
        if self.is_purchased is not None:
            result['IsPurchased'] = self.is_purchased
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.purchase_url is not None:
            result['PurchaseUrl'] = self.purchase_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPermissionToPurchase') is not None:
            self.has_permission_to_purchase = m.get('HasPermissionToPurchase')
        if m.get('IsPurchased') is not None:
            self.is_purchased = m.get('IsPurchased')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('PurchaseUrl') is not None:
            self.purchase_url = m.get('PurchaseUrl')
        return self


class ListProductsResponseBodyServices(TeaModel):
    def __init__(
        self,
        is_open: bool = None,
        open_url: str = None,
        service_code: str = None,
    ):
        self.is_open = is_open
        self.open_url = open_url
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_open is not None:
            result['IsOpen'] = self.is_open
        if self.open_url is not None:
            result['OpenUrl'] = self.open_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsOpen') is not None:
            self.is_open = m.get('IsOpen')
        if m.get('OpenUrl') is not None:
            self.open_url = m.get('OpenUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        products: List[ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        services: List[ListProductsResponseBodyServices] = None,
    ):
        self.products = products
        self.request_id = request_id
        self.services = services

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Products'] = []
        if self.products is not None:
            for k in self.products:
                result['Products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('Products') is not None:
            for k in m.get('Products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListProductsResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The quota name. Fuzzy search is supported.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListQuotasResponseBodyQuotasSpecs(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The specification name.
        self.name = name
        # The specification type. The parameter can be left empty.
        self.type = type
        # The specification value.
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
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        mode: str = None,
        name: str = None,
        product_code: str = None,
        quota_type: str = None,
        specs: List[ListQuotasResponseBodyQuotasSpecs] = None,
    ):
        # The alias of the quota.
        self.display_name = display_name
        # The quota ID.
        self.id = id
        # The billing method. Valid values:
        # 
        # *   isolate: subscription
        # *   share: pay-as-you-go
        self.mode = mode
        # The quota name.
        self.name = name
        # The product code. Valid values:
        # 
        # *   PAI_isolate: CPU subscription resource groups of PAI
        # *   PAI_share: GPU pay-as-you-go resource groups of PAI
        self.product_code = product_code
        # The quota type. Valid value:
        # 
        # PAI: indicates GPU resource groups of MaxCompute.
        self.quota_type = quota_type
        # The quota specifications.
        self.specs = specs

    def validate(self):
        if self.specs:
            for k in self.specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        result['Specs'] = []
        if self.specs is not None:
            for k in self.specs:
                result['Specs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        self.specs = []
        if m.get('Specs') is not None:
            for k in m.get('Specs'):
                temp_model = ListQuotasResponseBodyQuotasSpecs()
                self.specs.append(temp_model.from_map(k))
        return self


class ListQuotasResponseBody(TeaModel):
    def __init__(
        self,
        quotas: List[ListQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned quotas.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id
        # The number of quotas that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotasResponseBody = None,
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
            temp_model = ListQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        labels: str = None,
        option: str = None,
        page_number: int = None,
        page_size: int = None,
        product_types: str = None,
        quota_ids: str = None,
        resource_name: str = None,
        resource_types: str = None,
        verbose: bool = None,
        verbose_fields: str = None,
        workspace_id: str = None,
    ):
        # The name of the resource group. You can call [ListResources](https://help.aliyun.com/document_detail/449143.html) to obtain the name of the resource group.
        self.group_name = group_name
        # Tag-based filter conditions. Multiple conditions are separated by commas (,). Only resources that meet all the specified tag-based filter conditions are returned.
        # 
        # This parameter is available only for resources whose ProductType is ACS.
        self.labels = labels
        # The operation to perform. Valid values:
        # 
        # *   ListResourceByWorkspace: obtains the resources in the workspace. This is the default value.
        # *   ListResource: obtains the resources of the user.
        self.option = option
        # The page number. The pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # **This field is no longer used and will be removed. Use the ResourceType field instead.
        self.product_types = product_types
        # The quota IDs, which are separated by commas (,). Only resources that contain all the specified quotas are returned.
        # 
        # >  This parameter is available only for resources whose ResourceTypes is ACS.
        self.quota_ids = quota_ids
        # The resource name. The value must meet the following requirements:
        # 
        # *   The name must be 3 to 28 characters in length.
        # *   The name is unique in the region.
        self.resource_name = resource_name
        # The resource types. Valid values:
        # 
        # *   MaxCompute
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        self.resource_types = resource_types
        # Specifies whether to show detailed information, which includes the Quotas field. Valid values:
        # 
        # *   true (default)
        # *   false
        self.verbose = verbose
        # The fields to return. Multiple fields are separated by commas (,). Valid values:
        # 
        # *   Quota
        # *   Label
        # *   IsDefault
        self.verbose_fields = verbose_fields
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # *   This parameter is required when the Option parameter is set to ListResourceByWorkspace.
        # *   You do not need to configure this parameter when the Option parameter is set to ListResource.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.option is not None:
            result['Option'] = self.option
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_types is not None:
            result['ProductTypes'] = self.product_types
        if self.quota_ids is not None:
            result['QuotaIds'] = self.quota_ids
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.verbose_fields is not None:
            result['VerboseFields'] = self.verbose_fields
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductTypes') is not None:
            self.product_types = m.get('ProductTypes')
        if m.get('QuotaIds') is not None:
            self.quota_ids = m.get('QuotaIds')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('VerboseFields') is not None:
            self.verbose_fields = m.get('VerboseFields')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListResourcesResponseBodyResourcesEncryption(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        enabled: bool = None,
        key: str = None,
    ):
        # The encryption algorithm.
        self.algorithm = algorithm
        # Indicates whether the resources are encrypted.
        self.enabled = enabled
        # The primary key for the encryption.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListResourcesResponseBodyResourcesExecutor(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
    ):
        # This parameter is invalid and deprecated.
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ListResourcesResponseBodyResourcesLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListResourcesResponseBodyResourcesQuotasSpecs(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The specification name.
        self.name = name
        # The specification description.
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


class ListResourcesResponseBodyResourcesQuotas(TeaModel):
    def __init__(
        self,
        card_type: str = None,
        display_name: str = None,
        id: str = None,
        mode: str = None,
        name: str = None,
        product_code: str = None,
        quota_type: str = None,
        specs: List[ListResourcesResponseBodyResourcesQuotasSpecs] = None,
    ):
        # The resource group type. Valid values:
        # 
        # *   CPU
        # *   GPU
        self.card_type = card_type
        # The alias of the quota.
        self.display_name = display_name
        # The quota ID.
        self.id = id
        # The billing method. Valid values:
        # 
        # *   isolate: subscription
        # *   share: pay-as-you-go
        self.mode = mode
        # The quota name.
        self.name = name
        # The product code. Valid values:
        # 
        # *   PAI_isolate: CPU subscription resource groups of PAI
        # *   PAI_share: GPU pay-as-you-go resource groups of PAI
        # *   MaxCompute_share: pay-as-you-go resource groups of MaxCompute
        # *   MaxCompute_isolate: subscription resource groups of MaxCompute
        # *   DataWorks_isolate: subscription resource groups of DataWorks
        # *   DataWorks_share: pay-as-you-go resource groups of DataWorks
        # *   DLC_share: pay-as-you-go resource groups of Deep Learning Containers (DLC)
        self.product_code = product_code
        # The quota type. Valid values:
        # 
        # *   PAI
        # *   MaxCompute
        # *   DLC
        self.quota_type = quota_type
        # The quota specifications.
        self.specs = specs

    def validate(self):
        if self.specs:
            for k in self.specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        result['Specs'] = []
        if self.specs is not None:
            for k in self.specs:
                result['Specs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        self.specs = []
        if m.get('Specs') is not None:
            for k in m.get('Specs'):
                temp_model = ListResourcesResponseBodyResourcesQuotasSpecs()
                self.specs.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        encryption: ListResourcesResponseBodyResourcesEncryption = None,
        env_type: str = None,
        executor: ListResourcesResponseBodyResourcesExecutor = None,
        gmt_create_time: str = None,
        group_name: str = None,
        id: str = None,
        is_default: bool = None,
        labels: List[ListResourcesResponseBodyResourcesLabels] = None,
        name: str = None,
        product_type: str = None,
        quotas: List[ListResourcesResponseBodyResourcesQuotas] = None,
        resource_type: str = None,
        spec: Dict[str, Any] = None,
        workspace_id: str = None,
    ):
        # The encryption information, which is valid only for MaxCompute resources.
        self.encryption = encryption
        # The environment type. Valid values:
        # 
        # *   dev: development environment
        # *   prod: production environment
        self.env_type = env_type
        # This parameter is invalid and deprecated.
        self.executor = executor
        # The time when the resource group is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The name of the resource group, which is unique within the Alibaba Cloud account.
        self.group_name = group_name
        # The resource ID.
        self.id = id
        # Indicates whether the resource is the default resource. Each type of resources has a default resource. Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default
        # The tags.
        self.labels = labels
        # The resource name.
        self.name = name
        # **This field is no longer used and will be removed. Use the ResourceType field.
        self.product_type = product_type
        # The quotas.
        self.quotas = quotas
        # The resource type. Valid values:
        # 
        # *   MaxCompute
        # *   DLC
        # *   FLINK
        self.resource_type = resource_type
        # The resource specification.
        self.spec = spec
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.executor:
            self.executor.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption is not None:
            result['Encryption'] = self.encryption.to_map()
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.executor is not None:
            result['Executor'] = self.executor.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encryption') is not None:
            temp_model = ListResourcesResponseBodyResourcesEncryption()
            self.encryption = temp_model.from_map(m['Encryption'])
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Executor') is not None:
            temp_model = ListResourcesResponseBodyResourcesExecutor()
            self.executor = temp_model.from_map(m['Executor'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListResourcesResponseBodyResourcesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListResourcesResponseBodyResourcesQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[ListResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources
        # The number of resources that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
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
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunMetricsRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        max_results: int = None,
        page_token: int = None,
    ):
        # The metric key of the run.
        # 
        # This parameter is required.
        self.key = key
        # The maximum number of entries in the request. Default value: 10.
        self.max_results = max_results
        # The pagination token, which starts from 0. Default value: 0.
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        return self


class ListRunMetricsResponseBody(TeaModel):
    def __init__(
        self,
        metrics: List[RunMetric] = None,
        next_page_token: int = None,
        request_id: str = None,
    ):
        # The metrics.
        self.metrics = metrics
        # The pagination token that is used to retrieve the next page. You do not need to specify this parameter for the first request. You must specify the pagination token in the result of the previous query. If the pagination token is 0, no next page exists. You can obtain the pagination token that is used to retrieve the next page in the value of the **NextPageToken** field.
        self.next_page_token = next_page_token
        # Id of the request
        self.request_id = request_id

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
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = RunMetric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRunMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRunMetricsResponseBody = None,
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
            temp_model = ListRunMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunsRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        gmt_create_time: str = None,
        labels: str = None,
        max_results: int = None,
        name: str = None,
        order: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        page_token: int = None,
        sort_by: str = None,
        source_id: str = None,
        source_type: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The ID of the experiment that the run belongs.
        self.experiment_id = experiment_id
        # The time when the instance was created.
        self.gmt_create_time = gmt_create_time
        # The label. Exact match is supported. Valid values:
        # 
        # *   Single-label query: Set the value to is_evaluation.
        # *   Multi-label query (not recommended in non-special scenarios and may have performance issues): Set the value to is_evaluation:true,LLM_evaluation:true. Multiple labels are separated with commas (,), indicating that the key-value pairs of multiple labels must be matched at the same time.
        self.labels = labels
        # The maximum number of entries in the request. Default value: 10.
        self.max_results = max_results
        # The run name.
        self.name = name
        # The order in which the entries are sorted by the specific field on the returned page. This parameter must be used together with SortBy.
        # 
        # *   ASC
        # *   DESC (default)
        self.order = order
        # The strings by which the results are sorted. The following parameters can be used to sort the results: GmtCreateTime and Name. The sorting order can be ASC (default) and DESC. Separate multiple strings with commas (,).
        self.order_by = order_by
        # The page number. The value must be greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The pagination token, which starts from 0. Default value: 0.
        self.page_token = page_token
        # The field used for sorting. Valid values:
        # 
        # *   Name: the name of the run.
        # *   GmtCreateTime: the time when the run is created.
        self.sort_by = sort_by
        # The ID of the workload associated with the run.
        self.source_id = source_id
        # The type of the workload associated with the run.
        self.source_type = source_type
        # Specifies whether to show detailed information, including Metrics, Params, and Labels. Valid values:
        # 
        # *   true
        # *   false (default)
        self.verbose = verbose
        # The ID of the workspace to which the experiment belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # >  If you do not specify a workspace ID, the system returns the runs of the default workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListRunsResponseBody(TeaModel):
    def __init__(
        self,
        next_page_token: int = None,
        runs: List[Run] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        # The pagination token that is used to retrieve the next page. You do not need to specify this parameter for the first request. You must specify the pagination token in the result of the previous query. If the pagination token is 0, no next page exists. You can obtain the pagination token that is used to retrieve the next page in the value of the **NextPageToken** field.
        self.next_page_token = next_page_token
        # The runs.
        self.runs = runs
        # The total number of entries returned. By default, this parameter is not returned.
        self.total_count = total_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.runs:
            for k in self.runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['Runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['Runs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.runs = []
        if m.get('Runs') is not None:
            for k in m.get('Runs'):
                temp_model = Run()
                self.runs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRunsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRunsResponseBody = None,
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
            temp_model = ListRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserConfigsRequest(TeaModel):
    def __init__(
        self,
        category_names: str = None,
        config_keys: str = None,
    ):
        # The category. Currently, only DataPrivacyConfig is supported.
        self.category_names = category_names
        # The configuration item keys. Currently, only customizePAIAssumedRole is supported.
        self.config_keys = config_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_names is not None:
            result['CategoryNames'] = self.category_names
        if self.config_keys is not None:
            result['ConfigKeys'] = self.config_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryNames') is not None:
            self.category_names = m.get('CategoryNames')
        if m.get('ConfigKeys') is not None:
            self.config_keys = m.get('ConfigKeys')
        return self


class ListUserConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        scope: str = None,
    ):
        # The category. Currently, only DataPrivacyConfig is supported.
        self.category_name = category_name
        # The key of the configuration item.
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value
        # The scope. Currently, subUser and owner are supported.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ListUserConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[ListUserConfigsResponseBodyConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configurations list.
        self.configs = configs
        # The request ID.
        self.request_id = request_id
        # The number of items returned.
        self.total_count = total_count

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = ListUserConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserConfigsResponseBody = None,
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
            temp_model = ListUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspaceUsersRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        # The display names of users who can be added to the workspace as members.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListWorkspaceUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListWorkspaceUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[ListWorkspaceUsersResponseBodyUsers] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The number of users who meet the filter conditions.
        self.total_count = total_count
        # The users.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListWorkspaceUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListWorkspaceUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkspaceUsersResponseBody = None,
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
            temp_model = ListWorkspaceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(
        self,
        fields: str = None,
        module_list: str = None,
        option: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        sort_by: str = None,
        status: str = None,
        verbose: bool = None,
        workspace_ids: str = None,
        workspace_name: str = None,
    ):
        # The list of returned fields of workspace details. Used to limit the fields in the returned results. Separate multiple fields with commas (,). Currently, only Id is supported, which is the workspace ID.
        self.fields = fields
        # The modules, separated by commas (,). Default value: PAI.
        self.module_list = module_list
        # The query options. Valid values:
        # 
        # *   GetWorkspaces (default): Obtains a list of Workspaces.
        # *   GetResourceLimits: Obtains a list of ResourceLimits.
        self.option = option
        # The order of results (ascending or descending). Valid values:
        # 
        # *   ASC: ascending order. This is the default value.
        # *   DESC: descending order.
        self.order = order
        # The page number of the workspace list. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The resource group ID. To obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # Specifies how to sort the results. Default value: GmtCreateTime. Valid values:
        # 
        # *   GmtCreateTime: Sort by the time when created.
        # *   GmtModifiedTime: Sort by the time when modified.
        self.sort_by = sort_by
        # The workspace status. Valid values:
        # 
        # *   ENABLED
        # *   INITIALIZING
        # *   FAILURE
        # *   DISABLED
        # *   FROZEN
        # *   UPDATING
        self.status = status
        # Specifies whether to display workspace details. Valid values:
        # 
        # *   false (default)
        # *   true
        self.verbose = verbose
        # The workspace IDs. Separate multiple IDs by commas (,).
        self.workspace_ids = workspace_ids
        # The name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.option is not None:
            result['Option'] = self.option
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(
        self,
        admin_names: List[str] = None,
        creator: str = None,
        description: str = None,
        env_types: List[str] = None,
        extra_infos: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        is_default: bool = None,
        status: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        resource_group_id: str = None,
    ):
        # The names of the administrator accounts.
        self.admin_names = admin_names
        # The user ID of the creator.
        self.creator = creator
        # The description of the workspace.
        self.description = description
        # The environment types of the workspace.
        self.env_types = env_types
        # the additional information. Only contains TenantId.
        self.extra_infos = extra_infos
        # The time when the workspace was created. The time (UTC+0) follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ss.SSSZ format.
        self.gmt_create_time = gmt_create_time
        # The time when the workspace was modified. The time (UTC+0) follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ss.SSSZ format.
        self.gmt_modified_time = gmt_modified_time
        # Indicates whether the workspace is the default workspace.
        self.is_default = is_default
        # The status of the workspace.
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_names is not None:
            result['AdminNames'] = self.admin_names
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.env_types is not None:
            result['EnvTypes'] = self.env_types
        if self.extra_infos is not None:
            result['ExtraInfos'] = self.extra_infos
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminNames') is not None:
            self.admin_names = m.get('AdminNames')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')
        if m.get('ExtraInfos') is not None:
            self.extra_infos = m.get('ExtraInfos')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_limits: Dict[str, Any] = None,
        total_count: int = None,
        workspaces: List[ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The type and quantity of resources that can be activated in a workspace. This list is returned when the Option is set to GetResourceLimits. Valid values:
        # 
        # *   MaxCompute_share: pay-as-you-go MaxCompute
        # *   MaxCompute_isolate: subscription MaxCompute
        # *   DLC_share: pay-as-you-go DLC
        # *   PAI_Isolate: subscription PAI
        # *   PAI_share: pay-as-you-go PAI
        # *   DataWorks_isolate: subscription DataWorks
        # *   DataWorks_share: pay-as-you-go DataWorks
        self.resource_limits = resource_limits
        # The number of workspaces that meet the query conditions.
        self.total_count = total_count
        # The list of workspace details. This list is returned when Option is set to GetWorkspaces.
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_limits is not None:
            result['ResourceLimits'] = self.resource_limits
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['Workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceLimits') is not None:
            self.resource_limits = m.get('ResourceLimits')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k in m.get('Workspaces'):
                temp_model = ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k))
        return self


class ListWorkspacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkspacesResponseBody = None,
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogRunMetricsRequest(TeaModel):
    def __init__(
        self,
        metrics: List[RunMetric] = None,
    ):
        # The metrics.
        self.metrics = metrics

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = RunMetric()
                self.metrics.append(temp_model.from_map(k))
        return self


class LogRunMetricsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class LogRunMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LogRunMetricsResponseBody = None,
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
            temp_model = LogRunMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishCodeSourceResponseBody(TeaModel):
    def __init__(
        self,
        code_source_id: str = None,
        request_id: str = None,
    ):
        # The ID of the code source that is successfully published.
        self.code_source_id = code_source_id
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishCodeSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishCodeSourceResponseBody = None,
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
            temp_model = PublishCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishDatasetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishDatasetResponseBody = None,
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
            temp_model = PublishDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishImageResponseBody = None,
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
            temp_model = PublishImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveImageResponseBody = None,
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
            temp_model = RemoveImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveImageLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveImageLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveImageLabelsResponseBody = None,
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
            temp_model = RemoveImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMemberRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveMemberRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveMemberRoleResponseBody = None,
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
            temp_model = RemoveMemberRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetExperimentLabelsRequest(TeaModel):
    def __init__(
        self,
        labels: List[LabelInfo] = None,
    ):
        # The tags.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = LabelInfo()
                self.labels.append(temp_model.from_map(k))
        return self


class SetExperimentLabelsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetExperimentLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetExperimentLabelsResponseBody = None,
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
            temp_model = SetExperimentLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserConfigsRequestConfigs(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        scope: str = None,
    ):
        # The category. Only DataPrivacyConfig is supported.
        # 
        # This parameter is required.
        self.category_name = category_name
        # The key of the configuration item.
        # 
        # This parameter is required.
        self.config_key = config_key
        # The value of the configuration item.
        # 
        # This parameter is required.
        self.config_value = config_value
        # The scope. Valid values: subUser and owner.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class SetUserConfigsRequest(TeaModel):
    def __init__(
        self,
        configs: List[SetUserConfigsRequestConfigs] = None,
    ):
        # The configurations list.
        self.configs = configs

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = SetUserConfigsRequestConfigs()
                self.configs.append(temp_model.from_map(k))
        return self


class SetUserConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetUserConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetUserConfigsResponseBody = None,
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
            temp_model = SetUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDatasetJobRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The dataset version.
        self.dataset_version = dataset_version
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class StopDatasetJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDatasetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDatasetJobResponseBody = None,
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
            temp_model = StopDatasetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCodeSourceRequest(TeaModel):
    def __init__(
        self,
        code_branch: str = None,
        code_commit: str = None,
        code_repo: str = None,
        code_repo_access_token: str = None,
        code_repo_user_name: str = None,
        description: str = None,
        display_name: str = None,
        mount_path: str = None,
    ):
        # The name of the code branch.
        self.code_branch = code_branch
        # The code commit ID.
        self.code_commit = code_commit
        # The address of the code repository.
        self.code_repo = code_repo
        # The access token corresponding to the username.
        self.code_repo_access_token = code_repo_access_token
        # The username used to access the code repository.
        self.code_repo_user_name = code_repo_user_name
        # The description of the code build.
        self.description = description
        # The name of the code build.
        self.display_name = display_name
        # The default mount path.
        self.mount_path = mount_path

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
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class UpdateCodeSourceResponseBody(TeaModel):
    def __init__(
        self,
        code_source_id: str = None,
        request_id: str = None,
    ):
        # The ID of the code build.
        self.code_source_id = code_source_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCodeSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCodeSourceResponseBody = None,
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
            temp_model = UpdateCodeSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConfigRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        labels: List[UpdateConfigRequestLabels] = None,
    ):
        # The category of the configuration item. Valid values:
        # 
        # *   CommonResourceConfig
        # *   DLCAutoRecycle
        # *   DLCPriorityConfig
        # *   DSWPriorityConfig
        # *   QuotaMaximumDuration
        # *   CommonTagConfig
        self.category_name = category_name
        # The key of the configuration item. Valid values:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   priorityConfig: Priority configuration. This key can be used only when CategoryName is set to DLCPriorityConfig or DSWPriorityConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: Preset tags of the workspace. Created resources must include tags.
        self.config_key = config_key
        # The value of the configuration item.
        self.config_value = config_value
        # The tags of the configuration item.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdateConfigRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class UpdateConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConfigResponseBody = None,
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
            temp_model = UpdateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigsRequestConfigsLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConfigsRequestConfigs(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        config_key: str = None,
        config_value: str = None,
        labels: List[UpdateConfigsRequestConfigsLabels] = None,
    ):
        # The category of the configuration item. Supported categories:
        # 
        # *   CommonResourceConfig
        # *   DLCAutoRecycle
        # *   DLCPriorityConfig
        # *   DSWPriorityConfig
        # *   QuotaMaximumDuration
        # *   CommonTagConfig
        self.category_name = category_name
        # The key of the configuration item. Supported keys:
        # 
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   isAutoRecycle: Automatic recycle configuration. This key can be used only when CategoryName is set to DLCAutoRecycle.
        # *   tempStoragePath: Temporary storage path. This key can be used only when CategoryName is set to CommonResourceConfig.
        # *   quotaMaximumDuration: Maximum run time of DLC jobs for a quota. This key can be used only when CategoryName is set to QuotaMaximumDuration.
        # *   predefinedTags: The predefined tags of the workspace. All created resources must have tags.
        self.config_key = config_key
        # The value of the configuration item.
        # 
        # *   When ConfigKey is predefinedTags, the ConfigValue follows this format: [{"Type":"Tag","Key":"Key1","Value":"{"Products":"DLC,DSW,EAS","Values":"value1,value2,value3"}"}]. "Products" indicates the products that use the predefined tags.
        self.config_value = config_value
        # The tags of the configuration item.
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdateConfigsRequestConfigsLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class UpdateConfigsRequest(TeaModel):
    def __init__(
        self,
        configs: List[UpdateConfigsRequestConfigs] = None,
    ):
        # The list of workspace configurations to update or add.
        self.configs = configs

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = UpdateConfigsRequestConfigs()
                self.configs.append(temp_model.from_map(k))
        return self


class UpdateConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConfigsResponseBody = None,
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
            temp_model = UpdateConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionRequestModels(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        model: str = None,
        model_type: str = None,
        tool_call: bool = None,
    ):
        # The display name of the model.
        self.display_name = display_name
        # The model identifier.
        self.model = model
        # The model type. Valid values:
        # 
        # *   LLM
        # *   Embedding
        # *   ReRank
        self.model_type = model_type
        # Indicates whether tool calling is supported. Valid values:
        # 
        # *   true
        # *   false
        self.tool_call = tool_call

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.model is not None:
            result['Model'] = self.model
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')
        return self


class UpdateConnectionRequest(TeaModel):
    def __init__(
        self,
        configs: Dict[str, str] = None,
        description: str = None,
        models: List[UpdateConnectionRequestModels] = None,
        secrets: Dict[str, str] = None,
    ):
        # The connection configuration. The connection configuration is in the key-value format. The keys configured for different connection types are different. For more information, see the supplementary description of the request parameters in CreateConnection.
        self.configs = configs
        # The connection description.
        self.description = description
        # The models.
        self.models = models
        # The key-value configuration to be encrypted, such as the database logon password and the key for model connection.
        self.secrets = secrets

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.secrets is not None:
            result['Secrets'] = self.secrets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = UpdateConnectionRequestModels()
                self.models.append(temp_model.from_map(k))
        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')
        return self


class UpdateConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConnectionResponseBody = None,
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
            temp_model = UpdateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetRequestSharingConfig(TeaModel):
    def __init__(
        self,
        shared_to: List[DatasetShareRelationship] = None,
    ):
        self.shared_to = shared_to

    def validate(self):
        if self.shared_to:
            for k in self.shared_to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SharedTo'] = []
        if self.shared_to is not None:
            for k in self.shared_to:
                result['SharedTo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shared_to = []
        if m.get('SharedTo') is not None:
            for k in m.get('SharedTo'):
                temp_model = DatasetShareRelationship()
                self.shared_to.append(temp_model.from_map(k))
        return self


class UpdateDatasetRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        edition: str = None,
        mount_access_read_write_role_id_list: List[str] = None,
        name: str = None,
        options: str = None,
        sharing_config: UpdateDatasetRequestSharingConfig = None,
    ):
        # The description of the dataset.
        self.description = description
        self.edition = edition
        # The list of role names in the workspace that have read and write permissions on the mounted database. The names starting with PAI are basic role names, and the names starting with role- are custom role names. If the list contains asterisks (\\*), all roles have read and write permissions.
        # 
        # *   If you set the value to ["PAI.AlgoOperator", "role-hiuwpd01ncrokkgp21"], the account of the specified role is granted the read and write permissions.
        # *   If you set the value to ["\\*"], all accounts are granted the read and write permissions.
        # *   If you set the value to [], only the creator of the dataset has the read and write permissions.
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        # The dataset name. You can call [ListDatasets](https://help.aliyun.com/document_detail/457222.html) to obtain the dataset name.
        self.name = name
        # The extended field, which is a JSON string. When you use the dataset in Deep Learning Containers (DLC), you can set mountPath to specify the default mount path of the dataset.
        self.options = options
        self.sharing_config = sharing_config

    def validate(self):
        if self.sharing_config:
            self.sharing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.mount_access_read_write_role_id_list is not None:
            result['MountAccessReadWriteRoleIdList'] = self.mount_access_read_write_role_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.options is not None:
            result['Options'] = self.options
        if self.sharing_config is not None:
            result['SharingConfig'] = self.sharing_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('MountAccessReadWriteRoleIdList') is not None:
            self.mount_access_read_write_role_id_list = m.get('MountAccessReadWriteRoleIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('SharingConfig') is not None:
            temp_model = UpdateDatasetRequestSharingConfig()
            self.sharing_config = temp_model.from_map(m['SharingConfig'])
        return self


class UpdateDatasetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetResponseBody = None,
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
            temp_model = UpdateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetFileMetasRequest(TeaModel):
    def __init__(
        self,
        dataset_file_metas: List[DatasetFileMetaConentUpdate] = None,
        dataset_version: str = None,
        tag_job_id: str = None,
        workspace_id: str = None,
    ):
        # The metadata records to be updated for the dataset files.
        # 
        # This parameter is required.
        self.dataset_file_metas = dataset_file_metas
        # The dataset version.
        self.dataset_version = dataset_version
        # The ID of the tagging job that is associated with the metadata tag of the dataset file.
        self.tag_job_id = tag_job_id
        # The ID of the workspace to which the dataset belongs. To obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_file_metas:
            for k in self.dataset_file_metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatasetFileMetas'] = []
        if self.dataset_file_metas is not None:
            for k in self.dataset_file_metas:
                result['DatasetFileMetas'].append(k.to_map() if k else None)
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.tag_job_id is not None:
            result['TagJobId'] = self.tag_job_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_file_metas = []
        if m.get('DatasetFileMetas') is not None:
            for k in m.get('DatasetFileMetas'):
                temp_model = DatasetFileMetaConentUpdate()
                self.dataset_file_metas.append(temp_model.from_map(k))
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('TagJobId') is not None:
            self.tag_job_id = m.get('TagJobId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDatasetFileMetasResponseBody(TeaModel):
    def __init__(
        self,
        failed_details: List[DatasetFileMetaResponse] = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The metadata records that fail to be updated for the dataset files.
        self.failed_details = failed_details
        # The request ID.
        self.request_id = request_id
        # Indicates whether the metadata records of all dataset files were updated. Valid values: true and false. If the value is false, view the failure details specified by FailedDetails.
        self.status = status

    def validate(self):
        if self.failed_details:
            for k in self.failed_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedDetails'] = []
        if self.failed_details is not None:
            for k in self.failed_details:
                result['FailedDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_details = []
        if m.get('FailedDetails') is not None:
            for k in m.get('FailedDetails'):
                temp_model = DatasetFileMetaResponse()
                self.failed_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDatasetFileMetasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetFileMetasResponseBody = None,
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
            temp_model = UpdateDatasetFileMetasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetJobRequest(TeaModel):
    def __init__(
        self,
        dataset_version: str = None,
        description: str = None,
        workspace_id: str = None,
    ):
        # The dataset version name.
        self.dataset_version = dataset_version
        # The dataset job description.
        self.description = description
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version
        if self.description is not None:
            result['Description'] = self.description
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDatasetJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetJobResponseBody = None,
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
            temp_model = UpdateDatasetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetJobConfigRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        config_type: str = None,
        workspace_id: str = None,
    ):
        # The configuration content. Formats:
        # 
        # *   MultimodalIntelligentTag
        # 
        # { "apiKey":"sk-xxxxxxxxxxxxxxxxxxxxx" }
        # 
        # *   MultimodalSemanticIndex
        # 
        # { "defaultModelId": "xxx" "defaultModelVersion":"1.0.0" }
        self.config = config
        # The configuration type.
        # 
        # *   MultimodalIntelligentTag
        # *   MultimodalSemanticIndex
        self.config_type = config_type
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateDatasetJobConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetJobConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetJobConfigResponseBody = None,
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
            temp_model = UpdateDatasetJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetVersionRequest(TeaModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        description: str = None,
        options: str = None,
    ):
        self.data_count = data_count
        self.data_size = data_size
        self.description = description
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_count is not None:
            result['DataCount'] = self.data_count
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.description is not None:
            result['Description'] = self.description
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class UpdateDatasetVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDatasetVersionResponseBody = None,
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
            temp_model = UpdateDatasetVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDefaultWorkspaceRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
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


class UpdateDefaultWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDefaultWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDefaultWorkspaceResponseBody = None,
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
            temp_model = UpdateDefaultWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        name: str = None,
    ):
        # The accessibility of the experiment in the workspace. Valid values:
        # 
        # *   PRIVATE: The experiment is accessible only to you and the administrator of the workspace.
        # *   PUBLIC: The experiment is accessible to all users in the workspace.
        self.accessibility = accessibility
        # The experiment name. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be 1 to 63 characters in length.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentResponseBody = None,
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
            temp_model = UpdateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelRequest(TeaModel):
    def __init__(
        self,
        accessibility: str = None,
        domain: str = None,
        extra_info: Dict[str, Any] = None,
        model_description: str = None,
        model_doc: str = None,
        model_name: str = None,
        model_type: str = None,
        order_number: int = None,
        origin: str = None,
        parameter_size: int = None,
        task: str = None,
    ):
        # The visibility of the model in the workspace. Valid values:
        # 
        # *   PRIVATE: The model is visible only to you and the administrator of the workspace.
        # *   PUBLIC: The model is visible to all users in the workspace.
        self.accessibility = accessibility
        # The domain. This parameter describes the domain in which the model is applied. Valid values: nlp (natural language processing) and cv (computer vision).
        self.domain = domain
        # Other information about the model.
        self.extra_info = extra_info
        # The model description.
        self.model_description = model_description
        # The documentation of the model.
        self.model_doc = model_doc
        # The model name, which must be 1 to 127 characters in length.
        self.model_name = model_name
        # The model type. Valid values: Checkpoint and LoRA.
        self.model_type = model_type
        # The sequence number of the model. This parameter can be used for custom sorting.
        self.order_number = order_number
        # The source of the model. This parameter describes the community or organization to which the source model belongs. Valid values: ModelScope and HuggingFace.
        self.origin = origin
        self.parameter_size = parameter_size
        # The task. This parameter specifies the specific issue that the model resolves. Example: text-classification.
        self.task = task

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.model_description is not None:
            result['ModelDescription'] = self.model_description
        if self.model_doc is not None:
            result['ModelDoc'] = self.model_doc
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.order_number is not None:
            result['OrderNumber'] = self.order_number
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.parameter_size is not None:
            result['ParameterSize'] = self.parameter_size
        if self.task is not None:
            result['Task'] = self.task
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('ModelDescription') is not None:
            self.model_description = m.get('ModelDescription')
        if m.get('ModelDoc') is not None:
            self.model_doc = m.get('ModelDoc')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('OrderNumber') is not None:
            self.order_number = m.get('OrderNumber')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('ParameterSize') is not None:
            self.parameter_size = m.get('ParameterSize')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        return self


class UpdateModelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModelResponseBody = None,
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
            temp_model = UpdateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelVersionRequest(TeaModel):
    def __init__(
        self,
        approval_status: str = None,
        compression_spec: Dict[str, Any] = None,
        distillation_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        extra_info: Dict[str, Any] = None,
        inference_spec: Dict[str, Any] = None,
        metrics: Dict[str, Any] = None,
        options: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        version_description: str = None,
    ):
        # The approval status. Valid values:
        # 
        # *   Pending
        # *   Approved
        # *   Rejected
        self.approval_status = approval_status
        # The compression configuration.
        self.compression_spec = compression_spec
        self.distillation_spec = distillation_spec
        # The evaluation configuration.
        self.evaluation_spec = evaluation_spec
        # The additional information.
        self.extra_info = extra_info
        # Describes how to apply to downstream inference services. For example, describes the processor and container of Elastic Algorithm Service (EAS). Example: `{ "processor": "tensorflow_gpu_1.12" }`.
        self.inference_spec = inference_spec
        # The model metrics. The length after serialization is limited to 8,192.
        self.metrics = metrics
        # The extended field, which is of the JsonString type.
        self.options = options
        # The source ID.
        # 
        # *   If the source type is Custom, this field is not limited.
        # *   If the source type is PAIFlow or TrainingService, the format is:
        # 
        # <!---->
        # 
        #     region=<region_id>,workspaceId=<workspace_id>,kind=<kind>,id=<id>
        # 
        # Take note of the following parameters:
        # 
        # *   region is the region ID.
        # *   workspaceId is the ID of the workspace.
        # *   kind is the type. Valid values: PipelineRun (PAIFlow) and ServiceJob (training service).
        # *   id is a unique identifier.
        self.source_id = source_id
        # The type of the model source. Valid values:
        # 
        # *   Custom (default)
        # *   PAIFlow
        # *   TrainingService
        self.source_type = source_type
        # The training configurations used for fine-tuning and incremental training.
        self.training_spec = training_spec
        # The model version description.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status
        if self.compression_spec is not None:
            result['CompressionSpec'] = self.compression_spec
        if self.distillation_spec is not None:
            result['DistillationSpec'] = self.distillation_spec
        if self.evaluation_spec is not None:
            result['EvaluationSpec'] = self.evaluation_spec
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.inference_spec is not None:
            result['InferenceSpec'] = self.inference_spec
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.options is not None:
            result['Options'] = self.options
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.training_spec is not None:
            result['TrainingSpec'] = self.training_spec
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')
        if m.get('CompressionSpec') is not None:
            self.compression_spec = m.get('CompressionSpec')
        if m.get('DistillationSpec') is not None:
            self.distillation_spec = m.get('DistillationSpec')
        if m.get('EvaluationSpec') is not None:
            self.evaluation_spec = m.get('EvaluationSpec')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TrainingSpec') is not None:
            self.training_spec = m.get('TrainingSpec')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        return self


class UpdateModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModelVersionResponseBody = None,
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
            temp_model = UpdateModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRunRequest(TeaModel):
    def __init__(
        self,
        labels: List[Label] = None,
        name: str = None,
        params: List[RunParam] = None,
    ):
        # The labels.
        self.labels = labels
        # The run name. The name must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be 1 to 63 characters in length.
        self.name = name
        # The parameters.
        self.params = params

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = RunParam()
                self.params.append(temp_model.from_map(k))
        return self


class UpdateRunResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRunResponseBody = None,
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
            temp_model = UpdateRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
    ):
        # The workspace description.
        self.description = description
        # The display name of the workspace.
        # 
        # *   The name must be 3 to 23 characters in length, and can contain letters, underscores (_), and digits.
        # *   The name must start with a letter.
        # *   The name must be unique in the current region.
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        return self


class UpdateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkspaceResponseBody = None,
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
            temp_model = UpdateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceResourceRequestLabels(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateWorkspaceResourceRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        is_default: bool = None,
        labels: List[UpdateWorkspaceResourceRequestLabels] = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        spec: Dict[str, Any] = None,
    ):
        # The group name.
        self.group_name = group_name
        # Specifies whether the resource is the default resource. This parameter can only be set to true and cannot be set to false.
        self.is_default = is_default
        # The resource tags. If you specify multiple tags, only resources that meet all the specified tag-based filter conditions are returned.
        self.labels = labels
        # **This field is no longer used and will be removed. Use the ResourceType field.
        self.product_type = product_type
        # The resource IDs.
        # 
        # You cannot leave both GroupName and ResourceIds empty. If you specify both the parameters, the value of GroupName of each resource ID in the dataset must be the same.
        self.resource_ids = resource_ids
        # The resource type. Valid values:
        # 
        # *   MaxCompute
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        self.resource_type = resource_type
        # The specification of the resource.
        self.spec = spec

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdateWorkspaceResourceRequestLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class UpdateWorkspaceResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_ids: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The updated resource IDs.
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        return self


class UpdateWorkspaceResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkspaceResourceResponseBody = None,
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
            temp_model = UpdateWorkspaceResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


