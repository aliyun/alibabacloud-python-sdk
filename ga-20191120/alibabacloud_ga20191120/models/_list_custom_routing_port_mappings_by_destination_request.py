# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomRoutingPortMappingsByDestinationRequest(DaraModel):
    def __init__(
        self,
        destination_address: str = None,
        endpoint_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The service IP address of the backend instance.
        # 
        # This parameter is required.
        self.destination_address = destination_address
        # The ID of the endpoint to which the backend instance belongs.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
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
        if self.destination_address is not None:
            result['DestinationAddress'] = self.destination_address

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationAddress') is not None:
            self.destination_address = m.get('DestinationAddress')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

