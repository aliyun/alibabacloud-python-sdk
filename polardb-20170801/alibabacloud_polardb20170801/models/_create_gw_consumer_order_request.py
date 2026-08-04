# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGwConsumerOrderRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        expire_time: str = None,
        gateway_id: str = None,
        key_count: int = None,
        package_spec: str = None,
        region_id: str = None,
    ):
        # The idempotency token.
        self.client_token = client_token
        # The expiration time of the API key in ISO-8601 format. The value must be later than the current time.
        self.expire_time = expire_time
        # The ID of the AI gateway instance.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # The number of API keys to generate (the number of capacity plans to order). Valid values: 1 to 30.
        # 
        # This parameter is required.
        self.key_count = key_count
        # The number of credits per API key. The value is a positive integer string.
        # 
        # This parameter is required.
        self.package_spec = package_spec
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query region information.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.key_count is not None:
            result['KeyCount'] = self.key_count

        if self.package_spec is not None:
            result['PackageSpec'] = self.package_spec

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('KeyCount') is not None:
            self.key_count = m.get('KeyCount')

        if m.get('PackageSpec') is not None:
            self.package_spec = m.get('PackageSpec')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

