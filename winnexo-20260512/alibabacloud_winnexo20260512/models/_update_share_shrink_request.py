# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateShareShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        output_item_id: str = None,
        output_item_name: str = None,
        refresh_share_link: bool = None,
        session_id: str = None,
        share_access_type: str = None,
        share_enabled: bool = None,
        share_user_group_ids_shrink: str = None,
        share_user_ids_shrink: str = None,
        target_type: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The output item ID.
        self.output_item_id = output_item_id
        # The name of the output item. This parameter must be used together with sessionId.
        self.output_item_name = output_item_name
        # Specifies whether to refresh the sharing link. This is supported only for output items that have sharing enabled or are being enabled in the current request.
        self.refresh_share_link = refresh_share_link
        # The session ID.
        self.session_id = session_id
        # The sharing scope. Valid values:
        # - PUBLIC: Accessible to all users.
        # - SPECIFIED: Accessible to specified users or user groups.
        self.share_access_type = share_access_type
        # Specifies whether sharing is enabled.
        self.share_enabled = share_enabled
        # The list of user group IDs within the specified scope. Pass an empty array to clear the list.
        self.share_user_group_ids_shrink = share_user_group_ids_shrink
        # The list of platform user IDs within the specified scope. Pass an empty array to clear the list.
        self.share_user_ids_shrink = share_user_ids_shrink
        # The type of the current permission. Valid values:
        # - period: Period type.
        # - objective: Objective type.
        # - kr: Key result type.
        # 
        # This parameter is required.
        self.target_type = target_type
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

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.output_item_id is not None:
            result['outputItemId'] = self.output_item_id

        if self.output_item_name is not None:
            result['outputItemName'] = self.output_item_name

        if self.refresh_share_link is not None:
            result['refreshShareLink'] = self.refresh_share_link

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.share_access_type is not None:
            result['shareAccessType'] = self.share_access_type

        if self.share_enabled is not None:
            result['shareEnabled'] = self.share_enabled

        if self.share_user_group_ids_shrink is not None:
            result['shareUserGroupIds'] = self.share_user_group_ids_shrink

        if self.share_user_ids_shrink is not None:
            result['shareUserIds'] = self.share_user_ids_shrink

        if self.target_type is not None:
            result['targetType'] = self.target_type

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

        if m.get('refreshShareLink') is not None:
            self.refresh_share_link = m.get('refreshShareLink')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('shareAccessType') is not None:
            self.share_access_type = m.get('shareAccessType')

        if m.get('shareEnabled') is not None:
            self.share_enabled = m.get('shareEnabled')

        if m.get('shareUserGroupIds') is not None:
            self.share_user_group_ids_shrink = m.get('shareUserGroupIds')

        if m.get('shareUserIds') is not None:
            self.share_user_ids_shrink = m.get('shareUserIds')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

