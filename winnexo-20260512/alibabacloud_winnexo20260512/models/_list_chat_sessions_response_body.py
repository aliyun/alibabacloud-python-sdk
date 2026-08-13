# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class ListChatSessionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        message: str = None,
        page: int = None,
        page_size: str = None,
        request_id: str = None,
        sessions: List[Any] = None,
        tenant_id: str = None,
        total: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 是否有更多数据
        self.has_more = has_more
        # 错误描述，成功时为空
        self.message = message
        self.page = page
        # 每页条数
        self.page_size = page_size
        # 请求追踪 ID
        self.request_id = request_id
        # 响应数据负载
        self.sessions = sessions
        # 租户ID
        self.tenant_id = tenant_id
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.sessions is not None:
            result['sessions'] = self.sessions

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessions') is not None:
            self.sessions = m.get('sessions')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

