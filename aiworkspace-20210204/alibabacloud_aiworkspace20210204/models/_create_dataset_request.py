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
        # The visibility of the workspace. Valid values:
        # - PRIVATE (default): visible only to yourself and administrators within the workspace.
        # - PUBLIC: visible to all users in the workspace.
        # - ROLE_PUBLIC: visible to specified workspace roles. For the role list, refer to AccessibleRoleIdList. Under this condition, the dataset owner and administrators always have visibility.
        self.accessibility = accessibility
        # Takes effect when Accessibility is set to ROLE_PUBLIC. The list of workspace role names that can view the dataset. IDs starting with PAI are basic role IDs, and IDs starting with role- are custom role IDs.
        self.accessible_role_id_list = accessible_role_id_list
        # The number of files in the dataset.
        self.data_count = data_count
        # The size of space occupied by the dataset files. Unit: bytes.
        self.data_size = data_size
        # The data source type. Valid values:
        # - OSS: Alibaba Cloud Object Storage Service (OSS).
        # - NAS: Alibaba Cloud Apsara File Storage NAS General Purpose.
        # - EXTREMENAS: Alibaba Cloud Apsara File Storage NAS Extreme.
        # - CPFS: Alibaba Cloud Cloud Parallel File Storage (CPFS) General Purpose.
        # - BMCPFS: Alibaba Cloud Cloud Parallel File Storage (CPFS) AI Edition. 
        # - MAXCOMPUTE: Alibaba Cloud MaxCompute.
        # - URL: public HTTP/HTTPS URL.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The data type of the dataset. Default value: COMMON. Valid values:
        # - COMMON: common.
        # - PIC: image.
        # - TEXT: text.
        # - VIDEO: video.
        # - AUDIO: audio.
        self.data_type = data_type
        # DatasetTaskRamRole
        self.dataset_task_ram_role = dataset_task_ram_role
        # The custom description of the dataset to distinguish it from other datasets.
        self.description = description
        # The dataset type. Default value: BASIC. Valid values:
        # 
        # - BASIC: basic. Does not support dataset file metadata management.
        # - ADVANCED: advanced. Only supported for OSS type. Each version supports up to 1 million file metadata entries.
        # - LOGICAL: logical. Only supported for OSS type. Each version supports up to 3 million file metadata entries.
        self.edition = edition
        # The storage import configuration of the dataset. OSS, NAS, and CPFS are supported.
        # 
        # <details>
        # <summary>OSS</summary>
        # {<BR>
        # "region": "${region}",//Region ID<BR>
        # "bucket": "${bucket}",//Bucket name<BR>
        # "path": "${path}" //File path<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>NAS</summary>
        # {<BR>
        # "region": "${region}",//Region ID<BR>
        # "fileSystemId": "${file_system_id}", //File system ID<BR>
        # "path": "${path}", //File system path<BR>
        # "mountTarget": "${mount_target}" //File system mount target<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>CPFS</summary>
        # {<BR>
        # "region": "${region}",//Region ID<BR>
        # "fileSystemId": "${file_system_id}", //File system ID<BR>
        # "protocolServiceId":"${protocol_service_id}", //File system protocol service<BR>
        # "exportId": "${export_id}", //File system export directory<BR>
        # "path": "${path}", //File system path<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>AI Edition CPFS</summary>
        # {<BR>
        # "region": "${region}",//Region ID<BR>
        # "fileSystemId": "${file_system_id}", //File system ID<BR>
        # "path": "${path}", //File system path<BR>
        # "mountTarget": "${mount_target}" //File system mount target, specific to AI Edition<BR>
        # "isVpcMount": boolean, //Whether it is a VPC mount target, specific to AI Edition<BR>
        # }<BR>
        # </details>
        self.import_info = import_info
        # The list of labels.
        self.labels = labels
        # The list of workspace role names that have read and write permissions when the dataset is mounted. IDs starting with PAI are basic role IDs, and IDs starting with role- are custom role IDs. If the list contains "*", all roles have read and write permissions.
        # - Specified roles: ["PAI.AlgoOperator", "role-hiuwpd01ncrokkgp21"]
        # - All accounts: ["*"]
        # - Dataset creator only: []
        self.mount_access_read_write_role_id_list = mount_access_read_write_role_id_list
        # The name of the dataset. Naming rules:
        # - Must start with a lowercase letter, uppercase letter, digit, or Chinese character.
        # - Can contain underscores (_) or hyphens (-).
        # - Must be 1 to 127 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The extended field in JsonString format.
        # When DLC uses the dataset, you can specify the default mount path of the dataset by configuring the mountPath field.
        self.options = options
        # The property of the dataset. Valid values:
        # - FILE: file.
        # - DIRECTORY: folder.
        # 
        # This parameter is required.
        self.property = property
        # The dataset provider. Cannot be set to pai.
        self.provider = provider
        # The data source provider type of the dataset. Valid values:
        # - Ecs (default)
        # - Lingjun
        self.provider_type = provider_type
        # The source dataset ID of the annotation dataset.
        self.source_dataset_id = source_dataset_id
        # The source dataset version of the annotation dataset.
        self.source_dataset_version = source_dataset_version
        # The data source ID.
        # - If SourceType is USER, SourceId can be customized.
        # - If SourceType is ITAG, which indicates a dataset generated from iTAG annotation results, SourceId is the iTAG task ID.
        # - If SourceType is PAI_PUBLIC_DATASET, which indicates a dataset created from a PAI public dataset, SourceId is empty by default.
        self.source_id = source_id
        # The data source type. Default value: USER.
        self.source_type = source_type
        # Examples of Uri configurations:
        # - If the data source type is OSS: `oss://bucket.endpoint/object`
        # - If the data source type is NAS:
        # General Purpose NAS format: `nas://<nasfisid>.region/subpath/to/dir/`;
        # CPFS 1.0: `nas://<cpfs-fsid>.region/subpath/to/dir/`;
        # CPFS 2.0: `nas://<cpfs-fsid>.region/<protocolserviceid>/`.
        # CPFS 1.0 and CPFS 2.0 are distinguished by the fsid format: CPFS 1.0 format is cpfs-<8 ASCII characters>; CPFS 2.0 format is cpfs-<16 ASCII characters>.
        # 
        # This parameter is required.
        self.uri = uri
        # The Alibaba Cloud account ID of the dataset owner. Workspace owners and administrators have permissions to create datasets for specified workspace members.
        self.user_id = user_id
        # UserMetricsEndpoints
        self.user_metrics_endpoints = user_metrics_endpoints
        # The description of the initial version of the dataset.
        self.version_description = version_description
        # The list of labels for the initial version.
        self.version_labels = version_labels
        # The ID of the workspace where the dataset resides. For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # If this parameter is not specified, the default workspace is used. If the default workspace does not exist, an error is returned.
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

