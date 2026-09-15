# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateWorkspaceResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The workspace details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateWorkspaceResponseBodyData(DaraModel):
    def __init__(
        self,
        ai_registry_namespace_id: str = None,
        authorization_status: str = None,
        bucket_name: str = None,
        cms_workspace_id: str = None,
        create_time: str = None,
        name: str = None,
        network_configuration: main_models.CreateWorkspaceResponseBodyDataNetworkConfiguration = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        status_reason: str = None,
        storage_type: str = None,
        tags: List[main_models.CreateWorkspaceResponseBodyDataTags] = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # The AI Registry namespace ID. This value is returned after the related resource binding is complete and may be empty during initialization.
        self.ai_registry_namespace_id = ai_registry_namespace_id
        # The OSS storage authorization status.
        self.authorization_status = authorization_status
        # The name of the private OSS bucket.
        self.bucket_name = bucket_name
        # The CloudMonitor workspace ID. This value is returned after the related resource binding is complete and may be empty during initialization.
        self.cms_workspace_id = cms_workspace_id
        # The time when the workspace was created, in ISO-8601 format.
        # 
        # This parameter is required.
        self.create_time = create_time
        # The workspace name.
        self.name = name
        # The network configuration of the workspace.
        self.network_configuration = network_configuration
        # The region ID of the workspace.
        self.region_id = region_id
        # The ID of the resource group to which the workspace belongs. This value may be empty if no resource group is specified.
        self.resource_group_id = resource_group_id
        # The workspace status.
        self.status = status
        # The supplementary reason for the current workspace status. This value is used to display the specific reason when initialization fails or authorization is pending, and may be empty under normal conditions.
        self.status_reason = status_reason
        # The storage type of the workspace.
        self.storage_type = storage_type
        # The list of workspace tags. An empty array is returned if no tags are set.
        # 
        # This parameter is required.
        self.tags = tags
        # The ID of the tenant to which the workspace belongs.
        self.tenant_id = tenant_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_registry_namespace_id is not None:
            result['aiRegistryNamespaceId'] = self.ai_registry_namespace_id

        if self.authorization_status is not None:
            result['authorizationStatus'] = self.authorization_status

        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.cms_workspace_id is not None:
            result['cmsWorkspaceId'] = self.cms_workspace_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.name is not None:
            result['name'] = self.name

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiRegistryNamespaceId') is not None:
            self.ai_registry_namespace_id = m.get('aiRegistryNamespaceId')

        if m.get('authorizationStatus') is not None:
            self.authorization_status = m.get('authorizationStatus')

        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('cmsWorkspaceId') is not None:
            self.cms_workspace_id = m.get('cmsWorkspaceId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.CreateWorkspaceResponseBodyDataNetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateWorkspaceResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateWorkspaceResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class CreateWorkspaceResponseBodyDataNetworkConfiguration(DaraModel):
    def __init__(
        self,
        vpc: main_models.CreateWorkspaceResponseBodyDataNetworkConfigurationVpc = None,
    ):
        # The VPC network configuration of the user.
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc is not None:
            result['vpc'] = self.vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpc') is not None:
            temp_model = main_models.CreateWorkspaceResponseBodyDataNetworkConfigurationVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        return self

class CreateWorkspaceResponseBodyDataNetworkConfigurationVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Specifies whether to enable VPC networking.
        self.enabled = enabled
        # The list of vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The ID of the user VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

