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
        # **OSS**
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "bucket": "${bucket}",//The bucket name.\\
        # "path": "${path}" // The file path.\\
        # }\\
        # 
        # 
        # **NAS**
        # 
        # {\\
        # "region": "${region}",// The region ID.\\
        # "fileSystemId": "${file_system_id}", // The file system ID.\\
        # "path": "${path}", // The file system path.\\
        # "mountTarget": "${mount_target}" // The mount point of the file system.\\
        # }\\
        # 
        # 
        # **CPFS**
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
        # **CPFS for Lingjun**
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

