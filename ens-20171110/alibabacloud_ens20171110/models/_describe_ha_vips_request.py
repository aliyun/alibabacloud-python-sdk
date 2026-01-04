# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeHaVipsRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        ha_vip_address: str = None,
        ha_vip_id: str = None,
        name: str = None,
        network_id: str = None,
        page_number: str = None,
        page_size: str = None,
        status: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the region.
        self.ens_region_id = ens_region_id
        # The IDs of edge nodes. You can specify 1 to 100 IDs.
        self.ens_region_ids = ens_region_ids
        # The IP address of the HAVIP.
        self.ha_vip_address = ha_vip_address
        # The ID of the HAVIP.
        self.ha_vip_id = ha_vip_id
        # The name of the HAVIP.
        self.name = name
        # The ID of the network.
        self.network_id = network_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The status of the HAVIP. Valid values:
        # 
        # *   Creating
        # *   Available
        # *   InUse
        # *   Deleting
        self.status = status
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

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

        if self.ha_vip_address is not None:
            result['HaVipAddress'] = self.ha_vip_address

        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id

        if self.name is not None:
            result['Name'] = self.name

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('HaVipAddress') is not None:
            self.ha_vip_address = m.get('HaVipAddress')

        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

