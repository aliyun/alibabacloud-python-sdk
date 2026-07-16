# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceEndpointRequest(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        client_token: str = None,
        component: str = None,
        domain: str = None,
        instance_id: str = None,
        resource_name: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.client_token = client_token
        # This parameter is required.
        self.component = component
        self.domain = domain
        # This parameter is required.
        self.instance_id = instance_id
        self.resource_name = resource_name

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

        if self.component is not None:
            result['Component'] = self.component

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Component') is not None:
            self.component = m.get('Component')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

