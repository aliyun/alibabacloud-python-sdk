# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceKnowledgeBaseAdminsShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        directory_id: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
        user_group_ids_shrink: str = None,
        user_ids_shrink: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # 企业知识库或内置帮助知识库根目录业务 ID
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id
        # 管理员用户组 ID 列表；默认空列表表示清空用户组管理员
        self.user_group_ids_shrink = user_group_ids_shrink
        # 直接管理员的平台用户 ID 列表；默认空列表表示清空可变用户管理员，普通库创建者保留
        self.user_ids_shrink = user_ids_shrink

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

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids_shrink is not None:
            result['userGroupIds'] = self.user_group_ids_shrink

        if self.user_ids_shrink is not None:
            result['userIds'] = self.user_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids_shrink = m.get('userGroupIds')

        if m.get('userIds') is not None:
            self.user_ids_shrink = m.get('userIds')

        return self

