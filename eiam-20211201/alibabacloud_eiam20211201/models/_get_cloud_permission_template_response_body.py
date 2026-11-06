# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetCloudPermissionTemplateResponseBody(DaraModel):
    def __init__(
        self,
        cloud_permission_template: main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplate = None,
        request_id: str = None,
    ):
        # The permission template.
        self.cloud_permission_template = cloud_permission_template
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cloud_permission_template:
            self.cloud_permission_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_permission_template is not None:
            result['CloudPermissionTemplate'] = self.cloud_permission_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudPermissionTemplate') is not None:
            temp_model = main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplate()
            self.cloud_permission_template = temp_model.from_map(m.get('CloudPermissionTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCloudPermissionTemplateResponseBodyCloudPermissionTemplate(DaraModel):
    def __init__(
        self,
        allow_request: bool = None,
        applicable_scope: main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateApplicableScope = None,
        cloud_account_id: str = None,
        cloud_permission_template_creator: main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateCloudPermissionTemplateCreator = None,
        cloud_permission_template_id: str = None,
        cloud_permission_template_init_result: main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateCloudPermissionTemplateInitResult = None,
        cloud_permission_template_name: str = None,
        cloud_permission_template_owner_id: str = None,
        cloud_permission_template_owner_type: str = None,
        cloud_permission_template_sharing_mode: str = None,
        cloud_permission_template_usage_type: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        permission_entity_external_id: str = None,
        permission_entity_id: str = None,
        permission_entity_type: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # Specifies whether users are allowed to request the permission.
        self.allow_request = allow_request
        # The applicable scope of the permission template.
        self.applicable_scope = applicable_scope
        # The ID of the cloud account to which the template belongs.
        self.cloud_account_id = cloud_account_id
        # The creator information of the permission template.
        self.cloud_permission_template_creator = cloud_permission_template_creator
        # The unique identifier of the permission template.
        self.cloud_permission_template_id = cloud_permission_template_id
        # The initialization result. This parameter is returned only when the status is init_failed.
        self.cloud_permission_template_init_result = cloud_permission_template_init_result
        # The name of the permission template.
        self.cloud_permission_template_name = cloud_permission_template_name
        # The ID of the application to which the exclusive template belongs. This parameter is empty for shared templates.
        self.cloud_permission_template_owner_id = cloud_permission_template_owner_id
        # The owner type of the exclusive template. Valid values: application (M2M applications) and user (human users). This parameter is empty for shared templates.
        self.cloud_permission_template_owner_type = cloud_permission_template_owner_type
        # The sharing mode of the permission template. Valid values: shared and exclusive.
        self.cloud_permission_template_sharing_mode = cloud_permission_template_sharing_mode
        # The usage type of the permission template. Valid values: user (privilege escalation for human users) and application (privilege escalation for M2M applications).
        self.cloud_permission_template_usage_type = cloud_permission_template_usage_type
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The description of the permission template.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The external unique identifier of the associated cloud role, which is the ARN of the role on the cloud provider side.
        self.permission_entity_external_id = permission_entity_external_id
        # The ID of the associated CloudAccountRole.
        self.permission_entity_id = permission_entity_id
        # The permission entity type. Fixed value: cloud_account_role.
        self.permission_entity_type = permission_entity_type
        # The status of the permission template. Valid values: initializing, init_failed, enabled, and disabled.
        self.status = status
        # The last update time. The value is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.applicable_scope:
            self.applicable_scope.validate()
        if self.cloud_permission_template_creator:
            self.cloud_permission_template_creator.validate()
        if self.cloud_permission_template_init_result:
            self.cloud_permission_template_init_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_request is not None:
            result['AllowRequest'] = self.allow_request

        if self.applicable_scope is not None:
            result['ApplicableScope'] = self.applicable_scope.to_map()

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_permission_template_creator is not None:
            result['CloudPermissionTemplateCreator'] = self.cloud_permission_template_creator.to_map()

        if self.cloud_permission_template_id is not None:
            result['CloudPermissionTemplateId'] = self.cloud_permission_template_id

        if self.cloud_permission_template_init_result is not None:
            result['CloudPermissionTemplateInitResult'] = self.cloud_permission_template_init_result.to_map()

        if self.cloud_permission_template_name is not None:
            result['CloudPermissionTemplateName'] = self.cloud_permission_template_name

        if self.cloud_permission_template_owner_id is not None:
            result['CloudPermissionTemplateOwnerId'] = self.cloud_permission_template_owner_id

        if self.cloud_permission_template_owner_type is not None:
            result['CloudPermissionTemplateOwnerType'] = self.cloud_permission_template_owner_type

        if self.cloud_permission_template_sharing_mode is not None:
            result['CloudPermissionTemplateSharingMode'] = self.cloud_permission_template_sharing_mode

        if self.cloud_permission_template_usage_type is not None:
            result['CloudPermissionTemplateUsageType'] = self.cloud_permission_template_usage_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.permission_entity_external_id is not None:
            result['PermissionEntityExternalId'] = self.permission_entity_external_id

        if self.permission_entity_id is not None:
            result['PermissionEntityId'] = self.permission_entity_id

        if self.permission_entity_type is not None:
            result['PermissionEntityType'] = self.permission_entity_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRequest') is not None:
            self.allow_request = m.get('AllowRequest')

        if m.get('ApplicableScope') is not None:
            temp_model = main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateApplicableScope()
            self.applicable_scope = temp_model.from_map(m.get('ApplicableScope'))

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudPermissionTemplateCreator') is not None:
            temp_model = main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateCloudPermissionTemplateCreator()
            self.cloud_permission_template_creator = temp_model.from_map(m.get('CloudPermissionTemplateCreator'))

        if m.get('CloudPermissionTemplateId') is not None:
            self.cloud_permission_template_id = m.get('CloudPermissionTemplateId')

        if m.get('CloudPermissionTemplateInitResult') is not None:
            temp_model = main_models.GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateCloudPermissionTemplateInitResult()
            self.cloud_permission_template_init_result = temp_model.from_map(m.get('CloudPermissionTemplateInitResult'))

        if m.get('CloudPermissionTemplateName') is not None:
            self.cloud_permission_template_name = m.get('CloudPermissionTemplateName')

        if m.get('CloudPermissionTemplateOwnerId') is not None:
            self.cloud_permission_template_owner_id = m.get('CloudPermissionTemplateOwnerId')

        if m.get('CloudPermissionTemplateOwnerType') is not None:
            self.cloud_permission_template_owner_type = m.get('CloudPermissionTemplateOwnerType')

        if m.get('CloudPermissionTemplateSharingMode') is not None:
            self.cloud_permission_template_sharing_mode = m.get('CloudPermissionTemplateSharingMode')

        if m.get('CloudPermissionTemplateUsageType') is not None:
            self.cloud_permission_template_usage_type = m.get('CloudPermissionTemplateUsageType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PermissionEntityExternalId') is not None:
            self.permission_entity_external_id = m.get('PermissionEntityExternalId')

        if m.get('PermissionEntityId') is not None:
            self.permission_entity_id = m.get('PermissionEntityId')

        if m.get('PermissionEntityType') is not None:
            self.permission_entity_type = m.get('PermissionEntityType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateCloudPermissionTemplateInitResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        result: str = None,
    ):
        # The error code returned when initialization fails.
        self.error_code = error_code
        # The error message returned when initialization fails.
        self.error_message = error_message
        # The initialization result. Valid values: success and failed.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateCloudPermissionTemplateCreator(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        creator_name: str = None,
        creator_type: str = None,
    ):
        # The identity identifier of the creator.
        self.creator_id = creator_id
        # The name of the creator.
        self.creator_name = creator_name
        # The type of the creator. Valid values: idaas_admin and idaas_user.
        self.creator_type = creator_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        return self

class GetCloudPermissionTemplateResponseBodyCloudPermissionTemplateApplicableScope(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        organizational_unit_ids: List[str] = None,
        scope_type: str = None,
        user_ids: List[str] = None,
    ):
        # The list of specified group IDs. This parameter has a value only when ScopeType is set to custom.
        self.group_ids = group_ids
        # The list of specified organizational unit IDs. This parameter has a value only when ScopeType is set to custom.
        self.organizational_unit_ids = organizational_unit_ids
        # The type of the applicable scope. Valid values: global and custom.
        self.scope_type = scope_type
        # The list of specified user IDs. This parameter has a value only when ScopeType is set to custom.
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

