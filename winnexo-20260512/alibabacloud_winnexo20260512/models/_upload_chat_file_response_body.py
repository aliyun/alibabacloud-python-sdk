# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadChatFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content_type: str = None,
        file_name: str = None,
        file_public_url: str = None,
        file_record_id: str = None,
        file_url: str = None,
        message: str = None,
        object_name: str = None,
        request_id: str = None,
        upload_signature_url: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 文件 MIME 类型
        self.content_type = content_type
        # 文件名
        self.file_name = file_name
        # 文件公开访问 URL（有效期 1 小时）
        self.file_public_url = file_public_url
        # 文件记录 ID
        self.file_record_id = file_record_id
        # 文件 remote_url（入库路径）
        self.file_url = file_url
        # 错误描述，成功时为空
        self.message = message
        # OSS 对象路径
        self.object_name = object_name
        # 请求追踪 ID
        self.request_id = request_id
        # 签名上传 URL（本接口为后端直传，该字段为空）
        self.upload_signature_url = upload_signature_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_public_url is not None:
            result['filePublicUrl'] = self.file_public_url

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.message is not None:
            result['message'] = self.message

        if self.object_name is not None:
            result['objectName'] = self.object_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.upload_signature_url is not None:
            result['uploadSignatureUrl'] = self.upload_signature_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('filePublicUrl') is not None:
            self.file_public_url = m.get('filePublicUrl')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('uploadSignatureUrl') is not None:
            self.upload_signature_url = m.get('uploadSignatureUrl')

        return self

