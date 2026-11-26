# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSourceContentRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        content: str = None,
        force_sync: bool = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The returned content.
        # 
        # This parameter is required.
        self.content = content
        # Specifies whether to force synchronous processing.
        self.force_sync = force_sync
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The ID of the data source.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The ID of the effective tenant.
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

        if self.content is not None:
            result['content'] = self.content

        if self.force_sync is not None:
            result['forceSync'] = self.force_sync

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('forceSync') is not None:
            self.force_sync = m.get('forceSync')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

