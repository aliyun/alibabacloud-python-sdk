# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceCustomDomain(DaraModel):
    def __init__(
        self,
        cert: str = None,
        date: int = None,
        domain: str = None,
        grafana_workspace_id: str = None,
        id: int = None,
        key: str = None,
        private_zone: str = None,
        protocol: str = None,
        status: str = None,
        uri: str = None,
    ):
        self.cert = cert
        self.date = date
        self.domain = domain
        self.grafana_workspace_id = grafana_workspace_id
        self.id = id
        self.key = key
        self.private_zone = private_zone
        self.protocol = protocol
        self.status = status
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert is not None:
            result['cert'] = self.cert

        if self.date is not None:
            result['date'] = self.date

        if self.domain is not None:
            result['domain'] = self.domain

        if self.grafana_workspace_id is not None:
            result['grafanaWorkspaceId'] = self.grafana_workspace_id

        if self.id is not None:
            result['id'] = self.id

        if self.key is not None:
            result['key'] = self.key

        if self.private_zone is not None:
            result['privateZone'] = self.private_zone

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.status is not None:
            result['status'] = self.status

        if self.uri is not None:
            result['uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert') is not None:
            self.cert = m.get('cert')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('grafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('grafanaWorkspaceId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('privateZone') is not None:
            self.private_zone = m.get('privateZone')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('uri') is not None:
            self.uri = m.get('uri')

        return self

