# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetConditionalAccessPolicyResponseBody(DaraModel):
    def __init__(
        self,
        conditional_access_policy: main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicy = None,
        request_id: str = None,
    ):
        # Details of the conditional access policy
        self.conditional_access_policy = conditional_access_policy
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.conditional_access_policy:
            self.conditional_access_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditional_access_policy is not None:
            result['ConditionalAccessPolicy'] = self.conditional_access_policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionalAccessPolicy') is not None:
            temp_model = main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicy()
            self.conditional_access_policy = temp_model.from_map(m.get('ConditionalAccessPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConditionalAccessPolicyResponseBodyConditionalAccessPolicy(DaraModel):
    def __init__(
        self,
        conditional_access_policy_id: str = None,
        conditional_access_policy_name: str = None,
        conditional_access_policy_type: str = None,
        conditions_config: main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfig = None,
        create_time: int = None,
        decision_config: main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyDecisionConfig = None,
        decision_type: str = None,
        description: str = None,
        evaluate_at: str = None,
        instance_id: str = None,
        last_updated_time: int = None,
        priority: int = None,
        status: str = None,
    ):
        # Conditional Access Policy ID
        self.conditional_access_policy_id = conditional_access_policy_id
        # Conditional Access Policy Name
        self.conditional_access_policy_name = conditional_access_policy_name
        # Type of the conditional access policy
        self.conditional_access_policy_type = conditional_access_policy_type
        # Conditional access policy content
        self.conditions_config = conditions_config
        # Creation time
        self.create_time = create_time
        # Action of the conditional access policy
        self.decision_config = decision_config
        # Execution type of the conditional access policy
        self.decision_type = decision_type
        # Description of the conditional access policy
        self.description = description
        # Execution point of the conditional access policy
        self.evaluate_at = evaluate_at
        # Instance ID
        self.instance_id = instance_id
        # Last updated time
        self.last_updated_time = last_updated_time
        # Priority
        self.priority = priority
        # Enable or disable status of the conditional access policy
        self.status = status

    def validate(self):
        if self.conditions_config:
            self.conditions_config.validate()
        if self.decision_config:
            self.decision_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditional_access_policy_id is not None:
            result['ConditionalAccessPolicyId'] = self.conditional_access_policy_id

        if self.conditional_access_policy_name is not None:
            result['ConditionalAccessPolicyName'] = self.conditional_access_policy_name

        if self.conditional_access_policy_type is not None:
            result['ConditionalAccessPolicyType'] = self.conditional_access_policy_type

        if self.conditions_config is not None:
            result['ConditionsConfig'] = self.conditions_config.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.decision_config is not None:
            result['DecisionConfig'] = self.decision_config.to_map()

        if self.decision_type is not None:
            result['DecisionType'] = self.decision_type

        if self.description is not None:
            result['Description'] = self.description

        if self.evaluate_at is not None:
            result['EvaluateAt'] = self.evaluate_at

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_updated_time is not None:
            result['LastUpdatedTime'] = self.last_updated_time

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionalAccessPolicyId') is not None:
            self.conditional_access_policy_id = m.get('ConditionalAccessPolicyId')

        if m.get('ConditionalAccessPolicyName') is not None:
            self.conditional_access_policy_name = m.get('ConditionalAccessPolicyName')

        if m.get('ConditionalAccessPolicyType') is not None:
            self.conditional_access_policy_type = m.get('ConditionalAccessPolicyType')

        if m.get('ConditionsConfig') is not None:
            temp_model = main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfig()
            self.conditions_config = temp_model.from_map(m.get('ConditionsConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DecisionConfig') is not None:
            temp_model = main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyDecisionConfig()
            self.decision_config = temp_model.from_map(m.get('DecisionConfig'))

        if m.get('DecisionType') is not None:
            self.decision_type = m.get('DecisionType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EvaluateAt') is not None:
            self.evaluate_at = m.get('EvaluateAt')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUpdatedTime') is not None:
            self.last_updated_time = m.get('LastUpdatedTime')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyDecisionConfig(DaraModel):
    def __init__(
        self,
        active_session_reuse_status: str = None,
        effect: str = None,
        mfa_authentication_interval_seconds: int = None,
        mfa_authentication_methods: List[str] = None,
        mfa_type: str = None,
    ):
        # Whether to enable session reuse
        self.active_session_reuse_status = active_session_reuse_status
        # Decision action of the conditional access policy
        self.effect = effect
        # Re-authentication interval (in seconds) for the conditional access policy
        self.mfa_authentication_interval_seconds = mfa_authentication_interval_seconds
        # Allowed MFA types for the conditional access policy
        self.mfa_authentication_methods = mfa_authentication_methods
        # MFA authentication type of the conditional access policy
        self.mfa_type = mfa_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_session_reuse_status is not None:
            result['ActiveSessionReuseStatus'] = self.active_session_reuse_status

        if self.effect is not None:
            result['Effect'] = self.effect

        if self.mfa_authentication_interval_seconds is not None:
            result['MfaAuthenticationIntervalSeconds'] = self.mfa_authentication_interval_seconds

        if self.mfa_authentication_methods is not None:
            result['MfaAuthenticationMethods'] = self.mfa_authentication_methods

        if self.mfa_type is not None:
            result['MfaType'] = self.mfa_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessionReuseStatus') is not None:
            self.active_session_reuse_status = m.get('ActiveSessionReuseStatus')

        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('MfaAuthenticationIntervalSeconds') is not None:
            self.mfa_authentication_interval_seconds = m.get('MfaAuthenticationIntervalSeconds')

        if m.get('MfaAuthenticationMethods') is not None:
            self.mfa_authentication_methods = m.get('MfaAuthenticationMethods')

        if m.get('MfaType') is not None:
            self.mfa_type = m.get('MfaType')

        return self

class GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfig(DaraModel):
    def __init__(
        self,
        applications: main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigApplications = None,
        network_zones: main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigNetworkZones = None,
        users: main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigUsers = None,
    ):
        # Target applications of the conditional access policy
        self.applications = applications
        # Network zones for the conditional access policy
        self.network_zones = network_zones
        # Target users of the conditional access policy
        self.users = users

    def validate(self):
        if self.applications:
            self.applications.validate()
        if self.network_zones:
            self.network_zones.validate()
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()

        if self.network_zones is not None:
            result['NetworkZones'] = self.network_zones.to_map()

        if self.users is not None:
            result['Users'] = self.users.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applications') is not None:
            temp_model = main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigApplications()
            self.applications = temp_model.from_map(m.get('Applications'))

        if m.get('NetworkZones') is not None:
            temp_model = main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigNetworkZones()
            self.network_zones = temp_model.from_map(m.get('NetworkZones'))

        if m.get('Users') is not None:
            temp_model = main_models.GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigUsers()
            self.users = temp_model.from_map(m.get('Users'))

        return self

class GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigUsers(DaraModel):
    def __init__(
        self,
        exclude_groups: List[str] = None,
        exclude_organizational_units: List[str] = None,
        exclude_users: List[str] = None,
        include_groups: List[str] = None,
        include_organizational_units: List[str] = None,
        include_users: List[str] = None,
    ):
        # Excluded user groups
        self.exclude_groups = exclude_groups
        # Excluded organizations
        self.exclude_organizational_units = exclude_organizational_units
        # Excluded users
        self.exclude_users = exclude_users
        # Selected user groups
        self.include_groups = include_groups
        # Included organizations
        self.include_organizational_units = include_organizational_units
        # Selected users
        self.include_users = include_users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_groups is not None:
            result['ExcludeGroups'] = self.exclude_groups

        if self.exclude_organizational_units is not None:
            result['ExcludeOrganizationalUnits'] = self.exclude_organizational_units

        if self.exclude_users is not None:
            result['ExcludeUsers'] = self.exclude_users

        if self.include_groups is not None:
            result['IncludeGroups'] = self.include_groups

        if self.include_organizational_units is not None:
            result['IncludeOrganizationalUnits'] = self.include_organizational_units

        if self.include_users is not None:
            result['IncludeUsers'] = self.include_users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeGroups') is not None:
            self.exclude_groups = m.get('ExcludeGroups')

        if m.get('ExcludeOrganizationalUnits') is not None:
            self.exclude_organizational_units = m.get('ExcludeOrganizationalUnits')

        if m.get('ExcludeUsers') is not None:
            self.exclude_users = m.get('ExcludeUsers')

        if m.get('IncludeGroups') is not None:
            self.include_groups = m.get('IncludeGroups')

        if m.get('IncludeOrganizationalUnits') is not None:
            self.include_organizational_units = m.get('IncludeOrganizationalUnits')

        if m.get('IncludeUsers') is not None:
            self.include_users = m.get('IncludeUsers')

        return self

class GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigNetworkZones(DaraModel):
    def __init__(
        self,
        exclude_network_zones: List[str] = None,
        include_network_zones: List[str] = None,
    ):
        # Excluded network zones
        self.exclude_network_zones = exclude_network_zones
        # Included network zones
        self.include_network_zones = include_network_zones

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_network_zones is not None:
            result['ExcludeNetworkZones'] = self.exclude_network_zones

        if self.include_network_zones is not None:
            result['IncludeNetworkZones'] = self.include_network_zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeNetworkZones') is not None:
            self.exclude_network_zones = m.get('ExcludeNetworkZones')

        if m.get('IncludeNetworkZones') is not None:
            self.include_network_zones = m.get('IncludeNetworkZones')

        return self

class GetConditionalAccessPolicyResponseBodyConditionalAccessPolicyConditionsConfigApplications(DaraModel):
    def __init__(
        self,
        exclude_applications: List[str] = None,
        include_applications: List[str] = None,
    ):
        # Excluded applications
        self.exclude_applications = exclude_applications
        # Selected applications
        self.include_applications = include_applications

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_applications is not None:
            result['ExcludeApplications'] = self.exclude_applications

        if self.include_applications is not None:
            result['IncludeApplications'] = self.include_applications

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeApplications') is not None:
            self.exclude_applications = m.get('ExcludeApplications')

        if m.get('IncludeApplications') is not None:
            self.include_applications = m.get('IncludeApplications')

        return self

