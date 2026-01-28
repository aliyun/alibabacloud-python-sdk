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
        self.authorization_resource = authorization_resource
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
        instance_id: str = None,
    ):
        # 资源实体标识
        self.authorization_resource_entity_id = authorization_resource_entity_id
        # 资源实体类型，枚举类型：asset（资产）、credential（凭据）、cloud_identity_role（云账号角色）
        self.authorization_resource_entity_type = authorization_resource_entity_type
        # 授权资源标识
        self.authorization_resource_id = authorization_resource_id
        # 授权规则标识
        self.authorization_rule_id = authorization_rule_id
        # 云账号ID。
        self.cloud_account_id = cloud_account_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

