# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKBSyncLinkRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        knowledge_base_id: str = None,
        link_id: str = None,
        mcp_endpoint: str = None,
        region_id: str = None,
        sheet_mcp_endpoint: str = None,
        sync_enabled: bool = None,
        sync_interval_minutes: int = None,
        user_id: str = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client secret.
        self.client_secret = client_secret
        # The unique identifier of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The synchronization link ID.
        # 
        # This parameter is required.
        self.link_id = link_id
        # The MCP Server address for DingTalk documents.
        self.mcp_endpoint = mcp_endpoint
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The MCP Server address for DingTalk spreadsheets.
        self.sheet_mcp_endpoint = sheet_mcp_endpoint
        # Specifies whether to enable automatic synchronization. This parameter can only be modified independently and cannot be changed together with other configurations.
        self.sync_enabled = sync_enabled
        # 20
        self.sync_interval_minutes = sync_interval_minutes
        # The DingTalk user ID for the operation.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

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

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

