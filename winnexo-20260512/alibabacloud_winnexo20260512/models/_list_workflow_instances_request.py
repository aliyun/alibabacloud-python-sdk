# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkflowInstancesRequest(DaraModel):
    def __init__(
        self,
        business_id: str = None,
        collaboration_group_id: str = None,
        initiator: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # 精确需求编号
        self.business_id = business_id
        # 协作空间 ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 精确外部发起人标签
        self.initiator = initiator
        # 标题或需求编号关键词
        self.keyword = keyword
        # 页码，从 1 开始
        self.page = page
        # 每页数量 1-100
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by
        # 排序方向
        self.sort_order = sort_order
        # Running/Completed/Failed/Terminated 筛选
        self.status = status
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['businessId'] = self.business_id

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.initiator is not None:
            result['initiator'] = self.initiator

        if self.keyword is not None:
            result['keyword'] = self.keyword

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
        if m.get('businessId') is not None:
            self.business_id = m.get('businessId')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

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

