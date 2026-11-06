# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListPermissionRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListPermissionRulesResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of permission rules.
        self.items = items
        # The maximum number of entries returned in the current request.
        self.max_results = max_results
        # The message about the request processing result.
        self.message = message
        # The token for the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of rules that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListPermissionRulesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListPermissionRulesResponseBodyItems(DaraModel):
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
        # The list of targets to which the rule applies.
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

