# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetKnowledgeBaseVisibilityRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        cascade_mode: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        target_id: str = None,
        target_type: str = None,
        tenant_id: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
        visibility_mode: str = None,
    ):
        # token
        self.app_token = app_token
        # Specifies how to handle subfolders.
        self.cascade_mode = cascade_mode
        # The user code.
        self.ops_user_code = ops_user_code
        # The ID of the operator.
        self.ops_user_id = ops_user_id
        # The target ID, which varies based on the target type.
        # - If the type is period, specify the period ID.
        # - If the type is objective, specify the objective ID.
        # - If the type is kr, specify the keyResult ID.
        # 
        # This parameter is required.
        self.target_id = target_id
        # The type of the current permission. Valid values:
        # - period: period type
        # - objective: objective type
        # - kr: keyResult type
        # 
        # This parameter is required.
        self.target_type = target_type
        # The ID of the tenant to which the resource belongs. If this parameter is not specified, the current tenant of the caller is used.
        self.tenant_id = tenant_id
        # The collection of user groups.
        self.user_group_ids = user_group_ids
        # The collection of user IDs.
        self.user_ids = user_ids
        # The visibility scope mode.
        # 
        # This parameter is required.
        self.visibility_mode = visibility_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.cascade_mode is not None:
            result['cascadeMode'] = self.cascade_mode

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.target_id is not None:
            result['targetId'] = self.target_id

        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['userIds'] = self.user_ids

        if self.visibility_mode is not None:
            result['visibilityMode'] = self.visibility_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('cascadeMode') is not None:
            self.cascade_mode = m.get('cascadeMode')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')

        if m.get('visibilityMode') is not None:
            self.visibility_mode = m.get('visibilityMode')

        return self

