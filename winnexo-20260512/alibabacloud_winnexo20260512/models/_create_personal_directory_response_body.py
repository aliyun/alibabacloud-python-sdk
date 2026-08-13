# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        directory_id: str = None,
        directory_kind: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        message: str = None,
        name: str = None,
        operating_object_name: str = None,
        parent_directory_id: str = None,
        path: str = None,
        request_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 目录描述
        self.description = description
        # 新建目录 ID
        self.directory_id = directory_id
        # 目录 KB 归属类型：normal / aliding_kb_root / aliding_kb_internal
        self.directory_kind = directory_kind
        # 创建时间戳（毫秒）
        self.gmt_create = gmt_create
        # 修改时间戳（毫秒）
        self.gmt_modified = gmt_modified
        # 错误描述，成功时为空
        self.message = message
        # 文件名
        self.name = name
        # 所属数字员工名称
        self.operating_object_name = operating_object_name
        # 父目录 ID（service 若回填默认根目录，这里返回回填后的父目录 ID）
        self.parent_directory_id = parent_directory_id
        # 文件 OSS URL
        self.path = path
        # 请求追踪 ID
        self.request_id = request_id

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

        if self.directory_kind is not None:
            result['directoryKind'] = self.directory_kind

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id

        if self.path is not None:
            result['path'] = self.path

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryKind') is not None:
            self.directory_kind = m.get('directoryKind')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

