# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnterpriseCodeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enterprise_code: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically set **ClientToken** to the value of **RequestId**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token
        # The enterprise code.
        # 
        # The enterprise code must be five characters in length and must contain letters and digits. Each enterprise code must be globally unique.
        # 
        # This parameter is required.
        self.enterprise_code = enterprise_code
        # The ID of the region.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
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

        if self.enterprise_code is not None:
            result['EnterpriseCode'] = self.enterprise_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnterpriseCode') is not None:
            self.enterprise_code = m.get('EnterpriseCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

