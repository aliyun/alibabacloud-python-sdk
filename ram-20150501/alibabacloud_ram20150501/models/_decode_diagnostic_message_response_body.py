# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class DecodeDiagnosticMessageResponseBody(DaraModel):
    def __init__(
        self,
        decoded_diagnostic_message: main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessage = None,
        request_id: str = None,
    ):
        # The decoded diagnostic information.
        self.decoded_diagnostic_message = decoded_diagnostic_message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.decoded_diagnostic_message:
            self.decoded_diagnostic_message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.decoded_diagnostic_message is not None:
            result['DecodedDiagnosticMessage'] = self.decoded_diagnostic_message.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DecodedDiagnosticMessage') is not None:
            temp_model = main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessage()
            self.decoded_diagnostic_message = temp_model.from_map(m.get('DecodedDiagnosticMessage'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessage(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_conditions: List[main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageAuthConditions] = None,
        auth_principal: main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageAuthPrincipal = None,
        auth_resource: str = None,
        explicit_deny: bool = None,
        matched_policies: List[main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageMatchedPolicies] = None,
        no_permission_policy_type: str = None,
    ):
        # The operation that is used for authentication in the request.
        self.auth_action = auth_action
        # The conditions that are used for authentication in the request.
        self.auth_conditions = auth_conditions
        # The operator that is used for authentication in the request.
        self.auth_principal = auth_principal
        # The resource that is used for authentication in the request.
        self.auth_resource = auth_resource
        # Indicates whether the access denied error is caused by an explicit deny.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.explicit_deny = explicit_deny
        # The policies that are matched.
        self.matched_policies = matched_policies
        # The type of the policy that causes the access denied error.
        # 
        # Valid values:
        # 
        # *   AssumeRolePolicy: role-specific trust policy
        # *   ControlPolicy: control policy
        # *   AccountLevelIdentityBasedPolicy: identity-based policy at the account level
        # *   ResourceGroupLevelIdentityBasedPolicy: identity-based policy at the resource group level
        # *   SessionPolicy: session policy
        self.no_permission_policy_type = no_permission_policy_type

    def validate(self):
        if self.auth_conditions:
            for v1 in self.auth_conditions:
                 if v1:
                    v1.validate()
        if self.auth_principal:
            self.auth_principal.validate()
        if self.matched_policies:
            for v1 in self.matched_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        result['AuthConditions'] = []
        if self.auth_conditions is not None:
            for k1 in self.auth_conditions:
                result['AuthConditions'].append(k1.to_map() if k1 else None)

        if self.auth_principal is not None:
            result['AuthPrincipal'] = self.auth_principal.to_map()

        if self.auth_resource is not None:
            result['AuthResource'] = self.auth_resource

        if self.explicit_deny is not None:
            result['ExplicitDeny'] = self.explicit_deny

        result['MatchedPolicies'] = []
        if self.matched_policies is not None:
            for k1 in self.matched_policies:
                result['MatchedPolicies'].append(k1.to_map() if k1 else None)

        if self.no_permission_policy_type is not None:
            result['NoPermissionPolicyType'] = self.no_permission_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        self.auth_conditions = []
        if m.get('AuthConditions') is not None:
            for k1 in m.get('AuthConditions'):
                temp_model = main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageAuthConditions()
                self.auth_conditions.append(temp_model.from_map(k1))

        if m.get('AuthPrincipal') is not None:
            temp_model = main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageAuthPrincipal()
            self.auth_principal = temp_model.from_map(m.get('AuthPrincipal'))

        if m.get('AuthResource') is not None:
            self.auth_resource = m.get('AuthResource')

        if m.get('ExplicitDeny') is not None:
            self.explicit_deny = m.get('ExplicitDeny')

        self.matched_policies = []
        if m.get('MatchedPolicies') is not None:
            for k1 in m.get('MatchedPolicies'):
                temp_model = main_models.DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageMatchedPolicies()
                self.matched_policies.append(temp_model.from_map(k1))

        if m.get('NoPermissionPolicyType') is not None:
            self.no_permission_policy_type = m.get('NoPermissionPolicyType')

        return self

class DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageMatchedPolicies(DaraModel):
    def __init__(
        self,
        attached_entity_type: str = None,
        attached_scope: str = None,
        effect: str = None,
        policy_identifier: str = None,
        policy_type: str = None,
        policy_version: str = None,
    ):
        # The type of the entity to which the policy is attached.
        # 
        # Valid values:
        # 
        # *   RamUser: RAM user
        # *   RamRole: RAM role
        # *   ResourceDirectoryTarget: entity in a resource directory
        # *   RamGroup: RAM user group
        self.attached_entity_type = attached_entity_type
        # The authorization scope of the policy.
        # 
        # Valid values:
        # 
        # *   Account: Alibaba Cloud account
        # *   Folder: folder in the resource directory
        # *   ResourceGroup: resource group
        self.attached_scope = attached_scope
        # The effect of the policy.
        # 
        # Valid values:
        # 
        # *   Deny
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Allow
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.effect = effect
        # The identifier of the policy.
        # 
        # *   Control policy: the ID of the control policy
        # *   RAM policy: the name of the policy
        self.policy_identifier = policy_identifier
        # The type of the policy.
        # 
        # Valid values:
        # *   Custom: custom policy
        # *   System: system policy
        self.policy_type = policy_type
        # The version number of the policy.
        # 
        # > Only custom policies have version numbers.
        self.policy_version = policy_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_entity_type is not None:
            result['AttachedEntityType'] = self.attached_entity_type

        if self.attached_scope is not None:
            result['AttachedScope'] = self.attached_scope

        if self.effect is not None:
            result['Effect'] = self.effect

        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedEntityType') is not None:
            self.attached_entity_type = m.get('AttachedEntityType')

        if m.get('AttachedScope') is not None:
            self.attached_scope = m.get('AttachedScope')

        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        return self

class DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageAuthPrincipal(DaraModel):
    def __init__(
        self,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
    ):
        # The identity.
        # 
        # *   If the operator is a RAM user, the ID of the user is displayed.
        # *   If the operator is a RAM role, the name and session name of the role are displayed. Example: RoleName:RoleSessionName.
        # *   If the operator is an SSO federated identity, the type and name of the identity provider (IdP) are displayed. Example: saml-provider/AzureAD.
        self.auth_principal_display_name = auth_principal_display_name
        # The ID of the Alibaba Cloud account to which the identity belongs.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type that is used for authentication in the request.
        # 
        # Valid values:
        # 
        # *   SubUser: RAM user
        # *   AssumedRoleUser: RAM role
        # *   Federated: SSO federated identity
        self.auth_principal_type = auth_principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        return self

class DecodeDiagnosticMessageResponseBodyDecodedDiagnosticMessageAuthConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_values: List[str] = None,
    ):
        # The key of the condition.
        self.condition_key = condition_key
        # The values that correspond to the key.
        self.condition_values = condition_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_values is not None:
            result['ConditionValues'] = self.condition_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionValues') is not None:
            self.condition_values = m.get('ConditionValues')

        return self

