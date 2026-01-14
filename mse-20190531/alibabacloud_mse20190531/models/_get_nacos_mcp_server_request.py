# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNacosMcpServerRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        mcp_server_id: str = None,
        mcp_server_version: str = None,
        namespace_id: str = None,
    ):
        self.accept_language = accept_language
        self.instance_id = instance_id
        self.mcp_server_id = mcp_server_id
        self.mcp_server_version = mcp_server_version
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mcp_server_id is not None:
            result['McpServerId'] = self.mcp_server_id

        if self.mcp_server_version is not None:
            result['McpServerVersion'] = self.mcp_server_version

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('McpServerId') is not None:
            self.mcp_server_id = m.get('McpServerId')

        if m.get('McpServerVersion') is not None:
            self.mcp_server_version = m.get('McpServerVersion')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

