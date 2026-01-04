# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePublicIpAddressPoolResponseBody(DaraModel):
    def __init__(
        self,
        public_ip_address_pool_id: str = None,
        pulbic_ip_address_pool_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the IP address pool.
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The ID of the IP address pool.
        self.pulbic_ip_address_pool_id = pulbic_ip_address_pool_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the IP address pool belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id

        if self.pulbic_ip_address_pool_id is not None:
            result['PulbicIpAddressPoolId'] = self.pulbic_ip_address_pool_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')

        if m.get('PulbicIpAddressPoolId') is not None:
            self.pulbic_ip_address_pool_id = m.get('PulbicIpAddressPoolId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

