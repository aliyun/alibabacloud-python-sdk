# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalAlidingKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory_id: str = None,
        gmt_create: str = None,
        kb_url: str = None,
        message: str = None,
        name: str = None,
        operating_object_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 新建知识库根目录 ID
        self.directory_id = directory_id
        # 创建时间 ISO8601
        self.gmt_create = gmt_create
        # 知识库 URL（echo 回入参，便于调用方对齐）
        self.kb_url = kb_url
        # 错误描述，成功时为空
        self.message = message
        # 文件名
        self.name = name
        # 所属数字员工名称（echo 回入参，可为 null）
        self.operating_object_name = operating_object_name
        # 请求追踪 ID
        self.request_id = request_id
        # 知识库根目录状态（创建后为 RUNNING；后台同步完成后转 READY 或 FAILED）
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.kb_url is not None:
            result['kbUrl'] = self.kb_url

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('kbUrl') is not None:
            self.kb_url = m.get('kbUrl')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

