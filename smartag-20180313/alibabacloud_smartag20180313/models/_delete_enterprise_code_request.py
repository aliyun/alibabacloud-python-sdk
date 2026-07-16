# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEnterpriseCodeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enterprise_code: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # The client generates the value of this parameter. Ensure that the value is unique among different requests. The value can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The enterprise code.
        # 
        # This parameter is required.
        self.enterprise_code = enterprise_code
        # The region ID.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) to query the regions supported by Smart Access Gateway and the corresponding region IDs.
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

