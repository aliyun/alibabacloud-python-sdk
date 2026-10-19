# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeVSwitchesRequest(DaraModel):
    def __init__(
        self,
        enable_ipv_6: bool = None,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        network_id: str = None,
        page_number: int = None,
        page_size: int = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        v_switch_name: str = None,
    ):
        # Specifies whether to query vSwitches with IPv6 CIDR blocks enabled. Valid values:
        # - true: Queries vSwitches with IPv6 CIDR blocks enabled in the specified region.
        # - false: Does not query vSwitches with IPv6 CIDR blocks enabled in the specified region.
        # 
        # If you do not specify this parameter, the system queries all vSwitches by default.
        self.enable_ipv_6 = enable_ipv_6
        # The ENS edge zone ID.
        self.ens_region_id = ens_region_id
        # The array of ENS edge zone IDs. Array length: 1 to 100.
        self.ens_region_ids = ens_region_ids
        # The ID of the VPC to which the vSwitch to be queried belongs.
        self.network_id = network_id
        # The page number of the list. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page in a paging query. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The array of vSwitch IDs. Array length: 1 to 100.
        self.v_switch_ids = v_switch_ids
        # The vSwitch name.
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

