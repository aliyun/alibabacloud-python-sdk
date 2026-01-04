# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeBgpNetworksResponseBody(DaraModel):
    def __init__(
        self,
        bgp_networks: main_models.DescribeBgpNetworksResponseBodyBgpNetworks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # BGP networks.
        self.bgp_networks = bgp_networks
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of advertised BGP networks.
        self.total_count = total_count

    def validate(self):
        if self.bgp_networks:
            self.bgp_networks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_networks is not None:
            result['BgpNetworks'] = self.bgp_networks.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpNetworks') is not None:
            temp_model = main_models.DescribeBgpNetworksResponseBodyBgpNetworks()
            self.bgp_networks = temp_model.from_map(m.get('BgpNetworks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBgpNetworksResponseBodyBgpNetworks(DaraModel):
    def __init__(
        self,
        bgp_network: List[main_models.DescribeBgpNetworksResponseBodyBgpNetworksBgpNetwork] = None,
    ):
        self.bgp_network = bgp_network

    def validate(self):
        if self.bgp_network:
            for v1 in self.bgp_network:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BgpNetwork'] = []
        if self.bgp_network is not None:
            for k1 in self.bgp_network:
                result['BgpNetwork'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bgp_network = []
        if m.get('BgpNetwork') is not None:
            for k1 in m.get('BgpNetwork'):
                temp_model = main_models.DescribeBgpNetworksResponseBodyBgpNetworksBgpNetwork()
                self.bgp_network.append(temp_model.from_map(k1))

        return self

class DescribeBgpNetworksResponseBodyBgpNetworksBgpNetwork(DaraModel):
    def __init__(
        self,
        dst_cidr_block: str = None,
        router_id: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The CIDR block of the advertised BGP network.
        self.dst_cidr_block = dst_cidr_block
        # The ID of the VBR.
        self.router_id = router_id
        # The status of the advertised BGP network.
        self.status = status
        # The ID of the virtual private cloud (VPC) in which the master instance resides.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_cidr_block is not None:
            result['DstCidrBlock'] = self.dst_cidr_block

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstCidrBlock') is not None:
            self.dst_cidr_block = m.get('DstCidrBlock')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

