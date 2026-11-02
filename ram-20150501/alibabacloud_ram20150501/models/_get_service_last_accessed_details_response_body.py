# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class GetServiceLastAccessedDetailsResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        job_completion_time: str = None,
        job_creation_time: str = None,
        job_error: main_models.GetServiceLastAccessedDetailsResponseBodyJobError = None,
        job_status: str = None,
        job_type: str = None,
        marker: str = None,
        request_id: str = None,
        services_last_accessed: List[main_models.GetServiceLastAccessedDetailsResponseBodyServicesLastAccessed] = None,
    ):
        # Specifies whether the returned results are truncated. Valid values:
        # - true
        # - false
        self.is_truncated = is_truncated
        # The time when the task was completed.
        self.job_completion_time = job_completion_time
        # The time when the task was created.
        self.job_creation_time = job_creation_time
        # The error message returned when the task fails. This parameter is not returned when the task is completed.
        self.job_error = job_error
        # The status of the task. Valid values:
        # 
        # - IN_PROGRESS: The task is being processed.
        # - COMPLETED: The task is completed.
        # - FAILED: The task failed.
        self.job_status = job_status
        # The granularity of the permission audit report. Valid values:
        # - SERVICE_LEVEL: Analyzes the recent access information at the RAM code granularity for cloud services supported by permission audit.
        # - ACTION_LEVEL: Analyzes the recent access information at the RAM action granularity for operation-level cloud services supported by permission audit.
        self.job_type = job_type
        # This parameter is returned only when IsTruncated is set to true. If true is returned, you must call this operation again and use Marker to obtain the truncated content.
        # 
        # This parameter is required.
        self.marker = marker
        # The ID of the request.
        self.request_id = request_id
        # The list of last access information for cloud services. This list is empty if the RAM identity does not have access permissions for any cloud service.
        self.services_last_accessed = services_last_accessed

    def validate(self):
        if self.job_error:
            self.job_error.validate()
        if self.services_last_accessed:
            for v1 in self.services_last_accessed:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.job_completion_time is not None:
            result['JobCompletionTime'] = self.job_completion_time

        if self.job_creation_time is not None:
            result['JobCreationTime'] = self.job_creation_time

        if self.job_error is not None:
            result['JobError'] = self.job_error.to_map()

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServicesLastAccessed'] = []
        if self.services_last_accessed is not None:
            for k1 in self.services_last_accessed:
                result['ServicesLastAccessed'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('JobCompletionTime') is not None:
            self.job_completion_time = m.get('JobCompletionTime')

        if m.get('JobCreationTime') is not None:
            self.job_creation_time = m.get('JobCreationTime')

        if m.get('JobError') is not None:
            temp_model = main_models.GetServiceLastAccessedDetailsResponseBodyJobError()
            self.job_error = temp_model.from_map(m.get('JobError'))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.services_last_accessed = []
        if m.get('ServicesLastAccessed') is not None:
            for k1 in m.get('ServicesLastAccessed'):
                temp_model = main_models.GetServiceLastAccessedDetailsResponseBodyServicesLastAccessed()
                self.services_last_accessed.append(temp_model.from_map(k1))

        return self

class GetServiceLastAccessedDetailsResponseBodyServicesLastAccessed(DaraModel):
    def __init__(
        self,
        grant_policies: List[main_models.GetServiceLastAccessedDetailsResponseBodyServicesLastAccessedGrantPolicies] = None,
        last_authenticated: str = None,
        last_authenticated_entity: str = None,
        ramcode: str = None,
        service_codes: List[str] = None,
        total_authenticated_entities: int = None,
        tracked_actions_last_accessed: List[main_models.GetServiceLastAccessedDetailsResponseBodyServicesLastAccessedTrackedActionsLastAccessed] = None,
    ):
        # The list of access policies that grant permission to access the cloud service.
        self.grant_policies = grant_policies
        # The time when the analyzed RAM identity last attempted to access the service.
        self.last_authenticated = last_authenticated
        # The ARN of the analyzed RAM identity.
        self.last_authenticated_entity = last_authenticated_entity
        # The RAM code of the cloud service.
        self.ramcode = ramcode
        # The list of cloud service codes.
        self.service_codes = service_codes
        # The number of identities that attempted to access the service.
        self.total_authenticated_entities = total_authenticated_entities
        # The list of operation-level access information. This information is returned when the granularity of the created permission audit task is ACTION_LEVEL.
        self.tracked_actions_last_accessed = tracked_actions_last_accessed

    def validate(self):
        if self.grant_policies:
            for v1 in self.grant_policies:
                 if v1:
                    v1.validate()
        if self.tracked_actions_last_accessed:
            for v1 in self.tracked_actions_last_accessed:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GrantPolicies'] = []
        if self.grant_policies is not None:
            for k1 in self.grant_policies:
                result['GrantPolicies'].append(k1.to_map() if k1 else None)

        if self.last_authenticated is not None:
            result['LastAuthenticated'] = self.last_authenticated

        if self.last_authenticated_entity is not None:
            result['LastAuthenticatedEntity'] = self.last_authenticated_entity

        if self.ramcode is not None:
            result['RAMCode'] = self.ramcode

        if self.service_codes is not None:
            result['ServiceCodes'] = self.service_codes

        if self.total_authenticated_entities is not None:
            result['TotalAuthenticatedEntities'] = self.total_authenticated_entities

        result['TrackedActionsLastAccessed'] = []
        if self.tracked_actions_last_accessed is not None:
            for k1 in self.tracked_actions_last_accessed:
                result['TrackedActionsLastAccessed'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_policies = []
        if m.get('GrantPolicies') is not None:
            for k1 in m.get('GrantPolicies'):
                temp_model = main_models.GetServiceLastAccessedDetailsResponseBodyServicesLastAccessedGrantPolicies()
                self.grant_policies.append(temp_model.from_map(k1))

        if m.get('LastAuthenticated') is not None:
            self.last_authenticated = m.get('LastAuthenticated')

        if m.get('LastAuthenticatedEntity') is not None:
            self.last_authenticated_entity = m.get('LastAuthenticatedEntity')

        if m.get('RAMCode') is not None:
            self.ramcode = m.get('RAMCode')

        if m.get('ServiceCodes') is not None:
            self.service_codes = m.get('ServiceCodes')

        if m.get('TotalAuthenticatedEntities') is not None:
            self.total_authenticated_entities = m.get('TotalAuthenticatedEntities')

        self.tracked_actions_last_accessed = []
        if m.get('TrackedActionsLastAccessed') is not None:
            for k1 in m.get('TrackedActionsLastAccessed'):
                temp_model = main_models.GetServiceLastAccessedDetailsResponseBodyServicesLastAccessedTrackedActionsLastAccessed()
                self.tracked_actions_last_accessed.append(temp_model.from_map(k1))

        return self

class GetServiceLastAccessedDetailsResponseBodyServicesLastAccessedTrackedActionsLastAccessed(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        last_accessed_entity: str = None,
        last_accessed_time: str = None,
        service_codes: List[str] = None,
    ):
        # The action.
        self.action_name = action_name
        # The ARN of the analyzed RAM identity.
        self.last_accessed_entity = last_accessed_entity
        # The time when the analyzed RAM identity last attempted to perform the action.
        self.last_accessed_time = last_accessed_time
        # The list of cloud service codes.
        self.service_codes = service_codes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.last_accessed_entity is not None:
            result['LastAccessedEntity'] = self.last_accessed_entity

        if self.last_accessed_time is not None:
            result['LastAccessedTime'] = self.last_accessed_time

        if self.service_codes is not None:
            result['ServiceCodes'] = self.service_codes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('LastAccessedEntity') is not None:
            self.last_accessed_entity = m.get('LastAccessedEntity')

        if m.get('LastAccessedTime') is not None:
            self.last_accessed_time = m.get('LastAccessedTime')

        if m.get('ServiceCodes') is not None:
            self.service_codes = m.get('ServiceCodes')

        return self

class GetServiceLastAccessedDetailsResponseBodyServicesLastAccessedGrantPolicies(DaraModel):
    def __init__(
        self,
        attached_entity: str = None,
        attached_scope: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The ARN of the entity to which the access policy grants permission. Valid values:
        # 
        # - RAM user: acs:ram::<account_id>:user/<user_name>
        # - RAM role: acs:ram::<account_id>:role/<role_name>
        # - RAM user group: acs:ram::<account_id>:group/<group_name>
        self.attached_entity = attached_entity
        # The authorization scope of the access policy. Valid values:
        # - Account ID (format: 123459***): account-level authorization
        # - Resource group ID (format: rg-123***): resource group-level authorization
        self.attached_scope = attached_scope
        # The name of the access policy that grants permission.
        self.policy_name = policy_name
        # The type of the access policy. Valid values:
        # - System: system policy
        # - Custom: custom policy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_entity is not None:
            result['AttachedEntity'] = self.attached_entity

        if self.attached_scope is not None:
            result['AttachedScope'] = self.attached_scope

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedEntity') is not None:
            self.attached_entity = m.get('AttachedEntity')

        if m.get('AttachedScope') is not None:
            self.attached_scope = m.get('AttachedScope')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

class GetServiceLastAccessedDetailsResponseBodyJobError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

