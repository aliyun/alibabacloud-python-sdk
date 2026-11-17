# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCollaborationGroupMembersRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # The collaboration workspace ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The search keyword. This parameter is optional and can be up to 256 characters in length.
        self.keyword = keyword
        # The page number. Pages start from 1.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The tenant ID. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

