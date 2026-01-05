# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class EnableNetworkInterfaceQoSRequest(DaraModel):
    def __init__(
        self,
        network_interface_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        qo_s: main_models.EnableNetworkInterfaceQoSRequestQoS = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # QoS Speed Limit Settings
        self.qo_s = qo_s
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.qo_s:
            self.qo_s.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qo_s is not None:
            result['QoS'] = self.qo_s.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QoS') is not None:
            temp_model = main_models.EnableNetworkInterfaceQoSRequestQoS()
            self.qo_s = temp_model.from_map(m.get('QoS'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class EnableNetworkInterfaceQoSRequestQoS(DaraModel):
    def __init__(
        self,
        bandwidth_rx: int = None,
        bandwidth_tx: int = None,
        concurrent_connections: int = None,
        pps_rx: int = None,
        pps_tx: int = None,
    ):
        # The maximum inbound internal bandwidth.
        # 
        # Unit: kbit/s, step size: 1000 (1Mbps), value range: [50000, +♾️)
        self.bandwidth_rx = bandwidth_rx
        # The maximum outbound internal bandwidth.
        # 
        # Unit: kbit/s, step size: 1000 (1Mbps), value range: [50000, +♾️)
        self.bandwidth_tx = bandwidth_tx
        # Maximum Number of Sessions
        # 
        # Step size: 10000, value range: [10000, +♾️)
        self.concurrent_connections = concurrent_connections
        # The inbound packet forwarding rate over the internal network.
        # 
        # Unit: pps, step size: 10000, value range: [10000, +♾️)
        self.pps_rx = pps_rx
        # The outbound packet forwarding rate over the internal network.
        # 
        # Unit: pps, step size: 10000, value range: [10000, +♾️)
        self.pps_tx = pps_tx

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_rx is not None:
            result['BandwidthRx'] = self.bandwidth_rx

        if self.bandwidth_tx is not None:
            result['BandwidthTx'] = self.bandwidth_tx

        if self.concurrent_connections is not None:
            result['ConcurrentConnections'] = self.concurrent_connections

        if self.pps_rx is not None:
            result['PpsRx'] = self.pps_rx

        if self.pps_tx is not None:
            result['PpsTx'] = self.pps_tx

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthRx') is not None:
            self.bandwidth_rx = m.get('BandwidthRx')

        if m.get('BandwidthTx') is not None:
            self.bandwidth_tx = m.get('BandwidthTx')

        if m.get('ConcurrentConnections') is not None:
            self.concurrent_connections = m.get('ConcurrentConnections')

        if m.get('PpsRx') is not None:
            self.pps_rx = m.get('PpsRx')

        if m.get('PpsTx') is not None:
            self.pps_tx = m.get('PpsTx')

        return self

