# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        accessible_role_id_list: List[str] = None,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        data_type: str = None,
        dataset_task_ram_role: str = None,
        description: str = None,
        dry_run: bool = None,
        edition: str = None,
        import_info: str = None,
        labels: List[main_models.Label] = None,
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
        user_metrics_endpoints: List[main_models.UserMetricsEndpoint] = None,
        version_description: str = None,
        version_labels: List[main_models.Label] = None,
        workspace_id: str = None,
    ):
        # The workspace visibility. Valid values:
        # - PRIVATE: Visible only to the creator and administrators in the workspace. This is the default value.
        # - PUBLIC: Visible to all users in the workspace.
        # - ROLE_PUBLIC: Visible to specified workspace roles. For the role list, refer to AccessibleRoleIdList. The dataset owner and administrators always have visibility regardless of the specified roles.
        self.accessibility = accessibility
        # Takes effect only when Accessibility is set to ROLE_PUBLIC. The list of workspace role names that have visibility to the dataset. Role IDs starting with PAI are basic role IDs, and those starting with role- are custom role IDs.
        self.accessible_role_id_list = accessible_role_id_list
        # The number of files in the dataset.
        self.data_count = data_count
        # The storage space occupied by the dataset files. Unit: bytes.
        self.data_size = data_size
        # The data source type. Valid values:
        # - OSS: Alibaba Cloud Object Storage Service (OSS).
        # - NAS: Alibaba Cloud File Storage NAS (General-purpose).
        # - EXTREMENAS: Alibaba Cloud File Storage NAS (Extreme).
        # - CPFS: Alibaba Cloud Cloud Paralleled File System (CPFS) (General-purpose).
        # - BMCPFS: Alibaba Cloud Cloud Paralleled File System (CPFS) (AI-optimized). 
        # - MAXCOMPUTE: Alibaba Cloud MaxCompute.
        # - URL: A public HTTP or HTTPS URL.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The data type of the dataset. Default value: COMMON. Valid values:
        # - COMMON: Common data.
        # - PIC: Image data.
        # - TEXT: Text data.
        # - VIDEO: Video data.
        # - AUDIO: Audio data.
        self.data_type = data_type
        # DatasetTaskRamRole
        self.dataset_task_ram_role = dataset_task_ram_role
        # The custom description of the dataset, which is used to distinguish it from other datasets.
        self.description = description
        # Specifies whether to perform only a dry run without actually creating the dataset.
        self.dry_run = dry_run
        # The dataset edition. Default value: BASIC. Valid values:
        # - BASIC: Basic edition. Does not support file metadata management for the dataset.
        # - ADVANCED: Advanced edition. Only OSS datasets are supported. Each version supports metadata management for up to 1 million files.
        # - LOGICAL: Logical edition. Only OSS datasets are supported. Each version supports metadata management for up to 3 million files.
        self.edition = edition
        # The storage import configuration of the dataset. OSS, NAS, and CPFS are supported.
        # 
        # <details>
        # <summary>OSS</summary>
        # {<BR>
        # "region": "${region}",// The region ID.<BR>
        # "bucket": "${bucket}",// The bucket name.<BR>
        # "path": "${path}" // The file path.<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>NAS</summary>
        # {<BR>
        # "region": "${region}",// The region ID.<BR>
        # "fileSystemId": "${file_system_id}", // The file system ID.<BR>
        # "path": "${path}", // The file system path.<BR>
        # "mountTarget": "${mount_target}" // The mount target of the file system.<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>CPFS</summary>
        # {<BR>
        # "region": "${region}",// The region ID.<BR>
        # "fileSystemId": "${file_system_id}", // The file system ID.<BR>
        # "protocolServiceId":"${protocol_service_id}", // The protocol service of the file system.<BR>
        # "exportId": "${export_id}", // The export directory of the file system.<BR>
        # "path": "${path}", // The file system path.<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>AI-optimized CPFS</summary>
        # {<BR>
        # "region": "${region}",// The region ID.<BR>
        # "fileSystemId": "${file_system_id}", // The file system ID.<BR>
        # "path": "${path}", // The file system path.<BR>
        # "mountTarget": "${mount_target}", // The mount target of the file system. Specific to the AI-optimized edition.<BR>
        # "isVpcMount": boolean, // Specifies whether the mount target is a VPC mount target. Specific to the AI-optimized edition.<BR>
        # }<BR>
        # </details>
        self.import_info = import_info
        # The list of labels.
        self.labels = labels
        # The list of workspace role names that have read and write permissions when the dataset is mounted. Role IDs starting with PAI are basic role IDs, and those starting with role- are custom role IDs. If the list contains an asterisk (*), all roles have read and write permissions.
        # - Specified roles: ["PAI.AlgoOperator", "role-hiuwpd01ncrokkgp21"]
        # - All roles: ["*"]
        # - Dataset creator only: []
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        # The name of the dataset. The naming rules are as follows:
        # - The name must start with a lowercase letter, an uppercase letter, a digit, or a Chinese character.
        # - The name can contain underscores (_) and hyphens (-).
        # - The name must be 1 to 127 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The extended fields in JSON string format. When DLC uses the dataset, you can configure the mountPath field to specify the default mount path of the dataset.
        self.options = options
        # The property of the dataset. Valid values:
        # - FILE: File.
        # - DIRECTORY: Directory.
        # 
        # This parameter is required.
        self.property = property
        # The provider of the dataset. You cannot set this parameter to pai.
        self.provider = provider
        # The data source type of the dataset. Valid values:
        # - Ecs: Elastic Compute Service (ECS). This is the default value.
        # - Lingjun: Lingjun.
        self.provider_type = provider_type
        # The ID of the source dataset from which the labeled dataset is generated.
        self.source_dataset_id = source_dataset_id
        # The version of the source dataset from which the labeled dataset is generated.
        self.source_dataset_version = source_dataset_version
        # The ID of the data source.
        # - When SourceType is set to USER, SourceId can be customized.
        # - When SourceType is set to ITAG, which indicates that the dataset is generated from the labeling results of the iTAG module, SourceId is the iTAG task ID.
        # - When SourceType is set to PAI_PUBLIC_DATASET, which indicates that the dataset is created from a PAI public dataset, SourceId is empty by default.
        self.source_id = source_id
        # The data source type. Default value: USER.
        self.source_type = source_type
        # The URI configuration examples are as follows:
        # - If the data source type is OSS: `oss://bucket.endpoint/object`
        # - If the data source type is NAS:
        # For general-purpose NAS, the format is `nas://<nasfisid>.region/subpath/to/dir/`.
        # For CPFS 1.0, the format is `nas://<cpfs-fsid>.region/subpath/to/dir/`.
        # For CPFS 2.0, the format is `nas://<cpfs-fsid>.region/<protocolserviceid>/`.
        # CPFS 1.0 and CPFS 2.0 are distinguished by the format of the fsid: the format for CPFS 1.0 is cpfs-<8 ASCII characters>, and the format for CPFS 2.0 is cpfs-<16 ASCII characters>.
        # 
        # This parameter is required.
        self.uri = uri
        # The Alibaba Cloud account ID of the dataset owner. The workspace owner and administrators have the permissions to create datasets for specified workspace members.
        self.user_id = user_id
        # UserMetricsEndpoints
        self.user_metrics_endpoints = user_metrics_endpoints
        # The description of the initial version of the dataset.
        self.version_description = version_description
        # The list of labels for the initial version.
        self.version_labels = version_labels
        # The ID of the workspace to which the dataset belongs. For more information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # If you do not configure this parameter, the default workspace is used. If the default workspace does not exist, an error is reported.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.user_metrics_endpoints:
            for v1 in self.user_metrics_endpoints:
                 if v1:
                    v1.validate()
        if self.version_labels:
            for v1 in self.version_labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.accessible_role_id_list is not None:
            result['AccessibleRoleIdList'] = self.accessible_role_id_list

        if self.data_count is not None:
            result['DataCount'] = self.data_count

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.dataset_task_ram_role is not None:
            result['DatasetTaskRamRole'] = self.dataset_task_ram_role

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.import_info is not None:
            result['ImportInfo'] = self.import_info

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

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

        result['UserMetricsEndpoints'] = []
        if self.user_metrics_endpoints is not None:
            for k1 in self.user_metrics_endpoints:
                result['UserMetricsEndpoints'].append(k1.to_map() if k1 else None)

        if self.version_description is not None:
            result['VersionDescription'] = self.version_description

        result['VersionLabels'] = []
        if self.version_labels is not None:
            for k1 in self.version_labels:
                result['VersionLabels'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AccessibleRoleIdList') is not None:
            self.accessible_role_id_list = m.get('AccessibleRoleIdList')

        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DatasetTaskRamRole') is not None:
            self.dataset_task_ram_role = m.get('DatasetTaskRamRole')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

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

        self.user_metrics_endpoints = []
        if m.get('UserMetricsEndpoints') is not None:
            for k1 in m.get('UserMetricsEndpoints'):
                temp_model = main_models.UserMetricsEndpoint()
                self.user_metrics_endpoints.append(temp_model.from_map(k1))

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        self.version_labels = []
        if m.get('VersionLabels') is not None:
            for k1 in m.get('VersionLabels'):
                temp_model = main_models.Label()
                self.version_labels.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

