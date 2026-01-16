# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcEndpointRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        service_id: str = None,
        zone_id: str = None,
        dry_run: bool = None,
    ):
        # The returned result details.
        self.client_token = client_token
        self.service_id = service_id
        self.zone_id = zone_id
        # The ID of the user endpoint service associated with the endpoint.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

