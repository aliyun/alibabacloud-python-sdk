# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        is_active: bool = None,
        role_codes: List[str] = None,
        tenant_id: str = None,
        user_group_ids: List[str] = None,
        wn_user_id: str = None,
    ):
        # 新的显示名称（不传不修改，传则不可为空，最多100字）
        self.display_name = display_name
        # 启用/停用状态（不传不修改）。false=停用，true=启用
        self.is_active = is_active
        # 新的系统角色 code 列表（全量替换，至少包含一个角色）。可选值: SUPER_ADMIN / SYSTEM_ADMIN / SEMANTIC_ADMIN / SKILL_ADMIN / KB_ADMIN / AGENT_ADMIN / APPLICATION_USER
        self.role_codes = role_codes
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 新的用户组ID列表（全量替换，不传不修改）
        self.user_group_ids = user_group_ids
        # 目标用户ID（WINNEXO 平台用户ID）
        # 
        # This parameter is required.
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.role_codes is not None:
            result['roleCodes'] = self.role_codes

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('roleCodes') is not None:
            self.role_codes = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

