# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBasicAccelerateIpIdleCountRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the basic GA instance that you want to query.
        # 
        # You can call the [GetBasicAccelerator](https://help.aliyun.com/document_detail/2253380.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.ip_set_id = ip_set_id
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

