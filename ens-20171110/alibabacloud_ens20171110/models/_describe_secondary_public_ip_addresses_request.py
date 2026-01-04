# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSecondaryPublicIpAddressesRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        isp: str = None,
        page_number: int = None,
        page_size: int = None,
        secondary_public_ip_address: str = None,
        secondary_public_ip_id: str = None,
    ):
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        self.ens_region_ids = ens_region_ids
        # The Internet service provider. Valid values:
        # 
        # *   cmcc: China Mobile.
        # *   unicom: China Unicom.
        # *   telecom: China Telecom.
        self.isp = isp
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The secondary IP address.
        self.secondary_public_ip_address = secondary_public_ip_address
        # The ID of the secondary public IP address.
        self.secondary_public_ip_id = secondary_public_ip_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.secondary_public_ip_address is not None:
            result['SecondaryPublicIpAddress'] = self.secondary_public_ip_address

        if self.secondary_public_ip_id is not None:
            result['SecondaryPublicIpId'] = self.secondary_public_ip_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecondaryPublicIpAddress') is not None:
            self.secondary_public_ip_address = m.get('SecondaryPublicIpAddress')

        if m.get('SecondaryPublicIpId') is not None:
            self.secondary_public_ip_id = m.get('SecondaryPublicIpId')

        return self

