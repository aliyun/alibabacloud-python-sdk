# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        is_active: bool = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        role_codes: List[str] = None,
        tenant_id: str = None,
    ):
        # The list of Alibaba Cloud account IDs.
        self.account_ids = account_ids
        # Specifies whether the account is activated.
        #  - **true**: Activated.
        # - **false**: Not activated.
        self.is_active = is_active
        # The keyword for searching products. Fuzzy match is supported.
        self.keyword = keyword
        # The page number.
        self.page = page
        # The number of entries per page.
        # 
        # > The maximum number of entries per page is 30.
        self.page_size = page_size
        # The list of new system role codes (full replacement, at least one role must be included). Valid values: SUPER_ADMIN / SYSTEM_ADMIN / SEMANTIC_ADMIN / SKILL_ADMIN / KB_ADMIN / AGENT_ADMIN / APPLICATION_USER.
        self.role_codes = role_codes
        # The tenant ID. This is a common parameter. The winnexo-cli passes this parameter explicitly by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['accountIds'] = self.account_ids

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.role_codes is not None:
            result['roleCodes'] = self.role_codes

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids = m.get('accountIds')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('roleCodes') is not None:
            self.role_codes = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

