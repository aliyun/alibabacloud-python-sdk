# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGrantVSwitchesToCenRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        enabled_ipv_6: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The CEN instance ID.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # Specifies whether to enable IPv6. true: enables IPv6. false: disables IPv6. If you do not specify a value, vSwitches are not filtered based on this attribute.
        self.enabled_ipv_6 = enabled_ipv_6
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **10**.
        self.page_size = page_size
        # The region ID of the VPC.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone.
        # 
        # *   If you specify a zone ID, the system queries the information about the vSwitches in the specified zone.
        # *   If you do not specify a zone ID, the system queries the information about the vSwitches in all zones.
        # 
        # You can call the [DescribeZones](https://help.aliyun.com/document_detail/36064.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.enabled_ipv_6 is not None:
            result['EnabledIpv6'] = self.enabled_ipv_6

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('EnabledIpv6') is not None:
            self.enabled_ipv_6 = m.get('EnabledIpv6')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

