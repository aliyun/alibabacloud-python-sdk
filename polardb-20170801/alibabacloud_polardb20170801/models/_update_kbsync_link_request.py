# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKBSyncLinkRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        feishu_chat_member_stale_ttl_seconds: int = None,
        knowledge_base_id: str = None,
        link_id: str = None,
        mcp_endpoint: str = None,
        region_id: str = None,
        sheet_mcp_endpoint: str = None,
        sync_enabled: bool = None,
        sync_interval_minutes: int = None,
        user_access_token: str = None,
        user_id: str = None,
        user_refresh_token: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client secret.
        self.client_secret = client_secret
        # The validity period of a successful Lark group member snapshot used for fallback reuse, in seconds. This parameter can be explicitly set only for FEISHU synchronization links. A value of -1 indicates that the snapshot never expires. A value of 0 disables snapshot fallback reuse. A positive integer indicates the maximum age of a snapshot allowed for reuse. If this parameter is omitted, the original value is retained. Explicitly passing -1 restores the default behavior.
        self.feishu_chat_member_stale_ttl_seconds = feishu_chat_member_stale_ttl_seconds
        # The unique identifier of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The ID of the synchronization link.
        # 
        # This parameter is required.
        self.link_id = link_id
        # The endpoint of the DingTalk Docs MCP server.
        self.mcp_endpoint = mcp_endpoint
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The endpoint of the DingTalk Sheets MCP server.
        self.sheet_mcp_endpoint = sheet_mcp_endpoint
        # Specifies whether to enable automatic synchronization. This parameter must be modified individually and cannot be changed along with other configurations.
        self.sync_enabled = sync_enabled
        # 20
        self.sync_interval_minutes = sync_interval_minutes
        # The new Lark user access token.
        self.user_access_token = user_access_token
        # The ID of the DingTalk user that performs the operation.
        self.user_id = user_id
        # The new Lark user refresh token. Pass this parameter together with UserAccessToken. Passing empty strings for both parameters indicates deletion.
        self.user_refresh_token = user_refresh_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.feishu_chat_member_stale_ttl_seconds is not None:
            result['FeishuChatMemberStaleTtlSeconds'] = self.feishu_chat_member_stale_ttl_seconds

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.mcp_endpoint is not None:
            result['McpEndpoint'] = self.mcp_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sheet_mcp_endpoint is not None:
            result['SheetMcpEndpoint'] = self.sheet_mcp_endpoint

        if self.sync_enabled is not None:
            result['SyncEnabled'] = self.sync_enabled

        if self.sync_interval_minutes is not None:
            result['SyncIntervalMinutes'] = self.sync_interval_minutes

        if self.user_access_token is not None:
            result['UserAccessToken'] = self.user_access_token

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_refresh_token is not None:
            result['UserRefreshToken'] = self.user_refresh_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('FeishuChatMemberStaleTtlSeconds') is not None:
            self.feishu_chat_member_stale_ttl_seconds = m.get('FeishuChatMemberStaleTtlSeconds')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('McpEndpoint') is not None:
            self.mcp_endpoint = m.get('McpEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SheetMcpEndpoint') is not None:
            self.sheet_mcp_endpoint = m.get('SheetMcpEndpoint')

        if m.get('SyncEnabled') is not None:
            self.sync_enabled = m.get('SyncEnabled')

        if m.get('SyncIntervalMinutes') is not None:
            self.sync_interval_minutes = m.get('SyncIntervalMinutes')

        if m.get('UserAccessToken') is not None:
            self.user_access_token = m.get('UserAccessToken')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserRefreshToken') is not None:
            self.user_refresh_token = m.get('UserRefreshToken')

        return self

