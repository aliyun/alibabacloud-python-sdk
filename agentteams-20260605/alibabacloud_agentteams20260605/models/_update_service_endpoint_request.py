# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceEndpointRequest(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        client_token: str = None,
        domain: str = None,
        endpoint_id: str = None,
        instance_id: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.client_token = client_token
        self.domain = domain
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

