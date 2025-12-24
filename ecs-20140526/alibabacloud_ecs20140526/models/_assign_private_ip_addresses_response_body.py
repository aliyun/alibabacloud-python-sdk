# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AssignPrivateIpAddressesResponseBody(DaraModel):
    def __init__(
        self,
        assigned_private_ip_addresses_set: main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSet = None,
        request_id: str = None,
    ):
        # Details about the ENI and the secondary private IP addresses that are assigned to the ENI.
        self.assigned_private_ip_addresses_set = assigned_private_ip_addresses_set
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.assigned_private_ip_addresses_set:
            self.assigned_private_ip_addresses_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_private_ip_addresses_set is not None:
            result['AssignedPrivateIpAddressesSet'] = self.assigned_private_ip_addresses_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedPrivateIpAddressesSet') is not None:
            temp_model = main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSet()
            self.assigned_private_ip_addresses_set = temp_model.from_map(m.get('AssignedPrivateIpAddressesSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSet(DaraModel):
    def __init__(
        self,
        ipv_4prefix_set: main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSetIpv4PrefixSet = None,
        network_interface_id: str = None,
        private_ip_set: main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSetPrivateIpSet = None,
    ):
        # Details about the assigned IPv4 prefixes.
        self.ipv_4prefix_set = ipv_4prefix_set
        # The ENI ID.
        self.network_interface_id = network_interface_id
        # The secondary private IP addresses that are assigned to the ENI.
        self.private_ip_set = private_ip_set

    def validate(self):
        if self.ipv_4prefix_set:
            self.ipv_4prefix_set.validate()
        if self.private_ip_set:
            self.private_ip_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix_set is not None:
            result['Ipv4PrefixSet'] = self.ipv_4prefix_set.to_map()

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.private_ip_set is not None:
            result['PrivateIpSet'] = self.private_ip_set.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4PrefixSet') is not None:
            temp_model = main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSetIpv4PrefixSet()
            self.ipv_4prefix_set = temp_model.from_map(m.get('Ipv4PrefixSet'))

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrivateIpSet') is not None:
            temp_model = main_models.AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSetPrivateIpSet()
            self.private_ip_set = temp_model.from_map(m.get('PrivateIpSet'))

        return self

class AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSetPrivateIpSet(DaraModel):
    def __init__(
        self,
        private_ip_address: List[str] = None,
    ):
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

class AssignPrivateIpAddressesResponseBodyAssignedPrivateIpAddressesSetIpv4PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_4prefixes: List[str] = None,
    ):
        self.ipv_4prefixes = ipv_4prefixes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefixes is not None:
            result['Ipv4Prefixes'] = self.ipv_4prefixes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefixes') is not None:
            self.ipv_4prefixes = m.get('Ipv4Prefixes')

        return self

