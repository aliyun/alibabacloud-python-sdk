# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetAuthorizationResourceResponseBody(DaraModel):
    def __init__(
        self,
        authorization_resource: main_models.GetAuthorizationResourceResponseBodyAuthorizationResource = None,
        request_id: str = None,
    ):
        # The authorization resource.
        self.authorization_resource = authorization_resource
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.authorization_resource:
            self.authorization_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_resource is not None:
            result['AuthorizationResource'] = self.authorization_resource.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResource') is not None:
            temp_model = main_models.GetAuthorizationResourceResponseBodyAuthorizationResource()
            self.authorization_resource = temp_model.from_map(m.get('AuthorizationResource'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAuthorizationResourceResponseBodyAuthorizationResource(DaraModel):
    def __init__(
        self,
        authorization_resource_entity_id: str = None,
        authorization_resource_entity_type: str = None,
        authorization_resource_id: str = None,
        authorization_rule_id: str = None,
        cloud_account_id: str = None,
        condition: main_models.GetAuthorizationResourceResponseBodyAuthorizationResourceCondition = None,
        create_time: int = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # The resource entity ID associated with the authorization resource.
        self.authorization_resource_entity_id = authorization_resource_entity_id
        # The resource entity type associated with the authorization resource. Valid values:
        # - cloud_account_role: cloud role.
        self.authorization_resource_entity_type = authorization_resource_entity_type
        # The authorization resource ID.
        self.authorization_resource_id = authorization_resource_id
        # The authorization rule ID.
        self.authorization_rule_id = authorization_rule_id
        # The cloud account ID to which the resource entity associated with the authorization resource belongs.
        self.cloud_account_id = cloud_account_id
        # The condition restriction.
        self.condition = condition
        # The creation time.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The update time.
        self.update_time = update_time

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

        if self.authorization_resource_id is not None:
            result['AuthorizationResourceId'] = self.authorization_resource_id

        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.condition is not None:
            result['Condition'] = self.condition.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResourceEntityId') is not None:
            self.authorization_resource_entity_id = m.get('AuthorizationResourceEntityId')

        if m.get('AuthorizationResourceEntityType') is not None:
            self.authorization_resource_entity_type = m.get('AuthorizationResourceEntityType')

        if m.get('AuthorizationResourceId') is not None:
            self.authorization_resource_id = m.get('AuthorizationResourceId')

        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('Condition') is not None:
            temp_model = main_models.GetAuthorizationResourceResponseBodyAuthorizationResourceCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetAuthorizationResourceResponseBodyAuthorizationResourceCondition(DaraModel):
    def __init__(
        self,
        credential_condition: main_models.GetAuthorizationResourceResponseBodyAuthorizationResourceConditionCredentialCondition = None,
    ):
        # The credential condition.
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
            temp_model = main_models.GetAuthorizationResourceResponseBodyAuthorizationResourceConditionCredentialCondition()
            self.credential_condition = temp_model.from_map(m.get('CredentialCondition'))

        return self

class GetAuthorizationResourceResponseBodyAuthorizationResourceConditionCredentialCondition(DaraModel):
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

