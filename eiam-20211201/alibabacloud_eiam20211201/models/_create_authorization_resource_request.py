# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateAuthorizationResourceRequest(DaraModel):
    def __init__(
        self,
        authorization_resource_entity_id: str = None,
        authorization_resource_entity_type: str = None,
        authorization_rule_id: str = None,
        client_token: str = None,
        condition: main_models.CreateAuthorizationResourceRequestCondition = None,
        instance_id: str = None,
    ):
        # The ID of the resource entity associated with the authorization resource.
        # 
        # This parameter is required.
        self.authorization_resource_entity_id = authorization_resource_entity_id
        # The type of the resource entity associated with the authorization resource. Valid values:
        # 
        # - cloud_account_role: cloud role
        # 
        # This parameter is required.
        self.authorization_resource_entity_type = authorization_resource_entity_type
        # The authorization rule ID.
        # 
        # This parameter is required.
        self.authorization_rule_id = authorization_rule_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate a parameter value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see References [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The effective condition.
        self.condition = condition
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_resource_entity_id is not None:
            result['AuthorizationResourceEntityId'] = self.authorization_resource_entity_id

        if self.authorization_resource_entity_type is not None:
            result['AuthorizationResourceEntityType'] = self.authorization_resource_entity_type

        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.condition is not None:
            result['Condition'] = self.condition.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResourceEntityId') is not None:
            self.authorization_resource_entity_id = m.get('AuthorizationResourceEntityId')

        if m.get('AuthorizationResourceEntityType') is not None:
            self.authorization_resource_entity_type = m.get('AuthorizationResourceEntityType')

        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Condition') is not None:
            temp_model = main_models.CreateAuthorizationResourceRequestCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class CreateAuthorizationResourceRequestCondition(DaraModel):
    def __init__(
        self,
        credential_condition: main_models.CreateAuthorizationResourceRequestConditionCredentialCondition = None,
    ):
        # The effective condition when used as a credential.
        self.credential_condition = credential_condition

    def validate(self):
        if self.credential_condition:
            self.credential_condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_condition is not None:
            result['CredentialCondition'] = self.credential_condition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialCondition') is not None:
            temp_model = main_models.CreateAuthorizationResourceRequestConditionCredentialCondition()
            self.credential_condition = temp_model.from_map(m.get('CredentialCondition'))

        return self

class CreateAuthorizationResourceRequestConditionCredentialCondition(DaraModel):
    def __init__(
        self,
        allow_same_name_identity: bool = None,
    ):
        # Specifies whether same-name identity accounts are supported.
        self.allow_same_name_identity = allow_same_name_identity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_same_name_identity is not None:
            result['AllowSameNameIdentity'] = self.allow_same_name_identity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSameNameIdentity') is not None:
            self.allow_same_name_identity = m.get('AllowSameNameIdentity')

        return self

