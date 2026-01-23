# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RouteItem(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        instance_domain: str = None,
        storage_domain: str = None,
    ):
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # This parameter is required.
        self.instance_domain = instance_domain
        # This parameter is required.
        self.storage_domain = storage_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.instance_domain is not None:
            result['InstanceDomain'] = self.instance_domain

        if self.storage_domain is not None:
            result['StorageDomain'] = self.storage_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('InstanceDomain') is not None:
            self.instance_domain = m.get('InstanceDomain')

        if m.get('StorageDomain') is not None:
            self.storage_domain = m.get('StorageDomain')

        return self

