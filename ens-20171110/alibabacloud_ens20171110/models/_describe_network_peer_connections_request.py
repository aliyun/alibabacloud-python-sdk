# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNetworkPeerConnectionsRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
        name: str = None,
        network_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The ID of the network peer connection.
        self.instance_id = instance_id
        # The name of the network peer connection.
        self.name = name
        # The IDs of the networks involved in the connection. The query does not distinguish between the requester and accepter.
        self.network_ids = network_ids
        # The page number for the returned results. Default: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default: **10**. Valid values: **10** to **100**.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.network_ids is not None:
            result['NetworkIds'] = self.network_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkIds') is not None:
            self.network_ids = m.get('NetworkIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

