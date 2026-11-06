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
        # 协作空间ID，必填，长度1至64。调用者必须是该租户下该空间的有效成员。可从ListCollaborationGroups返回的items中获取。
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 成员显示名称搜索关键词，可选，最长256字符；忽略大小写，先筛选后分页。不传时查询全部有效成员。
        self.keyword = keyword
        # 页码，从1开始；请求省略时默认为1。
        self.page = page
        # 每页记录数，取值1至100；请求省略时默认为20。
        self.page_size = page_size
        # 业务租户ID，可选。必须属于当前调用身份的可访问租户；无权访问时拒绝请求。未传时按现有鉴权规则解析租户，多租户用户无法唯一确定时需显式指定。
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

