# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNodeCidrListRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        region: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # The region in which DBS is activated. Valid values:
        # 
        # - **cn-hangzhou**: China (Hangzhou)
        # 
        # - **cn-shanghai**: China (Shanghai)
        # 
        # - **cn-qingdao**: China (Qingdao)
        # 
        # - **cn-beijing**: China (Beijing)
        # 
        # - **cn-shenzhen**: China (Shenzhen)
        # 
        # - **cn-hongkong**: China (Hong Kong)
        # 
        # - **ap-southeast-1**: Singapore (Singapore)
        # 
        # - **cn-hangzhou-finance**: China East 1 Finance
        # 
        # - **cn-shanghai-finance**: China East 2 Finance
        # 
        # - **cn-shenzhen-finance**: China South 1 Finance
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

