# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
        custom_suffix: str = None,
        description: str = None,
    ):
        self.service_name = service_name
        self.custom_suffix = custom_suffix
        self.description = description

    def validate(self):
        self.validate_required(self.service_name, 'service_name')

    def to_map(self):
        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.custom_suffix is not None:
            result['CustomSuffix'] = self.custom_suffix
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('CustomSuffix') is not None:
            self.custom_suffix = m.get('CustomSuffix')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateServiceLinkedRoleResponseRole(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        description: str = None,
        assume_role_policy_document: str = None,
        is_service_linked_role: bool = None,
        arn: str = None,
        role_id: str = None,
        create_date: str = None,
        role_principal_name: str = None,
    ):
        self.role_name = role_name
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document
        self.is_service_linked_role = is_service_linked_role
        self.arn = arn
        self.role_id = role_id
        self.create_date = create_date
        self.role_principal_name = role_principal_name

    def validate(self):
        self.validate_required(self.role_name, 'role_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.assume_role_policy_document, 'assume_role_policy_document')
        self.validate_required(self.is_service_linked_role, 'is_service_linked_role')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.role_id, 'role_id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.role_principal_name, 'role_principal_name')

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.description is not None:
            result['Description'] = self.description
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: CreateServiceLinkedRoleResponseRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.role, 'role')
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateServiceLinkedRoleResponseRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class GetServiceLinkedRoleDeletionStatusRequest(TeaModel):
    def __init__(
        self,
        deletion_task_id: str = None,
    ):
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsagesRoleUsageResources(TeaModel):
    def __init__(
        self,
        resource: List[str] = None,
    ):
        # Resource
        self.resource = resource

    def validate(self):
        self.validate_required(self.resource, 'resource')

    def to_map(self):
        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsagesRoleUsage(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsagesRoleUsageResources = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        self.validate_required(self.region, 'region')
        self.validate_required(self.resources, 'resources')
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsagesRoleUsageResources()
            self.resources = temp_model.from_map(m['Resources'])
        return self


class GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsages(TeaModel):
    def __init__(
        self,
        role_usage: List[GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsagesRoleUsage] = None,
    ):
        self.role_usage = role_usage

    def validate(self):
        self.validate_required(self.role_usage, 'role_usage')
        if self.role_usage:
            for k in self.role_usage:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RoleUsage'] = []
        if self.role_usage is not None:
            for k in self.role_usage:
                result['RoleUsage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_usage = []
        if m.get('RoleUsage') is not None:
            for k in m.get('RoleUsage'):
                temp_model = GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsagesRoleUsage()
                self.role_usage.append(temp_model.from_map(k))
        return self


class GetServiceLinkedRoleDeletionStatusResponseReason(TeaModel):
    def __init__(
        self,
        message: str = None,
        role_usages: GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsages = None,
    ):
        self.message = message
        self.role_usages = role_usages

    def validate(self):
        self.validate_required(self.message, 'message')
        self.validate_required(self.role_usages, 'role_usages')
        if self.role_usages:
            self.role_usages.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.role_usages is not None:
            result['RoleUsages'] = self.role_usages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RoleUsages') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseReasonRoleUsages()
            self.role_usages = temp_model.from_map(m['RoleUsages'])
        return self


class GetServiceLinkedRoleDeletionStatusResponse(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        reason: GetServiceLinkedRoleDeletionStatusResponseReason = None,
    ):
        self.status = status
        self.request_id = request_id
        self.reason = reason

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.reason, 'reason')
        if self.reason:
            self.reason.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Reason') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseReason()
            self.reason = temp_model.from_map(m['Reason'])
        return self


class ListTrustedServiceStatusRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTrustedServiceStatusResponseEnabledServicePrincipalsEnabledServicePrincipal(TeaModel):
    def __init__(
        self,
        service_principal: str = None,
        enable_time: str = None,
    ):
        self.service_principal = service_principal
        self.enable_time = enable_time

    def validate(self):
        self.validate_required(self.service_principal, 'service_principal')
        self.validate_required(self.enable_time, 'enable_time')

    def to_map(self):
        result = dict()
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        return self


class ListTrustedServiceStatusResponseEnabledServicePrincipals(TeaModel):
    def __init__(
        self,
        enabled_service_principal: List[ListTrustedServiceStatusResponseEnabledServicePrincipalsEnabledServicePrincipal] = None,
    ):
        self.enabled_service_principal = enabled_service_principal

    def validate(self):
        self.validate_required(self.enabled_service_principal, 'enabled_service_principal')
        if self.enabled_service_principal:
            for k in self.enabled_service_principal:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EnabledServicePrincipal'] = []
        if self.enabled_service_principal is not None:
            for k in self.enabled_service_principal:
                result['EnabledServicePrincipal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enabled_service_principal = []
        if m.get('EnabledServicePrincipal') is not None:
            for k in m.get('EnabledServicePrincipal'):
                temp_model = ListTrustedServiceStatusResponseEnabledServicePrincipalsEnabledServicePrincipal()
                self.enabled_service_principal.append(temp_model.from_map(k))
        return self


class ListTrustedServiceStatusResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        enabled_service_principals: ListTrustedServiceStatusResponseEnabledServicePrincipals = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.enabled_service_principals = enabled_service_principals

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.enabled_service_principals, 'enabled_service_principals')
        if self.enabled_service_principals:
            self.enabled_service_principals.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.enabled_service_principals is not None:
            result['EnabledServicePrincipals'] = self.enabled_service_principals.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('EnabledServicePrincipals') is not None:
            temp_model = ListTrustedServiceStatusResponseEnabledServicePrincipals()
            self.enabled_service_principals = temp_model.from_map(m['EnabledServicePrincipals'])
        return self


class DeleteServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        self.validate_required(self.role_name, 'role_name')

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        deletion_task_id: str = None,
    ):
        self.request_id = request_id
        self.deletion_task_id = deletion_task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.deletion_task_id, 'deletion_task_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        new_assume_role_policy_document: str = None,
        new_max_session_duration: int = None,
    ):
        self.role_name = role_name
        self.new_assume_role_policy_document = new_assume_role_policy_document
        self.new_max_session_duration = new_max_session_duration

    def validate(self):
        self.validate_required(self.role_name, 'role_name')
        self.validate_required(self.new_assume_role_policy_document, 'new_assume_role_policy_document')

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.new_assume_role_policy_document is not None:
            result['NewAssumeRolePolicyDocument'] = self.new_assume_role_policy_document
        if self.new_max_session_duration is not None:
            result['NewMaxSessionDuration'] = self.new_max_session_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('NewAssumeRolePolicyDocument') is not None:
            self.new_assume_role_policy_document = m.get('NewAssumeRolePolicyDocument')
        if m.get('NewMaxSessionDuration') is not None:
            self.new_max_session_duration = m.get('NewMaxSessionDuration')
        return self


class UpdateRoleResponseRole(TeaModel):
    def __init__(
        self,
        max_session_duration: int = None,
        update_date: str = None,
        role_name: str = None,
        description: str = None,
        assume_role_policy_document: str = None,
        arn: str = None,
        role_id: str = None,
        create_date: str = None,
        role_principal_name: str = None,
    ):
        self.max_session_duration = max_session_duration
        self.update_date = update_date
        self.role_name = role_name
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document
        self.arn = arn
        self.role_id = role_id
        self.create_date = create_date
        self.role_principal_name = role_principal_name

    def validate(self):
        self.validate_required(self.max_session_duration, 'max_session_duration')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.role_name, 'role_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.assume_role_policy_document, 'assume_role_policy_document')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.role_id, 'role_id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.role_principal_name, 'role_principal_name')

    def to_map(self):
        result = dict()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.description is not None:
            result['Description'] = self.description
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class UpdateRoleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: UpdateRoleResponseRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.role, 'role')
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = UpdateRoleResponseRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        service: str = None,
        region: str = None,
        resource_type: str = None,
        resource_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.resource_group_id = resource_group_id
        self.service = service
        self.region = region
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service is not None:
            result['Service'] = self.service
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListResourcesResponseResourcesResource(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        service: str = None,
        resource_type: str = None,
        region_id: str = None,
        create_date: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.service = service
        self.resource_type = resource_type
        self.region_id = region_id
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.service, 'service')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.service is not None:
            result['Service'] = self.service
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListResourcesResponseResources(TeaModel):
    def __init__(
        self,
        resource: List[ListResourcesResponseResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        self.validate_required(self.resource, 'resource')
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = ListResourcesResponseResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        resources: ListResourcesResponseResources = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.resources = resources

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.resources, 'resources')
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Resources') is not None:
            temp_model = ListResourcesResponseResources()
            self.resources = temp_model.from_map(m['Resources'])
        return self


class CreateCloudAccountRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        parent_folder_id: str = None,
        email: str = None,
        payer_account_id: str = None,
    ):
        self.display_name = display_name
        self.parent_folder_id = parent_folder_id
        self.email = email
        self.payer_account_id = payer_account_id

    def validate(self):
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.email, 'email')

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.email is not None:
            result['Email'] = self.email
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        return self


class CreateCloudAccountResponseAccount(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        account_id: str = None,
        display_name: str = None,
        account_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        modify_time: str = None,
        type: str = None,
        status: str = None,
        record_id: str = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.account_id = account_id
        self.display_name = display_name
        self.account_name = account_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.modify_time = modify_time
        self.type = type
        self.status = status
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.type, 'type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CreateCloudAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: CreateCloudAccountResponseAccount = None,
    ):
        self.request_id = request_id
        self.account = account

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account is not None:
            result['Account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Account') is not None:
            temp_model = CreateCloudAccountResponseAccount()
            self.account = temp_model.from_map(m['Account'])
        return self


class DeleteRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        self.validate_required(self.role_name, 'role_name')

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteRoleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        language: str = None,
    ):
        self.role_name = role_name
        self.language = language

    def validate(self):
        self.validate_required(self.role_name, 'role_name')

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetRoleResponseRoleLatestDeletionTask(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        self.create_date = create_date
        self.deletion_task_id = deletion_task_id

    def validate(self):
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.deletion_task_id, 'deletion_task_id')

    def to_map(self):
        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetRoleResponseRole(TeaModel):
    def __init__(
        self,
        max_session_duration: int = None,
        update_date: str = None,
        role_name: str = None,
        description: str = None,
        assume_role_policy_document: str = None,
        is_service_linked_role: bool = None,
        arn: str = None,
        role_id: str = None,
        create_date: str = None,
        role_principal_name: str = None,
        latest_deletion_task: GetRoleResponseRoleLatestDeletionTask = None,
    ):
        self.max_session_duration = max_session_duration
        self.update_date = update_date
        self.role_name = role_name
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document
        self.is_service_linked_role = is_service_linked_role
        self.arn = arn
        self.role_id = role_id
        self.create_date = create_date
        self.role_principal_name = role_principal_name
        self.latest_deletion_task = latest_deletion_task

    def validate(self):
        self.validate_required(self.max_session_duration, 'max_session_duration')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.role_name, 'role_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.assume_role_policy_document, 'assume_role_policy_document')
        self.validate_required(self.is_service_linked_role, 'is_service_linked_role')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.role_id, 'role_id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.role_principal_name, 'role_principal_name')
        self.validate_required(self.latest_deletion_task, 'latest_deletion_task')
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        result = dict()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.description is not None:
            result['Description'] = self.description
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('LatestDeletionTask') is not None:
            temp_model = GetRoleResponseRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        return self


class GetRoleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: GetRoleResponseRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.role, 'role')
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = GetRoleResponseRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        language: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ListRolesResponseRolesRoleLatestDeletionTask(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        self.create_date = create_date
        self.deletion_task_id = deletion_task_id

    def validate(self):
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.deletion_task_id, 'deletion_task_id')

    def to_map(self):
        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class ListRolesResponseRolesRole(TeaModel):
    def __init__(
        self,
        max_session_duration: int = None,
        update_date: str = None,
        role_name: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        arn: str = None,
        role_id: str = None,
        create_date: str = None,
        role_principal_name: str = None,
        latest_deletion_task: ListRolesResponseRolesRoleLatestDeletionTask = None,
    ):
        self.max_session_duration = max_session_duration
        self.update_date = update_date
        self.role_name = role_name
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.arn = arn
        self.role_id = role_id
        self.create_date = create_date
        self.role_principal_name = role_principal_name
        self.latest_deletion_task = latest_deletion_task

    def validate(self):
        self.validate_required(self.max_session_duration, 'max_session_duration')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.role_name, 'role_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.is_service_linked_role, 'is_service_linked_role')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.role_id, 'role_id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.role_principal_name, 'role_principal_name')
        self.validate_required(self.latest_deletion_task, 'latest_deletion_task')
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        result = dict()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('LatestDeletionTask') is not None:
            temp_model = ListRolesResponseRolesRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        return self


class ListRolesResponseRoles(TeaModel):
    def __init__(
        self,
        role: List[ListRolesResponseRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        self.validate_required(self.role, 'role')
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = ListRolesResponseRolesRole()
                self.role.append(temp_model.from_map(k))
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        roles: ListRolesResponseRoles = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.roles = roles

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.roles, 'roles')
        if self.roles:
            self.roles.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Roles') is not None:
            temp_model = ListRolesResponseRoles()
            self.roles = temp_model.from_map(m['Roles'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        description: str = None,
        assume_role_policy_document: str = None,
        max_session_duration: int = None,
    ):
        self.role_name = role_name
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document
        self.max_session_duration = max_session_duration

    def validate(self):
        self.validate_required(self.role_name, 'role_name')
        self.validate_required(self.assume_role_policy_document, 'assume_role_policy_document')

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.description is not None:
            result['Description'] = self.description
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        return self


class CreateRoleResponseRole(TeaModel):
    def __init__(
        self,
        max_session_duration: int = None,
        role_name: str = None,
        description: str = None,
        assume_role_policy_document: str = None,
        arn: str = None,
        role_id: str = None,
        create_date: str = None,
        role_principal_name: str = None,
    ):
        self.max_session_duration = max_session_duration
        self.role_name = role_name
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document
        self.arn = arn
        self.role_id = role_id
        self.create_date = create_date
        self.role_principal_name = role_principal_name

    def validate(self):
        self.validate_required(self.max_session_duration, 'max_session_duration')
        self.validate_required(self.role_name, 'role_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.assume_role_policy_document, 'assume_role_policy_document')
        self.validate_required(self.arn, 'arn')
        self.validate_required(self.role_id, 'role_id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.role_principal_name, 'role_principal_name')

    def to_map(self):
        result = dict()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.description is not None:
            result['Description'] = self.description
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: CreateRoleResponseRole = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.role, 'role')
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateRoleResponseRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class ListPolicyAttachmentsRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        policy_type: str = None,
        policy_name: str = None,
        principal_type: str = None,
        principal_name: str = None,
        page_number: int = None,
        page_size: int = None,
        language: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.principal_type = principal_type
        self.principal_name = principal_name
        self.page_number = page_number
        self.page_size = page_size
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ListPolicyAttachmentsResponsePolicyAttachmentsPolicyAttachment(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        description: str = None,
        resource_group_id: str = None,
        attach_date: str = None,
        policy_name: str = None,
        principal_name: str = None,
        principal_type: str = None,
    ):
        self.policy_type = policy_type
        self.description = description
        self.resource_group_id = resource_group_id
        self.attach_date = attach_date
        self.policy_name = policy_name
        self.principal_name = principal_name
        self.principal_type = principal_type

    def validate(self):
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.attach_date, 'attach_date')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.principal_name, 'principal_name')
        self.validate_required(self.principal_type, 'principal_type')

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class ListPolicyAttachmentsResponsePolicyAttachments(TeaModel):
    def __init__(
        self,
        policy_attachment: List[ListPolicyAttachmentsResponsePolicyAttachmentsPolicyAttachment] = None,
    ):
        self.policy_attachment = policy_attachment

    def validate(self):
        self.validate_required(self.policy_attachment, 'policy_attachment')
        if self.policy_attachment:
            for k in self.policy_attachment:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PolicyAttachment'] = []
        if self.policy_attachment is not None:
            for k in self.policy_attachment:
                result['PolicyAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_attachment = []
        if m.get('PolicyAttachment') is not None:
            for k in m.get('PolicyAttachment'):
                temp_model = ListPolicyAttachmentsResponsePolicyAttachmentsPolicyAttachment()
                self.policy_attachment.append(temp_model.from_map(k))
        return self


class ListPolicyAttachmentsResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        policy_attachments: ListPolicyAttachmentsResponsePolicyAttachments = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.policy_attachments = policy_attachments

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.policy_attachments, 'policy_attachments')
        if self.policy_attachments:
            self.policy_attachments.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.policy_attachments is not None:
            result['PolicyAttachments'] = self.policy_attachments.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PolicyAttachments') is not None:
            temp_model = ListPolicyAttachmentsResponsePolicyAttachments()
            self.policy_attachments = temp_model.from_map(m['PolicyAttachments'])
        return self


class DetachPolicyRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        policy_type: str = None,
        policy_name: str = None,
        principal_type: str = None,
        principal_name: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.principal_type = principal_type
        self.principal_name = principal_name

    def validate(self):
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.principal_type, 'principal_type')
        self.validate_required(self.principal_name, 'principal_name')

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class DetachPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachPolicyRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        policy_type: str = None,
        policy_name: str = None,
        principal_type: str = None,
        principal_name: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.principal_type = principal_type
        self.principal_name = principal_name

    def validate(self):
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.principal_type, 'principal_type')
        self.validate_required(self.principal_name, 'principal_name')

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class AttachPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.version_id, 'version_id')

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponsePolicyVersion(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        is_default_version: bool = None,
        policy_document: str = None,
        create_date: str = None,
    ):
        self.version_id = version_id
        self.is_default_version = is_default_version
        self.policy_document = policy_document
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.version_id, 'version_id')
        self.validate_required(self.is_default_version, 'is_default_version')
        self.validate_required(self.policy_document, 'policy_document')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetPolicyVersionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy_version: GetPolicyVersionResponsePolicyVersion = None,
    ):
        self.request_id = request_id
        self.policy_version = policy_version

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy_version, 'policy_version')
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PolicyVersion') is not None:
            temp_model = GetPolicyVersionResponsePolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        return self


class SetDefaultPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.version_id, 'version_id')

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class SetDefaultPolicyVersionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.resource_group_id, 'resource_group_id')

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteResourceGroupResponseResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteResourceGroupResponseResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[DeleteResourceGroupResponseResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        self.validate_required(self.region_status, 'region_status')
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = DeleteResourceGroupResponseResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class DeleteResourceGroupResponseResourceGroup(TeaModel):
    def __init__(
        self,
        status: str = None,
        account_id: str = None,
        display_name: str = None,
        id: str = None,
        create_date: str = None,
        name: str = None,
        region_statuses: DeleteResourceGroupResponseResourceGroupRegionStatuses = None,
    ):
        self.status = status
        self.account_id = account_id
        self.display_name = display_name
        self.id = id
        self.create_date = create_date
        self.name = name
        self.region_statuses = region_statuses

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region_statuses, 'region_statuses')
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = DeleteResourceGroupResponseResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        return self


class DeleteResourceGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: DeleteResourceGroupResponseResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_group, 'resource_group')
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = DeleteResourceGroupResponseResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
        language: str = None,
    ):
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.language = language

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.policy_type, 'policy_type')

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetPolicyResponsePolicy(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        update_date: str = None,
        description: str = None,
        attachment_count: int = None,
        policy_name: str = None,
        default_version: str = None,
        policy_document: str = None,
        create_date: str = None,
    ):
        self.policy_type = policy_type
        self.update_date = update_date
        self.description = description
        self.attachment_count = attachment_count
        self.policy_name = policy_name
        self.default_version = default_version
        self.policy_document = policy_document
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.description, 'description')
        self.validate_required(self.attachment_count, 'attachment_count')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.default_version, 'default_version')
        self.validate_required(self.policy_document, 'policy_document')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy: GetPolicyResponsePolicy = None,
    ):
        self.request_id = request_id
        self.policy = policy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy, 'policy')
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            temp_model = GetPolicyResponsePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class UpdateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        new_display_name: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.new_display_name = new_display_name

    def validate(self):
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.new_display_name, 'new_display_name')

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        return self


class UpdateResourceGroupResponseResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        id: str = None,
        create_date: str = None,
        name: str = None,
    ):
        self.account_id = account_id
        self.display_name = display_name
        self.id = id
        self.create_date = create_date
        self.name = name

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: UpdateResourceGroupResponseResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_group, 'resource_group')
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = UpdateResourceGroupResponseResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class ListResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.status = status
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListResourceGroupsResponseResourceGroupsResourceGroup(TeaModel):
    def __init__(
        self,
        status: str = None,
        account_id: str = None,
        display_name: str = None,
        id: str = None,
        create_date: str = None,
        name: str = None,
    ):
        self.status = status
        self.account_id = account_id
        self.display_name = display_name
        self.id = id
        self.create_date = create_date
        self.name = name

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListResourceGroupsResponseResourceGroups(TeaModel):
    def __init__(
        self,
        resource_group: List[ListResourceGroupsResponseResourceGroupsResourceGroup] = None,
    ):
        self.resource_group = resource_group

    def validate(self):
        self.validate_required(self.resource_group, 'resource_group')
        if self.resource_group:
            for k in self.resource_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k in self.resource_group:
                result['ResourceGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k in m.get('ResourceGroup'):
                temp_model = ListResourceGroupsResponseResourceGroupsResourceGroup()
                self.resource_group.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        resource_groups: ListResourceGroupsResponseResourceGroups = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.resource_groups = resource_groups

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.resource_groups, 'resource_groups')
        if self.resource_groups:
            self.resource_groups.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceGroups') is not None:
            temp_model = ListResourceGroupsResponseResourceGroups()
            self.resource_groups = temp_model.from_map(m['ResourceGroups'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        page_number: int = None,
        page_size: int = None,
        language: str = None,
    ):
        self.policy_type = policy_type
        self.page_number = page_number
        self.page_size = page_size
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ListPoliciesResponsePoliciesPolicy(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        update_date: str = None,
        description: str = None,
        attachment_count: int = None,
        policy_name: str = None,
        default_version: str = None,
        create_date: str = None,
    ):
        self.policy_type = policy_type
        self.update_date = update_date
        self.description = description
        self.attachment_count = attachment_count
        self.policy_name = policy_name
        self.default_version = default_version
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.update_date, 'update_date')
        self.validate_required(self.description, 'description')
        self.validate_required(self.attachment_count, 'attachment_count')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.default_version, 'default_version')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListPoliciesResponsePolicies(TeaModel):
    def __init__(
        self,
        policy: List[ListPoliciesResponsePoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        self.validate_required(self.policy, 'policy')
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesResponsePoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        policies: ListPoliciesResponsePolicies = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.policies = policies

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.policies, 'policies')
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Policies') is not None:
            temp_model = ListPoliciesResponsePolicies()
            self.policies = temp_model.from_map(m['Policies'])
        return self


class ListPolicyVersionsRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name

    def validate(self):
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.policy_name, 'policy_name')

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class ListPolicyVersionsResponsePolicyVersionsPolicyVersion(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        is_default_version: bool = None,
        create_date: str = None,
    ):
        self.version_id = version_id
        self.is_default_version = is_default_version
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.version_id, 'version_id')
        self.validate_required(self.is_default_version, 'is_default_version')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListPolicyVersionsResponsePolicyVersions(TeaModel):
    def __init__(
        self,
        policy_version: List[ListPolicyVersionsResponsePolicyVersionsPolicyVersion] = None,
    ):
        self.policy_version = policy_version

    def validate(self):
        self.validate_required(self.policy_version, 'policy_version')
        if self.policy_version:
            for k in self.policy_version:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PolicyVersion'] = []
        if self.policy_version is not None:
            for k in self.policy_version:
                result['PolicyVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_version = []
        if m.get('PolicyVersion') is not None:
            for k in m.get('PolicyVersion'):
                temp_model = ListPolicyVersionsResponsePolicyVersionsPolicyVersion()
                self.policy_version.append(temp_model.from_map(k))
        return self


class ListPolicyVersionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy_versions: ListPolicyVersionsResponsePolicyVersions = None,
    ):
        self.request_id = request_id
        self.policy_versions = policy_versions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy_versions, 'policy_versions')
        if self.policy_versions:
            self.policy_versions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy_versions is not None:
            result['PolicyVersions'] = self.policy_versions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PolicyVersions') is not None:
            temp_model = ListPolicyVersionsResponsePolicyVersions()
            self.policy_versions = temp_model.from_map(m['PolicyVersions'])
        return self


class CreateResourceAccountRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
        account_name_prefix: str = None,
    ):
        self.display_name = display_name
        self.parent_folder_id = parent_folder_id
        self.payer_account_id = payer_account_id
        self.account_name_prefix = account_name_prefix

    def validate(self):
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')
        return self


class CreateResourceAccountResponseAccount(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        join_method: str = None,
        resource_directory_id: str = None,
        type: str = None,
        account_id: str = None,
        display_name: str = None,
        join_time: str = None,
        folder_id: str = None,
        account_name: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.join_method = join_method
        self.resource_directory_id = resource_directory_id
        self.type = type
        self.account_id = account_id
        self.display_name = display_name
        self.join_time = join_time
        self.folder_id = folder_id
        self.account_name = account_name

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.type is not None:
            result['Type'] = self.type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class CreateResourceAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: CreateResourceAccountResponseAccount = None,
    ):
        self.request_id = request_id
        self.account = account

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account is not None:
            result['Account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Account') is not None:
            temp_model = CreateResourceAccountResponseAccount()
            self.account = temp_model.from_map(m['Account'])
        return self


class ListHandshakesForResourceDirectoryRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHandshakesForResourceDirectoryResponseHandshakesHandshake(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        handshake_id: str = None,
        master_account_name: str = None,
        note: str = None,
        create_time: str = None,
        target_type: str = None,
        master_account_id: str = None,
        expire_time: str = None,
        target_entity: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.handshake_id = handshake_id
        self.master_account_name = master_account_name
        self.note = note
        self.create_time = create_time
        self.target_type = target_type
        self.master_account_id = master_account_id
        self.expire_time = expire_time
        self.target_entity = target_entity

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.handshake_id, 'handshake_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.note, 'note')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.target_type, 'target_type')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.target_entity, 'target_entity')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.note is not None:
            result['Note'] = self.note
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        return self


class ListHandshakesForResourceDirectoryResponseHandshakes(TeaModel):
    def __init__(
        self,
        handshake: List[ListHandshakesForResourceDirectoryResponseHandshakesHandshake] = None,
    ):
        self.handshake = handshake

    def validate(self):
        self.validate_required(self.handshake, 'handshake')
        if self.handshake:
            for k in self.handshake:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Handshake'] = []
        if self.handshake is not None:
            for k in self.handshake:
                result['Handshake'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.handshake = []
        if m.get('Handshake') is not None:
            for k in m.get('Handshake'):
                temp_model = ListHandshakesForResourceDirectoryResponseHandshakesHandshake()
                self.handshake.append(temp_model.from_map(k))
        return self


class ListHandshakesForResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        handshakes: ListHandshakesForResourceDirectoryResponseHandshakes = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.handshakes = handshakes

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.handshakes, 'handshakes')
        if self.handshakes:
            self.handshakes.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.handshakes is not None:
            result['Handshakes'] = self.handshakes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Handshakes') is not None:
            temp_model = ListHandshakesForResourceDirectoryResponseHandshakes()
            self.handshakes = temp_model.from_map(m['Handshakes'])
        return self


class DestroyResourceDirectoryRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DestroyResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_document: str = None,
        set_as_default: bool = None,
    ):
        self.policy_name = policy_name
        self.policy_document = policy_document
        self.set_as_default = set_as_default

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.policy_document, 'policy_document')

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')
        return self


class CreatePolicyVersionResponsePolicyVersion(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        is_default_version: bool = None,
        create_date: str = None,
    ):
        self.version_id = version_id
        self.is_default_version = is_default_version
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.version_id, 'version_id')
        self.validate_required(self.is_default_version, 'is_default_version')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreatePolicyVersionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy_version: CreatePolicyVersionResponsePolicyVersion = None,
    ):
        self.request_id = request_id
        self.policy_version = policy_version

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy_version, 'policy_version')
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PolicyVersion') is not None:
            temp_model = CreatePolicyVersionResponsePolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        return self


class DeletePolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.version_id, 'version_id')

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeletePolicyVersionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.resource_group_id, 'resource_group_id')

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetResourceGroupResponseResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetResourceGroupResponseResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[GetResourceGroupResponseResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        self.validate_required(self.region_status, 'region_status')
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = GetResourceGroupResponseResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class GetResourceGroupResponseResourceGroup(TeaModel):
    def __init__(
        self,
        status: str = None,
        account_id: str = None,
        display_name: str = None,
        id: str = None,
        create_date: str = None,
        name: str = None,
        region_statuses: GetResourceGroupResponseResourceGroupRegionStatuses = None,
    ):
        self.status = status
        self.account_id = account_id
        self.display_name = display_name
        self.id = id
        self.create_date = create_date
        self.name = name
        self.region_statuses = region_statuses

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region_statuses, 'region_statuses')
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = GetResourceGroupResponseResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        return self


class GetResourceGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: GetResourceGroupResponseResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_group, 'resource_group')
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = GetResourceGroupResponseResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class InitResourceDirectoryRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class InitResourceDirectoryResponseResourceDirectory(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        root_folder_id: str = None,
        create_time: str = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.master_account_id = master_account_id
        self.master_account_name = master_account_name
        self.root_folder_id = root_folder_id
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.root_folder_id, 'root_folder_id')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class InitResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: InitResourceDirectoryResponseResourceDirectory = None,
    ):
        self.request_id = request_id
        self.resource_directory = resource_directory

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_directory, 'resource_directory')
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = InitResourceDirectoryResponseResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class GetHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        self.handshake_id = handshake_id

    def validate(self):
        self.validate_required(self.handshake_id, 'handshake_id')

    def to_map(self):
        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class GetHandshakeResponseHandshake(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        handshake_id: str = None,
        master_account_name: str = None,
        note: str = None,
        create_time: str = None,
        target_type: str = None,
        master_account_id: str = None,
        master_account_real_name: str = None,
        expire_time: str = None,
        invited_account_real_name: str = None,
        target_entity: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.handshake_id = handshake_id
        self.master_account_name = master_account_name
        self.note = note
        self.create_time = create_time
        self.target_type = target_type
        self.master_account_id = master_account_id
        self.master_account_real_name = master_account_real_name
        self.expire_time = expire_time
        self.invited_account_real_name = invited_account_real_name
        self.target_entity = target_entity

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.handshake_id, 'handshake_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.note, 'note')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.target_type, 'target_type')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.master_account_real_name, 'master_account_real_name')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.invited_account_real_name, 'invited_account_real_name')
        self.validate_required(self.target_entity, 'target_entity')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.note is not None:
            result['Note'] = self.note
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_real_name is not None:
            result['MasterAccountRealName'] = self.master_account_real_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.invited_account_real_name is not None:
            result['InvitedAccountRealName'] = self.invited_account_real_name
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountRealName') is not None:
            self.master_account_real_name = m.get('MasterAccountRealName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InvitedAccountRealName') is not None:
            self.invited_account_real_name = m.get('InvitedAccountRealName')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        return self


class GetHandshakeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        handshake: GetHandshakeResponseHandshake = None,
    ):
        self.request_id = request_id
        self.handshake = handshake

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.handshake, 'handshake')
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Handshake') is not None:
            temp_model = GetHandshakeResponseHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        return self


class CancelHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        self.handshake_id = handshake_id

    def validate(self):
        self.validate_required(self.handshake_id, 'handshake_id')

    def to_map(self):
        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class CancelHandshakeResponseHandshake(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
        resource_directory_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        target_entity: str = None,
        target_type: str = None,
        note: str = None,
        status: str = None,
        create_time: str = None,
        modify_time: str = None,
        expire_time: str = None,
    ):
        self.handshake_id = handshake_id
        self.resource_directory_id = resource_directory_id
        self.master_account_id = master_account_id
        self.master_account_name = master_account_name
        self.target_entity = target_entity
        self.target_type = target_type
        self.note = note
        self.status = status
        self.create_time = create_time
        self.modify_time = modify_time
        self.expire_time = expire_time

    def validate(self):
        self.validate_required(self.handshake_id, 'handshake_id')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.target_entity, 'target_entity')
        self.validate_required(self.target_type, 'target_type')
        self.validate_required(self.note, 'note')
        self.validate_required(self.status, 'status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.expire_time, 'expire_time')

    def to_map(self):
        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.note is not None:
            result['Note'] = self.note
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class CancelHandshakeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        handshake: CancelHandshakeResponseHandshake = None,
    ):
        self.request_id = request_id
        self.handshake = handshake

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.handshake, 'handshake')
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Handshake') is not None:
            temp_model = CancelHandshakeResponseHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        description: str = None,
        policy_document: str = None,
    ):
        self.policy_name = policy_name
        self.description = description
        self.policy_document = policy_document

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.policy_document, 'policy_document')

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        return self


class CreatePolicyResponsePolicy(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        description: str = None,
        policy_name: str = None,
        default_version: str = None,
        create_date: str = None,
    ):
        self.policy_type = policy_type
        self.description = description
        self.policy_name = policy_name
        self.default_version = default_version
        self.create_date = create_date

    def validate(self):
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.default_version, 'default_version')
        self.validate_required(self.create_date, 'create_date')

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy: CreatePolicyResponsePolicy = None,
    ):
        self.request_id = request_id
        self.policy = policy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy, 'policy')
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            temp_model = CreatePolicyResponsePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class DeclineHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        self.handshake_id = handshake_id

    def validate(self):
        self.validate_required(self.handshake_id, 'handshake_id')

    def to_map(self):
        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class DeclineHandshakeResponseHandshake(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
        resource_directory_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        target_entity: str = None,
        target_type: str = None,
        note: str = None,
        status: str = None,
        create_time: str = None,
        modify_time: str = None,
        expire_time: str = None,
    ):
        self.handshake_id = handshake_id
        self.resource_directory_id = resource_directory_id
        self.master_account_id = master_account_id
        self.master_account_name = master_account_name
        self.target_entity = target_entity
        self.target_type = target_type
        self.note = note
        self.status = status
        self.create_time = create_time
        self.modify_time = modify_time
        self.expire_time = expire_time

    def validate(self):
        self.validate_required(self.handshake_id, 'handshake_id')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.target_entity, 'target_entity')
        self.validate_required(self.target_type, 'target_type')
        self.validate_required(self.note, 'note')
        self.validate_required(self.status, 'status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.expire_time, 'expire_time')

    def to_map(self):
        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.note is not None:
            result['Note'] = self.note
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class DeclineHandshakeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        handshake: DeclineHandshakeResponseHandshake = None,
    ):
        self.request_id = request_id
        self.handshake = handshake

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.handshake, 'handshake')
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Handshake') is not None:
            temp_model = DeclineHandshakeResponseHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        self.policy_name = policy_name

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHandshakesForAccountRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHandshakesForAccountResponseHandshakesHandshake(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        handshake_id: str = None,
        master_account_name: str = None,
        note: str = None,
        create_time: str = None,
        target_type: str = None,
        master_account_id: str = None,
        expire_time: str = None,
        target_entity: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.handshake_id = handshake_id
        self.master_account_name = master_account_name
        self.note = note
        self.create_time = create_time
        self.target_type = target_type
        self.master_account_id = master_account_id
        self.expire_time = expire_time
        self.target_entity = target_entity

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.handshake_id, 'handshake_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.note, 'note')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.target_type, 'target_type')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.target_entity, 'target_entity')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.note is not None:
            result['Note'] = self.note
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        return self


class ListHandshakesForAccountResponseHandshakes(TeaModel):
    def __init__(
        self,
        handshake: List[ListHandshakesForAccountResponseHandshakesHandshake] = None,
    ):
        self.handshake = handshake

    def validate(self):
        self.validate_required(self.handshake, 'handshake')
        if self.handshake:
            for k in self.handshake:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Handshake'] = []
        if self.handshake is not None:
            for k in self.handshake:
                result['Handshake'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.handshake = []
        if m.get('Handshake') is not None:
            for k in m.get('Handshake'):
                temp_model = ListHandshakesForAccountResponseHandshakesHandshake()
                self.handshake.append(temp_model.from_map(k))
        return self


class ListHandshakesForAccountResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        handshakes: ListHandshakesForAccountResponseHandshakes = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.handshakes = handshakes

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.handshakes, 'handshakes')
        if self.handshakes:
            self.handshakes.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.handshakes is not None:
            result['Handshakes'] = self.handshakes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Handshakes') is not None:
            temp_model = ListHandshakesForAccountResponseHandshakes()
            self.handshakes = temp_model.from_map(m['Handshakes'])
        return self


class InviteAccountToResourceDirectoryRequest(TeaModel):
    def __init__(
        self,
        target_entity: str = None,
        target_type: str = None,
        note: str = None,
    ):
        self.target_entity = target_entity
        self.target_type = target_type
        self.note = note

    def validate(self):
        self.validate_required(self.target_entity, 'target_entity')
        self.validate_required(self.target_type, 'target_type')

    def to_map(self):
        result = dict()
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class InviteAccountToResourceDirectoryResponseHandshake(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        handshake_id: str = None,
        master_account_name: str = None,
        note: str = None,
        create_time: str = None,
        target_type: str = None,
        master_account_id: str = None,
        expire_time: str = None,
        target_entity: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.resource_directory_id = resource_directory_id
        self.handshake_id = handshake_id
        self.master_account_name = master_account_name
        self.note = note
        self.create_time = create_time
        self.target_type = target_type
        self.master_account_id = master_account_id
        self.expire_time = expire_time
        self.target_entity = target_entity

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.handshake_id, 'handshake_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.note, 'note')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.target_type, 'target_type')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.target_entity, 'target_entity')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.note is not None:
            result['Note'] = self.note
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        return self


class InviteAccountToResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        handshake: InviteAccountToResourceDirectoryResponseHandshake = None,
    ):
        self.request_id = request_id
        self.handshake = handshake

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.handshake, 'handshake')
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Handshake') is not None:
            temp_model = InviteAccountToResourceDirectoryResponseHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        return self


class AcceptHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        self.handshake_id = handshake_id

    def validate(self):
        self.validate_required(self.handshake_id, 'handshake_id')

    def to_map(self):
        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class AcceptHandshakeResponseHandshake(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
        resource_directory_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        target_entity: str = None,
        target_type: str = None,
        note: str = None,
        status: str = None,
        create_time: str = None,
        modify_time: str = None,
        expire_time: str = None,
    ):
        self.handshake_id = handshake_id
        self.resource_directory_id = resource_directory_id
        self.master_account_id = master_account_id
        self.master_account_name = master_account_name
        self.target_entity = target_entity
        self.target_type = target_type
        self.note = note
        self.status = status
        self.create_time = create_time
        self.modify_time = modify_time
        self.expire_time = expire_time

    def validate(self):
        self.validate_required(self.handshake_id, 'handshake_id')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.master_account_id, 'master_account_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.target_entity, 'target_entity')
        self.validate_required(self.target_type, 'target_type')
        self.validate_required(self.note, 'note')
        self.validate_required(self.status, 'status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.expire_time, 'expire_time')

    def to_map(self):
        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.note is not None:
            result['Note'] = self.note
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class AcceptHandshakeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        handshake: AcceptHandshakeResponseHandshake = None,
    ):
        self.request_id = request_id
        self.handshake = handshake

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.handshake, 'handshake')
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Handshake') is not None:
            temp_model = AcceptHandshakeResponseHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        return self


class UpdateAccountRequest(TeaModel):
    def __init__(
        self,
        new_display_name: str = None,
        account_id: str = None,
    ):
        self.new_display_name = new_display_name
        self.account_id = account_id

    def validate(self):
        self.validate_required(self.new_display_name, 'new_display_name')
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class UpdateAccountResponseAccount(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        join_method: str = None,
        resource_directory_id: str = None,
        type: str = None,
        account_id: str = None,
        display_name: str = None,
        join_time: str = None,
        folder_id: str = None,
        account_name: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.join_method = join_method
        self.resource_directory_id = resource_directory_id
        self.type = type
        self.account_id = account_id
        self.display_name = display_name
        self.join_time = join_time
        self.folder_id = folder_id
        self.account_name = account_name

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.type is not None:
            result['Type'] = self.type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class UpdateAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: UpdateAccountResponseAccount = None,
    ):
        self.request_id = request_id
        self.account = account

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account is not None:
            result['Account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Account') is not None:
            temp_model = UpdateAccountResponseAccount()
            self.account = temp_model.from_map(m['Account'])
        return self


class GetFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        self.folder_id = folder_id

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')

    def to_map(self):
        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class GetFolderResponseFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        self.create_time = create_time
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.parent_folder_id = parent_folder_id

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_name, 'folder_name')
        self.validate_required(self.parent_folder_id, 'parent_folder_id')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class GetFolderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        folder: GetFolderResponseFolder = None,
    ):
        self.request_id = request_id
        self.folder = folder

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.folder, 'folder')
        if self.folder:
            self.folder.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Folder') is not None:
            temp_model = GetFolderResponseFolder()
            self.folder = temp_model.from_map(m['Folder'])
        return self


class ListAccountsForParentRequest(TeaModel):
    def __init__(
        self,
        parent_folder_id: str = None,
        query_keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.parent_folder_id = parent_folder_id
        self.query_keyword = query_keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAccountsForParentResponseAccountsAccount(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        join_method: str = None,
        resource_directory_id: str = None,
        type: str = None,
        account_id: str = None,
        display_name: str = None,
        join_time: str = None,
        folder_id: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.join_method = join_method
        self.resource_directory_id = resource_directory_id
        self.type = type
        self.account_id = account_id
        self.display_name = display_name
        self.join_time = join_time
        self.folder_id = folder_id

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.folder_id, 'folder_id')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.type is not None:
            result['Type'] = self.type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class ListAccountsForParentResponseAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListAccountsForParentResponseAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        self.validate_required(self.account, 'account')
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsForParentResponseAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        accounts: ListAccountsForParentResponseAccounts = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.accounts = accounts

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.accounts, 'accounts')
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Accounts') is not None:
            temp_model = ListAccountsForParentResponseAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        return self


class CreateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        display_name: str = None,
    ):
        self.name = name
        self.display_name = display_name

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        return self


class CreateResourceGroupResponseResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateResourceGroupResponseResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[CreateResourceGroupResponseResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        self.validate_required(self.region_status, 'region_status')
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = CreateResourceGroupResponseResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class CreateResourceGroupResponseResourceGroup(TeaModel):
    def __init__(
        self,
        status: str = None,
        account_id: str = None,
        display_name: str = None,
        id: str = None,
        create_date: str = None,
        name: str = None,
        region_statuses: CreateResourceGroupResponseResourceGroupRegionStatuses = None,
    ):
        self.status = status
        self.account_id = account_id
        self.display_name = display_name
        self.id = id
        self.create_date = create_date
        self.name = name
        self.region_statuses = region_statuses

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region_statuses, 'region_statuses')
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = CreateResourceGroupResponseResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        return self


class CreateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: CreateResourceGroupResponseResourceGroup = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_group, 'resource_group')
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = CreateResourceGroupResponseResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class PromoteResourceAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        email: str = None,
    ):
        self.account_id = account_id
        self.email = email

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.email, 'email')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class PromoteResourceAccountResponseAccount(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        type: str = None,
        status: str = None,
        record_id: str = None,
        modify_time: str = None,
        account_name: str = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.account_id = account_id
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.type = type
        self.status = status
        self.record_id = record_id
        self.modify_time = modify_time
        self.account_name = account_name

    def validate(self):
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.type, 'type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class PromoteResourceAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: PromoteResourceAccountResponseAccount = None,
    ):
        self.request_id = request_id
        self.account = account

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account is not None:
            result['Account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Account') is not None:
            temp_model = PromoteResourceAccountResponseAccount()
            self.account = temp_model.from_map(m['Account'])
        return self


class ListAccountsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAccountsResponseAccountsAccount(TeaModel):
    def __init__(
        self,
        status: str = None,
        modify_time: str = None,
        join_method: str = None,
        resource_directory_id: str = None,
        type: str = None,
        account_id: str = None,
        display_name: str = None,
        join_time: str = None,
        folder_id: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.join_method = join_method
        self.resource_directory_id = resource_directory_id
        self.type = type
        self.account_id = account_id
        self.display_name = display_name
        self.join_time = join_time
        self.folder_id = folder_id

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.folder_id, 'folder_id')

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.type is not None:
            result['Type'] = self.type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class ListAccountsResponseAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListAccountsResponseAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        self.validate_required(self.account, 'account')
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsResponseAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        accounts: ListAccountsResponseAccounts = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.accounts = accounts

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.accounts, 'accounts')
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Accounts') is not None:
            temp_model = ListAccountsResponseAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        return self


class CancelPromoteResourceAccountRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelPromoteResourceAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFolderRequest(TeaModel):
    def __init__(
        self,
        parent_folder_id: str = None,
        folder_name: str = None,
    ):
        self.parent_folder_id = parent_folder_id
        self.folder_name = folder_name

    def validate(self):
        self.validate_required(self.folder_name, 'folder_name')

    def to_map(self):
        result = dict()
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        return self


class CreateFolderResponseFolder(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        parent_folder_id: str = None,
        folder_name: str = None,
        create_time: str = None,
    ):
        self.folder_id = folder_id
        self.parent_folder_id = parent_folder_id
        self.folder_name = folder_name
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.parent_folder_id, 'parent_folder_id')
        self.validate_required(self.folder_name, 'folder_name')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class CreateFolderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        folder: CreateFolderResponseFolder = None,
    ):
        self.request_id = request_id
        self.folder = folder

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.folder, 'folder')
        if self.folder:
            self.folder.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Folder') is not None:
            temp_model = CreateFolderResponseFolder()
            self.folder = temp_model.from_map(m['Folder'])
        return self


class DeleteFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        self.folder_id = folder_id

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')

    def to_map(self):
        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class DeleteFolderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetAccountResponseAccount(TeaModel):
    def __init__(
        self,
        identity_information: str = None,
        status: str = None,
        modify_time: str = None,
        join_method: str = None,
        resource_directory_id: str = None,
        type: str = None,
        account_id: str = None,
        display_name: str = None,
        join_time: str = None,
        folder_id: str = None,
        account_name: str = None,
    ):
        self.identity_information = identity_information
        self.status = status
        self.modify_time = modify_time
        self.join_method = join_method
        self.resource_directory_id = resource_directory_id
        self.type = type
        self.account_id = account_id
        self.display_name = display_name
        self.join_time = join_time
        self.folder_id = folder_id
        self.account_name = account_name

    def validate(self):
        self.validate_required(self.identity_information, 'identity_information')
        self.validate_required(self.status, 'status')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = dict()
        if self.identity_information is not None:
            result['IdentityInformation'] = self.identity_information
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.type is not None:
            result['Type'] = self.type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityInformation') is not None:
            self.identity_information = m.get('IdentityInformation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: GetAccountResponseAccount = None,
    ):
        self.request_id = request_id
        self.account = account

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account is not None:
            result['Account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Account') is not None:
            temp_model = GetAccountResponseAccount()
            self.account = temp_model.from_map(m['Account'])
        return self


class GetResourceDirectoryRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetResourceDirectoryResponseResourceDirectory(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        master_account_name: str = None,
        create_time: str = None,
        root_folder_id: str = None,
        master_account_id: str = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.master_account_name = master_account_name
        self.create_time = create_time
        self.root_folder_id = root_folder_id
        self.master_account_id = master_account_id

    def validate(self):
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.master_account_name, 'master_account_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.root_folder_id, 'root_folder_id')
        self.validate_required(self.master_account_id, 'master_account_id')

    def to_map(self):
        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        return self


class GetResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: GetResourceDirectoryResponseResourceDirectory = None,
    ):
        self.request_id = request_id
        self.resource_directory = resource_directory

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_directory, 'resource_directory')
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = GetResourceDirectoryResponseResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class UpdateFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        new_folder_name: str = None,
    ):
        self.folder_id = folder_id
        self.new_folder_name = new_folder_name

    def validate(self):
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.new_folder_name, 'new_folder_name')

    def to_map(self):
        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.new_folder_name is not None:
            result['NewFolderName'] = self.new_folder_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('NewFolderName') is not None:
            self.new_folder_name = m.get('NewFolderName')
        return self


class UpdateFolderResponseFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        self.create_time = create_time
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.parent_folder_id = parent_folder_id

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_name, 'folder_name')
        self.validate_required(self.parent_folder_id, 'parent_folder_id')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class UpdateFolderResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        folder: UpdateFolderResponseFolder = None,
    ):
        self.request_id = request_id
        self.folder = folder

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.folder, 'folder')
        if self.folder:
            self.folder.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Folder') is not None:
            temp_model = UpdateFolderResponseFolder()
            self.folder = temp_model.from_map(m['Folder'])
        return self


class MoveAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        destination_folder_id: str = None,
    ):
        self.account_id = account_id
        self.destination_folder_id = destination_folder_id

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.destination_folder_id, 'destination_folder_id')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.destination_folder_id is not None:
            result['DestinationFolderId'] = self.destination_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DestinationFolderId') is not None:
            self.destination_folder_id = m.get('DestinationFolderId')
        return self


class MoveAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAncestorsRequest(TeaModel):
    def __init__(
        self,
        child_id: str = None,
    ):
        self.child_id = child_id

    def validate(self):
        self.validate_required(self.child_id, 'child_id')

    def to_map(self):
        result = dict()
        if self.child_id is not None:
            result['ChildId'] = self.child_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildId') is not None:
            self.child_id = m.get('ChildId')
        return self


class ListAncestorsResponseFoldersFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
    ):
        self.create_time = create_time
        self.folder_id = folder_id
        self.folder_name = folder_name

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_name, 'folder_name')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        return self


class ListAncestorsResponseFolders(TeaModel):
    def __init__(
        self,
        folder: List[ListAncestorsResponseFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        self.validate_required(self.folder, 'folder')
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListAncestorsResponseFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListAncestorsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        folders: ListAncestorsResponseFolders = None,
    ):
        self.request_id = request_id
        self.folders = folders

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.folders, 'folders')
        if self.folders:
            self.folders.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Folders') is not None:
            temp_model = ListAncestorsResponseFolders()
            self.folders = temp_model.from_map(m['Folders'])
        return self


class ResendCreateCloudAccountEmailRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendCreateCloudAccountEmailResponseAccount(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        type: str = None,
        status: str = None,
        record_id: str = None,
        modify_time: str = None,
        account_name: str = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.account_id = account_id
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.type = type
        self.status = status
        self.record_id = record_id
        self.modify_time = modify_time
        self.account_name = account_name

    def validate(self):
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.type, 'type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class ResendCreateCloudAccountEmailResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: ResendCreateCloudAccountEmailResponseAccount = None,
    ):
        self.request_id = request_id
        self.account = account

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account is not None:
            result['Account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Account') is not None:
            temp_model = ResendCreateCloudAccountEmailResponseAccount()
            self.account = temp_model.from_map(m['Account'])
        return self


class GetPayerForAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetPayerForAccountResponse(TeaModel):
    def __init__(
        self,
        payer_account_name: str = None,
        request_id: str = None,
        payer_account_id: str = None,
    ):
        self.payer_account_name = payer_account_name
        self.request_id = request_id
        self.payer_account_id = payer_account_id

    def validate(self):
        self.validate_required(self.payer_account_name, 'payer_account_name')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.payer_account_id, 'payer_account_id')

    def to_map(self):
        result = dict()
        if self.payer_account_name is not None:
            result['PayerAccountName'] = self.payer_account_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayerAccountName') is not None:
            self.payer_account_name = m.get('PayerAccountName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        return self


class ResendPromoteResourceAccountEmailRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendPromoteResourceAccountEmailResponseAccount(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        type: str = None,
        status: str = None,
        record_id: str = None,
        modify_time: str = None,
        account_name: str = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.account_id = account_id
        self.display_name = display_name
        self.folder_id = folder_id
        self.join_method = join_method
        self.join_time = join_time
        self.type = type
        self.status = status
        self.record_id = record_id
        self.modify_time = modify_time
        self.account_name = account_name

    def validate(self):
        self.validate_required(self.resource_directory_id, 'resource_directory_id')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.join_method, 'join_method')
        self.validate_required(self.join_time, 'join_time')
        self.validate_required(self.type, 'type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class ResendPromoteResourceAccountEmailResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: ResendPromoteResourceAccountEmailResponseAccount = None,
    ):
        self.request_id = request_id
        self.account = account

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account is not None:
            result['Account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Account') is not None:
            temp_model = ResendPromoteResourceAccountEmailResponseAccount()
            self.account = temp_model.from_map(m['Account'])
        return self


class ListFoldersForParentRequest(TeaModel):
    def __init__(
        self,
        parent_folder_id: str = None,
        query_keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.parent_folder_id = parent_folder_id
        self.query_keyword = query_keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFoldersForParentResponseFoldersFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
    ):
        self.create_time = create_time
        self.folder_id = folder_id
        self.folder_name = folder_name

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.folder_id, 'folder_id')
        self.validate_required(self.folder_name, 'folder_name')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        return self


class ListFoldersForParentResponseFolders(TeaModel):
    def __init__(
        self,
        folder: List[ListFoldersForParentResponseFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        self.validate_required(self.folder, 'folder')
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListFoldersForParentResponseFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListFoldersForParentResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        folders: ListFoldersForParentResponseFolders = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.folders = folders

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.folders, 'folders')
        if self.folders:
            self.folders.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Folders') is not None:
            temp_model = ListFoldersForParentResponseFolders()
            self.folders = temp_model.from_map(m['Folders'])
        return self


class RemoveCloudAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        self.account_id = account_id

    def validate(self):
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class RemoveCloudAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelCreateCloudAccountRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelCreateCloudAccountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


