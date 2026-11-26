# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMemoryAutoExtractionSwitchRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        clear_existing: bool = None,
        enabled: bool = None,
        group_id: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        owner_type: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # Specifies whether to synchronously clear the automatically collected memory. This parameter can be used when enabling or disabling the feature.
        self.clear_existing = clear_existing
        # Specifies whether to enable automatic memory collection.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The ID of the collaboration workspace. This parameter is required when ownerType is set to group.
        self.group_id = group_id
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The owner type. Valid values:
        # - user: the personal memory of the authenticated user
        # - group: the memory of the specified collaboration workspace
        self.owner_type = owner_type
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
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

        if self.clear_existing is not None:
            result['clearExisting'] = self.clear_existing

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('clearExisting') is not None:
            self.clear_existing = m.get('clearExisting')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

