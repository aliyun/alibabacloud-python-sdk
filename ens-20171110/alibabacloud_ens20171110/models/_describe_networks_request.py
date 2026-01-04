# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNetworksRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        network_id: str = None,
        network_ids: List[str] = None,
        network_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The IDs of edge nodes. You can specify 1 to 100 IDs.
        self.ens_region_ids = ens_region_ids
        # The ID of the network.
        self.network_id = network_id
        # The IDs of VPCs You can specify 1 to 100 IDs.
        self.network_ids = network_ids
        # The name of the network.
        self.network_name = network_name
        # The page number of the returned page. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 50**. Default value: **10**.
        self.page_size = page_size

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

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_ids is not None:
            result['NetworkIds'] = self.network_ids

        if self.network_name is not None:
            result['NetworkName'] = self.network_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkIds') is not None:
            self.network_ids = m.get('NetworkIds')

        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

