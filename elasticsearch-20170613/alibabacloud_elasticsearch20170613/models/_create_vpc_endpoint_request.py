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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must ensure that it is unique among different requests. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The ID of the endpoint service that you created. The endpoint on the service VPC side is associated with this service ID.
        self.service_id = service_id
        # The zone ID of the endpoint service that you created.
        self.zone_id = zone_id
        # Specifies whether to only perform a dry run on the request. Valid values:
        # 
        # - true: sends a check request and does not create an endpoint node. The check items include whether the AccessKey pair is valid, the authorization of the Resource Access Management (RAM) user, and whether the required parameters are specified.
        # - false (default): immediately triggers the creation of an endpoint node.
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

