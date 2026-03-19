# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupGatewayListRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        identifier: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region: str = None,
    ):
        # A client token used to ensure the idempotence of the request. This prevents duplicate requests.
        self.client_token = client_token
        # The unique identifier of the backup gateway. You can query multiple gateways by separating the identifiers with commas (,).
        self.identifier = identifier
        self.owner_id = owner_id
        # The page number. The value must be greater than or equal to 0 and cannot exceed the maximum value of an integer. The default value is 0.
        self.page_num = page_num
        # The number of records on each page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        # 
        # > The default value is 30.
        self.page_size = page_size
        # The region of the DBS instance. Valid values:
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
        # - **ap-southeast-1**: Singapore
        # 
        # - **cn-hangzhou-finance**: Hangzhou Finance Cloud
        # 
        # - **cn-shanghai-finance**: Shanghai Finance Cloud
        # 
        # - **cn-shenzhen-finance**: Shenzhen Finance Cloud
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

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

