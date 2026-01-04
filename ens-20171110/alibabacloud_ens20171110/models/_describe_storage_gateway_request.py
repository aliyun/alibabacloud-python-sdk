# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStorageGatewayRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        gateway_id: str = None,
        gateway_type: str = None,
        page_number: str = None,
        page_size: str = None,
        vpc_id: str = None,
    ):
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The type of the gateway. Set this parameter to **1**. **1** indicates iSCSI.
        self.gateway_type = gateway_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

