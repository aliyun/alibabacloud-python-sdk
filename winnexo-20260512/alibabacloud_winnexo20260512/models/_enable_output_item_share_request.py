# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EnableOutputItemShareRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        output_item_id: str = None,
        output_item_name: str = None,
        session_id: str = None,
        share_access_type: str = None,
        share_user_group_ids: List[str] = None,
        share_user_ids: List[int] = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The ID of the output item.
        self.output_item_id = output_item_id
        # The name of the output item. This parameter must be used together with sessionId. If multiple output items have the same name, the request is rejected and you are prompted to use outputItemId instead.
        self.output_item_name = output_item_name
        # The session ID used for exact filtering. The length is 1 to 128 characters. This parameter applies to common sessions, skill sessions, and the executionId of task executions.
        self.session_id = session_id
        # The sharing scope. Valid values:
        # - PUBLIC: Accessible to all users.
        # - SPECIFIED: Accessible only to specified users or user groups.
        self.share_access_type = share_access_type
        # The list of user group IDs within the specified scope.
        self.share_user_group_ids = share_user_group_ids
        # The list of platform user IDs within the specified scope.
        self.share_user_ids = share_user_ids
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

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.output_item_id is not None:
            result['outputItemId'] = self.output_item_id

        if self.output_item_name is not None:
            result['outputItemName'] = self.output_item_name

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.share_access_type is not None:
            result['shareAccessType'] = self.share_access_type

        if self.share_user_group_ids is not None:
            result['shareUserGroupIds'] = self.share_user_group_ids

        if self.share_user_ids is not None:
            result['shareUserIds'] = self.share_user_ids

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('outputItemId') is not None:
            self.output_item_id = m.get('outputItemId')

        if m.get('outputItemName') is not None:
            self.output_item_name = m.get('outputItemName')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('shareAccessType') is not None:
            self.share_access_type = m.get('shareAccessType')

        if m.get('shareUserGroupIds') is not None:
            self.share_user_group_ids = m.get('shareUserGroupIds')

        if m.get('shareUserIds') is not None:
            self.share_user_ids = m.get('shareUserIds')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

