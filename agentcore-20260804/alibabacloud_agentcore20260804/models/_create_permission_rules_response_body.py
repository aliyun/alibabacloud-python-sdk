# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreatePermissionRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreatePermissionRulesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The creation result.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request processing result message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreatePermissionRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreatePermissionRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        rules: List[main_models.CreatePermissionRulesResponseBodyDataRules] = None,
    ):
        # The list of created permission rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.CreatePermissionRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreatePermissionRulesResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        effect: str = None,
        enforcement_mode: str = None,
        permission_rule_id: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
        source: str = None,
        source_detail: str = None,
        target_scope: str = None,
        targets: List[str] = None,
        updated_at: str = None,
    ):
        # The creation time in RFC 3339 format.
        self.created_at = created_at
        # The authorization effect.
        self.effect = effect
        # The rule enforcement mode.
        self.enforcement_mode = enforcement_mode
        # The permission rule ID.
        self.permission_rule_id = permission_rule_id
        # The principal ID.
        self.principal_id = principal_id
        # The principal name.
        self.principal_name = principal_name
        # The principal type.
        self.principal_type = principal_type
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The rule source.
        self.source = source
        # The rule source details.
        self.source_detail = source_detail
        # The target scope.
        self.target_scope = target_scope
        # The list of targets for the rule.
        self.targets = targets
        # The update time in RFC 3339 format.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.effect is not None:
            result['effect'] = self.effect

        if self.enforcement_mode is not None:
            result['enforcementMode'] = self.enforcement_mode

        if self.permission_rule_id is not None:
            result['permissionRuleId'] = self.permission_rule_id

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_name is not None:
            result['principalName'] = self.principal_name

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.source is not None:
            result['source'] = self.source

        if self.source_detail is not None:
            result['sourceDetail'] = self.source_detail

        if self.target_scope is not None:
            result['targetScope'] = self.target_scope

        if self.targets is not None:
            result['targets'] = self.targets

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('effect') is not None:
            self.effect = m.get('effect')

        if m.get('enforcementMode') is not None:
            self.enforcement_mode = m.get('enforcementMode')

        if m.get('permissionRuleId') is not None:
            self.permission_rule_id = m.get('permissionRuleId')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalName') is not None:
            self.principal_name = m.get('principalName')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourceDetail') is not None:
            self.source_detail = m.get('sourceDetail')

        if m.get('targetScope') is not None:
            self.target_scope = m.get('targetScope')

        if m.get('targets') is not None:
            self.targets = m.get('targets')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

