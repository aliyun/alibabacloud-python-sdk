# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKBSyncLinkRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        description: str = None,
        feishu_chat_member_stale_ttl_seconds: int = None,
        knowledge_base_id: str = None,
        link_name: str = None,
        mcp_endpoint: str = None,
        region_id: str = None,
        sheet_mcp_endpoint: str = None,
        source_dir: str = None,
        source_type: str = None,
        sync_interval_minutes: int = None,
        tenant_id: str = None,
        user_access_token: str = None,
        user_id: str = None,
        user_refresh_token: str = None,
    ):
        # The client ID.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client secret.
        # 
        # This parameter is required.
        self.client_secret = client_secret
        # The description of the synchronization link.
        self.description = description
        # The validity period of the Lark group member snapshot for fallback reuse, in seconds. This parameter can be explicitly set only for FEISHU synchronization links. A value of -1 indicates that the snapshot never expires. A value of 0 disables snapshot fallback reuse. A positive integer indicates the maximum age of the snapshot allowed for reuse. Default value: -1. If this parameter is omitted, -1 takes effect.
        self.feishu_chat_member_stale_ttl_seconds = feishu_chat_member_stale_ttl_seconds
        # The unique identifier of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The name of the link.
        # 
        # This parameter is required.
        self.link_name = link_name
        # The endpoint of the DingTalk document MCP server.
        self.mcp_endpoint = mcp_endpoint
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The endpoint of the DingTalk sheet MCP server.
        self.sheet_mcp_endpoint = sheet_mcp_endpoint
        # The source directory address for synchronization.
        # 
        # This parameter is required.
        self.source_dir = source_dir
        # The data source type. Valid values: FEISHU and SHAREPOINT.
        # 
        # This parameter is required.
        self.source_type = source_type
        # The synchronization interval, in minutes.
        self.sync_interval_minutes = sync_interval_minutes
        # The tenant ID. This parameter is required when SourceType is set to SHAREPOINT.
        self.tenant_id = tenant_id
        # The Lark user access token. This token is used only when the application identity cannot retrieve group members because the bot is not in the group chat.
        self.user_access_token = user_access_token
        # The ID of the DingTalk operator.
        self.user_id = user_id
        # The Lark user refresh token. This token must be provided together with UserAccessToken to automatically rotate the fallback identity for retrieving group members.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.feishu_chat_member_stale_ttl_seconds is not None:
            result['FeishuChatMemberStaleTtlSeconds'] = self.feishu_chat_member_stale_ttl_seconds

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.link_name is not None:
            result['LinkName'] = self.link_name

        if self.mcp_endpoint is not None:
            result['McpEndpoint'] = self.mcp_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sheet_mcp_endpoint is not None:
            result['SheetMcpEndpoint'] = self.sheet_mcp_endpoint

        if self.source_dir is not None:
            result['SourceDir'] = self.source_dir

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.sync_interval_minutes is not None:
            result['SyncIntervalMinutes'] = self.sync_interval_minutes

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FeishuChatMemberStaleTtlSeconds') is not None:
            self.feishu_chat_member_stale_ttl_seconds = m.get('FeishuChatMemberStaleTtlSeconds')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('LinkName') is not None:
            self.link_name = m.get('LinkName')

        if m.get('McpEndpoint') is not None:
            self.mcp_endpoint = m.get('McpEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SheetMcpEndpoint') is not None:
            self.sheet_mcp_endpoint = m.get('SheetMcpEndpoint')

        if m.get('SourceDir') is not None:
            self.source_dir = m.get('SourceDir')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SyncIntervalMinutes') is not None:
            self.sync_interval_minutes = m.get('SyncIntervalMinutes')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserAccessToken') is not None:
            self.user_access_token = m.get('UserAccessToken')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserRefreshToken') is not None:
            self.user_refresh_token = m.get('UserRefreshToken')

        return self

