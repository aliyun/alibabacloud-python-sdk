# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadChatFileByBase64Request(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        content_type: str = None,
        file_content_base_64: str = None,
        file_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The MIME type of the file.
        self.content_type = content_type
        # The Base64-encoded string of the file content.
        # 
        # This parameter is required.
        self.file_content_base_64 = file_content_base_64
        # The file name.
        # 
        # This parameter is required.
        self.file_name = file_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.file_content_base_64 is not None:
            result['fileContentBase64'] = self.file_content_base_64

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('fileContentBase64') is not None:
            self.file_content_base_64 = m.get('fileContentBase64')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

