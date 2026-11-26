# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        app_token: str = None,
        is_active: bool = None,
        keyword: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        role_codes_shrink: str = None,
        tenant_id: str = None,
    ):
        # The list of cloud account IDs.
        self.account_ids_shrink = account_ids_shrink
        # The platform application token issued by the console. If specified, the operation is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # Specifies whether the account is activated. Valid values:
        # - **true**: Activated.
        # - **false**: Not activated.
        self.is_active = is_active
        # The keyword for searching products. Fuzzy match is supported.
        self.keyword = keyword
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The page number.
        self.page = page
        # The number of entries to return per page.
        # 
        # > The maximum number of entries per page is 30.
        self.page_size = page_size
        # The list of new system role codes. This list fully replaces the existing roles and must contain at least one role. Valid values: SUPER_ADMIN, SYSTEM_ADMIN, SEMANTIC_ADMIN, SKILL_ADMIN, KB_ADMIN, AGENT_ADMIN, and APPLICATION_USER.
        self.role_codes_shrink = role_codes_shrink
        # The tenant ID. This is a common parameter and is explicitly passed by using the --tenant-id option in winnexo-cli.
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

        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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

        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('roleCodes') is not None:
            self.role_codes_shrink = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

