# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSourceUploadSignatureRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        content_type: str = None,
        expires: int = None,
        filename: str = None,
        group_id: str = None,
        operating_object_name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        scope: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The content type. Valid values:
        # 
        # - Text
        # - Markdown
        self.content_type = content_type
        # The expiration time of the signed URL, in seconds. Default value: 3600.
        self.expires = expires
        # The file name.
        # 
        # This parameter is required.
        self.filename = filename
        # The collaboration space ID passed from the frontend. This parameter is required when scope is set to group. The value must be a space accessible to the current user and is used in the OSS path for locating. The value must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). This parameter is not used for other scope values.
        self.group_id = group_id
        # The name of the digital employee (operating object name, optional).
        self.operating_object_name = operating_object_name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The permission scope.
        self.scope = scope
        # The tenant ID to which the task belongs.
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

        if self.expires is not None:
            result['expires'] = self.expires

        if self.filename is not None:
            result['filename'] = self.filename

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('expires') is not None:
            self.expires = m.get('expires')

        if m.get('filename') is not None:
            self.filename = m.get('filename')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

