# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainExtensionAttributeResponseBody(DaraModel):
    def __init__(
        self,
        domain: str = None,
        domain_extension_id: str = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        request_id: str = None,
        server_certificate_id: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The ID of the additional certificate.
        self.domain_extension_id = domain_extension_id
        # The frontend port of the HTTPS listener that is configured for the SLB instance. Valid values: **1** to **65535**.
        self.listener_port = listener_port
        # The ID of the SLB instance.
        self.load_balancer_id = load_balancer_id
        # The request ID.
        self.request_id = request_id
        # The ID of the server certificate used by the domain name.
        self.server_certificate_id = server_certificate_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        return self

