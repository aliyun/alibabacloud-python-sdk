# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetPageResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        id: int = None,
        kind: str = None,
        name: str = None,
        request_id: str = None,
        site_ids: List[int] = None,
        update_time: str = None,
    ):
        # 自定义响应页面内容BASE64编码
        # 
        # This parameter is required.
        self.content = content
        # 自定义响应页面内容类型
        # 
        # This parameter is required.
        self.content_type = content_type
        # 自定义响应页面描述
        self.description = description
        # 自定义响应页面ID
        self.id = id
        self.kind = kind
        # 自定义响应页面名称
        # 
        # This parameter is required.
        self.name = name
        self.request_id = request_id
        self.site_ids = site_ids
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_ids is not None:
            result['SiteIds'] = self.site_ids

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

