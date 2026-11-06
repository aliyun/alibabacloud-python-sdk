# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateCloudPermissionTemplateRequest(DaraModel):
    def __init__(
        self,
        allow_request: bool = None,
        applicable_scope: main_models.CreateCloudPermissionTemplateRequestApplicableScope = None,
        client_token: str = None,
        cloud_account_id: str = None,
        cloud_account_resources: List[main_models.CreateCloudPermissionTemplateRequestCloudAccountResources] = None,
        cloud_permission_template_name: str = None,
        cloud_permission_template_usage_type: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # Specifies whether users are allowed to apply for the permission template. Default value: true.
        self.allow_request = allow_request
        # The applicable scope of the permission template, including the scope type and specified users, groups, or organizational units.
        self.applicable_scope = applicable_scope
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The cloud account ID.
        # 
        # This parameter is required.
        self.cloud_account_id = cloud_account_id
        # The list of cloud account resource policies.
        self.cloud_account_resources = cloud_account_resources
        # The name of the permission template. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.cloud_permission_template_name = cloud_permission_template_name
        # The usage type of the permission template. Valid values:
        # - user: Privilege escalation for human users.
        # - application: Privilege escalation for M2M applications.
        # Default value: user.
        self.cloud_permission_template_usage_type = cloud_permission_template_usage_type
        # The description of the permission template. The description can be up to 128 characters in length.
        self.description = description
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.applicable_scope:
            self.applicable_scope.validate()
        if self.cloud_account_resources:
            for v1 in self.cloud_account_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_request is not None:
            result['AllowRequest'] = self.allow_request

        if self.applicable_scope is not None:
            result['ApplicableScope'] = self.applicable_scope.to_map()

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        result['CloudAccountResources'] = []
        if self.cloud_account_resources is not None:
            for k1 in self.cloud_account_resources:
                result['CloudAccountResources'].append(k1.to_map() if k1 else None)

        if self.cloud_permission_template_name is not None:
            result['CloudPermissionTemplateName'] = self.cloud_permission_template_name

        if self.cloud_permission_template_usage_type is not None:
            result['CloudPermissionTemplateUsageType'] = self.cloud_permission_template_usage_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRequest') is not None:
            self.allow_request = m.get('AllowRequest')

        if m.get('ApplicableScope') is not None:
            temp_model = main_models.CreateCloudPermissionTemplateRequestApplicableScope()
            self.applicable_scope = temp_model.from_map(m.get('ApplicableScope'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        self.cloud_account_resources = []
        if m.get('CloudAccountResources') is not None:
            for k1 in m.get('CloudAccountResources'):
                temp_model = main_models.CreateCloudPermissionTemplateRequestCloudAccountResources()
                self.cloud_account_resources.append(temp_model.from_map(k1))

        if m.get('CloudPermissionTemplateName') is not None:
            self.cloud_permission_template_name = m.get('CloudPermissionTemplateName')

        if m.get('CloudPermissionTemplateUsageType') is not None:
            self.cloud_permission_template_usage_type = m.get('CloudPermissionTemplateUsageType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class CreateCloudPermissionTemplateRequestCloudAccountResources(DaraModel):
    def __init__(
        self,
        cloud_account_resource_id: str = None,
    ):
        # The ID of the cloud account resource.
        self.cloud_account_resource_id = cloud_account_resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_resource_id is not None:
            result['CloudAccountResourceId'] = self.cloud_account_resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountResourceId') is not None:
            self.cloud_account_resource_id = m.get('CloudAccountResourceId')

        return self

class CreateCloudPermissionTemplateRequestApplicableScope(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        organizational_unit_ids: List[str] = None,
        scope_type: str = None,
        user_ids: List[str] = None,
    ):
        # The list of group IDs.
        self.group_ids = group_ids
        # The list of organizational unit IDs.
        self.organizational_unit_ids = organizational_unit_ids
        # The type of the applicable scope. Valid values: global and custom.
        self.scope_type = scope_type
        # The list of user IDs.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

