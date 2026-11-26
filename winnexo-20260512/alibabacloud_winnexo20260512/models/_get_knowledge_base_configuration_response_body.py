# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetKnowledgeBaseConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        change_record_enabled: bool = None,
        code: str = None,
        directory_id: str = None,
        message: str = None,
        oo_visibility_mode: str = None,
        operating_object_names: List[str] = None,
        request_id: str = None,
    ):
        # 是否开启后续内容更新的 AI 版本摘要
        self.change_record_enabled = change_record_enabled
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 企业知识库根目录 ID
        self.directory_id = directory_id
        # 错误描述，成功时为 success
        self.message = message
        # 数字员工可见模式；历史未显式设置 ALL 的配置按 SPECIFIED 返回
        self.oo_visibility_mode = oo_visibility_mode
        # 显式关联的数字员工名称；ALL 返回空数组，SPECIFIED 空数组表示没有关联员工
        self.operating_object_names = operating_object_names
        # 请求追踪 ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_record_enabled is not None:
            result['changeRecordEnabled'] = self.change_record_enabled

        if self.code is not None:
            result['code'] = self.code

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.message is not None:
            result['message'] = self.message

        if self.oo_visibility_mode is not None:
            result['ooVisibilityMode'] = self.oo_visibility_mode

        if self.operating_object_names is not None:
            result['operatingObjectNames'] = self.operating_object_names

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changeRecordEnabled') is not None:
            self.change_record_enabled = m.get('changeRecordEnabled')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('ooVisibilityMode') is not None:
            self.oo_visibility_mode = m.get('ooVisibilityMode')

        if m.get('operatingObjectNames') is not None:
            self.operating_object_names = m.get('operatingObjectNames')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

