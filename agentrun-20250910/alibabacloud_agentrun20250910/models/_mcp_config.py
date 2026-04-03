# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class McpConfig(DaraModel):
    def __init__(
        self,
        bound_configuration: main_models.BoundConfiguration = None,
        mcp_proxy_configuration: main_models.McpProxyConfiguration = None,
        proxy_enabled: bool = None,
        session_affinity: str = None,
        session_affinity_config: str = None,
    ):
        # 工具的绑定配置，定义工具与 HTTP 路径和方法的映射关系
        self.bound_configuration = bound_configuration
        # MCP 代理的详细配置，包括钩子函数等，用于在 MCP 请求处理过程中执行自定义逻辑
        self.mcp_proxy_configuration = mcp_proxy_configuration
        # 是否启用 MCP 代理功能，启用后可以通过代理配置对 MCP 请求进行拦截和处理
        self.proxy_enabled = proxy_enabled
        # 会话亲和性策略，用于控制请求的路由方式。NONE：无亲和性，MCP_SSE：基于 SSE 的会话亲和性，MCP_STREAMABLE：基于流式 HTTP 的会话亲和性
        self.session_affinity = session_affinity
        # 会话亲和性的详细配置信息，JSON 格式字符串，包含会话保持的具体参数
        self.session_affinity_config = session_affinity_config

    def validate(self):
        if self.bound_configuration:
            self.bound_configuration.validate()
        if self.mcp_proxy_configuration:
            self.mcp_proxy_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_configuration is not None:
            result['boundConfiguration'] = self.bound_configuration.to_map()

        if self.mcp_proxy_configuration is not None:
            result['mcpProxyConfiguration'] = self.mcp_proxy_configuration.to_map()

        if self.proxy_enabled is not None:
            result['proxyEnabled'] = self.proxy_enabled

        if self.session_affinity is not None:
            result['sessionAffinity'] = self.session_affinity

        if self.session_affinity_config is not None:
            result['sessionAffinityConfig'] = self.session_affinity_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boundConfiguration') is not None:
            temp_model = main_models.BoundConfiguration()
            self.bound_configuration = temp_model.from_map(m.get('boundConfiguration'))

        if m.get('mcpProxyConfiguration') is not None:
            temp_model = main_models.McpProxyConfiguration()
            self.mcp_proxy_configuration = temp_model.from_map(m.get('mcpProxyConfiguration'))

        if m.get('proxyEnabled') is not None:
            self.proxy_enabled = m.get('proxyEnabled')

        if m.get('sessionAffinity') is not None:
            self.session_affinity = m.get('sessionAffinity')

        if m.get('sessionAffinityConfig') is not None:
            self.session_affinity_config = m.get('sessionAffinityConfig')

        return self

