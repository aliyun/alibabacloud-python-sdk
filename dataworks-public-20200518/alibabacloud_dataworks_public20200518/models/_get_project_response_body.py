# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetProjectResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the workspace.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetProjectResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetProjectResponseBodyData(DaraModel):
    def __init__(
        self,
        appkey: str = None,
        base_project: bool = None,
        default_di_resource_group_identifier: str = None,
        destination: int = None,
        dev_storage_quota: str = None,
        development_type: int = None,
        disable_development: bool = None,
        env_types: List[str] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_allow_download: int = None,
        is_default: int = None,
        max_flow_node: int = None,
        prod_storage_quota: str = None,
        project_description: str = None,
        project_id: int = None,
        project_identifier: str = None,
        project_mode: int = None,
        project_name: str = None,
        project_owner_base_id: str = None,
        protected_mode: int = None,
        resident_area: str = None,
        resource_manager_resource_group_id: str = None,
        scheduler_max_retry_times: int = None,
        scheduler_retry_interval: int = None,
        status: int = None,
        table_privacy_mode: int = None,
        tags: List[main_models.GetProjectResponseBodyDataTags] = None,
        tenant_id: int = None,
        use_proxy_odps_account: bool = None,
    ):
        # This parameter is deprecated.
        self.appkey = appkey
        # This parameter is deprecated.
        self.base_project = base_project
        # The identifier of the default resource group that is automatically assigned when you purchase a MaxCompute exclusive resource group.
        self.default_di_resource_group_identifier = default_di_resource_group_identifier
        # This parameter is deprecated.
        self.destination = destination
        # This parameter is deprecated.
        self.dev_storage_quota = dev_storage_quota
        # This parameter is deprecated.
        self.development_type = development_type
        # Indicates whether the development role is disabled. Valid values:
        #  - **false** (default): The development role is enabled.
        #  - **true**: The development role is disabled.
        self.disable_development = disable_development
        # The environment context of the workspace.
        self.env_types = env_types
        # The time when the workspace was created. Example: `Dec 3, 2019 9:12:20 PM`.
        self.gmt_create = gmt_create
        # The time when the workspace was last modified. Example: `Dec 3, 2019 9:12:20 PM`.
        self.gmt_modified = gmt_modified
        # Indicates whether downloading query results from the IDE is allowed. Valid values:
        # - **1**: Downloading is allowed.
        # - **0**: Downloading is not allowed.
        self.is_allow_download = is_allow_download
        # Indicates whether the workspace is the default workspace. Valid values:
        # - **1**: Yes.
        # - **0**: No.
        self.is_default = is_default
        # This parameter is deprecated.
        self.max_flow_node = max_flow_node
        # This parameter is deprecated.
        self.prod_storage_quota = prod_storage_quota
        # The description of the workspace.
        self.project_description = project_description
        # The workspace ID.
        self.project_id = project_id
        # The name of the workspace.
        self.project_identifier = project_identifier
        # The mode of the workspace. Valid values:
        # - **2**: basic mode.
        # - **3**: standard mode.
        self.project_mode = project_mode
        # The display name of the workspace.
        self.project_name = project_name
        # The Alibaba Cloud ID of the workspace owner.
        self.project_owner_base_id = project_owner_base_id
        # Indicates whether protected mode is enabled for the workspace. Valid values:
        # - **1**: Protected mode is enabled.
        # - **0**: Protected mode is not enabled.
        self.protected_mode = protected_mode
        # The type of the workspace. Valid values:
        # - **private**: private zone.
        # - **swap**: swap zone.
        self.resident_area = resident_area
        # The resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The default maximum number of automatic reruns upon an error.
        self.scheduler_max_retry_times = scheduler_max_retry_times
        # The default interval between automatic reruns upon an error. Unit: ms. The maximum value is 30 minutes. Note the unit conversion.
        self.scheduler_retry_interval = scheduler_retry_interval
        # The status of the workspace. Valid values:
        # - **0**: AVAILABLE. The workspace is running normally.
        # - **1**: DELETED. The workspace has been deleted.
        # - **2**: INITIALIZING. The workspace is being initialized.
        # - **3**: INIT_FAILED. The workspace failed to be initialized.
        # - **4**: FORBIDDEN. The workspace is manually disabled.
        # - **5**: DELETING. The workspace is being deleted.
        # - **6**: DEL_FAILED. The workspace failed to be deleted.
        # - **7**: FROZEN. The workspace is frozen due to overdue payment.
        # - **8**: UPDATING. The workspace is being updated (a compute engine is being added and initialized).
        # - **9**: UPDATE_FAILED. The workspace failed to be updated (a compute engine failed to be added and initialized).
        self.status = status
        # The visibility of MaxCompute tables. Valid values:
        # - **0**: MaxCompute tables are not visible to users within the tenant.
        # - **1**: MaxCompute tables are visible to users within the tenant.
        self.table_privacy_mode = table_privacy_mode
        # The list of tags bound to the workspace.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # Indicates whether a proxy account is used to access the MaxCompute engine.
        self.use_proxy_odps_account = use_proxy_odps_account

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appkey is not None:
            result['Appkey'] = self.appkey

        if self.base_project is not None:
            result['BaseProject'] = self.base_project

        if self.default_di_resource_group_identifier is not None:
            result['DefaultDiResourceGroupIdentifier'] = self.default_di_resource_group_identifier

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.dev_storage_quota is not None:
            result['DevStorageQuota'] = self.dev_storage_quota

        if self.development_type is not None:
            result['DevelopmentType'] = self.development_type

        if self.disable_development is not None:
            result['DisableDevelopment'] = self.disable_development

        if self.env_types is not None:
            result['EnvTypes'] = self.env_types

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.is_allow_download is not None:
            result['IsAllowDownload'] = self.is_allow_download

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.max_flow_node is not None:
            result['MaxFlowNode'] = self.max_flow_node

        if self.prod_storage_quota is not None:
            result['ProdStorageQuota'] = self.prod_storage_quota

        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.project_mode is not None:
            result['ProjectMode'] = self.project_mode

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_owner_base_id is not None:
            result['ProjectOwnerBaseId'] = self.project_owner_base_id

        if self.protected_mode is not None:
            result['ProtectedMode'] = self.protected_mode

        if self.resident_area is not None:
            result['ResidentArea'] = self.resident_area

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.scheduler_max_retry_times is not None:
            result['SchedulerMaxRetryTimes'] = self.scheduler_max_retry_times

        if self.scheduler_retry_interval is not None:
            result['SchedulerRetryInterval'] = self.scheduler_retry_interval

        if self.status is not None:
            result['Status'] = self.status

        if self.table_privacy_mode is not None:
            result['TablePrivacyMode'] = self.table_privacy_mode

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.use_proxy_odps_account is not None:
            result['UseProxyOdpsAccount'] = self.use_proxy_odps_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Appkey') is not None:
            self.appkey = m.get('Appkey')

        if m.get('BaseProject') is not None:
            self.base_project = m.get('BaseProject')

        if m.get('DefaultDiResourceGroupIdentifier') is not None:
            self.default_di_resource_group_identifier = m.get('DefaultDiResourceGroupIdentifier')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DevStorageQuota') is not None:
            self.dev_storage_quota = m.get('DevStorageQuota')

        if m.get('DevelopmentType') is not None:
            self.development_type = m.get('DevelopmentType')

        if m.get('DisableDevelopment') is not None:
            self.disable_development = m.get('DisableDevelopment')

        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IsAllowDownload') is not None:
            self.is_allow_download = m.get('IsAllowDownload')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MaxFlowNode') is not None:
            self.max_flow_node = m.get('MaxFlowNode')

        if m.get('ProdStorageQuota') is not None:
            self.prod_storage_quota = m.get('ProdStorageQuota')

        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('ProjectMode') is not None:
            self.project_mode = m.get('ProjectMode')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectOwnerBaseId') is not None:
            self.project_owner_base_id = m.get('ProjectOwnerBaseId')

        if m.get('ProtectedMode') is not None:
            self.protected_mode = m.get('ProtectedMode')

        if m.get('ResidentArea') is not None:
            self.resident_area = m.get('ResidentArea')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SchedulerMaxRetryTimes') is not None:
            self.scheduler_max_retry_times = m.get('SchedulerMaxRetryTimes')

        if m.get('SchedulerRetryInterval') is not None:
            self.scheduler_retry_interval = m.get('SchedulerRetryInterval')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TablePrivacyMode') is not None:
            self.table_privacy_mode = m.get('TablePrivacyMode')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetProjectResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UseProxyOdpsAccount') is not None:
            self.use_proxy_odps_account = m.get('UseProxyOdpsAccount')

        return self

class GetProjectResponseBodyDataTags(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

