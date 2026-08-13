# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListUserVisibleKnowledgeBasesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListUserVisibleKnowledgeBasesResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        self.items = items
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 知识库总数
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListUserVisibleKnowledgeBasesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListUserVisibleKnowledgeBasesResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator_id: int = None,
        creator_name: str = None,
        description: str = None,
        directory_id: str = None,
        directory_kind: str = None,
        directory_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        name: str = None,
    ):
        # 知识库创建人用户 ID
        self.creator_id = creator_id
        # 知识库创建人名称
        self.creator_name = creator_name
        # 知识库描述
        self.description = description
        # 知识库根目录唯一标识
        self.directory_id = directory_id
        # 目录归属类型
        self.directory_kind = directory_kind
        # 目录类型
        self.directory_type = directory_type
        # 创建时间戳（毫秒）
        self.gmt_create = gmt_create
        # 修改时间戳（毫秒）
        self.gmt_modified = gmt_modified
        # 知识库名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.directory_kind is not None:
            result['directoryKind'] = self.directory_kind

        if self.directory_type is not None:
            result['directoryType'] = self.directory_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryKind') is not None:
            self.directory_kind = m.get('directoryKind')

        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

