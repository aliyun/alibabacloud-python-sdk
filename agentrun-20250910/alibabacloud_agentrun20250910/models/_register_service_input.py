# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterServiceInput(DaraModel):
    def __init__(
        self,
        credential_name: str = None,
        protocol: str = None,
        resource_name: str = None,
        service_backend_endpoint: str = None,
        service_name: str = None,
        service_type: str = None,
        tenant_id: str = None,
    ):
        # 关联的凭证ID，用于服务认证
        self.credential_name = credential_name
        # 服务的协议类型
        # 
        # This parameter is required.
        self.protocol = protocol
        # 关联的资源名称
        self.resource_name = resource_name
        # 转发的下游服务端点URL，必须是有效的HTTP/HTTPS地址（这里是 FC trigger endpoint）
        # 
        # This parameter is required.
        self.service_backend_endpoint = service_backend_endpoint
        # 服务名称，在租户内唯一
        # 
        # This parameter is required.
        self.service_name = service_name
        # 服务类型
        # 
        # This parameter is required.
        self.service_type = service_type
        # 租户ID，用于多租户隔离
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.service_backend_endpoint is not None:
            result['serviceBackendEndpoint'] = self.service_backend_endpoint

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('serviceBackendEndpoint') is not None:
            self.service_backend_endpoint = m.get('serviceBackendEndpoint')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

