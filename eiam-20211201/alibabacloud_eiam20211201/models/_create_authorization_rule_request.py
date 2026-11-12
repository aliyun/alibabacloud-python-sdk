# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAuthorizationRuleRequest(DaraModel):
    def __init__(
        self,
        authorization_resource_scope: str = None,
        authorization_rule_name: str = None,
        authorization_rule_scenario_label: str = None,
        client_token: str = None,
        description: str = None,
        instance_id: str = None,
        project_id: str = None,
        subject_type: str = None,
    ):
        # The scope of authorized resources. Valid values:
        # - global: global resources under the project
        # - custom: resources under a specified project scope
        self.authorization_resource_scope = authorization_resource_scope
        # The name of the authorization rule. The name can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.authorization_rule_name = authorization_rule_name
        # The scenario label of the authorization rule. The label can be up to 64 characters in length.
        self.authorization_rule_scenario_label = authorization_rule_scenario_label
        # The client token that is used to ensure the idempotence of the request. You can generate the value from your client and make sure that the value is unique across different requests. The ClientToken parameter only supports ASCII characters and cannot exceed 64 characters in length. For more information, see References: [How to ensure idempotence](https://www.alibabacloud.com/help/zh/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the authorization rule. The description can be up to 128 characters in length.
        self.description = description
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the project associated with the authorization rule. If you are unsure about the project to associate, you can use the default project. The ID of the default project is iprj_system_default.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of subject to which the authorization rule applies, such as user (for human users) or application (for machine users). When explicitly specified, only privileged cloud account rules with a custom resource scope are supported. If this field is omitted for custom scope rules in this scenario, the default value is user.
        self.subject_type = subject_type

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

        if self.authorization_rule_scenario_label is not None:
            result['AuthorizationRuleScenarioLabel'] = self.authorization_rule_scenario_label

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResourceScope') is not None:
            self.authorization_resource_scope = m.get('AuthorizationResourceScope')

        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')

        if m.get('AuthorizationRuleScenarioLabel') is not None:
            self.authorization_rule_scenario_label = m.get('AuthorizationRuleScenarioLabel')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')

        return self

