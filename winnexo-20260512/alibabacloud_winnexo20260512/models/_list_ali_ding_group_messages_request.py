# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAliDingGroupMessagesRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        chat_id: str = None,
        direction: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page_size: int = None,
        tenant_id: str = None,
        time: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The session ID, typically used for JSSDK.
        # 
        # This parameter is required.
        self.chat_id = chat_id
        # The traffic direction. Valid values:
        # - OutBound: outbound.
        # - InBound: inbound.
        # - Both: bidirectional.
        self.direction = direction
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The number of entries per page.
        self.page_size = page_size
        # The tenant ID. This is a common parameter. Pass it explicitly through `--tenant-id` in winnexo-cli.
        self.tenant_id = tenant_id
        # The relationship information.
        # 
        # This parameter is required.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.direction is not None:
            result['direction'] = self.direction

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

