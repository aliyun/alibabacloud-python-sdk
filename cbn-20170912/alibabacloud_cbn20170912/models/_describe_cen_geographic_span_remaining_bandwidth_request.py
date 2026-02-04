# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCenGeographicSpanRemainingBandwidthRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        geographic_region_aid: str = None,
        geographic_region_bid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance to which the bandwidth plan is associated.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The ID of one of the connected areas of the bandwidth plan. Valid values:
        # 
        # *   **China**: Chinese mainland
        # *   **North-America**: North America
        # *   **Asia-Pacific**: Asia Pacific
        # *   **Europe**: Europe
        # 
        # This parameter is required.
        self.geographic_region_aid = geographic_region_aid
        # The ID of the other area connected by the bandwidth plan. Valid values:
        # 
        # *   **China**: Chinese mainland
        # *   **North-America**: North America
        # *   **Asia-Pacific**: Asia Pacific
        # *   **Europe**: Europe
        # 
        # This parameter is required.
        self.geographic_region_bid = geographic_region_bid
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**. Valid values: **1** to **50**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid

        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')

        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

