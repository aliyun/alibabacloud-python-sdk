# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkPeerConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        network_peer_connects: List[main_models.DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnects] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.network_peer_connects = network_peer_connects
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.network_peer_connects:
            for v1 in self.network_peer_connects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkPeerConnects'] = []
        if self.network_peer_connects is not None:
            for k1 in self.network_peer_connects:
                result['NetworkPeerConnects'].append(k1.to_map() if k1 else None)

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
        self.network_peer_connects = []
        if m.get('NetworkPeerConnects') is not None:
            for k1 in m.get('NetworkPeerConnects'):
                temp_model = main_models.DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnects()
                self.network_peer_connects.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnects(DaraModel):
    def __init__(
        self,
        accepting_network: main_models.DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnectsAcceptingNetwork = None,
        accepting_network_id: str = None,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        name: str = None,
        network: main_models.DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnectsNetwork = None,
        network_id: str = None,
        status: str = None,
    ):
        self.accepting_network = accepting_network
        self.accepting_network_id = accepting_network_id
        self.creation_time = creation_time
        self.description = description
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.name = name
        self.network = network
        self.network_id = network_id
        self.status = status

    def validate(self):
        if self.accepting_network:
            self.accepting_network.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepting_network is not None:
            result['AcceptingNetwork'] = self.accepting_network.to_map()

        if self.accepting_network_id is not None:
            result['AcceptingNetworkId'] = self.accepting_network_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptingNetwork') is not None:
            temp_model = main_models.DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnectsAcceptingNetwork()
            self.accepting_network = temp_model.from_map(m.get('AcceptingNetwork'))

        if m.get('AcceptingNetworkId') is not None:
            self.accepting_network_id = m.get('AcceptingNetworkId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            temp_model = main_models.DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnectsNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnectsNetwork(DaraModel):
    def __init__(
        self,
        ipv_4cidrs: List[str] = None,
        network_id: str = None,
    ):
        self.ipv_4cidrs = ipv_4cidrs
        self.network_id = network_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        return self

class DescribeNetworkPeerConnectionsResponseBodyNetworkPeerConnectsAcceptingNetwork(DaraModel):
    def __init__(
        self,
        ipv_4cidrs: List[str] = None,
        network_id: str = None,
    ):
        self.ipv_4cidrs = ipv_4cidrs
        self.network_id = network_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        return self

