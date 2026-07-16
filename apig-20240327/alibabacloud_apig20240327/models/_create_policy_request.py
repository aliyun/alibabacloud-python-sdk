# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyRequest(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        config: str = None,
        description: str = None,
        name: str = None,
    ):
        # The policy type. Valid values:
        # 
        # - RateLimit: rate limiting. Limits the request rate.
        # - ConcurrencyLimit: concurrency limiting. Limits the number of concurrent requests.
        # - CircuitBreaker: circuit breaker. Automatically triggers circuit breaking when backend exceptions occur.
        # - HttpRewrite: HTTP rewrite. Rewrites the request URL or path.
        # - HeaderModify: header modification. Adds, removes, or modifies HTTP request headers.
        # - Cors: Cross-Origin Resource Sharing (CORS). Controls cross-origin requests.
        # - Authentication: general authentication. A general request authentication policy.
        # - FlowCopy: traffic mirroring. Copies requests to an additional backend.
        # - Timeout: timeout. Sets the request timeout period.
        # - Retry: retry. Automatically retries failed requests.
        # - IpAccessControl: IP access control. Filters requests based on IP whitelists and blacklists.
        # - DirectResponse: direct response. Returns a fixed response directly.
        # - Redirect: redirect. Redirects requests to another address.
        # - Fallback: fallback. Returns a fallback response when the backend is unavailable.
        # - ServiceTls: server-side TLS. Configures TLS for backend services.
        # - ServiceLb: service load balancing. Configures load balancing for backend services.
        # - ServicePortTls: service port TLS. Configures TLS for backend service ports.
        # - Waf: Web Application Firewall (WAF). Provides request security protection.
        # - JWTAuth: JWT authentication. Authenticates requests based on JSON Web Tokens (JWT).
        # - OIDCAuth: OIDC authentication. Authenticates requests based on the OpenID Connect (OIDC) protocol.
        # - ExternalZAuth: external authentication. Integrates with an external authentication service.
        # - AiProxy: AI proxy.
        # - ModelRouter: model router.
        # - AiStatistics: AI statistics.
        # - AiSecurityGuard: AI security guard. Detects the security of AI request and response content.
        # - AiFallback: AI fallback. Falls back to an alternative model when the AI service is unavailable.
        # - ModelMapper: model mapper.
        # - AiTokenRateLimit: AI token rate limiting. Limits the rate based on token consumption.
        # - AiCache: AI cache. Caches AI response results.
        # - DynamicRoute: dynamic route.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The policy configuration.
        # 
        # This parameter is required.
        self.config = config
        # The description.
        self.description = description
        # The policy name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_name is not None:
            result['className'] = self.class_name

        if self.config is not None:
            result['config'] = self.config

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

