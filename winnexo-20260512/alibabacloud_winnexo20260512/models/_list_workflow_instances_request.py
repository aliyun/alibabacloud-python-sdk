# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkflowInstancesRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        business_id: str = None,
        collaboration_group_id: str = None,
        initiator: str = None,
        keyword: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The exact requirement ID.
        self.business_id = business_id
        # The collaboration space ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The exact external initiator tag.
        self.initiator = initiator
        # The keyword for the title or requirement ID.
        self.keyword = keyword
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The page number. Pages start from 1.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The sort field.
        self.sort_by = sort_by
        # The sort order.
        self.sort_order = sort_order
        # Filters the instances by status. Valid values: Running, Completed, Failed, and Terminated.
        self.status = status
        # The tenant ID. This is a common parameter. If you use winnexo-cli, pass this parameter explicitly by using --tenant-id.
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

        if self.business_id is not None:
            result['businessId'] = self.business_id

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.initiator is not None:
            result['initiator'] = self.initiator

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

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.status is not None:
            result['status'] = self.status

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('businessId') is not None:
            self.business_id = m.get('businessId')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')

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

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

