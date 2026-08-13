# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadChatFileRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        file_name: str = None,
        file_url: str = None,
        operating_object_name: str = None,
        tenant_id: str = None,
    ):
        # 文件 MIME 类型（可选，不传时按 application/octet-stream 处理）
        self.content_type = content_type
        # 原始文件名（含后缀，如 report.pdf）。中转生成的 OSS 地址不携带原始文件名，后端据此确定文件后缀与展示名
        # 
        # This parameter is required.
        self.file_name = file_name
        # 文件的 OSS 地址。使用 SDK 的 UploadChatFileAdvance 方法时由 SDK 中转上传后自动回填；直接调用本 API 时需自行传入可被服务端访问的 OSS 地址
        # 
        # This parameter is required.
        self.file_url = file_url
        # Agent 命名空间标识
        self.operating_object_name = operating_object_name
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

