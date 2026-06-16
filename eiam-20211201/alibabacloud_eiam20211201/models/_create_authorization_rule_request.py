# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAuthorizationRuleRequest(DaraModel):
    def __init__(
        self,
        authorization_resource_scope: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        description: str = None,
        instance_id: str = None,
        project_id: str = None,
    ):
        # The scope of authorized resources. Valid values:
        # 
        # - global: all resources within the project.
        # 
        # - custom: specified resources within the project.
        self.authorization_resource_scope = authorization_resource_scope
        # The name of the authorization rule. The name can be up to 64 characters long.
        # 
        # This parameter is required.
        self.authorization_rule_name = authorization_rule_name
        # A unique identifier that you provide to ensure the idempotence of the request. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the authorization rule. The description can be up to 128 characters long.
        self.description = description
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the project to associate with the authorization rule. If you are unsure which project to use, you can associate the rule with the default project, iprj_system_default.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_resource_scope is not None:
            result['AuthorizationResourceScope'] = self.authorization_resource_scope

        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResourceScope') is not None:
            self.authorization_resource_scope = m.get('AuthorizationResourceScope')

        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

