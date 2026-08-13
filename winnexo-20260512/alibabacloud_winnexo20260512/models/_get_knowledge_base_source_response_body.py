# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKnowledgeBaseSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        directory_id: str = None,
        directory_path: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        source_id: str = None,
        source_kind: str = None,
        source_tags: str = None,
        source_type: str = None,
        status: str = None,
        status_message: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 知识描述
        self.description = description
        # 所属分类 ID
        self.directory_id = directory_id
        # 所属分类完整路径
        self.directory_path = directory_path
        # 创建时间戳（毫秒）
        self.gmt_create = gmt_create
        # 修改时间戳（毫秒）
        self.gmt_modified = gmt_modified
        # 错误描述，成功时为空
        self.message = message
        # 文件名
        self.name = name
        # 请求追踪 ID
        self.request_id = request_id
        # 知识 ID
        self.source_id = source_id
        # 知识 KB 归属类型：aliding_kb_doc（阿里钉知识库文档）/ normal（普通知识）
        self.source_kind = source_kind
        # 知识标签（JSON 字符串列表）
        self.source_tags = source_tags
        # 知识类型（TEXT / FILE / ONLINE_DOC 等）
        self.source_type = source_type
        # 处理状态（READY / RUNNING / FAILED 等）
        self.status = status
        # 状态附加信息（如失败原因）
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.directory_path is not None:
            result['directoryPath'] = self.directory_path

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_kind is not None:
            result['sourceKind'] = self.source_kind

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        if self.status_message is not None:
            result['statusMessage'] = self.status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryPath') is not None:
            self.directory_path = m.get('directoryPath')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceKind') is not None:
            self.source_kind = m.get('sourceKind')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusMessage') is not None:
            self.status_message = m.get('statusMessage')

        return self

