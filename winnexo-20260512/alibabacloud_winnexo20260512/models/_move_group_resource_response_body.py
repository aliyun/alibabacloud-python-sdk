# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveGroupResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        group_id: str = None,
        message: str = None,
        request_id: str = None,
        source_directory_id: str = None,
        source_id: str = None,
        target_directory_id: str = None,
    ):
        # 业务状态码，成功为200
        self.code = code
        # 协作空间 ID
        self.group_id = group_id
        # 错误描述
        self.message = message
        # 请求追踪ID
        self.request_id = request_id
        # 移动前的目录 ID
        self.source_directory_id = source_directory_id
        # 移动的资料 ID，移动前后保持不变
        self.source_id = source_id
        # 移动后的目录 ID
        self.target_directory_id = target_directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_directory_id is not None:
            result['sourceDirectoryId'] = self.source_directory_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.target_directory_id is not None:
            result['targetDirectoryId'] = self.target_directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceDirectoryId') is not None:
            self.source_directory_id = m.get('sourceDirectoryId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('targetDirectoryId') is not None:
            self.target_directory_id = m.get('targetDirectoryId')

        return self

