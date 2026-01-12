# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CustomDomain(DaraModel):
    def __init__(
        self,
        cert_config: main_models.CertConfig = None,
        created_at: str = None,
        description: str = None,
        domain_name: str = None,
        domain_type: str = None,
        protocol: str = None,
        route_config: main_models.RouteConfig = None,
        tls_config: main_models.TLSConfig = None,
        updated_at: str = None,
    ):
        # HTTPS 证书的信息。
        self.cert_config = cert_config
        # 创建时间
        self.created_at = created_at
        # 描述
        self.description = description
        # 域名。填写已在阿里云备案或接入备案的自定义域名名称。
        self.domain_name = domain_name
        self.domain_type = domain_type
        # 域名支持的协议类型：● HTTP：仅支持 HTTP 协议。● HTTPS：仅支持 HTTPS 协议。● HTTP,HTTPS：支持 HTTP 及 HTTPS 协议。
        self.protocol = protocol
        # 路由表：自定义域名访问时的 PATH 到 资源 的映射。
        self.route_config = route_config
        # TLS 配置信息。
        self.tls_config = tls_config
        # 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.domain_name is not None:
            result['domainName'] = self.domain_name

        if self.domain_type is not None:
            result['domainType'] = self.domain_type

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()

        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certConfig') is not None:
            temp_model = main_models.CertConfig()
            self.cert_config = temp_model.from_map(m.get('certConfig'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')

        if m.get('domainType') is not None:
            self.domain_type = m.get('domainType')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('routeConfig') is not None:
            temp_model = main_models.RouteConfig()
            self.route_config = temp_model.from_map(m.get('routeConfig'))

        if m.get('tlsConfig') is not None:
            temp_model = main_models.TLSConfig()
            self.tls_config = temp_model.from_map(m.get('tlsConfig'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

