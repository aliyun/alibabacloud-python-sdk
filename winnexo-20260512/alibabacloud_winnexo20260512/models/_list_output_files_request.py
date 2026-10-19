# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOutputFilesRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        collaboration_group_id: str = None,
        item_type: str = None,
        keyword: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        session_id: str = None,
        shared_only: bool = None,
        tags: List[str] = None,
        tenant_id: str = None,
    ):
        # 精确业务编号，来自文件登记或工作流实例关联
        self.biz_id = biz_id
        # 可选协作空间 ID；未传保持当前用户个人产出范围
        self.collaboration_group_id = collaboration_group_id
        # The type of the output item. Valid values: ppt, html, document, picture, slides, video, audio, email, and others.
        self.item_type = item_type
        # The keyword for searching. Matches the output title or item name.
        self.keyword = keyword
        # The name of the digital employee (operating object). Used to filter results by name.
        self.operating_object_name = operating_object_name
        # The page number, starting from 1.
        self.page = page
        # The number of items per page. Valid values: 1 to 100.
        self.page_size = page_size
        # 精确会话 ID，覆盖普通会话、技能会话与任务 executionId
        self.session_id = session_id
        # Specifies whether to display only outputs and output items with sharing enabled.
        self.shared_only = shared_only
        # 全部匹配的标签列表，来自文件登记或实例 variables.tags
        self.tags = tags
        # The tenant ID. This is a common parameter. In winnexo-cli, pass it explicitly by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.shared_only is not None:
            result['sharedOnly'] = self.shared_only

        if self.tags is not None:
            result['tags'] = self.tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sharedOnly') is not None:
            self.shared_only = m.get('sharedOnly')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

