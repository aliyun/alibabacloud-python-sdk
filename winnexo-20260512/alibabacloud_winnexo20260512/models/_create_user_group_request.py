# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserGroupRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        description: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        parent_id: str = None,
        tenant_id: str = None,
        user_group_name: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The description of the user group.
        self.description = description
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The ID of the parent user group. If this parameter is not specified, the user group is created under the root node.
        self.parent_id = parent_id
        # The tenant ID. This is a common parameter that can be explicitly passed by using the `--tenant-id` option in winnexo-cli.
        self.tenant_id = tenant_id
        # The name of the user group. The name must be unique under the same parent node.
        # 
        # This parameter is required.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.description is not None:
            result['description'] = self.description

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_name is not None:
            result['userGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupName') is not None:
            self.user_group_name = m.get('userGroupName')

        return self

