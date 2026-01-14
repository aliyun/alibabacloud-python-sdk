# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBasicAccelerateIpsRequest(DaraModel):
    def __init__(
        self,
        accelerate_ip_address: str = None,
        accelerate_ip_id: str = None,
        client_token: str = None,
        ip_set_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The accelerated IP address of the basic GA instance.
        self.accelerate_ip_address = accelerate_ip_address
        # The ID of the accelerated IP address of the basic GA instance.
        self.accelerate_ip_id = accelerate_ip_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the acceleration region.
        # 
        # You can call the [GetBasicAccelerator](https://help.aliyun.com/document_detail/2253380.html) operation to query the ID of the acceleration region.
        # 
        # This parameter is required.
        self.ip_set_id = ip_set_id
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **10**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query and no next queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
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
        if self.accelerate_ip_address is not None:
            result['AccelerateIpAddress'] = self.accelerate_ip_address

        if self.accelerate_ip_id is not None:
            result['AccelerateIpId'] = self.accelerate_ip_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateIpAddress') is not None:
            self.accelerate_ip_address = m.get('AccelerateIpAddress')

        if m.get('AccelerateIpId') is not None:
            self.accelerate_ip_id = m.get('AccelerateIpId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

