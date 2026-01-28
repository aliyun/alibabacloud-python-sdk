# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizationRulesResponseBody(DaraModel):
    def __init__(
        self,
        authorization_rules: List[main_models.ListAuthorizationRulesResponseBodyAuthorizationRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorization_rules = authorization_rules
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorization_rules:
            for v1 in self.authorization_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizationRules'] = []
        if self.authorization_rules is not None:
            for k1 in self.authorization_rules:
                result['AuthorizationRules'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorization_rules = []
        if m.get('AuthorizationRules') is not None:
            for k1 in m.get('AuthorizationRules'):
                temp_model = main_models.ListAuthorizationRulesResponseBodyAuthorizationRules()
                self.authorization_rules.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuthorizationRulesResponseBodyAuthorizationRules(DaraModel):
    def __init__(
        self,
        authorization_resource_scope: str = None,
        authorization_rule_creation_type: str = None,
        authorization_rule_id: str = None,
        authorization_rule_name: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        project_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # 授权资源范围，枚举值：global（项目下所有资源）、custom（指定资源）。
        self.authorization_resource_scope = authorization_resource_scope
        # 授权规则的创建类型，枚举类型：user_created（用户创建)，approval_created（审批创建)。
        self.authorization_rule_creation_type = authorization_rule_creation_type
        # 授权规则标识。
        self.authorization_rule_id = authorization_rule_id
        # 授权规则名称。
        self.authorization_rule_name = authorization_rule_name
        # 创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time
        # 授权规则描述，长度限制为128字符。
        self.description = description
        # 实例ID。
        self.instance_id = instance_id
        # 授权规则关联的项目标识。
        self.project_id = project_id
        # 授权规则状态，枚举值：enabled（启用）、disabled（禁用）。
        self.status = status
        # 最近一次更新时间，Unix时间戳格式，单位为毫秒。
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

