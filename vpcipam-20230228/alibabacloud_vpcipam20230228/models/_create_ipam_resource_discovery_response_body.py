# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpamResourceDiscoveryResponseBody(DaraModel):
    def __init__(
        self,
        ipam_resource_discovery_id: str = None,
        request_id: str = None,
    ):
        # The ID of the instance for resource discovery.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

