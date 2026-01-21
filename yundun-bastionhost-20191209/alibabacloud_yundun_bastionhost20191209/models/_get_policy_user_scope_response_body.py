# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetPolicyUserScopeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_scope: main_models.GetPolicyUserScopeResponseBodyUserScope = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The users to whom the control policy applies.
        self.user_scope = user_scope

    def validate(self):
        if self.user_scope:
            self.user_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_scope is not None:
            result['UserScope'] = self.user_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserScope') is not None:
            temp_model = main_models.GetPolicyUserScopeResponseBodyUserScope()
            self.user_scope = temp_model.from_map(m.get('UserScope'))

        return self

class GetPolicyUserScopeResponseBodyUserScope(DaraModel):
    def __init__(
        self,
        scope_type: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The scope of users to whom the control policy applies.
        # *   If **All** is returned for this parameter, the control policy applies to all users.
        # 
        # *   If no value is returned for this parameter, the control policy applies to the assets specified in the return values of UserGroupIds and UserIds.
        self.scope_type = scope_type
        # The user groups to which the control policy applies.
        self.user_group_ids = user_group_ids
        # The users to whom the control policy applies.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

