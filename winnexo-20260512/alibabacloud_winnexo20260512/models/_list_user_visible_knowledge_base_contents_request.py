# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserVisibleKnowledgeBaseContentsRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        directory_id: str = None,
        keyword: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        sort_field: str = None,
        sort_order: str = None,
        source_types: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The directory ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The search keyword. Fuzzy search on version names is supported.
        self.keyword = keyword
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The field by which to sort the returned results. Valid values:
        # 
        # - event_time: the event creation time
        # - event_execute_start_time: the event execution start time
        # - event_execute_finish_time: the event execution completion time
        self.sort_field = sort_field
        # Specifies the sort order. This parameter takes effect only when sortBy is specified. Valid values: ASC and DESC. The values are case-insensitive.
        self.sort_order = sort_order
        # The list of service source types.
        self.source_types = source_types
        # The tenant ID. This is a common parameter. For winnexo-cli, it is explicitly passed by using the --tenant-id option.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

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

        if self.sort_field is not None:
            result['sortField'] = self.sort_field

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.source_types is not None:
            result['sourceTypes'] = self.source_types

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

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

        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('sourceTypes') is not None:
            self.source_types = m.get('sourceTypes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

