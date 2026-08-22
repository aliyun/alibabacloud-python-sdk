# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetAuthorizationRuleResponseBody(DaraModel):
    def __init__(
        self,
        authorization_rule: main_models.GetAuthorizationRuleResponseBodyAuthorizationRule = None,
        request_id: str = None,
    ):
        # The authorization rule object.
        self.authorization_rule = authorization_rule
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.authorization_rule:
            self.authorization_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_rule is not None:
            result['AuthorizationRule'] = self.authorization_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRule') is not None:
            temp_model = main_models.GetAuthorizationRuleResponseBodyAuthorizationRule()
            self.authorization_rule = temp_model.from_map(m.get('AuthorizationRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAuthorizationRuleResponseBodyAuthorizationRule(DaraModel):
    def __init__(
        self,
        authorization_resource_scope: str = None,
        authorization_rule_creation_type: str = None,
        authorization_rule_id: str = None,
        authorization_rule_name: str = None,
        authorization_rule_scenario_label: str = None,
        authorization_rule_subject_id: str = None,
        authorization_rule_subject_scope: str = None,
        authorization_rule_subject_type: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        project_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The authorization resource scope. Valid values:
        # - global: All resources under the project.
        # - custom: Specified resources within the project scope.
        self.authorization_resource_scope = authorization_resource_scope
        # The creation type of the authorization rule. Valid values:
        # - system_init: Created by the system.
        # - user_custom: Created by the user.
        self.authorization_rule_creation_type = authorization_rule_creation_type
        # The authorization rule ID.
        self.authorization_rule_id = authorization_rule_id
        # The authorization rule name.
        self.authorization_rule_name = authorization_rule_name
        # The scenario label of the authorization rule.
        self.authorization_rule_scenario_label = authorization_rule_scenario_label
        # The subject ID associated with the authorization rule.
        self.authorization_rule_subject_id = authorization_rule_subject_id
        # The subject scope of the authorization rule. Valid values:
        # - shared: Shared type, which supports all subjects, including accounts and applications.
        # - exclusive: Exclusive type.
        self.authorization_rule_subject_scope = authorization_rule_subject_scope
        # The subject type associated with the authorization rule. This parameter is valid only when the authorization rule subject scope is exclusive. Valid values:
        # - application: Application.
        # - user: Account.
        self.authorization_rule_subject_type = authorization_rule_subject_type
        # The creation time, in UNIX timestamp format, measured in milliseconds.
        self.create_time = create_time
        # The description of the authorization rule.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The project ID associated with the authorization rule.
        self.project_id = project_id
        # The authorization rule status. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.status = status
        # The last update time, in UNIX timestamp format, measured in milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_resource_scope is not None:
            result['AuthorizationResourceScope'] = self.authorization_resource_scope

        if self.authorization_rule_creation_type is not None:
            result['AuthorizationRuleCreationType'] = self.authorization_rule_creation_type

        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id

        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name

        if self.authorization_rule_scenario_label is not None:
            result['AuthorizationRuleScenarioLabel'] = self.authorization_rule_scenario_label

        if self.authorization_rule_subject_id is not None:
            result['AuthorizationRuleSubjectId'] = self.authorization_rule_subject_id

        if self.authorization_rule_subject_scope is not None:
            result['AuthorizationRuleSubjectScope'] = self.authorization_rule_subject_scope

        if self.authorization_rule_subject_type is not None:
            result['AuthorizationRuleSubjectType'] = self.authorization_rule_subject_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationResourceScope') is not None:
            self.authorization_resource_scope = m.get('AuthorizationResourceScope')

        if m.get('AuthorizationRuleCreationType') is not None:
            self.authorization_rule_creation_type = m.get('AuthorizationRuleCreationType')

        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')

        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')

        if m.get('AuthorizationRuleScenarioLabel') is not None:
            self.authorization_rule_scenario_label = m.get('AuthorizationRuleScenarioLabel')

        if m.get('AuthorizationRuleSubjectId') is not None:
            self.authorization_rule_subject_id = m.get('AuthorizationRuleSubjectId')

        if m.get('AuthorizationRuleSubjectScope') is not None:
            self.authorization_rule_subject_scope = m.get('AuthorizationRuleSubjectScope')

        if m.get('AuthorizationRuleSubjectType') is not None:
            self.authorization_rule_subject_type = m.get('AuthorizationRuleSubjectType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

