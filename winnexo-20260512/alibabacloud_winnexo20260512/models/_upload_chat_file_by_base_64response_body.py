# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadChatFileByBase64ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        file_record_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 文件记录 ID
        self.file_record_id = file_record_id
        # 错误描述，成功时为空
        self.message = message
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

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

