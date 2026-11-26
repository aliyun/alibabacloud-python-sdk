# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveGroupOutputFileToGroupResourceShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        directory_id: str = None,
        group_id: str = None,
        item_ids_shrink: str = None,
        mode: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The ID of the target personal directory. If not specified, the user\"s default directory is automatically resolved.
        self.directory_id = directory_id
        # The project group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # itemIds
        # 
        # This parameter is required.
        self.item_ids_shrink = item_ids_shrink
        # The save mode. Valid values:
        # - link: creates a link (1:1 idempotent, editing the output synchronizes the resource).
        # - copy: creates a copy (unlimited times, snapshot).
        # 
        # This parameter is required.
        self.mode = mode
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The tenant ID. This is a common parameter. In winnexo-cli, pass this value explicitly by using --tenant-id.
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

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.item_ids_shrink is not None:
            result['itemIds'] = self.item_ids_shrink

        if self.mode is not None:
            result['mode'] = self.mode

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

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('itemIds') is not None:
            self.item_ids_shrink = m.get('itemIds')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

