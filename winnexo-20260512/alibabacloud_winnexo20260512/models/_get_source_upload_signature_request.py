# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSourceUploadSignatureRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        expires: int = None,
        filename: str = None,
        operating_object_name: str = None,
        scope: str = None,
        tenant_id: str = None,
    ):
        # 文件 Content-Type（可选，不传则自动推断）
        self.content_type = content_type
        # 签名 URL 过期时间（秒），默认 3600
        self.expires = expires
        # 文件名（含后缀，如 report.pdf）
        # 
        # This parameter is required.
        self.filename = filename
        # Agent 命名空间标识（数字员工名称）
        self.operating_object_name = operating_object_name
        # 数据源归属范围: source（个人数据源，映射 PERSONAL）/ knowledge（企业知识库，映射 TENANT）
        self.scope = scope
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

        if self.expires is not None:
            result['expires'] = self.expires

        if self.filename is not None:
            result['filename'] = self.filename

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.scope is not None:
            result['scope'] = self.scope

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('expires') is not None:
            self.expires = m.get('expires')

        if m.get('filename') is not None:
            self.filename = m.get('filename')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

