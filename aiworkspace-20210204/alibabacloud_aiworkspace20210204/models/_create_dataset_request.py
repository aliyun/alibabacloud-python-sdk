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
        description: str = None,
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
        version_description: str = None,
        version_labels: List[main_models.Label] = None,
        workspace_id: str = None,
    ):
        # The visibility of the dataset in the workspace. Valid values:
        # 
        # - PRIVATE (default): The dataset is visible only to its owner and administrators in the workspace.
        # 
        # - PUBLIC: The dataset is visible to all users in the workspace.
        # 
        # - ROLE_PUBLIC: The dataset is visible to users with specific workspace roles. The list of roles is specified in the `AccessibleRoleIdList` parameter. The dataset owner and administrators always retain visibility.
        self.accessibility = accessibility
        # This parameter takes effect only when `Accessibility` is set to `ROLE_PUBLIC`. This parameter specifies a list of workspace role IDs that can view this dataset. Role IDs that start with `PAI.` are built-in roles, and role IDs that start with `role-` are custom roles.
        self.accessible_role_id_list = accessible_role_id_list
        # The number of files in the dataset.
        self.data_count = data_count
        # The size of the dataset files, in bytes.
        self.data_size = data_size
        # The type of the data source. Valid values:
        # 
        # - OSS: Object Storage Service (OSS).
        # 
        # - NAS: general-purpose Apsara File Storage NAS.
        # 
        # - EXTREMENAS: Extreme NAS.
        # 
        # - CPFS: general-purpose Cloud Parallel File Storage (CPFS).
        # 
        # - BMCPFS: AI Computing Edition of CPFS.
        # 
        # - MAXCOMPUTE: MaxCompute.
        # 
        # - URL: a public HTTP or HTTPS URL.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The data type of the dataset. The default value is `COMMON`. Valid values:
        # 
        # - COMMON: common
        # 
        # - PIC: image
        # 
        # - TEXT: text
        # 
        # - VIDEO: video
        # 
        # - AUDIO: audio
        self.data_type = data_type
        # A custom description to distinguish the dataset from other datasets.
        self.description = description
        # The edition of the dataset. The default value is BASIC. Valid values:
        # 
        # - BASIC: Basic. Does not support dataset file metadata management.
        # 
        # - ADVANCED: Advanced. Supported only for OSS datasets. Each version supports metadata management for up to 1 million files.
        # 
        # - LOGICAL: Logical. Supported only for OSS datasets. Each version supports metadata management for up to 3 million files.
        self.edition = edition
        # The storage import configuration of the dataset. `OSS`, `NAS`, and `CPFS` are supported.
        # 
        # <details>
        # 
        # <summary>
        # 
        # OSS
        # 
        # </summary>
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "bucket": "${bucket}",// The bucket name.\\
        # "path": "${path}" // The file path.\\
        # }
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # NAS
        # 
        # </summary>
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "fileSystemId": "${file_system_id}", // The file system ID.\\
        # "path": "${path}", // The file system path.\\
        # "mountTarget": "${mount_target}" // The mount target of the file system.\\
        # }
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # CPFS
        # 
        # </summary>
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "fileSystemId": "${file_system_id}", // The file system ID.\\
        # "protocolServiceId":"${protocol_service_id}", // The protocol service of the file system.\\
        # "exportId": "${export_id}", // The exported directory of the file system.\\
        # "path": "${path}", // The file system path.\\
        # }
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # CPFS (AI Computing Edition)
        # 
        # </summary>
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "fileSystemId": "${file_system_id}", // The file system ID.\\
        # "path": "${path}", // The file system path.\\
        # "mountTarget": "${mount_target}", // The mount target of the file system. This parameter is specific to the AI Computing Edition.\\
        # "isVpcMount": boolean, // Specifies whether the mount target is in a VPC. This parameter is specific to the AI Computing Edition.\\
        # }
        # 
        # </details>
        self.import_info = import_info
        # A list of labels.
        self.labels = labels
        # A list of workspace role IDs that are granted read and write permissions when the dataset is mounted. Role IDs that start with `PAI.` are built-in roles, and role IDs that start with `role-` are custom roles. If the list contains an asterisk (\\*), all roles are granted read and write permissions.
        # 
        # - Accounts with specified roles: `["PAI.AlgoOperator", "role-hiuwpd01ncrokkgp21"]`
        # 
        # - All accounts: `["*"]`
        # 
        # - Dataset creator only: `[]`
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        # The name of the dataset. The name must meet the following requirements:
        # 
        # - Starts with a lowercase letter, an uppercase letter, a number, or a Chinese character.
        # 
        # - Can contain underscores (_) and hyphens (-).
        # 
        # - Must be 1 to 127 characters long.
        # 
        # This parameter is required.
        self.name = name
        # The extended fields, which are a JSON string.
        # When a Data Lake Compute (DLC) job uses the dataset, you can configure the `mountPath` field to specify the default mount path of the dataset.
        self.options = options
        # The property of the dataset. Valid values:
        # 
        # - FILE: A file.
        # 
        # - DIRECTORY: A directory.
        # 
        # This parameter is required.
        self.property = property
        # The provider of the dataset. You cannot set this parameter to `pai`.
        self.provider = provider
        # The type of the data source provider. Valid values:
        # 
        # - Ecs (default)
        # 
        # - Lingjun
        self.provider_type = provider_type
        # The ID of the source dataset for a labeled dataset.
        self.source_dataset_id = source_dataset_id
        # The version of the source dataset for a labeled dataset.
        self.source_dataset_version = source_dataset_version
        # The ID of the data source.
        # 
        # - If `SourceType` is `USER`, you can specify a custom value for `SourceId`.
        # 
        # - If `SourceType` is `ITAG`, this parameter specifies the iTAG task ID from which the dataset was generated.
        # 
        # - If `SourceType` is `PAI_PUBLIC_DATASET`, the dataset is from a public PAI dataset, and this parameter is empty by default.
        self.source_id = source_id
        # The source of the data. The default value is USER.
        self.source_type = source_type
        # The URI of the data. The URI format varies based on the `DataSourceType` value.
        # 
        # - For an `OSS` data source: `oss://bucket.endpoint/object`
        # 
        # - For a `NAS` data source:
        #   For general-purpose `NAS`: `nas://<nasfisid>.region/subpath/to/dir/`.
        #   For `CPFS` 1.0: `nas://<cpfs-fsid>.region/subpath/to/dir/`.
        #   For `CPFS` 2.0: `nas://<cpfs-fsid>.region/<protocolserviceid>/`.
        #   `CPFS` 1.0 and `CPFS` 2.0 are distinguished by the format of the file system ID (fsid). The fsid for `CPFS` 1.0 is in the `cpfs-<8-character ASCII string>` format. The fsid for `CPFS` 2.0 is in the `cpfs-<16-character ASCII string>` format.
        # 
        # This parameter is required.
        self.uri = uri
        # The Alibaba Cloud account ID of the dataset owner. Workspace owners and administrators can create datasets for specified members of a workspace.
        self.user_id = user_id
        # The description of the initial version of the dataset.
        self.version_description = version_description
        # A list of labels for the initial version.
        self.version_labels = version_labels
        # The ID of the workspace to which the dataset belongs. For more information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # If this parameter is not specified, the default workspace is used. If the default workspace does not exist, an error is returned.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
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

        if self.description is not None:
            result['Description'] = self.description

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

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

