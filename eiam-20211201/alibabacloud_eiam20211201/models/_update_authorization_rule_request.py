# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuthorizationRuleRequest(DaraModel):
    def __init__(
        self,
        authorization_resource_scope: str = None,
        authorization_rule_id: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # The scope of the authorized resources. Valid values:
        # 
        # - global: global resources within the project.
        # 
        # - custom: specified resources within the project.
        self.authorization_resource_scope = authorization_resource_scope
        # The authorization rule ID.
        # 
        # This parameter is required.
        self.authorization_rule_id = authorization_rule_id
        # The name of the authorization rule. The name can be up to 64 characters long.
        self.authorization_rule_name = authorization_rule_name
        # A client token that ensures the idempotence of the request. Generate a unique value for this parameter from your client. The token can contain only ASCII characters and must be no more than 64 characters in length. For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_resource_scope is not None:
            result['AuthorizationResourceScope'] = self.authorization_resource_scope

        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResourceScope') is not None:
            self.authorization_resource_scope = m.get('AuthorizationResourceScope')

        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

