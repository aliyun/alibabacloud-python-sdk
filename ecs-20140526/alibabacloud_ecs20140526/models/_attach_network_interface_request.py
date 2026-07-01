# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachNetworkInterfaceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_card_index: int = None,
        network_interface_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        trunk_network_instance_id: str = None,
        wait_for_network_configuration_ready: bool = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The index of the network card specified for the ENI.
        # 
        # >Valid values of NetworkCardIndex depend on the instance family. If the instance type does not support network cards, you cannot specify this parameter. If the instance type supports network cards, see [Instance families](https://help.aliyun.com/document_detail/25378.html) for valid values.
        self.network_card_index = network_card_index
        # The network interface controller (NIC) ID.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the trunk ENI.
        # >This parameter is not yet available.
        self.trunk_network_instance_id = trunk_network_instance_id
        # >This parameter is deprecated.
        self.wait_for_network_configuration_ready = wait_for_network_configuration_ready

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_card_index is not None:
            result['NetworkCardIndex'] = self.network_card_index

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.trunk_network_instance_id is not None:
            result['TrunkNetworkInstanceId'] = self.trunk_network_instance_id

        if self.wait_for_network_configuration_ready is not None:
            result['WaitForNetworkConfigurationReady'] = self.wait_for_network_configuration_ready

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkCardIndex') is not None:
            self.network_card_index = m.get('NetworkCardIndex')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrunkNetworkInstanceId') is not None:
            self.trunk_network_instance_id = m.get('TrunkNetworkInstanceId')

        if m.get('WaitForNetworkConfigurationReady') is not None:
            self.wait_for_network_configuration_ready = m.get('WaitForNetworkConfigurationReady')

        return self

