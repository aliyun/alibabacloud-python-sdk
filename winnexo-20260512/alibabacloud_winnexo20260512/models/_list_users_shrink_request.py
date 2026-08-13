# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        is_active: bool = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        role_codes_shrink: str = None,
        tenant_id: str = None,
    ):
        # 按 WINNEXO 登录账号精确批量查询（多选）；与其他筛选条件取交集。不传或传空列表 [] 均视为不按账号筛选（返回全部符合其他条件的成员）
        self.account_ids_shrink = account_ids_shrink
        # 启用/停用状态筛选
        self.is_active = is_active
        # 搜索关键词（模糊匹配显示名和账号）
        self.keyword = keyword
        # 页码（从1开始）
        self.page = page
        # 每页数量（最大100）
        self.page_size = page_size
        # 按角色筛选，可选值: SUPER_ADMIN / SYSTEM_ADMIN / SEMANTIC_ADMIN / SKILL_ADMIN / KB_ADMIN / AGENT_ADMIN / APPLICATION_USER
        self.role_codes_shrink = role_codes_shrink
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids_shrink is not None:
            result['accountIds'] = self.account_ids_shrink

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.role_codes_shrink is not None:
            result['roleCodes'] = self.role_codes_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids_shrink = m.get('accountIds')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('roleCodes') is not None:
            self.role_codes_shrink = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

