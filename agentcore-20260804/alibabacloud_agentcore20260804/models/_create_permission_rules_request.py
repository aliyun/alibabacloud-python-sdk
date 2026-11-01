# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreatePermissionRulesRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreatePermissionRulesRequestBody = None,
        client_token: str = None,
    ):
        # The request body for creating permission rules.
        self.body = body
        # The idempotency token.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreatePermissionRulesRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreatePermissionRulesRequestBody(DaraModel):
    def __init__(
        self,
        rules: List[main_models.CreatePermissionRulesRequestBodyRules] = None,
    ):
        # The list of permission rules to create.
        # 
        # This parameter is required.
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
                temp_model = main_models.CreatePermissionRulesRequestBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreatePermissionRulesRequestBodyRules(DaraModel):
    def __init__(
        self,
        effect: str = None,
        enforcement_mode: str = None,
        principal_id: str = None,
        principal_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
        source: str = None,
        target_scope: str = None,
        targets: List[str] = None,
    ):
        # The authorization effect.
        # 
        # This parameter is required.
        self.effect = effect
        # The rule enforcement mode.
        # 
        # This parameter is required.
        self.enforcement_mode = enforcement_mode
        # The principal ID.
        # 
        # This parameter is required.
        self.principal_id = principal_id
        # The principal type.
        # 
        # This parameter is required.
        self.principal_type = principal_type
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The rule source.
        # 
        # This parameter is required.
        self.source = source
        # The target scope.
        # 
        # This parameter is required.
        self.target_scope = target_scope
        # The list of targets for the rule.
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect is not None:
            result['effect'] = self.effect

        if self.enforcement_mode is not None:
            result['enforcementMode'] = self.enforcement_mode

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.source is not None:
            result['source'] = self.source

        if self.target_scope is not None:
            result['targetScope'] = self.target_scope

        if self.targets is not None:
            result['targets'] = self.targets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')

        if m.get('enforcementMode') is not None:
            self.enforcement_mode = m.get('enforcementMode')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('targetScope') is not None:
            self.target_scope = m.get('targetScope')

        if m.get('targets') is not None:
            self.targets = m.get('targets')

        return self

