# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAdminKnowledgeBasesShrinkRequest(DaraModel):
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
        source_types_shrink: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If this parameter is passed, the operation is performed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The directory ID.
        self.directory_id = directory_id
        # The keyword for fuzzy search of component data in the form.
        self.keyword = keyword
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The page number. Default value: 1.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The field by which to sort the returned results. Valid values:
        # 
        # - event_time: the event creation time
        # - event_execute_start_time: the event execution start time
        # - event_execute_finish_time: the event execution finish time
        self.sort_field = sort_field
        # The sort order. This parameter takes effect only when the sort field is specified. Valid values: ASC and DESC. The values are case-insensitive.
        self.sort_order = sort_order
        # The list of service source types.
        self.source_types_shrink = source_types_shrink
        # The ID of the tenant to which the task belongs.
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

        if self.source_types_shrink is not None:
            result['sourceTypes'] = self.source_types_shrink

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
            self.source_types_shrink = m.get('sourceTypes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

