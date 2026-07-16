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
        # The client token that is used to ensure the idempotence of a request.
        # 
        # Generate a parameter value from your client to ensure that the value is unique among different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # The acceleration region instance ID of the basic Alibaba Cloud Global Accelerator (GA) instance that you want to query.
        # 
        # You can invoke [GetBasicAccelerator](https://help.aliyun.com/document_detail/2253380.html) to query the acceleration region instance ID.
        # 
        # This parameter is required.
        self.ip_set_id = ip_set_id
        # The region ID of Global Accelerator. Set the value to **cn-hangzhou**.
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

