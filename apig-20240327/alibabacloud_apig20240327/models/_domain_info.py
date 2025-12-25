# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DomainInfo(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        client_cacert: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        domain_id: str = None,
        force_https: bool = None,
        m_tlsenabled: bool = None,
        name: str = None,
        protocol: str = None,
        resource_group_id: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.cert_identifier = cert_identifier
        self.client_cacert = client_cacert
        self.create_from = create_from
        self.create_timestamp = create_timestamp
        self.domain_id = domain_id
        self.force_https = force_https
        self.m_tlsenabled = m_tlsenabled
        self.name = name
        self.protocol = protocol
        self.resource_group_id = resource_group_id
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier

        if self.client_cacert is not None:
            result['clientCACert'] = self.client_cacert

        if self.create_from is not None:
            result['createFrom'] = self.create_from

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.force_https is not None:
            result['forceHttps'] = self.force_https

        if self.m_tlsenabled is not None:
            result['mTLSEnabled'] = self.m_tlsenabled

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')

        if m.get('clientCACert') is not None:
            self.client_cacert = m.get('clientCACert')

        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')

        if m.get('mTLSEnabled') is not None:
            self.m_tlsenabled = m.get('mTLSEnabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

