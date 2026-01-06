# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetDatasetResponseBody(DaraModel):
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
        labels: List[main_models.Label] = None,
        latest_version: main_models.DatasetVersion = None,
        mount_access: str = None,
        mount_access_read_write_role_id_list: List[str] = None,
        name: str = None,
        options: str = None,
        owner_id: str = None,
        property: str = None,
        provider: str = None,
        provider_type: str = None,
        request_id: str = None,
        shared_from: main_models.DatasetShareRelationship = None,
        sharing_config: main_models.GetDatasetResponseBodySharingConfig = None,
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
        # **OSS**
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "bucket": "${bucket}",// The bucket name\\
        # "path": "${path}" // The file path\\
        # }\\
        # 
        # 
        # **NAS**
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "path": "${path}", // The file system path\\
        # "mountTarget": "${mount_target}" // The mount point of the file system\\
        # }\\
        # 
        # 
        # **CPFS**
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
        # **CPFS for Lingjun**
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
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.latest_version:
            self.latest_version.validate()
        if self.shared_from:
            self.shared_from.validate()
        if self.sharing_config:
            self.sharing_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestVersion') is not None:
            temp_model = main_models.DatasetVersion()
            self.latest_version = temp_model.from_map(m.get('LatestVersion'))

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
            temp_model = main_models.DatasetShareRelationship()
            self.shared_from = temp_model.from_map(m.get('SharedFrom'))

        if m.get('SharingConfig') is not None:
            temp_model = main_models.GetDatasetResponseBodySharingConfig()
            self.sharing_config = temp_model.from_map(m.get('SharingConfig'))

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

class GetDatasetResponseBodySharingConfig(DaraModel):
    def __init__(
        self,
        shared_to: List[main_models.DatasetShareRelationship] = None,
    ):
        self.shared_to = shared_to

    def validate(self):
        if self.shared_to:
            for v1 in self.shared_to:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SharedTo'] = []
        if self.shared_to is not None:
            for k1 in self.shared_to:
                result['SharedTo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shared_to = []
        if m.get('SharedTo') is not None:
            for k1 in m.get('SharedTo'):
                temp_model = main_models.DatasetShareRelationship()
                self.shared_to.append(temp_model.from_map(k1))

        return self

